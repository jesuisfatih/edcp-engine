"""
Shopify Gateway - 100% GraphQL API Layer (Shopify 2025-10)

Uses productSet mutation for creating products with up to 2000 variants.
All operations use GraphQL - NO REST API!
"""

import requests
import time
import json
from typing import List, Dict, Optional, Tuple
from domain_models import StylePart


class ShopifyGateway:
    """
    Gateway to Shopify Admin GraphQL API (2025-10)
    Uses productSet mutation for 2000+ variant support
    """
    
    def __init__(self, shop_domain: str, access_token: str):
        self.shop_domain = shop_domain.replace('https://', '').replace('http://', '').strip('/')
        if not self.shop_domain.startswith('http'):
            self.shop_domain = f"https://{self.shop_domain}"
        
        self.access_token = access_token
        self.api_version = "2025-10"
        self.graphql_url = f"{self.shop_domain}/admin/api/{self.api_version}/graphql.json"
        self.headers = {
            "X-Shopify-Access-Token": access_token,
            "Content-Type": "application/json"
        }
    
    def _execute_graphql(self, query: str, variables: Dict = None) -> Dict:
        """Execute GraphQL query/mutation with error handling"""
        payload = {'query': query}
        if variables:
            payload['variables'] = variables
        
        response = requests.post(
            self.graphql_url,
            headers=self.headers,
            json=payload,
            timeout=120
        )
        
        if response.status_code != 200:
            raise Exception(f"GraphQL HTTP {response.status_code}: {response.text[:500]}")
        
        result = response.json()
        
        if 'errors' in result:
            error_msgs = [e.get('message', str(e)) for e in result['errors']]
            raise Exception(f"GraphQL errors: {'; '.join(error_msgs)}")
        
        return result
    
    def create_product_with_variants(self, style_part: StylePart) -> Tuple[int, str, List[Dict]]:
        """
        Create product with up to 2000 variants using GraphQL productSet mutation
        
        Shopify 2025-10 API uses ProductSetInput structure:
        - productOptions: [{name, position, values: [{name}]}]
        - variants: [{optionValues: [{optionName, name}], price, sku, ...}]
        
        Returns: (product_id, product_gid, created_variants)
        """
        if style_part.variant_count > 2000:
            raise ValueError(f"Cannot create product with {style_part.variant_count} variants. Max is 2000.")
        
        print(f"   🚀 Creating product via GraphQL productSet: {style_part.title} ({style_part.variant_count} variants)")
        
        # Extract unique colors and sizes for productOptions
        colors = []
        sizes = []
        color_set = set()
        size_set = set()
        
        for v in style_part.variants:
            if v.color_name and v.color_name not in color_set:
                color_set.add(v.color_name)
                colors.append({"name": v.color_name})
            if v.size_name and v.size_name not in size_set:
                size_set.add(v.size_name)
                sizes.append({"name": v.size_name})
        
        print(f"   📊 Unique colors: {len(colors)}, Unique sizes: {len(sizes)}")
        
        # Build productOptions (Shopify 2025-10 format)
        product_options = [
            {
                "name": "Color",
                "position": 1,
                "values": colors
            },
            {
                "name": "Size",
                "position": 2,
                "values": sizes
            }
        ]
        
        # Build variants with optionValues (Shopify 2025-10 format)
        variants = []
        for v in style_part.variants:
            variant = {
                "optionValues": [
                    {"optionName": "Color", "name": v.color_name},
                    {"optionName": "Size", "name": v.size_name}
                ],
                "price": str(v.price),
                "sku": v.sku
            }
            
            if v.barcode:
                variant["barcode"] = v.barcode
            
            variants.append(variant)
        
        # Build media/files for images
        files = []
        if style_part.style.images:
            for img in style_part.style.images:
                if img.url:
                    file_input = {
                        "originalSource": img.url,
                        "contentType": "IMAGE"
                    }
                    if img.alt_text:
                        file_input["alt"] = img.alt_text
                    files.append(file_input)
        
        # GraphQL productSet mutation (Shopify 2025-10)
        mutation = """
        mutation productSet($synchronous: Boolean!, $productSet: ProductSetInput!) {
            productSet(synchronous: $synchronous, input: $productSet) {
                product {
                    id
                    legacyResourceId
                    title
                    handle
                    variants(first: 250) {
                        edges {
                            node {
                                id
                                legacyResourceId
                                sku
                                selectedOptions {
                                    name
                                    value
                                }
                                price
                            }
                        }
                    }
                    media(first: 50) {
                        edges {
                            node {
                                ... on MediaImage {
                                    id
                                    alt
                                }
                            }
                        }
                    }
                }
                productSetOperation {
                    id
                    status
                    userErrors {
                        field
                        message
                    }
                }
                userErrors {
                    field
                    message
                }
            }
        }
        """
        
        # Build ProductSetInput
        product_set_input = {
            "title": style_part.title,
            "descriptionHtml": style_part.style.description or "",
            "vendor": style_part.style.brand,
            "productType": style_part.style.product_type or "",
            "tags": style_part.style.tags,
            "status": "ACTIVE",
            "productOptions": product_options,
            "variants": variants
        }
        
        # Add files if any
        if files:
            product_set_input["files"] = files
        
        variables = {
            "synchronous": True,  # Wait for completion
            "productSet": product_set_input
        }
        
        print(f"   📋 Sending {len(variants)} variants, {len(files)} images via productSet...")
        
        # Execute mutation
        result = self._execute_graphql(mutation, variables)
        
        # Check for errors
        product_set_result = result.get('data', {}).get('productSet', {})
        
        # Check userErrors
        user_errors = product_set_result.get('userErrors', [])
        if user_errors:
            error_msgs = [f"{e.get('field', 'unknown')}: {e.get('message', '')}" for e in user_errors]
            raise Exception(f"productSet userErrors: {'; '.join(error_msgs)}")
        
        # Check productSetOperation userErrors
        operation = product_set_result.get('productSetOperation', {})
        op_errors = operation.get('userErrors', [])
        if op_errors:
            error_msgs = [f"{e.get('field', 'unknown')}: {e.get('message', '')}" for e in op_errors]
            raise Exception(f"productSetOperation errors: {'; '.join(error_msgs)}")
        
        product = product_set_result.get('product')
        if not product:
            raise Exception(f"No product returned from productSet: {result}")
        
        product_gid = product.get('id')
        product_id = int(product.get('legacyResourceId'))
        
        # Extract created variants
        created_variants = []
        variants_edges = product.get('variants', {}).get('edges', [])
        
        for edge in variants_edges:
            node = edge.get('node', {})
            variant_id = int(node.get('legacyResourceId'))
            options = node.get('selectedOptions', [])
            color = next((o.get('value', '') for o in options if o.get('name') == 'Color'), '')
            
            created_variants.append({
                'id': variant_id,
                'gid': node.get('id'),
                'sku': node.get('sku', ''),
                'option1': color,
                'price': node.get('price', '0')
            })
        
        print(f"   ✅ Product created via productSet: ID={product_id}, Variants={len(created_variants)}")
        
        # If more than 250 variants, fetch remaining
        if style_part.variant_count > 250:
            additional = self._fetch_remaining_variants(product_gid, 250)
            created_variants.extend(additional)
            print(f"   📦 Total variants: {len(created_variants)}")
        
        # Assign images to variants based on color
        self._assign_images_to_variants_graphql(product_gid, product)
        
        return product_id, product_gid, created_variants
    
    def _fetch_remaining_variants(self, product_gid: str, already_fetched: int) -> List[Dict]:
        """Fetch remaining variants using cursor pagination"""
        additional_variants = []
        
        query = """
        query getVariants($productId: ID!, $first: Int!, $after: String) {
            product(id: $productId) {
                variants(first: $first, after: $after) {
                    edges {
                        cursor
                        node {
                            id
                            legacyResourceId
                            sku
                            selectedOptions {
                                name
                                value
                            }
                            price
                        }
                    }
                    pageInfo {
                        hasNextPage
                        endCursor
                    }
                }
            }
        }
        """
        
        # Get cursor from first 250
        variables = {'productId': product_gid, 'first': 250, 'after': None}
        result = self._execute_graphql(query, variables)
        
        page_info = result.get('data', {}).get('product', {}).get('variants', {}).get('pageInfo', {})
        has_next = page_info.get('hasNextPage', False)
        cursor = page_info.get('endCursor')
        
        while has_next and cursor:
            variables['after'] = cursor
            result = self._execute_graphql(query, variables)
            
            variants_data = result.get('data', {}).get('product', {}).get('variants', {})
            edges = variants_data.get('edges', [])
            
            for edge in edges:
                node = edge.get('node', {})
                options = node.get('selectedOptions', [])
                color = next((o.get('value', '') for o in options if o.get('name') == 'Color'), '')
                
                additional_variants.append({
                    'id': int(node.get('legacyResourceId')),
                    'gid': node.get('id'),
                    'sku': node.get('sku', ''),
                    'option1': color,
                    'price': node.get('price', '0')
                })
            
            page_info = variants_data.get('pageInfo', {})
            has_next = page_info.get('hasNextPage', False)
            cursor = page_info.get('endCursor')
            
            time.sleep(0.1)  # Rate limiting
        
        return additional_variants
    
    def _assign_images_to_variants_graphql(self, product_gid: str, product_data: Dict):
        """Assign images to variants based on color matching"""
        media_edges = product_data.get('media', {}).get('edges', [])
        variants_edges = product_data.get('variants', {}).get('edges', [])
        
        if not media_edges or not variants_edges:
            print(f"   ⚠️ No images or variants to link")
            return
        
        # Build color → media_id mapping from alt tags
        color_to_media = {}
        for edge in media_edges:
            node = edge.get('node', {})
            alt = node.get('alt', '') or ''
            media_id = node.get('id')
            
            if alt.startswith('#Color_') and media_id:
                color_name = alt.replace('#Color_', '').strip().lower()
                if color_name and color_name not in color_to_media:
                    color_to_media[color_name] = media_id
        
        if not color_to_media:
            print(f"   ⚠️ No color mappings found in image alt tags")
            return
        
        # Group variants by color
        color_to_variants = {}
        for edge in variants_edges:
            node = edge.get('node', {})
            options = node.get('selectedOptions', [])
            variant_gid = node.get('id')
            
            color = next((o.get('value', '').lower() for o in options if o.get('name') == 'Color'), '')
            if color in color_to_media and variant_gid:
                if color not in color_to_variants:
                    color_to_variants[color] = []
                color_to_variants[color].append(variant_gid)
        
        # Use productVariantsBulkUpdate for efficiency
        mutation = """
        mutation productVariantsBulkUpdate($productId: ID!, $variants: [ProductVariantsBulkInput!]!) {
            productVariantsBulkUpdate(productId: $productId, variants: $variants) {
                productVariants {
                    id
                }
                userErrors {
                    field
                    message
                }
            }
        }
        """
        
        # Build bulk update input
        variant_updates = []
        for color, variant_gids in color_to_variants.items():
            media_id = color_to_media.get(color)
            if media_id:
                for variant_gid in variant_gids:
                    variant_updates.append({
                        "id": variant_gid,
                        "mediaId": media_id
                    })
        
        if not variant_updates:
            print(f"   ⚠️ No variant-image associations to make")
            return
        
        # Execute in batches of 100
        batch_size = 100
        assigned_count = 0
        
        for i in range(0, len(variant_updates), batch_size):
            batch = variant_updates[i:i+batch_size]
            
            try:
                variables = {
                    "productId": product_gid,
                    "variants": batch
                }
                
                result = self._execute_graphql(mutation, variables)
                updated = result.get('data', {}).get('productVariantsBulkUpdate', {}).get('productVariants', [])
                assigned_count += len(updated)
                
                time.sleep(0.1)
            except Exception as e:
                print(f"   ⚠️ Batch update error: {e}")
        
        print(f"   ✅ Assigned images to {assigned_count}/{len(variant_updates)} variants")
    
    def add_product_images(self, product_id: int, image_urls: List[str]) -> int:
        """Add images to product using GraphQL"""
        if not image_urls:
            return 0
        
        product_gid = f"gid://shopify/Product/{product_id}"
        
        mutation = """
        mutation productCreateMedia($productId: ID!, $media: [CreateMediaInput!]!) {
            productCreateMedia(productId: $productId, media: $media) {
                media {
                    ... on MediaImage {
                        id
                    }
                }
                mediaUserErrors {
                    field
                    message
                }
            }
        }
        """
        
        media_inputs = []
        for url in image_urls:
            if url and url.strip():
                media_inputs.append({
                    'originalSource': url.strip(),
                    'mediaContentType': 'IMAGE'
                })
        
        if not media_inputs:
            return 0
        
        try:
            variables = {
                'productId': product_gid,
                'media': media_inputs
            }
            
            result = self._execute_graphql(mutation, variables)
            media_created = result.get('data', {}).get('productCreateMedia', {}).get('media', [])
            return len(media_created)
        except Exception as e:
            print(f"   ⚠️ Failed to add images: {e}")
            return 0
    
    def add_variant_images(self, product_id: int, sku_to_image: Dict[str, str],
                          sku_to_variant_id: Dict[str, int]) -> int:
        """Add variant-specific images - handled in _assign_images_to_variants_graphql"""
        return 0
    
    def update_metafields(self, product_gid: str, metafields: Dict) -> bool:
        """Update product metafields using GraphQL"""
        if not metafields:
            return True
        
        inputs = []
        for key, value in metafields.items():
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
        
        mutation = """
        mutation metafieldsSet($metafields: [MetafieldsSetInput!]!) {
            metafieldsSet(metafields: $metafields) {
                metafields { id key }
                userErrors { field message }
            }
        }
        """
        
        try:
            result = self._execute_graphql(mutation, {'metafields': inputs})
            user_errors = result.get('data', {}).get('metafieldsSet', {}).get('userErrors', [])
            
            if user_errors:
                print(f"   ⚠️ Metafield errors: {user_errors[0].get('message')}")
                return False
            
            return True
        except Exception as e:
            print(f"   ⚠️ Metafield update failed: {e}")
            return False
    
    def get_product_by_id(self, product_id: int) -> Optional[Dict]:
        """Fetch product by ID using GraphQL"""
        query = """
        query getProduct($id: ID!) {
            product(id: $id) {
                id
                legacyResourceId
                title
                handle
                variants(first: 250) {
                    edges {
                        node {
                            id
                            legacyResourceId
                            sku
                        }
                    }
                }
            }
        }
        """
        
        try:
            product_gid = f"gid://shopify/Product/{product_id}"
            result = self._execute_graphql(query, {'id': product_gid})
            product = result.get('data', {}).get('product')
            
            if product:
                variants = []
                for edge in product.get('variants', {}).get('edges', []):
                    node = edge.get('node', {})
                    variants.append({
                        'id': int(node.get('legacyResourceId')),
                        'sku': node.get('sku', '')
                    })
                
                return {
                    'id': int(product.get('legacyResourceId')),
                    'title': product.get('title'),
                    'handle': product.get('handle'),
                    'variants': variants
                }
            
            return None
        except:
            return None
    
    def delete_all_products(self) -> int:
        """Delete all products using GraphQL"""
        deleted_count = 0
        
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
        
        mutation = """
        mutation productDelete($input: ProductDeleteInput!) {
            productDelete(input: $input) {
                deletedProductId
                userErrors {
                    field
                    message
                }
            }
        }
        """
        
        try:
            result = self._execute_graphql(query)
            products_edges = result.get('data', {}).get('products', {}).get('edges', [])
            
            for edge in products_edges:
                product_gid = edge.get('node', {}).get('id')
                if product_gid:
                    try:
                        del_result = self._execute_graphql(mutation, {
                            'input': {'id': product_gid}
                        })
                        
                        if del_result.get('data', {}).get('productDelete', {}).get('deletedProductId'):
                            deleted_count += 1
                        
                        time.sleep(0.2)
                    except:
                        pass
        except:
            pass
        
        return deleted_count
