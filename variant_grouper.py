"""
Variant Grouper - Groups S&S products by styleID into Shopify product groups
"""
from database import get_db
import json
import uuid
from typing import List, Dict, Optional
from datetime import datetime

class VariantGrouper:
    """Groups S&S products into Shopify product groups (by styleID)"""
    
    def __init__(self, sync_id: str, sync_options: Dict):
        self.sync_id = sync_id
        self.sync_options = sync_options
        self.base_url = "https://www.ssactivewear.com/"
        self.image_size = sync_options.get('image_size', '_fl')
    
    def group_products(self) -> int:
        """
        Group cached products by styleID and prepare for Shopify sync
        Returns: number of product groups created
        """
        print(f"🔄 Grouping products by styleID...")
        
        # Get cached products
        with get_db() as conn:
            cursor = conn.cursor()
            cursor.execute('''
                SELECT product_data, style_id, sku FROM ss_products_cache 
                WHERE sync_id = ?
                ORDER BY style_id, sku
            ''', (self.sync_id,))
            
            products = []
            for row in cursor.fetchall():
                try:
                    product = json.loads(row['product_data'])
                    products.append(product)
                except Exception as e:
                    print(f"⚠️ Error loading product: {e}")
                    continue
        
        if not products:
            print("⚠️ No cached products found")
            return 0
        
        # Group by styleID
        product_groups = {}
        for product in products:
            style_id = product.get('styleID')
            if not style_id:
                style_id = 'no_style'
            
            group_id = f"style_{style_id}_{self.sync_id}"
            
            if group_id not in product_groups:
                product_groups[group_id] = {
                    'group_id': group_id,
                    'style_id': style_id,
                    'products': []
                }
            
            product_groups[group_id]['products'].append(product)
        
        print(f"📦 Found {len(product_groups)} product groups from {len(products)} products")
        
        # Save groups to database
        groups_created = 0
        with get_db() as conn:
            cursor = conn.cursor()
            
            for group_id, group_data in product_groups.items():
                try:
                    # Use first product as base
                    base_product = group_data['products'][0]
                    
                    # Build title
                    title_parts = []
                    if base_product.get('brandName'):
                        title_parts.append(base_product['brandName'])
                    if base_product.get('styleName'):
                        title_parts.append(base_product['styleName'])
                    title = ' '.join(title_parts) if title_parts else base_product.get('sku', 'Product')
                    
                    # Build description
                    description = base_product.get('description', '')
                    
                    # Build product images (unique)
                    product_images = []
                    seen_images = set()
                    for p in group_data['products']:
                        if p.get('colorFrontImage'):
                            img_url = p['colorFrontImage'] if p['colorFrontImage'].startswith('http') else self.base_url + p['colorFrontImage'].replace('_fm', self.image_size)
                            if img_url not in seen_images:
                                product_images.append(img_url)
                                seen_images.add(img_url)
                    # Fallback: style-level image if no color image found
                    if not product_images and base_product.get('styleImage'):
                        img_url = base_product['styleImage'] if base_product['styleImage'].startswith('http') else self.base_url + base_product['styleImage'].replace('_fm', self.image_size)
                        product_images.append(img_url)
                        seen_images.add(img_url)
                    
                    # Build tags
                    tags = []
                    if self.sync_options.get('sync_tags', True):
                        if base_product.get('brandName'):
                            tags.append(base_product['brandName'])
                        if base_product.get('colorFamily'):
                            tags.append(base_product['colorFamily'])
                        if base_product.get('baseCategory'):
                            tags.append(base_product['baseCategory'])
                        if base_product.get('categoryNames'):
                            try:
                                for cname in base_product['categoryNames']:
                                    if cname and cname not in tags:
                                        tags.append(cname)
                            except Exception:
                                pass
                        # Add category IDs as tags if available
                        if base_product.get('categories'):
                            try:
                                cats = str(base_product['categories'])
                                tags.extend([c.strip() for c in cats.split(',') if c.strip()])
                            except Exception:
                                pass
                    
                    # Build metafields
                    metafields = {}
                    metafield_fields = [
                        'styleID', 'partNumber', 'brandName', 'styleName', 'title',
                        'baseCategory', 'catalogPageNumber', 'newStyle', 'comparableGroup',
                        'companionGroup', 'sustainableStyle'
                    ]
                    for field in metafield_fields:
                        if base_product.get(field) is not None:
                            metafields[field] = base_product[field]
                    # Include categoryNames list for downstream collections/tags
                    if base_product.get('categoryNames'):
                        metafields['categoryNames'] = base_product['categoryNames']
                    
                    # Save product group
                    cursor.execute('''
                        INSERT OR REPLACE INTO product_groups
                        (group_id, style_id, title, description, vendor, product_type, 
                         base_category, product_images, product_metafields, tags, status, sync_id)
                        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, 'pending', ?)
                    ''', (
                        group_id,
                        group_data['style_id'],
                        title,
                        description,
                        base_product.get('brandName', ''),
                        base_product.get('baseCategory', ''),
                        base_product.get('baseCategory', ''),
                        json.dumps(product_images),
                        json.dumps(metafields),
                        ', '.join(tags) if tags else '',
                        self.sync_id
                    ))
                    
                    # Save variants
                    price_field = self.sync_options.get('price_field', 'customerPrice')
                    
                    for product in group_data['products']:
                        price = product.get(price_field)
                        if not price or price == 0:
                            price = product.get('customerPrice', product.get('piecePrice', '0'))
                        
                        # Get variant image
                        variant_image = None
                        if product.get('colorFrontImage'):
                            variant_image = self.base_url + product['colorFrontImage'].replace('_fm', self.image_size)
                        
                        # Get color and size
                        color_name = product.get('colorName', '').strip() or f"Color-{product.get('sku', '')}"
                        size_name = product.get('sizeName', '').strip() or f"Size-{product.get('sku', '')}"
                        
                        # Build variant metafields
                        variant_metafields = {}
                        variant_metafield_fields = [
                            'colorName', 'colorCode', 'colorPriceCodeName', 'colorGroup', 'colorGroupName',
                            'colorFamilyID', 'colorFamily', 'sizeName', 'sizeCode', 'sizeOrder',
                            'sizePriceCodeName', 'qty', 'gtin', 'yourSku'
                        ]
                        for field in variant_metafield_fields:
                            if product.get(field) is not None:
                                variant_metafields[field] = product[field]
                        
                        cursor.execute('''
                            INSERT OR REPLACE INTO product_variants
                            (product_group_id, sku, color_name, size_name, price, inventory_quantity,
                             barcode, weight, weight_unit, variant_image_url, variant_metafields)
                            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                        ''', (
                            group_id,
                            product.get('sku', ''),
                            color_name,
                            size_name,
                            str(price),
                            product.get('qty', 0) if self.sync_options.get('update_inventory', True) else None,
                            product.get('gtin', '') or None,
                            product.get('unitWeight', 0) or 0,
                            'lb',
                            variant_image,
                            json.dumps(variant_metafields) if variant_metafields else None
                        ))
                    
                    # Save product images
                    for idx, img_url in enumerate(product_images):
                        cursor.execute('''
                            INSERT OR REPLACE INTO product_images
                            (product_group_id, image_url, image_type, sort_order)
                            VALUES (?, ?, 'product', ?)
                        ''', (group_id, img_url, idx))
                    
                    groups_created += 1
                    
                    if groups_created % 10 == 0:
                        print(f"   Created {groups_created}/{len(product_groups)} product groups...")
                        conn.commit()
                
                except Exception as e:
                    print(f"⚠️ Error creating product group {group_id}: {e}")
                    import traceback
                    traceback.print_exc()
                    continue
            
            conn.commit()
        
        print(f"✅ Created {groups_created} product groups with variants")
        return groups_created
    
    def get_product_groups(self, status: Optional[str] = None) -> List[Dict]:
        """Get product groups from database (optionally filtered by status)"""
        with get_db() as conn:
            cursor = conn.cursor()
            
            if status:
                cursor.execute('''
                    SELECT * FROM product_groups 
                    WHERE sync_id IS NULL OR sync_id = ?
                    AND status = ?
                    ORDER BY created_at
                ''', (self.sync_id, status))
            else:
                cursor.execute('''
                    SELECT * FROM product_groups 
                    WHERE sync_id IS NULL OR sync_id = ?
                    ORDER BY created_at
                ''', (self.sync_id,))
            
            groups = []
            for row in cursor.fetchall():
                group = dict(row)
                # Parse JSON fields
                if group.get('product_images'):
                    group['product_images'] = json.loads(group['product_images'])
                if group.get('product_metafields'):
                    group['product_metafields'] = json.loads(group['product_metafields'])
                if group.get('collections'):
                    group['collections'] = json.loads(group['collections']) if group['collections'] else []
                groups.append(group)
            
            return groups
    
    def get_variants_for_group(self, group_id: str) -> List[Dict]:
        """Get all variants for a product group"""
        with get_db() as conn:
            cursor = conn.cursor()
            cursor.execute('''
                SELECT * FROM product_variants 
                WHERE product_group_id = ?
                ORDER BY color_name, size_name
            ''', (group_id,))
            
            variants = []
            for row in cursor.fetchall():
                variant = dict(row)
                # Parse JSON fields
                if variant.get('variant_metafields'):
                    variant['variant_metafields'] = json.loads(variant['variant_metafields'])
                variants.append(variant)
            
            return variants
    
    def get_images_for_group(self, group_id: str) -> List[Dict]:
        """Get all images for a product group"""
        with get_db() as conn:
            cursor = conn.cursor()
            cursor.execute('''
                SELECT * FROM product_images 
                WHERE product_group_id = ?
                ORDER BY sort_order
            ''', (group_id,))
            
            return [dict(row) for row in cursor.fetchall()]

