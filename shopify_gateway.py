"""
Shopify Gateway - Clean API layer (no business logic)

Responsibility: Execute Shopify API commands with proper error handling
Knows about: 100-variant limit, rate limiting, retries
Knows nothing about: Style domain, reconciliation, business rules
"""

import requests
import time
import json
import urllib.parse
from typing import List, Dict, Optional, Tuple
from domain_models import StylePart


def delete_all_products_helper(gateway) -> int:
    """Delete all products - helper function"""
    graphql_url = f"{gateway.shop_domain}/admin/api/{gateway.api_version}/graphql.json"
    deleted_count = 0
    
    try:
        query = """
        query {
            products(first: 250) {
                edges {
                    node {
                        id
                    }
                }
            }
        }
        """
        
        resp = requests.post(graphql_url, headers=gateway.headers, json={'query': query}, timeout=30)
        
        if resp.status_code == 200:
            result = resp.json()
            products_edges = result.get('data', {}).get('products', {}).get('edges', [])
            
            for edge in products_edges:
                node = edge.get('node', {})
                product_gid = node.get('id', '')
                product_id = product_gid.replace('gid://shopify/Product/', '')
                
                if product_id:
                    delete_url = f"{gateway.base_url}/products/{product_id}.json"
                    del_resp = requests.delete(delete_url, headers=gateway.headers, timeout=30)
                    
                    if del_resp.status_code in [200, 204]:
                        deleted_count += 1
                    
                    time.sleep(0.2)
    except:
        pass
    
    return deleted_count


