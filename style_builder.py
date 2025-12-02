"""
Style Builder - Converts raw S&S data into domain Style objects

Responsibility: Transform cached S&S products into clean Style domain models
"""

from domain_models import Style, StyleVariant, StyleImage
from database import get_db
from typing import List, Dict, Optional
import json


class StyleBuilder:
    """Builds Style domain objects from cached S&S products"""
    
    def __init__(self, sync_id: str, log_callback=None):
        self.sync_id = sync_id
        self.log_callback = log_callback
    
    def _log(self, message: str):
        """Log to callback (for UI) and console"""
        print(message)
        if self.log_callback:
            self.log_callback('info', message)
    
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
        
        # Build variants FIRST (before creating Style object)
        seen_option_keys = set()
        variants_list = []  # Initialize list
        
        self._log(f"  📊 Building variants from {len(products)} products...")
        
        for idx, product in enumerate(products):
            try:
                variant = self._build_variant(product)
                
                # Deduplicate by option key
                if variant.option_key in seen_option_keys:
                    print(f"  Skipping duplicate variant: {variant.sku} ({variant.option_key})")
                    continue
                
                seen_option_keys.add(variant.option_key)
                variants_list.append(variant)
                
                if idx < 3:  # Log first 3 variants
                    self._log(f"  📊 Variant {idx+1}: {variant.sku} - {variant.color_name} / {variant.size_name}")
            except Exception as e:
                self._log(f"  ❌ Failed to build variant {idx}: {e}")
                continue
        
        self._log(f"  📊 Total variants built: {len(style.variants)}")
        
        # Build product images (unique URLs)
        image_urls = set()
        for product in products:
            urls = self._extract_image_urls(product)
            image_urls.update(urls)
        
        for idx, url in enumerate(sorted(image_urls)):
            style.images.append(StyleImage(url=url, position=idx))
        
        return style
    
    def _build_variant(self, product: Dict) -> StyleVariant:
        """Build a StyleVariant from S&S product data"""
        sku = product.get('sku', '')
        
        # Extract variant attributes
        color_name = product.get('colorName', '') or product.get('color', '')
        color_code = product.get('colorCode', '')
        size_name = product.get('sizeName', '') or product.get('size', '')
        size_code = product.get('sizeCode', '')
        
        # Price
        price_obj = product.get('pricing', {})
        price = 0.0
        if isinstance(price_obj, dict):
            # Try different price fields
            price = price_obj.get('customerPrice', 0) or price_obj.get('price', 0) or 0
        elif isinstance(price_obj, (int, float)):
            price = price_obj
        
        # Ensure price is float
        try:
            price = float(price)
        except:
            price = 0.0
        
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
        """Extract product-level metafields"""
        metafields = {}
        
        # Important fields to preserve
        fields = [
            'styleID', 'partNumber', 'brandName', 'styleName',
            'description', 'fabric', 'gender', 'baseCategory',
            'swatchUrl', 'catalogPage'
        ]
        
        for field in fields:
            value = product.get(field)
            if value is not None and value != '':
                metafields[field] = value
        
        return metafields
    
    def _extract_variant_metafields(self, product: Dict) -> Dict:
        """Extract variant-level metafields"""
        metafields = {}
        
        # Variant-specific fields
        fields = [
            'colorName', 'colorCode', 'colorFamily',
            'sizeName', 'sizeCode', 'sizeOrder',
            'gtin', 'yourSku'
        ]
        
        for field in fields:
            value = product.get(field)
            if value is not None and value != '':
                metafields[field] = value
        
        return metafields
    
    def _extract_image_urls(self, product: Dict) -> List[str]:
        """Extract all image URLs from product"""
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

