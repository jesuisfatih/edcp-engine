"""
Shopify Gateway - Clean API layer (no business logic)

Responsibility: Execute Shopify API commands with proper error handling
Knows about: 100-variant limit, rate limiting, retries
Knows nothing about: Style domain, reconciliation, business rules
"""

import requests
import time
import json
from typing import List, Dict, Optional, Tuple
from domain_models import StylePart


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
        
        # CRITICAL: Delete any existing product with same title
        # This prevents "variant already exists" errors
        try:
            search_url = f"{self.base_url}/products.json?title={requests.utils.quote(style_part.title)}&limit=10"
            search_resp = requests.get(search_url, headers=self.headers, timeout=30)
            
            if search_resp.status_code == 200:
                existing = search_resp.json().get('products', [])
                for product in existing:
                    if product.get('title', '').strip().lower() == style_part.title.strip().lower():
                        product_id = product.get('id')
                        print(f"   🗑️ Deleting existing product {product_id}: {product.get('title')}")
                        delete_url = f"{self.base_url}/products/{product_id}.json"
                        requests.delete(delete_url, headers=self.headers, timeout=30)
                        time.sleep(0.3)
        except Exception as e:
            print(f"   ⚠️ Could not check/delete existing products: {e}")
            # Continue anyway
        
        # Build REST API payload with deduplication
        variants_payload = []
        seen_options = set()  # Track option combinations to avoid duplicates
        
        for v in style_part.variants:
            # CRITICAL: Case-insensitive and whitespace-safe deduplication
            option_key = (
                v.color_name.strip().lower() if v.color_name else '',
                v.size_name.strip().lower() if v.size_name else ''
            )
            
            # Skip duplicate option combinations
            if option_key in seen_options:
                print(f"   ⚠️ Skipping duplicate variant: {v.sku} ({v.color_name} / {v.size_name})")
                continue
            
            seen_options.add(option_key)
            
            variant = {
                'option1': v.color_name,
                'option2': v.size_name,
                'sku': v.sku,
                'price': str(v.price),
                'barcode': v.barcode,
                'weight': float(v.weight),
                'weight_unit': 'lb',
                'inventory_management': 'shopify',
                'inventory_policy': 'deny'
            }
            
            # Add inventory if available
            if v.inventory_quantity is not None:
                variant['inventory_quantity'] = int(v.inventory_quantity)
            
            variants_payload.append(variant)
        
        print(f"   Final payload: {len(variants_payload)} unique variants (from {style_part.variant_count} total)")
        
        # DEBUG: Log all option combinations to check for duplicates
        if len(variants_payload) <= 10:
            print(f"   DEBUG: All variant options:")
            for idx, v in enumerate(variants_payload):
                print(f"     {idx+1}. {v['sku']}: {v['option1']} / {v['option2']}")
        
        # Product payload
        payload = {
            'product': {
                'title': style_part.title,
                'body_html': style_part.style.description,
                'vendor': style_part.style.brand,
                'product_type': style_part.style.product_type,
                'tags': ', '.join(style_part.style.tags),
                'status': 'active',
                'variants': variants_payload
            }
        }
        
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
                'price': variant.get('price', '0')
            })
        
        print(f"   ✅ Product created: ID={product_id}, Variants={len(created_variants)}")
        
        return product_id, product_gid, created_variants
    
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