class ShopifyGateway:
    """
    Gateway to Shopify Admin API
    All methods are command-style: execute and return result
    """
    
    def __init__(self, shop_domain: str, access_token: str):
        self.shop_domain = shop_domain.replace('https://', '').replace('http://', '').strip('/')
        if not self.shop_domain.startswith('http'):
            self.shop_domain = f"https://{self.shop_domain}"
        
        self.access_token = access_token
        self.api_version = "2025-10"
        self.base_url = f"{self.shop_domain}/admin/api/{self.api_version}"
        self.headers = {
            "X-Shopify-Access-Token": access_token,
            "Content-Type": "application/json"
        }
    
    def create_product_with_variants(self, style_part: StylePart) -> Tuple[int, str, List[Dict]]:
        """
        Create product with up to 100 variants using REST API
        
        CRITICAL: Deletes any existing product with same title first
        
        Returns: (product_id, product_gid, created_variants)
        Raises: Exception on failure
        """
        if style_part.variant_count > 100:
            raise ValueError(f"Cannot create product with {style_part.variant_count} variants. Max is 100. Use split_into_parts first.")
        
        print(f"   Creating product: {style_part.title} ({style_part.variant_count} variants)")
        
        # Build REST API payload
        # Variants are now pre-merged by StyleBuilder (no duplicates)
        variants_payload = []
        
        for v in style_part.variants:
            variant = {
                'option1': v.color_name,  # Clean color name (no numbering needed)
                'option2': v.size_name,   # Size
                'sku': v.sku,             # Primary SKU
                'price': str(v.price),
                'barcode': v.barcode,
                'weight': float(v.weight),
                'weight_unit': 'lb',
                'inventory_management': 'shopify',
                'inventory_policy': 'deny'
            }
            
            # Add aggregated inventory
            if v.inventory_quantity is not None:
                variant['inventory_quantity'] = int(v.inventory_quantity)
            
            variants_payload.append(variant)
        
        print(f"   Final payload: {len(variants_payload)} unique variants (from {style_part.variant_count} total)")
        
        # DEBUG: Log all option combinations to check for duplicates
        if len(variants_payload) <= 10:
            print(f"   DEBUG: All variant options:")
            for idx, v in enumerate(variants_payload):
                print(f"     {idx+1}. {v['sku']}: {v['option1']} / {v['option2']}")
        
        # Build images payload with alt tags for variant-image linking
        images_payload = []
        if style_part.style.images:
            for img in style_part.style.images:
                if img.url:
                    img_data = {'src': img.url}
                    # Add alt text for variant-image linking (e.g., #Color_White)
                    if img.alt_text:
                        img_data['alt'] = img.alt_text
                    images_payload.append(img_data)
            print(f"   📸 Adding {len(images_payload)} product images with color alt tags")
        
        # Product payload - CRITICAL: Must define options for Color and Size!
        payload = {
            'product': {
                'title': style_part.title,
                'body_html': style_part.style.description,
                'vendor': style_part.style.brand,
                'product_type': style_part.style.product_type,
                'tags': ', '.join(style_part.style.tags),
                'status': 'active',
                'options': [
                    {'name': 'Color'},
                    {'name': 'Size'}
                ],
                'variants': variants_payload,
                'images': images_payload
            }
        }
        
        # DEBUG: Log payload to see duplicates
        print(f"   📋 PAYLOAD DEBUG:")
        print(f"      Product title: {payload['product']['title']}")
        print(f"      Variants count: {len(variants_payload)}")
        
        # Check for duplicates in payload
        payload_options = {}
        for idx, v in enumerate(variants_payload):
            option_tuple = (v['option1'], v['option2'])
            if option_tuple in payload_options:
                print(f"      ❌ DUPLICATE in payload: Variant {idx+1} ({v['sku']}) has same options as Variant {payload_options[option_tuple]} ({v['option1']} / {v['option2']})")
            else:
                payload_options[option_tuple] = idx+1
        
        if len(payload_options) < len(variants_payload):
            print(f"      ⚠️ WARNING: {len(variants_payload)} variants but only {len(payload_options)} unique option combinations!")
        else:
            print(f"      ✅ All {len(variants_payload)} variants have unique option combinations")
        
        # Send request
        url = f"{self.base_url}/products.json"
        response = requests.post(url, headers=self.headers, json=payload, timeout=60)
        
        if response.status_code not in [200, 201]:
            error_msg = f"HTTP {response.status_code}"
            try:
                error_data = response.json()
                error_msg += f": {error_data}"
            except:
                error_msg += f": {response.text[:500]}"
            raise Exception(f"Failed to create product: {error_msg}")
        
        result = response.json()
        product = result.get('product', {})
        product_id = product.get('id')
        
        if not product_id:
            raise Exception(f"No product ID returned: {result}")
        
        product_gid = f"gid://shopify/Product/{product_id}"
        
        # Extract created variants
        created_variants = []
        for variant in product.get('variants', []):
            created_variants.append({
                'id': variant.get('id'),
                'gid': f"gid://shopify/ProductVariant/{variant['id']}",
                'sku': variant.get('sku', ''),
                'option1': variant.get('option1', ''),  # Color
                'price': variant.get('price', '0')
            })
        
        print(f"   ✅ Product created: ID={product_id}, Variants={len(created_variants)}")
        
        # CRITICAL: Assign images to variants based on color matching
        self._assign_images_to_variants(product_id, product)
        
        return product_id, product_gid, created_variants
    
    def _assign_images_to_variants(self, product_id: int, product_data: Dict):
        """
        Assign images to variants based on color matching.
        
        This ensures that when a customer selects a color variant,
        the correct product image is displayed.
        
        Matching logic:
        - Image alt text: "#Color_Faded Mustard" → color: "Faded Mustard"
        - Variant option1: "Faded Mustard"
        - All variants with matching color get the same image_id
        """
        images = product_data.get('images', [])
        variants = product_data.get('variants', [])
        
        if not images or not variants:
            print(f"   ⚠️ No images or variants to link")
            return
        
        # Build color → image_id mapping from alt tags
        # Alt format: "#Color_Faded Mustard" or "#Color_Tri Athletic Grey"
        color_to_image = {}
        for img in images:
            alt = img.get('alt', '') or ''
            image_id = img.get('id')
            
            if alt.startswith('#Color_') and image_id:
                # Extract color name: "#Color_Faded Mustard" → "Faded Mustard"
                color_name = alt.replace('#Color_', '').strip()
                if color_name:
                    # Normalize: lowercase for matching
                    color_key = color_name.lower()
                    if color_key not in color_to_image:
                        color_to_image[color_key] = image_id
                        print(f"   🖼️ Image {image_id} mapped to color: {color_name}")
        
        if not color_to_image:
            print(f"   ⚠️ No color mappings found in image alt tags")
            return
        
        # Assign images to variants
        assigned_count = 0
        for variant in variants:
            variant_id = variant.get('id')
            variant_color = variant.get('option1', '')  # Color is option1
            
            if not variant_id or not variant_color:
                continue
            
            # Normalize color for matching
            color_key = variant_color.lower()
            
            if color_key in color_to_image:
                image_id = color_to_image[color_key]
                
                # Update variant with image_id
                try:
                    url = f"{self.base_url}/variants/{variant_id}.json"
                    payload = {'variant': {'image_id': image_id}}
                    resp = requests.put(url, headers=self.headers, json=payload, timeout=15)
                    
                    if resp.status_code == 200:
                        assigned_count += 1
                    else:
                        print(f"   ⚠️ Failed to assign image to variant {variant_id}: {resp.status_code}")
                    
                    time.sleep(0.1)  # Small delay for rate limiting
                except Exception as e:
                    print(f"   ⚠️ Error assigning image to variant {variant_id}: {e}")
        
        print(f"   ✅ Assigned images to {assigned_count}/{len(variants)} variants")
    
    def add_product_images(self, product_id: int, image_urls: List[str]) -> int:
        """
        Add images to product using REST API
        Returns: number of images added
        """
        if not image_urls:
            return 0
        
        added_count = 0
        for img_url in image_urls:
            if not img_url or not img_url.strip():
                continue
            
            try:
                url = f"{self.base_url}/products/{product_id}/images.json"
                payload = {'image': {'src': img_url.strip()}}
                resp = requests.post(url, headers=self.headers, json=payload, timeout=30)
                
                if resp.status_code in [200, 201]:
                    added_count += 1
                
                time.sleep(0.3)  # Rate limiting
            except:
                pass
        
        return added_count
    
    def add_variant_images(self, product_id: int, sku_to_image: Dict[str, str],
                          sku_to_variant_id: Dict[str, int]) -> int:
        """
        Add variant-specific images
        Returns: number of images added
        """
        if not sku_to_image or not sku_to_variant_id:
            return 0
        
        added_count = 0
        for sku, img_url in sku_to_image.items():
            variant_id = sku_to_variant_id.get(sku)
            if not variant_id or not img_url:
                continue
            
            try:
                url = f"{self.base_url}/products/{product_id}/images.json"
                payload = {
                    'image': {
                        'src': img_url.strip(),
                        'variant_ids': [variant_id]
                    }
                }
                resp = requests.post(url, headers=self.headers, json=payload, timeout=30)
                
                if resp.status_code in [200, 201]:
                    added_count += 1
                
                time.sleep(0.3)  # Rate limiting
            except:
                pass
        
        return added_count
    
    def update_metafields(self, product_gid: str, metafields: Dict) -> bool:
        """
        Update product metafields using GraphQL
        Returns: success status
        """
        if not metafields:
            return True
        
        # Build metafield inputs
        inputs = []
        for key, value in metafields.items():
            # Determine value type
            if isinstance(value, bool):
                value_type = "boolean"
                value_str = "true" if value else "false"
            elif isinstance(value, int):
                value_type = "number_integer"
                value_str = str(value)
            elif isinstance(value, (dict, list)):
                value_type = "json"
                value_str = json.dumps(value)
            else:
                value_type = "single_line_text_field"
                value_str = str(value)
            
            inputs.append({
                "ownerId": product_gid,
                "namespace": "ssactivewear",
                "key": str(key).lower().replace(' ', '_'),
                "type": value_type,
                "value": value_str
            })
        
        if not inputs:
            return True
        
        # GraphQL mutation
        mutation = """
        mutation metafieldsSet($metafields: [MetafieldsSetInput!]!) {
            metafieldsSet(metafields: $metafields) {
                metafields { id key }
                userErrors { field message }
            }
        }
        """
        
        try:
            graphql_url = f"{self.shop_domain}/admin/api/{self.api_version}/graphql.json"
            response = requests.post(
                graphql_url,
                headers=self.headers,
                json={'query': mutation, 'variables': {'metafields': inputs}},
                timeout=30
            )
            response.raise_for_status()
            
            result = response.json()
            user_errors = result.get('data', {}).get('metafieldsSet', {}).get('userErrors', [])
            
            if user_errors:
                print(f"   ⚠️ Metafield errors: {user_errors[0].get('message')}")
                return False
            
            return True
        except Exception as e:
            print(f"   ⚠️ Metafield update failed: {e}")
            return False
    
    def get_product_by_id(self, product_id: int) -> Optional[Dict]:
        """
        Fetch product by ID using REST API
        Returns: product data or None
        """
        try:
            url = f"{self.base_url}/products/{product_id}.json"
            response = requests.get(url, headers=self.headers, timeout=30)
            
            if response.status_code == 200:
                return response.json().get('product')
            
            return None
        except:
            return None
    
    def delete_all_products(self) -> int:
        """Delete all products from Shopify"""
        return delete_all_products_helper(self)

