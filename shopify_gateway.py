"""
Shopify Gateway - 100% GraphQL API Layer (NO REST!)

Responsibility: Execute Shopify GraphQL API commands
Supports: Up to 2048 variants per product (GraphQL 2024-04+)
"""

import requests
import time
import json
from typing import List, Dict, Optional, Tuple
from domain_models import StylePart


class ShopifyGateway:
    """
    Gateway to Shopify Admin GraphQL API
    ALL operations use GraphQL - NO REST API!
    """
    
    def __init__(self, shop_domain: str, access_token: str):
        self.shop_domain = shop_domain.replace('https://', '').replace('http://', '').strip('/')
        if not self.shop_domain.startswith('http'):
            self.shop_domain = f"https://{self.shop_domain}"
        
        self.access_token = access_token
        self.api_version = "2024-10"  # Use 2024-04+ for 2048 variant support
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
            timeout=120  # Longer timeout for large operations
        )
        
        if response.status_code != 200:
            raise Exception(f"GraphQL HTTP {response.status_code}: {response.text[:500]}")
        
        result = response.json()
        
        # Check for GraphQL errors
        if 'errors' in result:
            error_msgs = [e.get('message', str(e)) for e in result['errors']]
            raise Exception(f"GraphQL errors: {'; '.join(error_msgs)}")
        
        return result
    
    def create_product_with_variants(self, style_part: StylePart) -> Tuple[int, str, List[Dict]]:
        """
        Create product with up to 2048 variants using GraphQL productCreate mutation
        
        Returns: (product_id, product_gid, created_variants)
        Raises: Exception on failure
        """
        if style_part.variant_count > 2048:
            raise ValueError(f"Cannot create product with {style_part.variant_count} variants. Max is 2048.")
        
        print(f"   🚀 Creating product via GraphQL: {style_part.title} ({style_part.variant_count} variants)")
        
        # Build variant inputs for GraphQL
        variant_inputs = []
        for v in style_part.variants:
            variant_input = {
                'options': [v.color_name, v.size_name],
                'sku': v.sku,
                'price': str(v.price),
                'inventoryManagement': 'SHOPIFY',
                'inventoryPolicy': 'DENY'
            }
            
            # Add barcode if available
            if v.barcode:
                variant_input['barcode'] = v.barcode
            
            # Add weight
            if v.weight:
                variant_input['weight'] = float(v.weight)
                variant_input['weightUnit'] = 'POUNDS'
            
            variant_inputs.append(variant_input)
        
        # Build media inputs (images with alt tags)
        media_inputs = []
        if style_part.style.images:
            for img in style_part.style.images:
                if img.url:
                    media_input = {
                        'originalSource': img.url,
                        'mediaContentType': 'IMAGE'
                    }
                    if img.alt_text:
                        media_input['alt'] = img.alt_text
                    media_inputs.append(media_input)
        
        # GraphQL mutation for creating product with variants
        mutation = """
        mutation productCreate($input: ProductInput!, $media: [CreateMediaInput!]) {
            productCreate(input: $input, media: $media) {
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
                                    image {
                                        id
                                    }
                                }
                            }
                        }
                    }
                }
                userErrors {
                    field
                    message
                }
            }
        }
        """
        
        # Build product input
        product_input = {
            'title': style_part.title,
            'descriptionHtml': style_part.style.description or '',
            'vendor': style_part.style.brand,
            'productType': style_part.style.product_type or '',
            'tags': style_part.style.tags,
            'status': 'ACTIVE',
            'options': ['Color', 'Size'],
            'variants': variant_inputs
        }
        
        variables = {
            'input': product_input,
            'media': media_inputs if media_inputs else None
        }
        
        print(f"   📋 Sending {len(variant_inputs)} variants, {len(media_inputs)} images to Shopify GraphQL...")
        
        # Execute mutation
        result = self._execute_graphql(mutation, variables)
        
        # Check for user errors
        product_create = result.get('data', {}).get('productCreate', {})
        user_errors = product_create.get('userErrors', [])
        
        if user_errors:
            error_msgs = [f"{e.get('field', 'unknown')}: {e.get('message', '')}" for e in user_errors]
            raise Exception(f"Product creation failed: {'; '.join(error_msgs)}")
        
        product = product_create.get('product')
        if not product:
            raise Exception(f"No product returned from GraphQL: {result}")
        
        product_gid = product.get('id')
        product_id = int(product.get('legacyResourceId'))
        
        # Extract created variants
        created_variants = []
        variants_edges = product.get('variants', {}).get('edges', [])
        
        for edge in variants_edges:
            node = edge.get('node', {})
            variant_id = int(node.get('legacyResourceId'))
            options = node.get('selectedOptions', [])
            color = options[0].get('value', '') if len(options) > 0 else ''
            
            created_variants.append({
                'id': variant_id,
                'gid': node.get('id'),
                'sku': node.get('sku', ''),
                'option1': color,
                'price': node.get('price', '0')
            })
        
        print(f"   ✅ Product created via GraphQL: ID={product_id}, Variants={len(created_variants)}")
        
        # If we have more than 250 variants, fetch remaining with pagination
        if style_part.variant_count > 250:
            additional_variants = self._fetch_remaining_variants(product_gid, len(created_variants))
            created_variants.extend(additional_variants)
            print(f"   📦 Total variants fetched: {len(created_variants)}")
        
        # Assign images to variants based on color matching
        self._assign_images_to_variants_graphql(product_gid, product)
        
        return product_id, product_gid, created_variants
    
    def _fetch_remaining_variants(self, product_gid: str, already_fetched: int) -> List[Dict]:
        """Fetch remaining variants using pagination"""
        additional_variants = []
        cursor = None
        
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
                    }
                }
            }
        }
        """
        
        # Skip already fetched variants
        variables = {
            'productId': product_gid,
            'first': 250,
            'after': None
        }
        
        # First, skip the already fetched ones
        skip_count = already_fetched
        while skip_count > 0:
            result = self._execute_graphql(query, variables)
            edges = result.get('data', {}).get('product', {}).get('variants', {}).get('edges', [])
            if not edges:
                break
            
            fetched = min(len(edges), skip_count)
            skip_count -= fetched
            
            if skip_count > 0 and len(edges) > 0:
                variables['after'] = edges[-1].get('cursor')
        
        # Now fetch remaining
        has_next = True
        while has_next:
            if variables.get('after'):
                result = self._execute_graphql(query, variables)
                product_data = result.get('data', {}).get('product', {})
                variants_data = product_data.get('variants', {})
                edges = variants_data.get('edges', [])
                
                for edge in edges:
                    node = edge.get('node', {})
                    options = node.get('selectedOptions', [])
                    color = options[0].get('value', '') if len(options) > 0 else ''
                    
                    additional_variants.append({
                        'id': int(node.get('legacyResourceId')),
                        'gid': node.get('id'),
                        'sku': node.get('sku', ''),
                        'option1': color,
                        'price': node.get('price', '0')
                    })
                
                has_next = variants_data.get('pageInfo', {}).get('hasNextPage', False)
                if has_next and edges:
                    variables['after'] = edges[-1].get('cursor')
            else:
                has_next = False
        
        return additional_variants
    
    def _assign_images_to_variants_graphql(self, product_gid: str, product_data: Dict):
        """
        Assign images to variants based on color matching using GraphQL
        """
        # Get media from product
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
                    print(f"   🖼️ Media mapped to color: {color_name}")
        
        if not color_to_media:
            print(f"   ⚠️ No color mappings found in image alt tags")
            return
        
        # Group variants by color for batch update
        color_to_variants = {}
        for edge in variants_edges:
            node = edge.get('node', {})
            options = node.get('selectedOptions', [])
            variant_gid = node.get('id')
            
            if options and variant_gid:
                color = options[0].get('value', '').lower()
                if color in color_to_media:
                    if color not in color_to_variants:
                        color_to_variants[color] = []
                    color_to_variants[color].append(variant_gid)
        
        # Update variants with images using GraphQL mutation
        mutation = """
        mutation productVariantUpdate($input: ProductVariantInput!) {
            productVariantUpdate(input: $input) {
                productVariant {
                    id
                }
                userErrors {
                    field
                    message
                }
            }
        }
        """
        
        assigned_count = 0
        for color, variant_gids in color_to_variants.items():
            media_id = color_to_media.get(color)
            if not media_id:
                continue
            
            for variant_gid in variant_gids:
                try:
                    variables = {
                        'input': {
                            'id': variant_gid,
                            'mediaId': media_id
                        }
                    }
                    
                    result = self._execute_graphql(mutation, variables)
                    errors = result.get('data', {}).get('productVariantUpdate', {}).get('userErrors', [])
                    
                    if not errors:
                        assigned_count += 1
                    
                    time.sleep(0.05)  # Rate limiting
                except Exception as e:
                    print(f"   ⚠️ Error assigning media to variant: {e}")
        
        total_variants = sum(len(v) for v in color_to_variants.values())
        print(f"   ✅ Assigned images to {assigned_count}/{total_variants} variants via GraphQL")
    
    def add_product_images(self, product_id: int, image_urls: List[str]) -> int:
        """
        Add images to product using GraphQL
        """
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
        """
        Add variant-specific images using GraphQL
        """
        if not sku_to_image or not sku_to_variant_id:
            return 0
        
        # This is now handled in _assign_images_to_variants_graphql
        # Keep method for compatibility
        return 0
    
    def update_metafields(self, product_gid: str, metafields: Dict) -> bool:
        """
        Update product metafields using GraphQL
        """
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
        """
        Fetch product by ID using GraphQL
        """
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
                # Convert to REST-like format for compatibility
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
                        
                        time.sleep(0.2)  # Rate limiting
                    except:
                        pass
        except:
            pass
        
        return deleted_count
