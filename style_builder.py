"""
Style Builder - Converts raw S&S data into domain Style objects

Responsibility: Transform cached S&S products into clean Style domain models
"""

from domain_models import Style, StyleVariant, StyleImage
from database import get_db
from typing import List, Dict, Optional
from datetime import datetime
import json


class StyleBuilder:
    """Builds Style domain objects from cached S&S products"""
    
    def __init__(self, sync_id: str, log_callback=None, arbitraj_settings=None):
        self.sync_id = sync_id
        self.log_callback = log_callback
        # Arbitraj (pricing) settings from frontend
        self.arbitraj_settings = arbitraj_settings or {}
        self.arbitraj_enabled = self.arbitraj_settings.get('enabled', False)
        
        if self.arbitraj_enabled:
            print(f"📊 Arbitraj fiyatlaması AKTIF: {self.arbitraj_settings}")
    
    def _log(self, message: str):
        """Log to callback (for UI) and console"""
        print(message)
        if self.log_callback:
            self.log_callback('info', message)
    
    def _apply_arbitraj_pricing(self, base_price: float) -> float:
        """Apply arbitraj pricing rules to base price"""
        if not self.arbitraj_enabled or base_price <= 0:
            return base_price
        
        settings = self.arbitraj_settings
        
        # Fixed price mode
        if settings.get('fixedPrice') is not None:
            final_price = float(settings['fixedPrice'])
        else:
            # Markup mode: price * (1 + markup/100)
            markup = float(settings.get('markupPercent', 0))
            final_price = base_price * (1 + markup / 100)
        
        # Apply rounding
        rounding_type = settings.get('roundingType', 'none')
        if rounding_type == '99':
            final_price = int(final_price) + 0.99
        elif rounding_type == '90':
            final_price = int(final_price) + 0.90
        elif rounding_type == '00':
            final_price = round(final_price)  # Round to nearest integer
        
        # Apply minimum price
        min_price = settings.get('minimumPrice')
        if min_price is not None and final_price < float(min_price):
            final_price = float(min_price)
        
        return round(final_price, 2)
    
    def build_style_from_group(self, style_id: str) -> Optional[Style]:
        """
        Build a Style object from all cached products with given style_id
        Returns None if no products found
        """
        self._log(f"  🔍 Building style {style_id} from cache...")
        
        # Fetch all products for this style
        with get_db() as conn:
            cursor = conn.cursor()
            cursor.execute('''
                SELECT product_data FROM ss_products_cache
                WHERE style_id = ? AND sync_id = ?
                ORDER BY sku
            ''', (style_id, self.sync_id))
            
            rows = cursor.fetchall()
        
        self._log(f"  📊 Found {len(rows)} rows in cache for style {style_id}")
        
        if not rows:
            self._log(f"  ❌ No rows found in cache for style {style_id}")
            return None
        
        # Parse product data
        products = []
        for idx, row in enumerate(rows):
            try:
                product = json.loads(row['product_data'])
                products.append(product)
            except Exception as e:
                self._log(f"  ❌ Failed to parse row {idx}: {e}")
                continue
        
        self._log(f"  📊 Parsed {len(products)} products from {len(rows)} rows")
        
        if not products:
            self._log(f"  ❌ No products after parsing for style {style_id}")
            return None
        
        # Use first product as base for style-level attributes
        base = products[0]
        
        self._log(f"  📋 Base product: brand={base.get('brandName')}, style={base.get('styleName')}")
        
        # Build Style object (will add variants later to avoid validation error)
        # NOTE: Style.__post_init__ checks for at least 1 variant
        # So we build it WITHOUT validation first
        style_data = {
            'style_id': str(style_id),
            'brand': base.get('brandName', ''),
            'name': base.get('styleName', f"Style {style_id}"),
            'description': base.get('description', '') or base.get('styleDescription', '') or '',
            'product_type': base.get('baseCategory', '') or base.get('category', ''),
            'tags': self._extract_tags(base),
            'metafields': self._extract_product_metafields(base),
            'collections': [],
            'variants': [],  # Will be populated below
            'images': []
        }
        
        self._log(f"  📦 Building Style object...")
        
        # Build variants with MULTI-LOCATION INVENTORY support
        # Merge same color/size combinations (different warehouses/SKUs)
        variant_map = {}  # {option_key: StyleVariant}
        merged_count = 0
        
        self._log(f"  🔨 Building variants from {len(products)} products (with location merge)...")
        
        for idx, product in enumerate(products):
            try:
                variant = self._build_variant(product)
                option_key = variant.option_key
                
                if option_key in variant_map:
                    # MERGE: Same color/size, different warehouse
                    existing = variant_map[option_key]
                    existing.skus.append(variant.sku)
                    
                    # Aggregate location inventory
                    if variant.inventory_quantity:
                        existing.location_inventory[variant.sku] = variant.inventory_quantity
                        
                        # Update total
                        existing.inventory_quantity = sum(existing.location_inventory.values())
                        
                        # CRITICAL: Use SKU with highest stock as primary
                        if variant.inventory_quantity > existing.location_inventory.get(existing.sku, 0):
                            # This SKU has more stock, make it primary
                            existing.sku = variant.sku
                            existing.barcode = variant.barcode  # Update barcode too
                    
                    merged_count += 1
                    
                    if merged_count <= 5:
                        self._log(f"  🔄 Merged {variant.sku} (stock: {variant.inventory_quantity}) into {existing.sku} - Total: {existing.inventory_quantity}")
                else:
                    # New variant
                    variant.skus = [variant.sku]
                    if variant.inventory_quantity:
                        variant.location_inventory = {variant.sku: variant.inventory_quantity}
                    variant_map[option_key] = variant
                    
                    if len(variant_map) <= 3:
                        self._log(f"  📦 Variant {len(variant_map)}: {variant.sku} - {variant.color_name} / {variant.size_name}")
            except Exception as e:
                self._log(f"  ❌ Failed to build variant {idx}: {e}")
                continue
        
        variants_list = list(variant_map.values())
        
        if merged_count > 0:
            self._log(f"  ✅ Merged {merged_count} duplicate SKUs into {len(variants_list)} unique variants")
        
        # Save SKU mapping to JSON file for reference
        if merged_count > 0:
            try:
                mapping_data = {
                    "style_id": str(style_id),
                    "timestamp": datetime.now().isoformat(),
                    "total_skus": len(products),
                    "unique_variants": len(variants_list),
                    "merged_count": merged_count,
                    "mappings": []
                }
                
                for v in variants_list:
                    if len(v.skus) > 1:
                        mapping_data["mappings"].append({
                            "primary_sku": v.sku,
                            "color": v.color_name,
                            "size": v.size_name,
                            "merged_skus": v.skus,
                            "total_inventory": v.inventory_quantity,
                            "location_inventory": v.location_inventory
                        })
                
                # Append to JSON file
                try:
                    with open('sku_mapping.json', 'r') as f:
                        existing = json.load(f)
                except:
                    existing = {"version": "1.0", "mappings": []}
                
                existing["mappings"].append(mapping_data)
                
                with open('sku_mapping.json', 'w') as f:
                    json.dump(existing, f, indent=2)
                
                self._log(f"  💾 SKU mapping saved to sku_mapping.json")
            except Exception as e:
                print(f"  Warning: Could not save SKU mapping: {e}")
        
        self._log(f"  ✅ Total variants built: {len(variants_list)}")
        
        # Build product images - ONE image per COLOR (not per URL)
        # This prevents duplicate images for same color different sizes
        # {color_name: url} - only keep first (front) image per color
        color_to_image = {}
        for product in products:
            color_name = product.get('colorName', '') or product.get('color', '')
            if not color_name or color_name in color_to_image:
                continue  # Skip if no color or already have image for this color
            
            # Get the primary (front) image for this color
            front_image = self._get_primary_color_image(product)
            if front_image:
                color_to_image[color_name] = front_image
        
        images_list = []
        for idx, (color_name, url) in enumerate(sorted(color_to_image.items())):
            # Format alt text as #Color_ColorName for Shopify variant image linking
            # IMPORTANT: Replace hyphens with spaces (Tri-Rust -> Tri Rust)
            clean_color = color_name.replace('-', ' ')
            alt_text = f"#Color_{clean_color}"
            images_list.append(StyleImage(url=url, alt_text=alt_text, position=idx))
        
        self._log(f"  📸 Built {len(images_list)} images (1 per color, {len(color_to_image)} unique colors)")
        
        # Add variants and images to style_data
        style_data['variants'] = variants_list  # CRITICAL: Add variants
        style_data['images'] = images_list
        
        # Validate before creating Style
        if not variants_list:
            self._log(f"  ❌ ERROR: No variants for style {style_id}")
            raise ValueError(f"Style {style_id} must have at least one variant")
        
        # Now create Style object with all data
        style = Style(**style_data)
        
        return style
    
    def _build_variant(self, product: Dict) -> StyleVariant:
        """Build a StyleVariant from S&S product data"""
        sku = product.get('sku', '')
        
        # Extract variant attributes
        color_name = product.get('colorName', '') or product.get('color', '')
        color_code = product.get('colorCode', '')
        size_name = product.get('sizeName', '') or product.get('size', '')
        size_code = product.get('sizeCode', '')
        
        # Price - S&S API returns price fields directly in product (not nested in 'pricing')
        price = 0.0
        
        # Try customerPrice first (user's negotiated price), then others
        price_fields = ['customerPrice', 'piecePrice', 'casePrice', 'dozenPrice', 'salePrice', 'price']
        for field in price_fields:
            val = product.get(field)
            if val is not None and val != '' and val != 0:
                try:
                    price = float(val)
                    if price > 0:
                        break
                except (ValueError, TypeError):
                    continue
        
        if price == 0:
            print(f"   ⚠️ No price found for SKU {sku}, checked fields: {price_fields}")
        
        # Apply arbitraj pricing if enabled
        original_price = price
        price = self._apply_arbitraj_pricing(price)
        if price != original_price and self.arbitraj_enabled:
            print(f"   💰 Arbitraj: ${original_price:.2f} → ${price:.2f} (SKU: {sku})")
        
        # Inventory
        inventory_qty = product.get('qty') or product.get('inventory', {}).get('qty')
        
        # Image
        image_url = product.get('colorFrontImage', '') or product.get('image', '')
        
        # Weight
        weight = product.get('unitWeight', 0) or 0
        
        # Barcode
        barcode = product.get('gtin', '') or product.get('barcode', '')
        
        # Metafields
        metafields = self._extract_variant_metafields(product)
        
        return StyleVariant(
            sku=sku,
            color_name=color_name,
            color_code=color_code,
            size_name=size_name,
            size_code=size_code,
            price=price,
            barcode=barcode,
            weight=float(weight),
            weight_unit='lb',
            inventory_quantity=int(inventory_qty) if inventory_qty is not None else None,
            image_url=image_url,
            metafields=metafields
        )
    
    def _extract_tags(self, product: Dict) -> List[str]:
        """Extract tags from product data"""
        tags = set()
        
        # Brand
        if product.get('brandName'):
            tags.add(product['brandName'])
        
        # Color family
        if product.get('colorFamily'):
            tags.add(product['colorFamily'])
        
        # Categories
        if product.get('baseCategory'):
            tags.add(product['baseCategory'])
        if product.get('category'):
            tags.add(product['category'])
        
        # Gender
        if product.get('gender'):
            tags.add(product['gender'])
        
        return sorted(list(tags))
    
    def _extract_product_metafields(self, product: Dict) -> Dict:
        """Extract ALL product-level metafields from S&S API"""
        metafields = {}
        
        # COMPLETE list of S&S API fields to preserve as metafields
        fields = [
            # Core identifiers
            'styleID', 'partNumber', 'brandName', 'styleName', 'title',
            # Categories
            'baseCategory', 'categories', 'categoryNames',
            # Descriptions
            'description', 'styleDescription', 'fabric', 'material',
            # Attributes
            'gender', 'fit', 'neckStyle', 'sleeveType', 'pocketType',
            'fabricWeight', 'fabricContent', 'careInstructions',
            # Pricing
            'mapPrice', 'piecePrice', 'dozenPrice', 'casePrice', 
            'customerPrice', 'salePrice', 'saleExpiration',
            # Packaging
            'caseQty', 'caseWeight', 'caseWidth', 'caseLength', 'caseHeight',
            'PolyPackQty', 'countryOfOrigin',
            # Flags
            'newStyle', 'sustainableStyle', 'closeoutStyle', 'noeRetailing',
            # Catalog
            'catalogPageNumber', 'swatchUrl', 'comparableGroup', 'companionGroup',
            # Brand info
            'brandID', 'brandLogoImage', 'brandURL',
            # Additional
            'unitWeight', 'pieceWeight'
        ]
        
        for field in fields:
            value = product.get(field)
            if value is not None and value != '':
                metafields[field] = value
        
        return metafields
    
    def _extract_variant_metafields(self, product: Dict) -> Dict:
        """Extract ALL variant-level metafields from S&S API"""
        metafields = {}
        
        # COMPLETE list of variant-specific fields
        fields = [
            # Color info
            'colorName', 'colorCode', 'colorPriceCodeName', 
            'colorGroup', 'colorGroupName', 'colorFamilyID', 'colorFamily',
            # Size info
            'sizeName', 'sizeCode', 'sizeOrder', 'sizePriceCodeName',
            # Identifiers
            'sku', 'gtin', 'yourSku', 'partNumber',
            # Pricing
            'piecePrice', 'dozenPrice', 'casePrice', 
            'customerPrice', 'salePrice', 'mapPrice',
            # Stock
            'qty', 'caseQty',
            # Weight
            'unitWeight', 'pieceWeight', 'caseWeight'
        ]
        
        for field in fields:
            value = product.get(field)
            if value is not None and value != '':
                metafields[field] = value
        
        return metafields
    
    def _extract_image_urls(self, product: Dict) -> List[str]:
        """Extract all image URLs from product (legacy method)"""
        urls = []
        
        # Different image fields in S&S data
        image_fields = [
            'colorFrontImage', 'colorBackImage', 'colorSideImage',
            'image', 'imageUrl', 'frontImage', 'backImage'
        ]
        
        for field in image_fields:
            url = product.get(field, '')
            if url and url.strip() and url.startswith('http'):
                urls.append(url.strip())
        
        return urls
    
    def _get_primary_color_image(self, product: Dict) -> Optional[str]:
        """
        Get the PRIMARY (front) image for a color.
        Returns only ONE image URL per color - typically the front image.
        This prevents multiple images for same color (S, M, L all sharing one image).
        """
        # Priority order: front image is most important
        priority_fields = [
            'colorFrontImage',      # Best: front view
            'colorOnModelFrontImage',  # On-model front
            'colorSideImage',       # Side view
            'colorBackImage',       # Back view
            'image',                # Generic
            'imageUrl'
        ]
        
        for field in priority_fields:
            url = product.get(field, '')
            if url and url.strip():
                # S&S URLs might be relative - make them absolute
                if not url.startswith('http'):
                    url = f"https://www.ssactivewear.com/{url.lstrip('/')}"
                return url.strip()
        
        return None
    
    def _extract_images_with_color(self, product: Dict, color_name: str) -> List[tuple]:
        """
        Extract image URLs with their associated color name
        Returns list of (url, color_name) tuples
        
        This enables Shopify variant-image linking via alt text like #Color_White
        """
        images = []
        
        # Different image fields in S&S data
        image_fields = [
            'colorFrontImage', 'colorBackImage', 'colorSideImage',
            'colorDirectSideImage', 'colorOnModelFrontImage', 
            'colorOnModelSideImage', 'colorOnModelBackImage',
            'image', 'imageUrl', 'frontImage', 'backImage'
        ]
        
        for field in image_fields:
            url = product.get(field, '')
            if url and url.strip():
                # S&S URLs might be relative - make them absolute
                if not url.startswith('http'):
                    url = f"https://www.ssactivewear.com/{url.lstrip('/')}"
                images.append((url.strip(), color_name))
        
        return images
    
    def build_all_styles(self) -> List[Style]:
        """
        Build Style objects for all unique style_ids in cache
        Returns list of Style objects
        """
        # Get unique style_ids
        with get_db() as conn:
            cursor = conn.cursor()
            cursor.execute('''
                SELECT DISTINCT style_id FROM ss_products_cache
                WHERE sync_id = ? AND style_id IS NOT NULL
                ORDER BY style_id
            ''', (self.sync_id,))
            
            style_ids = [row['style_id'] for row in cursor.fetchall()]
        
        # Build Style object for each
        styles = []
        for style_id in style_ids:
            style = self.build_style_from_group(str(style_id))
            if style:
                styles.append(style)
                self._log(f"  ✅ Built Style {style_id}: {style.variant_count} variants, {len(style.images)} images")
        
        return styles

