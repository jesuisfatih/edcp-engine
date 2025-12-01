from typing import List, Dict, Optional
import time
import requests

# Try to import shopify library, but don't fail if it's not available
try:
    import shopify
    SHOPIFY_AVAILABLE = True
except ImportError:
    SHOPIFY_AVAILABLE = False
    shopify = None

class ShopifyClient:
    """Client for Shopify Admin API (2025)"""
    
    def __init__(self, shop_domain: str, access_token: str):
        self.shop_domain = shop_domain.rstrip('/')
        if not self.shop_domain.startswith('http'):
            self.shop_domain = f"https://{self.shop_domain}"
        
        self.access_token = access_token
        self.api_version = "2025-01"
        self.base_url = f"{self.shop_domain}/admin/api/{self.api_version}"
        self.graphql_url = f"{self.shop_domain}/admin/api/{self.api_version}/graphql.json"
        self.headers = {
            "X-Shopify-Access-Token": access_token,
            "Content-Type": "application/json"
        }
        
        # Try to initialize Shopify Python library
        self.use_library = False
        if SHOPIFY_AVAILABLE:
            try:
                shopify.ShopifyResource.set_site(f"{self.base_url}")
                shopify.Session.setup(api_key=None, secret=None)
                self.session = shopify.Session(self.shop_domain, self.api_version, access_token)
                shopify.ShopifyResource.activate_session(self.session)
                self.use_library = True
            except Exception:
                # Fallback to direct REST API calls
                self.use_library = False
    
    def _normalize_weight_unit(self, unit: Optional[str]) -> str:
        """Convert various weight unit inputs to Shopify enum values"""
        if not unit:
            return 'POUNDS'
        
        normalized = str(unit).strip().lower()
        mapping = {
            'lb': 'POUNDS',
            'lbs': 'POUNDS',
            'pound': 'POUNDS',
            'pounds': 'POUNDS',
            'kg': 'KILOGRAMS',
            'kilogram': 'KILOGRAMS',
            'kilograms': 'KILOGRAMS',
            'g': 'GRAMS',
            'gram': 'GRAMS',
            'grams': 'GRAMS',
            'oz': 'OUNCES',
            'ounce': 'OUNCES',
            'ounces': 'OUNCES'
        }
        return mapping.get(normalized, 'POUNDS')
    
    def get_shop_info(self) -> Dict:
        """Get shop information"""
        try:
            if self.use_library:
                shop = shopify.Shop.current()
                return {
                    'name': shop.name,
                    'domain': shop.domain,
                    'email': shop.email,
                    'currency': shop.currency
                }
            else:
                response = requests.get(f"{self.base_url}/shop.json", headers=self.headers)
                response.raise_for_status()
                shop_data = response.json()['shop']
                return {
                    'name': shop_data['name'],
                    'domain': shop_data['domain'],
                    'email': shop_data.get('email', ''),
                    'currency': shop_data.get('currency', 'USD')
                }
        except Exception as e:
            raise Exception(f"Failed to connect to Shopify: {str(e)}")
    
    def get_collections(self) -> List[Dict]:
        """Get all collections"""
        try:
            all_collections = []
            
            if self.use_library:
                collections = shopify.CustomCollection.find()
                smart_collections = shopify.SmartCollection.find()
                
                for coll in collections:
                    all_collections.append({
                        'id': coll.id,
                        'title': coll.title,
                        'handle': coll.handle,
                        'type': 'custom'
                    })
                
                for coll in smart_collections:
                    all_collections.append({
                        'id': coll.id,
                        'title': coll.title,
                        'handle': coll.handle,
                        'type': 'smart'
                    })
            else:
                # Get custom collections
                response = requests.get(f"{self.base_url}/custom_collections.json", headers=self.headers)
                response.raise_for_status()
                for coll in response.json().get('custom_collections', []):
                    all_collections.append({
                        'id': coll['id'],
                        'title': coll['title'],
                        'handle': coll['handle'],
                        'type': 'custom'
                    })
                
                # Get smart collections
                response = requests.get(f"{self.base_url}/smart_collections.json", headers=self.headers)
                response.raise_for_status()
                for coll in response.json().get('smart_collections', []):
                    all_collections.append({
                        'id': coll['id'],
                        'title': coll['title'],
                        'handle': coll['handle'],
                        'type': 'smart'
                    })
            
            return all_collections
        except Exception as e:
            raise Exception(f"Failed to get collections: {str(e)}")
    
    def find_or_create_collection(self, title: str, handle: Optional[str] = None) -> Dict:
        """Find collection by title or create if not exists"""
        collections = self.get_collections()
        
        # Try to find existing collection
        for coll in collections:
            if coll['title'].lower() == title.lower():
                return coll
        
        # Create new collection
        if not handle:
            handle = title.lower().replace(' ', '-').replace('&', 'and')
        
        try:
            if self.use_library:
                collection = shopify.CustomCollection()
                collection.title = title
                collection.handle = handle
                collection.save()
                
                return {
                    'id': collection.id,
                    'title': collection.title,
                    'handle': collection.handle,
                    'type': 'custom'
                }
            else:
                payload = {
                    'custom_collection': {
                        'title': title,
                        'handle': handle
                    }
                }
                response = requests.post(
                    f"{self.base_url}/custom_collections.json",
                    headers=self.headers,
                    json=payload
                )
                response.raise_for_status()
                coll_data = response.json()['custom_collection']
                return {
                    'id': coll_data['id'],
                    'title': coll_data['title'],
                    'handle': coll_data['handle'],
                    'type': 'custom'
                }
        except Exception as e:
            raise Exception(f"Failed to create collection: {str(e)}")
    
    def get_product_by_sku(self, sku: str) -> Optional[Dict]:
        """Find product by SKU - FIXED: Uses cursor-based pagination"""
        try:
            if self.use_library:
                products = shopify.Product.find(limit=250)
                for product in products:
                    for variant in product.variants:
                        if variant.sku == sku:
                            return {
                                'id': product.id,
                                'title': product.title,
                                'handle': product.handle,
                                'variants': [{
                                    'id': variant.id,
                                    'sku': variant.sku,
                                    'price': variant.price
                                }]
                            }
                
                # If not found in first page, search more using cursor pagination
                page_info = None
                max_pages = 10
                page_count = 0
                
                while page_count < max_pages:
                    try:
                        if page_info:
                            products = shopify.Product.find(limit=250, page_info=page_info)
                        else:
                            # Get next page using pagination
                            products = shopify.Product.find(limit=250)
                        
                        if not products:
                            break
                        
                        for product in products:
                            for variant in product.variants:
                                if variant.sku == sku:
                                    return {
                                        'id': product.id,
                                        'title': product.title,
                                        'handle': product.handle,
                                        'variants': [{
                                            'id': variant.id,
                                            'sku': variant.sku,
                                            'price': variant.price
                                        }]
                                    }
                        
                        # Get next page info if available
                        if hasattr(products, 'next_page_url'):
                            page_info = products.next_page_url
                        else:
                            break
                        
                        page_count += 1
                    except Exception as e:
                        print(f"Error searching products page {page_count + 1}: {e}")
                        break
            else:
                # Use REST API - FIXED: Use cursor-based pagination (page_info)
                # Shopify 2025-01 API doesn't support 'page' parameter, use cursor pagination
                limit = 250
                page_info = None
                max_pages = 10
                page_count = 0
                
                while page_count < max_pages:
                    try:
                        # Rate limiting: Add delay between requests
                        if page_count > 0:
                            time.sleep(0.5)  # 500ms delay between pages
                        
                        url = f"{self.base_url}/products.json"
                        params = {'limit': limit}
                        
                        # Add page_info if we have it (cursor-based pagination)
                        if page_info:
                            params['page_info'] = page_info
                        
                        response = requests.get(url, headers=self.headers, params=params, timeout=30)
                        
                        # Check for errors
                        if response.status_code == 400:
                            error_data = response.text
                            print(f"Shopify API 400 Error: {error_data}")
                            # If first page fails, try with different limit
                            if page_count == 0:
                                # Try with smaller limit
                                params = {'limit': 50}
                                response = requests.get(url, headers=self.headers, params=params, timeout=30)
                                if response.status_code != 200:
                                    break
                            else:
                                break
                        else:
                            response.raise_for_status()
                        
                        data = response.json()
                        products = data.get('products', [])
                        
                        if not products:
                            break
                        
                        # Search for SKU in this batch
                        for product in products:
                            for variant in product.get('variants', []):
                                if variant.get('sku') == sku:
                                    return {
                                        'id': product['id'],
                                        'title': product['title'],
                                        'handle': product['handle'],
                                        'variants': [{
                                            'id': variant['id'],
                                            'sku': variant['sku'],
                                            'price': variant['price']
                                        }]
                                    }
                        
                        # Get next page info from Link header (cursor-based pagination)
                        link_header = response.headers.get('Link', '')
                        if link_header and 'rel="next"' in link_header:
                            # Extract page_info from Link header
                            # Format: <https://shop.myshopify.com/admin/api/2025-01/products.json?limit=250&page_info=...>; rel="next"
                            import re
                            match = re.search(r'page_info=([^>]+)', link_header)
                            if match:
                                page_info = match.group(1)
                            else:
                                break
                        else:
                            # No more pages
                            break
                        
                        page_count += 1
                    except requests.exceptions.HTTPError as e:
                        if e.response.status_code == 400:
                            print(f"Shopify API 400 Error on page {page_count + 1}: {e.response.text}")
                            if page_count == 0:
                                # Try first page with smaller limit
                                try:
                                    response = requests.get(f"{self.base_url}/products.json", 
                                                          headers=self.headers, 
                                                          params={'limit': 50}, 
                                                          timeout=30)
                                    if response.status_code == 200:
                                        products = response.json().get('products', [])
                                        for product in products:
                                            for variant in product.get('variants', []):
                                                if variant.get('sku') == sku:
                                                    return {
                                                        'id': product['id'],
                                                        'title': product['title'],
                                                        'handle': product['handle'],
                                                        'variants': [{
                                                            'id': variant['id'],
                                                            'sku': variant['sku'],
                                                            'price': variant['price']
                                                        }]
                                                    }
                                except:
                                    pass
                            break
                        else:
                            raise
                    except Exception as e:
                        print(f"Error searching products: {e}")
                        break
            
            return None
        except Exception as e:
            raise Exception(f"Failed to search product: {str(e)}")
    
    def get_product_by_title(self, title: str) -> Optional[Dict]:
        """Find product by title - MUCH FASTER than SKU search, avoids rate limiting"""
        try:
            if not title or not title.strip():
                return None
            
            # Use REST API with title search - much faster than pagination
            url = f"{self.base_url}/products.json"
            params = {
                'title': title.strip(),
                'limit': 10
            }
            
            # Rate limiting - minimal delay for title search
            time.sleep(0.2)
            
            response = requests.get(url, headers=self.headers, params=params, timeout=30)
            
            if response.status_code == 200:
                products = response.json().get('products', [])
                # Find exact match (case-insensitive)
                for product in products:
                    if product.get('title', '').strip().lower() == title.strip().lower():
                        return {
                            'id': product['id'],
                            'title': product['title'],
                            'handle': product['handle'],
                            'variants': product.get('variants', [])
                        }
            
            return None
        except Exception as e:
            print(f"Failed to search product by title: {e}")
            return None
    
    def _create_product_with_graphql(self, product_data: Dict) -> Dict:
        """Create product using GraphQL API (supports unlimited variants)"""
        try:
            variants = product_data.get('variants', [])
            variant_count = len(variants)
            
            # Step 1: Create product first (without variants/options/images)
            create_mutation = """
            mutation productCreate($input: ProductInput!) {
                productCreate(input: $input) {
                    product {
                        id
                        title
                        handle
                        status
                    }
                    userErrors {
                        field
                        message
                    }
                }
            }
            """
            
            option_names = []
            if variants and any(v.get('option1') for v in variants):
                option_names.append('Color')
            if variants and any(v.get('option2') for v in variants):
                option_names.append('Size')
            if variants and any(v.get('option3') for v in variants):
                option_names.append('Style')
            if variants and not option_names:
                option_names.append('Title')

            product_input = {
                'title': product_data.get('title', 'Product'),
                'descriptionHtml': product_data.get('description', '') or '',
                'vendor': product_data.get('vendor', '') or '',
                'productType': product_data.get('product_type', '') or '',
                'tags': product_data.get('tags', '').split(',') if product_data.get('tags') else [],
                'status': product_data.get('status', 'ACTIVE').upper(),
                'options': [{'name': name} for name in option_names] if option_names else [{'name': 'Title'}]
            }
            
            response = requests.post(
                self.graphql_url,
                headers=self.headers,
                json={'query': create_mutation, 'variables': {'input': product_input}},
                timeout=120
            )
            response.raise_for_status()
            result = response.json()
            
            if 'errors' in result:
                error_messages = [e.get('message', str(e)) for e in result['errors']]
                raise Exception(f"GraphQL errors: {', '.join(error_messages)}")
            
            product_create = result.get('data', {}).get('productCreate', {})
            user_errors = product_create.get('userErrors', [])
            
            if user_errors:
                error_messages = [e.get('message', str(e)) for e in user_errors]
                raise Exception(f"GraphQL user errors: {', '.join(error_messages)}")
            
            product = product_create.get('product')
            if not product:
                raise Exception("GraphQL mutation succeeded but no product returned")
            
            product_gid = product.get('id')
            product_id_str = product_gid.replace('gid://shopify/Product/', '')
            product_id = int(product_id_str) if product_id_str.isdigit() else None
            
            # Step 2: Get location ID for inventory
            location_id = None
            try:
                location_query = """
                query {
                    locations(first: 1) {
                        edges {
                            node {
                                id
                            }
                        }
                    }
                }
                """
                location_response = requests.post(
                    self.graphql_url,
                    headers=self.headers,
                    json={'query': location_query},
                    timeout=30
                )
                location_response.raise_for_status()
                location_result = location_response.json()
                if 'data' in location_result:
                    locations = location_result['data'].get('locations', {}).get('edges', [])
                    if locations:
                        location_id = locations[0]['node']['id']
            except Exception as e:
                print(f"Warning: Could not fetch location ID: {e}")
            
            # Step 4: Add variants using productVariantCreate (one by one)
            # CRITICAL: Shopify requires at least 1 variant per product
            if not variants or len(variants) == 0:
                raise Exception("Product must have at least 1 variant. No variants provided in product_data.")
            
            print(f"Processing {len(variants)} variants for product creation...")
            seen_variant_keys = set()
            seen_option_combinations = set()
            unique_variants = []
            
            for variant_data in variants:
                option1 = str(variant_data.get('option1') or '').strip()
                option2 = str(variant_data.get('option2') or '').strip()
                option3 = str(variant_data.get('option3') or '').strip()
                sku = str(variant_data.get('sku') or '').strip()
                
                # CRITICAL: Shopify doesn't allow duplicate option combinations
                option_combination = (option1, option2, option3)
                if option_combination in seen_option_combinations:
                    if option2 and sku:
                        option2 = f"{option2}-{sku[:6]}"
                        print(f"Warning: Duplicate option combination detected. Modified option2 to: {option2} for SKU: {sku}")
                    elif option1 and sku:
                        option1 = f"{option1}-{sku[:6]}"
                        print(f"Warning: Duplicate option combination detected. Modified option1 to: {option1} for SKU: {sku}")
                    else:
                        print(f"Warning: Duplicate option combination - modifying SKU: {sku}")
                        if not option1:
                            option1 = f"Option1-{sku[:6]}"
                        if not option2:
                            option2 = f"Option2-{sku[:6]}"
                
                seen_option_combinations.add((option1, option2, option3))
                
                variant_key = (option1, option2, option3, sku)
                if variant_key in seen_variant_keys:
                    print(f"Warning: Duplicate variant skipped - SKU: {sku}")
                    continue
                seen_variant_keys.add(variant_key)
                
                variant_input = {
                    'sku': sku if sku else None,
                    'price': str(variant_data.get('price', '0')),
                    'barcode': variant_data.get('barcode', '') or None,
                    'weight': variant_data.get('weight', 0) or 0,
                    'weightUnit': self._normalize_weight_unit(variant_data.get('weight_unit'))
                }
                
                # CRITICAL: selectedOptions must match the option names we set in Step 2
                # Option names MUST match exactly: 'Color', 'Size', 'Style' (or 'Title' if default)
                selected_options = []
                
                # Match option names to what we set in productOptionsUpdate
                if option1:
                    selected_options.append({'name': 'Color', 'value': option1})
                if option2:
                    selected_options.append({'name': 'Size', 'value': option2})
                if option3:
                    selected_options.append({'name': 'Style', 'value': option3})
                
                # CRITICAL: If no options provided, we MUST have at least one option value
                # This should match the default 'Title' option we created
                if not selected_options:
                    print(f"⚠️ WARNING: Variant {sku} has no option values, using SKU as default option value")
                    selected_options.append({'name': 'Title', 'value': sku if sku else f'Variant-{len(unique_variants)+1}'})
                
                variant_input['selectedOptions'] = selected_options
                
                # DEBUG: Log first few variants
                if len(unique_variants) < 3:
                    print(f"DEBUG: Variant {len(unique_variants)+1} selectedOptions: {selected_options}")
                
                if location_id and variant_data.get('inventory_quantity'):
                    variant_input['inventoryQuantities'] = [{
                        'availableQuantity': variant_data.get('inventory_quantity', 0) or 0,
                        'locationId': location_id
                    }]
                
                if variant_data.get('inventory_management') is None:
                    variant_input['inventoryPolicy'] = 'CONTINUE'
                else:
                    variant_input['inventoryPolicy'] = 'DENY'
                
                variant_input['_image'] = variant_data.get('image')
                variant_input['_metafields'] = variant_data.get('metafields', {})
                unique_variants.append(variant_input)
            
            # CRITICAL: Must have at least 1 variant
            if not unique_variants or len(unique_variants) == 0:
                raise Exception("No valid variants to create. All variants were filtered out or invalid.")
            
            print(f"Creating {len(unique_variants)} variants (from {len(variants)} input variants)...")
            
            if True:  # Always create variants
                variants_list = []
                variant_images_map = {}
                variant_metafields_map = {}
                
                # CRITICAL: Extract images and metafields BEFORE creating variants
                # This ensures we don't lose the data
                for v in unique_variants:
                    variant_sku = v.get('sku', '')
                    
                    # Get image URL (check both keys)
                    image_url = v.get('image') or v.get('_image')
                    if image_url and variant_sku:
                        variant_images_map[variant_sku] = image_url
                        if len(variant_images_map) <= 5:
                            print(f"📸 Mapped variant image for SKU {variant_sku}: {image_url[:60]}...")
                    
                    # Get metafields
                    metafields = v.get('metafields', {}) or v.get('_metafields', {})
                    if metafields and variant_sku:
                        variant_metafields_map[variant_sku] = metafields
                    
                    # CRITICAL: Remove image and metafields from variant_input
                    # These fields are not part of ProductVariantInput
                    if 'image' in v:
                        del v['image']
                    if '_image' in v:
                        del v['_image']
                    if 'metafields' in v:
                        del v['metafields']
                    if '_metafields' in v:
                        del v['_metafields']
                
                print(f"📊 Variant images map: {len(variant_images_map)} variants with images")
                print(f"📊 Variant metafields map: {len(variant_metafields_map)} variants with metafields")
                
                if len(variant_images_map) == 0:
                    print(f"⚠️ WARNING: No variant images found in product_data!")
                    print(f"   Checking first variant: {unique_variants[0] if unique_variants else 'N/A'}")
                
                variant_mutation = """
                mutation productVariantCreate($input: ProductVariantInput!) {
                    productVariantCreate(input: $input) {
                        productVariant {
                            id
                            sku
                            price
                            selectedOptions {
                                name
                                value
                            }
                        }
                        userErrors {
                            field
                            message
                        }
                    }
                }
                """
                
                print(f"Creating {len(unique_variants)} variants...")
                created_count = 0
                failed_count = 0
                
                for idx, variant_input in enumerate(unique_variants):
                    variant_sku = variant_input.get('sku', f'variant-{idx+1}')
                    
                    variant_payload = {
                        'price': variant_input.get('price', '0'),
                        'barcode': variant_input.get('barcode') or None,
                        'weight': variant_input.get('weight', 0) or 0,
                        'weightUnit': self._normalize_weight_unit(variant_input.get('weightUnit'))
                    }
                    
                    if variant_input.get('sku'):
                        variant_payload['sku'] = variant_input['sku']
                    
                    # CRITICAL: selectedOptions is REQUIRED - should never be empty after our fix above
                    if variant_input.get('selectedOptions'):
                        variant_payload['selectedOptions'] = variant_input['selectedOptions']
                    else:
                        # Fallback: create default option
                        print(f"CRITICAL ERROR: Variant {variant_sku} has no selectedOptions, creating default...")
                        variant_payload['selectedOptions'] = [{'name': 'Default', 'value': variant_sku if variant_sku else f'Variant-{idx+1}'}]
                    
                    if variant_input.get('inventoryQuantities'):
                        variant_payload['inventoryQuantities'] = variant_input['inventoryQuantities']
                    
                    if variant_input.get('inventoryPolicy'):
                        variant_payload['inventoryPolicy'] = variant_input['inventoryPolicy']
                    
                    try:
                        # DEBUG: Log variant payload before sending
                        if idx < 3:  # Log first 3 variants for debugging
                            print(f"DEBUG: Creating variant {idx+1}/{len(unique_variants)} - SKU: {variant_sku}")
                            print(f"DEBUG: Variant payload: {variant_payload}")
                        
                        # CRITICAL FIX: Use correct GraphQL mutation structure with input wrapper
                        variant_input = {
                            'productId': product_gid,
                            **variant_payload
                        }
                        
                        variant_response = requests.post(
                            self.graphql_url,
                            headers=self.headers,
                            json={
                                'query': variant_mutation,
                                'variables': {
                                    'input': variant_input
                                }
                            },
                            timeout=30
                        )
                        variant_response.raise_for_status()
                        variant_result = variant_response.json()
                        
                        # DEBUG: Log response for first few variants
                        if idx < 3:
                            print(f"DEBUG: Variant {idx+1} response: {variant_result}")
                        
                        if 'errors' in variant_result:
                            error_messages = [e.get('message', str(e)) for e in variant_result['errors']]
                            error_details = f"GraphQL errors for variant {variant_sku} ({idx+1}/{len(unique_variants)}): {', '.join(error_messages)}"
                            print(f"❌ {error_details}")
                            print(f"   Payload was: {variant_payload}")
                            failed_count += 1
                            continue
                        
                        variant_create = variant_result.get('data', {}).get('productVariantCreate', {})
                        variant_user_errors = variant_create.get('userErrors', [])
                        
                        if variant_user_errors:
                            error_messages = [e.get('message', str(e)) for e in variant_user_errors]
                            error_details = f"User errors for variant {variant_sku} ({idx+1}/{len(unique_variants)}): {', '.join(error_messages)}"
                            print(f"❌ {error_details}")
                            print(f"   Payload was: {variant_payload}")
                            failed_count += 1
                            continue
                        
                        variant_node = variant_create.get('productVariant', {})
                        if variant_node:
                            variant_id_str = variant_node.get('id', '').replace('gid://shopify/ProductVariant/', '')
                            variant_id = int(variant_id_str) if variant_id_str.isdigit() else None
                            variant_sku_created = variant_node.get('sku', '') or variant_sku
                            variant_gid_created = variant_node.get('id', '')
                            variants_list.append({
                                'id': variant_id,
                                'gid': variant_gid_created,
                                'sku': variant_sku_created,
                                'price': variant_node.get('price', '0')
                            })
                            created_count += 1
                            if idx < 5 or (idx + 1) % 10 == 0:
                                print(f"✅ Variant {idx+1}/{len(unique_variants)} created: SKU={variant_sku_created}, ID={variant_id}")
                        else:
                            error_msg = f"CRITICAL: Variant {variant_sku} mutation succeeded but no variant node returned in response"
                            print(f"❌ {error_msg}")
                            print(f"   Full response: {variant_result}")
                            failed_count += 1
                        
                        time.sleep(0.1)
                        
                    except requests.exceptions.HTTPError as e:
                        error_msg = f"HTTP Error creating variant {variant_sku} ({idx+1}/{len(unique_variants)}): {e}"
                        if hasattr(e, 'response') and e.response is not None:
                            try:
                                error_body = e.response.json()
                                error_msg += f" | Response: {error_body}"
                            except:
                                error_msg += f" | Response text: {e.response.text[:200]}"
                        print(f"❌ {error_msg}")
                        failed_count += 1
                        continue
                    except Exception as e:
                        error_msg = f"Exception creating variant {variant_sku} ({idx+1}/{len(unique_variants)}): {type(e).__name__}: {str(e)}"
                        print(f"❌ {error_msg}")
                        import traceback
                        print(f"   Traceback: {traceback.format_exc()[:300]}")
                        failed_count += 1
                        continue
                
                print(f"📊 Variant creation summary: {created_count} successful, {failed_count} failed out of {len(unique_variants)} total")
                
                # CRITICAL: If no variants were created, this is a fatal error
                if created_count == 0:
                    error_details = f"CRITICAL: Failed to create any variants for product '{product.get('title')}'. "
                    error_details += f"Product ID {product_id} was created but has no variants. "
                    error_details += f"Attempted to create {len(unique_variants)} variants, all failed. "
                    error_details += f"Product GID: {product_gid}"
                    
                    # Try to delete the orphaned product
                    try:
                        print(f"⚠️ Attempting to delete orphaned product {product_id}...")
                        self.delete_product_by_id(product_id)
                        print(f"✅ Orphaned product {product_id} deleted successfully")
                    except Exception as delete_error:
                        print(f"⚠️ Could not delete orphaned product {product_id}: {delete_error}")
                        error_details += f" (Orphaned product {product_id} could not be deleted: {delete_error})"
                    
                    raise Exception(error_details)
            else:
                raise Exception("CRITICAL: No variants to create. Product cannot exist without variants.")
            
            # Step 5: Add product images
            product_images = product_data.get('images', [])
            if product_images and len(product_images) > 0:
                print(f"📸 Adding {len(product_images)} product-level images...")
                image_count = 0
                for idx, img_url in enumerate(product_images):
                    if not img_url or not img_url.strip():
                        continue
                    
                    image_mutation = """
                    mutation productImageCreate($input: ImageInput!) {
                        productImageCreate(input: $input) {
                            image {
                                id
                                src
                            }
                            userErrors {
                                field
                                message
                            }
                        }
                    }
                    """
                    
                    # CRITICAL FIX: Use correct GraphQL mutation structure with input wrapper
                    image_input = {
                        'productId': product_gid,
                        'src': img_url.strip()
                    }
                    
                    try:
                        image_response = requests.post(
                            self.graphql_url,
                            headers=self.headers,
                            json={
                                'query': image_mutation,
                                'variables': {
                                    'input': image_input
                                }
                            },
                            timeout=30
                        )
                        image_response.raise_for_status()
                        result = image_response.json()
                        if 'errors' in result:
                            print(f"Warning: GraphQL error adding product image {idx+1}: {result['errors']}")
                        else:
                            user_errors = result.get('data', {}).get('productImageCreate', {}).get('userErrors', [])
                            if user_errors:
                                print(f"Warning: User errors adding product image {idx+1}: {user_errors}")
                            else:
                                image_count += 1
                                print(f"Successfully added product image {image_count}/{len(product_images)}")
                        time.sleep(0.15)
                    except Exception as e:
                        print(f"Warning: Could not add product image {idx+1} ({img_url[:50]}...): {e}")
                print(f"Product images complete: {image_count}/{len(product_images)} images added")
            else:
                print("Warning: No product images provided in product_data")
            
            # Step 6: Add variant-specific images
            if variant_images_map and len(variant_images_map) > 0:
                print(f"📸 Adding variant-specific images for {len(variant_images_map)} variants...")
                print(f"   Variant images map: {list(variant_images_map.keys())[:5]}...")  # Show first 5 SKUs
                variant_image_count = 0
                for variant_sku, image_url in variant_images_map.items():
                    if not image_url or not image_url.strip():
                        continue
                    
                    matching_variant = None
                    for v in variants_list:
                        # Try to match by SKU (exact match or case-insensitive)
                        v_sku = v.get('sku', '').strip()
                        if v_sku and variant_sku.strip():
                            if v_sku == variant_sku.strip() or v_sku.lower() == variant_sku.strip().lower():
                                matching_variant = v
                                break
                    
                    if matching_variant:
                        # Use GID if available, otherwise construct from ID
                        variant_gid = matching_variant.get('gid')
                        if not variant_gid:
                            variant_id = matching_variant.get('id')
                            if variant_id:
                                variant_gid = f"gid://shopify/ProductVariant/{variant_id}"
                            else:
                                print(f"⚠️ Warning: No GID or ID for variant SKU {variant_sku}, skipping image")
                                continue
                        
                        if 'None' in str(variant_gid):
                            print(f"⚠️ Warning: Invalid variant GID for SKU {variant_sku}, skipping image")
                            continue
                        
                        print(f"   Adding image for variant SKU {variant_sku} (GID: {variant_gid})")
                        image_mutation = """
                        mutation productImageCreate($input: ImageInput!) {
                            productImageCreate(input: $input) {
                                image {
                                    id
                                    src
                                }
                                userErrors {
                                    field
                                    message
                                }
                            }
                        }
                        """
                        
                        # CRITICAL FIX: Use correct GraphQL mutation structure with input wrapper
                        image_input = {
                            'productId': product_gid,
                            'src': image_url.strip(),
                            'variantIds': [variant_gid]
                        }
                        
                        try:
                            image_response = requests.post(
                                self.graphql_url,
                                headers=self.headers,
                                json={
                                    'query': image_mutation,
                                    'variables': {
                                        'input': image_input
                                    }
                                },
                                timeout=30
                            )
                            image_response.raise_for_status()
                            result = image_response.json()
                            if 'errors' in result:
                                print(f"Warning: GraphQL error adding variant image for {variant_sku}: {result['errors']}")
                            else:
                                user_errors = result.get('data', {}).get('productImageCreate', {}).get('userErrors', [])
                                if user_errors:
                                    print(f"Warning: User errors adding variant image for {variant_sku}: {user_errors}")
                                else:
                                    variant_image_count += 1
                                    if variant_image_count <= 3 or variant_image_count % 10 == 0:
                                        print(f"✅ Variant image {variant_image_count}/{len(variant_images_map)} added for SKU: {variant_sku}")
                            time.sleep(0.15)
                        except Exception as e:
                            print(f"❌ Error adding variant image for {variant_sku}: {e}")
                            import traceback
                            print(f"   Traceback: {traceback.format_exc()[:200]}")
                    else:
                        print(f"⚠️ Warning: Could not find variant with SKU {variant_sku} in created variants list for image mapping")
                        print(f"   Available variant SKUs: {[v.get('sku') for v in variants_list[:5]]}...")
                print(f"📸 Variant images complete: {variant_image_count}/{len(variant_images_map)} variant images added")
            else:
                print(f"⚠️ Warning: No variant images to add (variant_images_map is empty or None)")
                print(f"   Variants in product_data: {len(product_data.get('variants', []))}")
                if product_data.get('variants'):
                    sample_variant = product_data['variants'][0]
                    print(f"   Sample variant keys: {list(sample_variant.keys())}")
                    print(f"   Sample variant has 'image': {'image' in sample_variant}")
            
            # Step 7: Add product-level metafields
            if product_data.get('metafields'):
                print(f"Adding {len(product_data['metafields'])} product-level metafields...")
                self._add_product_metafields(product_gid, product_data['metafields'])
            
            # Step 7b: Add variant-level metafields
            if variant_metafields_map:
                print(f"Adding variant metafields for {len(variant_metafields_map)} variants...")
                for variant_sku, metafields in variant_metafields_map.items():
                    if not metafields:
                        continue
                    
                    matching_variant = None
                    for v in variants_list:
                        v_sku = v.get('sku', '').strip()
                        if v_sku and variant_sku.strip():
                            if v_sku == variant_sku.strip() or v_sku.lower() == variant_sku.strip().lower():
                                matching_variant = v
                                break
                    
                    if matching_variant:
                        variant_gid = matching_variant.get('gid') or f"gid://shopify/ProductVariant/{matching_variant.get('id')}"
                        if variant_gid and 'None' not in variant_gid:
                            print(f"Adding {len(metafields)} metafields for variant SKU: {variant_sku}")
                            self._add_variant_metafields(variant_gid, metafields)
                        else:
                            print(f"Warning: Invalid variant GID for SKU {variant_sku}, skipping metafields")
                    else:
                        print(f"Warning: Could not find variant with SKU {variant_sku} for metafields")
            
            # Step 8: Add to collections
            if product_data.get('collections'):
                print(f"Adding product to {len(product_data['collections'])} collections...")
                for coll_id in product_data['collections']:
                    try:
                        self.add_product_to_collection(product_id, coll_id)
                    except Exception as e:
                        print(f"Warning: Could not add product to collection {coll_id}: {e}")
            
            print(f"Product creation complete: {product.get('title')} (ID: {product_id}) with {len(variants_list)} variants")
            
            return {
                'id': product_id,
                'title': product.get('title', ''),
                'handle': product.get('handle', ''),
                'status': 'created',
                'variants': variants_list
            }
            
        except Exception as e:
            raise Exception(f"Failed to create product with GraphQL: {str(e)}")
    
    def _add_product_metafields(self, product_gid: str, metafields: Dict):
        """Add metafields to a product using GraphQL"""
        try:
            if not metafields:
                return
            
            metafields_list = []
            for key, value in metafields.items():
                if value is None or value == '':
                    continue
                
                if isinstance(value, bool):
                    value_type = 'boolean'
                    value_str = str(value).lower()
                elif isinstance(value, (int, float)):
                    value_type = 'number_integer' if isinstance(value, int) else 'number_decimal'
                    value_str = str(value)
                else:
                    value_type = 'single_line_text_field'
                    value_str = str(value)
                
                metafields_list.append({
                    'namespace': 'ssactivewear',
                    'key': key.lower().replace(' ', '_'),
                    'value': value_str,
                    'type': value_type
                })
            
            if not metafields_list:
                return
            
            for metafield in metafields_list:
                try:
                    metafield_mutation_single = """
                    mutation metafieldsSet($metafields: [MetafieldsSetInput!]!) {
                        metafieldsSet(metafields: $metafields) {
                            metafields {
                                id
                                namespace
                                key
                            }
                            userErrors {
                                field
                                message
                            }
                        }
                    }
                    """
                    
                    metafield_input = {
                        'ownerId': product_gid,
                        'namespace': metafield['namespace'],
                        'key': metafield['key'],
                        'value': metafield['value'],
                        'type': metafield['type']
                    }
                    
                    response = requests.post(
                        self.graphql_url,
                        headers=self.headers,
                        json={
                            'query': metafield_mutation_single,
                            'variables': {
                                'metafields': [metafield_input]
                            }
                        },
                        timeout=30
                    )
                    response.raise_for_status()
                    result = response.json()
                    
                    if 'errors' in result:
                        print(f"Warning: Error adding metafield {metafield['key']}: {result['errors']}")
                    else:
                        user_errors = result.get('data', {}).get('metafieldsSet', {}).get('userErrors', [])
                        if user_errors:
                            print(f"Warning: User errors adding metafield {metafield['key']}: {user_errors}")
                    
                    time.sleep(0.1)
                except Exception as e:
                    print(f"Warning: Could not add metafield {metafield.get('key', 'unknown')}: {e}")
            
        except Exception as e:
            print(f"Warning: Error adding metafields: {e}")
    
    def _add_variant_metafields(self, variant_gid: str, metafields: Dict):
        """Add metafields to a variant using GraphQL"""
        try:
            if not metafields:
                return
            
            for key, value in metafields.items():
                if value is None or value == '':
                    continue
                
                if isinstance(value, bool):
                    value_type = 'boolean'
                    value_str = str(value).lower()
                elif isinstance(value, (int, float)):
                    value_type = 'number_integer' if isinstance(value, int) else 'number_decimal'
                    value_str = str(value)
                else:
                    value_type = 'single_line_text_field'
                    value_str = str(value)
                
                try:
                    metafield_mutation = """
                    mutation metafieldsSet($metafields: [MetafieldsSetInput!]!) {
                        metafieldsSet(metafields: $metafields) {
                            metafields {
                                id
                                namespace
                                key
                            }
                            userErrors {
                                field
                                message
                            }
                        }
                    }
                    """
                    
                    metafield_input = {
                        'ownerId': variant_gid,
                        'namespace': 'ssactivewear',
                        'key': key.lower().replace(' ', '_'),
                        'value': value_str,
                        'type': value_type
                    }
                    
                    response = requests.post(
                        self.graphql_url,
                        headers=self.headers,
                        json={
                            'query': metafield_mutation,
                            'variables': {
                                'metafields': [metafield_input]
                            }
                        },
                        timeout=30
                    )
                    response.raise_for_status()
                    result = response.json()
                    
                    if 'errors' in result:
                        print(f"Warning: Error adding variant metafield {key}: {result['errors']}")
                    else:
                        user_errors = result.get('data', {}).get('metafieldsSet', {}).get('userErrors', [])
                        if user_errors:
                            print(f"Warning: User errors adding variant metafield {key}: {user_errors}")
                    
                    time.sleep(0.1)
                except Exception as e:
                    print(f"Warning: Could not add variant metafield {key}: {e}")
            
        except Exception as e:
            print(f"Warning: Error adding variant metafields: {e}")
    
    def create_product(self, product_data: Dict) -> Dict:
        """Create a new product in Shopify - ALWAYS uses GraphQL (no REST API)"""
        try:
            variants = product_data.get('variants', [])
            variant_count = len(variants)
            
            print(f"🚀 Creating product with {variant_count} variants using GraphQL API...")
            print(f"   Product title: {product_data.get('title', 'N/A')}")
            print(f"   Variants in data: {len(product_data.get('variants', []))}")
            print(f"   Images in data: {len(product_data.get('images', []))}")
            result = self._create_product_with_graphql(product_data)
            print(f"✅ Product creation result: {result.get('status', 'unknown')}, ID: {result.get('id')}, Variants created: {len(result.get('variants', []))}")
            return result
            
        except Exception as e:
            raise Exception(f"Failed to create product: {str(e)}")
    
    def _create_product_with_rest(self, product_data: Dict) -> Dict:
        """DEPRECATED: REST API method - kept for fallback only (not used)"""
        raise Exception("REST API method is deprecated. Use GraphQL instead.")
    

    def update_product(self, product_id: int, product_data: Dict) -> Dict:
        """Update existing product using GraphQL API"""
        try:
            product_gid = f"gid://shopify/Product/{product_id}"
            print(f"[update] Updating product {product_id} using GraphQL API...")

            # Preprocess incoming variants for images/metafields mapping
            variant_images_map = {}
            variant_metafields_map = {}
            variants_input = product_data.get('variants', []) or []
            for v in variants_input:
                sku = str(v.get('sku', '')).strip()
                if not sku:
                    continue
                image_url = v.get('image') or v.get('_image') or v.get('variant_image_url')
                if image_url:
                    variant_images_map[sku] = image_url
                metafields = v.get('metafields') or v.get('_metafields') or v.get('variant_metafields')
                if metafields:
                    variant_metafields_map[sku] = metafields

            # Step 1: Update product basic info
            if any(key in product_data for key in ['title', 'description', 'vendor', 'product_type', 'tags', 'status']):
                update_mutation = """
                mutation productUpdate($input: ProductInput!) {
                    productUpdate(input: $input) {
                        product {
                            id
                            title
                        }
                        userErrors {
                            field
                            message
                        }
                    }
                }
                """

                product_input = {}
                if 'title' in product_data:
                    product_input['id'] = product_gid
                if 'title' in product_data:
                    product_input['title'] = product_data['title']
                if 'description' in product_data:
                    product_input['descriptionHtml'] = product_data['description'] or ''
                if 'vendor' in product_data:
                    product_input['vendor'] = product_data['vendor'] or ''
                if 'product_type' in product_data:
                    product_input['productType'] = product_data['product_type'] or ''
                if 'tags' in product_data:
                    if isinstance(product_data['tags'], str):
                        product_input['tags'] = [t.strip() for t in product_data['tags'].split(',') if t.strip()]
                    elif isinstance(product_data['tags'], list):
                        product_input['tags'] = product_data['tags']
                if 'status' in product_data:
                    product_input['status'] = product_data['status'].upper()

                if product_input:
                    product_input['id'] = product_gid
                    response = requests.post(
                        self.graphql_url,
                        headers=self.headers,
                        json={'query': update_mutation, 'variables': {'input': product_input}},
                        timeout=30
                    )
                    response.raise_for_status()
                    result = response.json()

                    if 'errors' in result:
                        error_messages = [e.get('message', str(e)) for e in result['errors']]
                        raise Exception(f"GraphQL errors updating product: {', '.join(error_messages)}")

                    product_update = result.get('data', {}).get('productUpdate', {})
                    user_errors = product_update.get('userErrors', [])
                    if user_errors:
                        error_messages = [e.get('message', str(e)) for e in user_errors]
                        raise Exception(f"GraphQL user errors updating product: {', '.join(error_messages)}")

                    print("[update] Product basic info updated")
                    time.sleep(0.2)

            # Step 2: Get existing product variants (with pagination)
            existing_variants = {}
            variant_lookup_by_sku = {}
            try:
                get_product_query = """
                query getProduct($id: ID!, $cursor: String) {
                    product(id: $id) {
                        id
                        variants(first: 250, after: $cursor) {
                            pageInfo {
                                hasNextPage
                                endCursor
                            }
                            edges {
                                node {
                                    id
                                    sku
                                    selectedOptions {
                                        name
                                        value
                                    }
                                }
                            }
                        }
                    }
                }
                """

                cursor = None
                total_variants_fetched = 0
                while True:
                    get_response = requests.post(
                        self.graphql_url,
                        headers=self.headers,
                        json={'query': get_product_query, 'variables': {'id': product_gid, 'cursor': cursor}},
                        timeout=30
                    )
                    get_response.raise_for_status()
                    get_result = get_response.json()

                    if 'data' in get_result and get_result['data'].get('product'):
                        variants_edges = get_result['data']['product'].get('variants', {}).get('edges', [])
                        for edge in variants_edges:
                            variant_node = edge.get('node', {})
                            variant_gid = variant_node.get('id', '')
                            variant_sku = variant_node.get('sku', '').strip()
                            selected_options = variant_node.get('selectedOptions', [])

                            option_key = tuple(sorted([f"{opt.get('name')}:{opt.get('value')}" for opt in selected_options]))
                            existing_variants[variant_gid] = {
                                'sku': variant_sku,
                                'options': option_key,
                                'selectedOptions': selected_options
                            }
                            if variant_sku:
                                variant_lookup_by_sku[variant_sku.lower()] = variant_gid
                            total_variants_fetched += 1

                        page_info = get_result['data']['product'].get('variants', {}).get('pageInfo', {})
                        if page_info.get('hasNextPage') and page_info.get('endCursor'):
                            cursor = page_info.get('endCursor')
                            continue

                    break

                print(f"[update] Found {len(existing_variants)} existing variants (fetched {total_variants_fetched})")
            except Exception as e:
                print(f"[update] Warning: Could not fetch existing variants: {e}")

            # Step 3: Update or create variants
            if variants_input:
                print(f"[update] Processing {len(variants_input)} variants for update...")

                # Get location ID for inventory
                location_id = None
                try:
                    location_query = """
                    query {
                        locations(first: 1) {
                            edges {
                                node {
                                    id
                                }
                            }
                        }
                    }
                    """
                    location_response = requests.post(
                        self.graphql_url,
                        headers=self.headers,
                        json={'query': location_query},
                        timeout=30
                    )
                    location_response.raise_for_status()
                    location_result = location_response.json()
                    if 'data' in location_result:
                        locations = location_result['data'].get('locations', {}).get('edges', [])
                        if locations:
                            location_id = locations[0]['node']['id']
                except Exception as e:
                    print(f"[update] Warning: Could not fetch location ID: {e}")

                updated_count = 0
                created_count = 0
                failed_count = 0
                variant_records = []  # Track variant GIDs/SKUs after update/create for images/metafields

                for variant_data in variants_input:
                    variant_sku = (variant_data.get('sku') or '').strip()
                    option1 = (variant_data.get('option1') or '').strip()
                    option2 = (variant_data.get('option2') or '').strip()
                    option3 = (variant_data.get('option3') or '').strip()

                    new_selected_options = []
                    if option1:
                        new_selected_options.append({'name': 'Color', 'value': option1})
                    if option2:
                        new_selected_options.append({'name': 'Size', 'value': option2})
                    if option3:
                        new_selected_options.append({'name': 'Style', 'value': option3})

                    new_option_key = tuple(sorted([f"{opt.get('name')}:{opt.get('value')}" for opt in new_selected_options]))

                    matching_variant_gid = None
                    for existing_gid, existing_info in existing_variants.items():
                        existing_sku = existing_info.get('sku', '').strip()
                        existing_option_key = existing_info.get('options', ())
                        if variant_sku and existing_sku and variant_sku == existing_sku:
                            matching_variant_gid = existing_gid
                            break
                        elif new_option_key and existing_option_key == new_option_key:
                            matching_variant_gid = existing_gid
                            break
                    if not matching_variant_gid and variant_sku:
                        matching_variant_gid = variant_lookup_by_sku.get(variant_sku.lower())

                    if matching_variant_gid:
                        variant_update_mutation = """
                        mutation productVariantUpdate($input: ProductVariantInput!) {
                            productVariantUpdate(input: $input) {
                                productVariant { id sku }
                                userErrors { field message }
                            }
                        }
                        """

                        variant_input = {'id': matching_variant_gid}
                        if 'price' in variant_data:
                            variant_input['price'] = str(variant_data.get('price', '0'))
                        if variant_sku:
                            variant_input['sku'] = variant_sku
                        if 'barcode' in variant_data and variant_data.get('barcode'):
                            variant_input['barcode'] = variant_data['barcode']
                        if 'weight' in variant_data:
                            variant_input['weight'] = variant_data.get('weight', 0)
                            variant_input['weightUnit'] = self._normalize_weight_unit(variant_data.get('weight_unit'))

                        if location_id and variant_data.get('inventory_quantity') is not None:
                            variant_input['inventoryQuantities'] = [{
                                'availableQuantity': variant_data.get('inventory_quantity', 0) or 0,
                                'locationId': location_id
                            }]

                        try:
                            update_response = requests.post(
                                self.graphql_url,
                                headers=self.headers,
                                json={'query': variant_update_mutation, 'variables': {'input': variant_input}},
                                timeout=30
                            )
                            update_response.raise_for_status()
                            update_result = update_response.json()

                            if 'errors' in update_result:
                                print(f"[update] Error updating variant {variant_sku}: {update_result['errors']}")
                                failed_count += 1
                            else:
                                user_errors = update_result.get('data', {}).get('productVariantUpdate', {}).get('userErrors', [])
                                if user_errors:
                                    print(f"[update] User errors updating variant {variant_sku}: {user_errors}")
                                    failed_count += 1
                                else:
                                    updated_count += 1
                                    variant_node = update_result.get('data', {}).get('productVariantUpdate', {}).get('productVariant', {})
                                    variant_gid_updated = variant_node.get('id', matching_variant_gid)
                                    variant_sku_updated = variant_node.get('sku', variant_sku)
                                    variant_records.append({'gid': variant_gid_updated, 'sku': variant_sku_updated or variant_sku})
                                    if updated_count <= 3 or updated_count % 10 == 0:
                                        print(f"[update] Variant {variant_sku} updated ({updated_count}/{len(variants_input)})")

                            time.sleep(0.1)
                        except Exception as e:
                            print(f"[update] Exception updating variant {variant_sku}: {e}")
                            failed_count += 1
                    else:
                        variant_create_mutation = """
                        mutation productVariantCreate($productId: ID!, $variant: ProductVariantInput!) {
                            productVariantCreate(productId: $productId, variant: $variant) {
                                productVariant { id sku }
                                userErrors { field message }
                            }
                        }
                        """

                        variant_input = {
                            'price': str(variant_data.get('price', '0')),
                            'sku': variant_sku if variant_sku else None,
                            'barcode': variant_data.get('barcode', '') or None,
                            'weight': variant_data.get('weight', 0) or 0,
                            'weightUnit': self._normalize_weight_unit(variant_data.get('weight_unit'))
                        }

                        if new_selected_options:
                            variant_input['selectedOptions'] = new_selected_options
                        else:
                            variant_input['selectedOptions'] = [{'name': 'Title', 'value': variant_sku if variant_sku else f"Variant-{created_count+1}"}]

                        if location_id and variant_data.get('inventory_quantity') is not None:
                            variant_input['inventoryQuantities'] = [{
                                'availableQuantity': variant_data.get('inventory_quantity', 0) or 0,
                                'locationId': location_id
                            }]

                        try:
                            create_response = requests.post(
                                self.graphql_url,
                                headers=self.headers,
                                json={'query': variant_create_mutation, 'variables': {'productId': product_gid, 'variant': variant_input}},
                                timeout=30
                            )
                            create_response.raise_for_status()
                            create_result = create_response.json()

                            if 'errors' in create_result:
                                print(f"[update] Error creating variant {variant_sku}: {create_result['errors']}")
                                failed_count += 1
                            else:
                                user_errors = create_result.get('data', {}).get('productVariantCreate', {}).get('userErrors', [])
                                if user_errors:
                                    print(f"[update] User errors creating variant {variant_sku}: {user_errors}")
                                    failed_count += 1
                                else:
                                    created_count += 1
                                    variant_node = create_result.get('data', {}).get('productVariantCreate', {}).get('productVariant', {})
                                    variant_records.append({'gid': variant_node.get('id'), 'sku': variant_node.get('sku', variant_sku)})
                                    if created_count <= 3 or created_count % 10 == 0:
                                        print(f"[update] Variant {variant_sku} created ({created_count} new variants)")

                            time.sleep(0.1)
                        except Exception as e:
                            print(f"[update] Exception creating variant {variant_sku}: {e}")
                            failed_count += 1

                print(f"[update] Variant update summary: {updated_count} updated, {created_count} created, {failed_count} failed")

            # Step 4: Add product-level images (append; no delete)
            if 'images' in product_data and product_data['images']:
                print(f"[update] Adding {len(product_data['images'])} product images during update...")
                image_mutation = """
                mutation productImageCreate($input: ImageInput!) {
                    productImageCreate(input: $input) {
                        image { id src }
                        userErrors { field message }
                    }
                }
                """
                added_images = 0
                for idx, img_url in enumerate(product_data['images']):
                    if not img_url or not str(img_url).strip():
                        continue
                    try:
                        image_response = requests.post(
                            self.graphql_url,
                            headers=self.headers,
                            json={'query': image_mutation, 'variables': {'input': {'productId': product_gid, 'src': str(img_url).strip()}}},
                            timeout=30
                        )
                        image_response.raise_for_status()
                        image_result = image_response.json()
                        user_errors = image_result.get('data', {}).get('productImageCreate', {}).get('userErrors', [])
                        if user_errors:
                            print(f"[update] User errors adding product image {idx+1}: {user_errors}")
                        else:
                            added_images += 1
                    except Exception as e:
                        print(f"[update] Could not add product image {idx+1}: {e}")
                    time.sleep(0.1)
                print(f"[update] Product images added: {added_images}/{len(product_data['images'])}")

            # Step 5: Add variant-specific images (append)
            if variant_images_map and 'variant_records' in locals() and variant_records:
                print(f"[update] Linking images to {len(variant_images_map)} variants during update...")
                image_mutation = """
                mutation productImageCreate($input: ImageInput!) {
                    productImageCreate(input: $input) {
                        image { id src }
                        userErrors { field message }
                    }
                }
                """
                linked = 0
                for variant_sku, image_url in variant_images_map.items():
                    if not image_url:
                        continue
                    matching_variant = None
                    for rec in variant_records:
                        rec_sku = (rec.get('sku') or '').strip()
                        if rec_sku and variant_sku and rec_sku.lower() == variant_sku.lower():
                            matching_variant = rec
                            break
                    if not matching_variant:
                        continue

                    variant_gid = matching_variant.get('gid')
                    if not variant_gid:
                        continue

                    try:
                        image_response = requests.post(
                            self.graphql_url,
                            headers=self.headers,
                            json={'query': image_mutation, 'variables': {'input': {'productId': product_gid, 'src': str(image_url).strip(), 'variantIds': [variant_gid]}}},
                            timeout=30
                        )
                        image_response.raise_for_status()
                        image_result = image_response.json()
                        user_errors = image_result.get('data', {}).get('productImageCreate', {}).get('userErrors', [])
                        if user_errors:
                            print(f"[update] User errors adding variant image for SKU {variant_sku}: {user_errors}")
                        else:
                            linked += 1
                    except Exception as e:
                        print(f"[update] Could not add variant image for SKU {variant_sku}: {e}")
                    time.sleep(0.1)
                print(f"[update] Variant images linked: {linked}/{len(variant_images_map)}")

            # Step 6: Update product metafields if provided
            if 'metafields' in product_data and product_data['metafields']:
                print(f"[update] Updating {len(product_data['metafields'])} product metafields...")
                self._add_product_metafields(product_gid, product_data['metafields'])

            # Step 7: Update variant metafields if provided
            if variant_metafields_map and 'variant_records' in locals() and variant_records:
                print(f"[update] Updating variant metafields for {len(variant_metafields_map)} variants...")
                for variant_sku, metafields in variant_metafields_map.items():
                    if not metafields:
                        continue

                    matching_variant = None
                    for rec in variant_records:
                        rec_sku = (rec.get('sku') or '').strip()
                        if rec_sku and variant_sku and rec_sku.lower() == variant_sku.lower():
                            matching_variant = rec
                            break

                    if not matching_variant:
                        continue

                    variant_gid = matching_variant.get('gid')
                    if variant_gid and 'None' not in str(variant_gid):
                        self._add_variant_metafields(variant_gid, metafields)

            return {'id': product_id, 'status': 'updated'}

        except requests.exceptions.HTTPError as e:
            error_msg = f"HTTP Error updating product {product_id}: {e}"
            if hasattr(e, 'response') and e.response is not None:
                try:
                    error_body = e.response.json()
                    error_msg += f" | Response: {error_body}"
                except:
                    error_msg += f" | Response text: {e.response.text[:500]}"
            raise Exception(error_msg)
        except Exception as e:
            raise Exception(f"Failed to update product: {str(e)}")

    def add_product_to_collection(self, product_id: int, collection_id: int):
        """Add product to collection - FIXED: Better error handling for 422"""
        try:
            try:
                if self.use_library:
                    collection = shopify.CustomCollection.find(collection_id)
                    if collection:
                        products = collection.products()
                        for p in products:
                            if p.id == product_id:
                                return
                        collection.add_product(product_id)
                else:
                    response = requests.get(
                        f"{self.base_url}/collects.json",
                        headers=self.headers,
                        params={'collection_id': collection_id, 'limit': 250},
                        timeout=30
                    )
                    if response.status_code == 200:
                        collects = response.json().get('collects', [])
                        for collect in collects:
                            if collect.get('product_id') == product_id:
                                return
                    
                    payload = {
                        'collect': {
                            'product_id': product_id,
                            'collection_id': collection_id
                        }
                    }
                    response = requests.post(
                        f"{self.base_url}/collects.json",
                        headers=self.headers,
                        json=payload,
                        timeout=30
                    )
                    
                    if response.status_code == 422:
                        error_data = response.text
                        if 'already' in error_data.lower() or 'duplicate' in error_data.lower():
                            return
                        else:
                            print(f"Warning: Could not add product {product_id} to collection {collection_id}: {error_data}")
                            return
                    
                    response.raise_for_status()
            except requests.exceptions.HTTPError as e:
                if e.response.status_code == 422:
                    error_data = e.response.text
                    if 'already' in error_data.lower() or 'duplicate' in error_data.lower():
                        return
                    else:
                        print(f"Warning: Could not add product {product_id} to collection {collection_id}: {error_data}")
                        return
                else:
                    raise
        except Exception as e:
            error_msg = str(e).lower()
            if "already" in error_msg or "duplicate" in error_msg or "422" in error_msg:
                return
            print(f"Warning: Failed to add product {product_id} to collection {collection_id}: {str(e)}")
            return
    
    def delete_product(self, product_id: int):
        """Delete a product from Shopify"""
        try:
            if self.use_library:
                product = shopify.Product.find(product_id)
                if product:
                    product.destroy()
            else:
                response = requests.delete(
                    f"{self.base_url}/products/{product_id}.json",
                    headers=self.headers,
                    timeout=30
                )
                response.raise_for_status()
        except Exception as e:
            raise Exception(f"Failed to delete product: {str(e)}")
    
    def delete_collection(self, collection_id: int, collection_type: str = 'custom'):
        """Delete a collection from Shopify"""
        try:
            if self.use_library:
                if collection_type == 'custom':
                    collection = shopify.CustomCollection.find(collection_id)
                else:
                    collection = shopify.SmartCollection.find(collection_id)
                if collection:
                    collection.destroy()
            else:
                endpoint = 'custom_collections' if collection_type == 'custom' else 'smart_collections'
                response = requests.delete(
                    f"{self.base_url}/{endpoint}/{collection_id}.json",
                    headers=self.headers,
                    timeout=30
                )
                response.raise_for_status()
        except Exception as e:
            raise Exception(f"Failed to delete collection: {str(e)}")
    
    def delete_product_by_id(self, product_id: int):
        """Delete product by ID"""
        return self.delete_product(product_id)
    
    def delete_collection_by_id(self, collection_id: int, collection_type: str = 'custom'):
        """Delete collection by ID"""
        return self.delete_collection(collection_id, collection_type)
    
    def rollback_last_sync(self, sync_products: List[Dict]):
        """Rollback last sync by deleting products"""
        deleted_count = 0
        for sync_product in sync_products:
            try:
                if sync_product.get('created_by_api', 1) == 1:
                    self.delete_product(sync_product['shopify_product_id'])
                    deleted_count += 1
            except Exception as e:
                print(f"Warning: Could not delete product {sync_product.get('shopify_product_id')}: {e}")
        return deleted_count
    
    def delete_all_data(self):
        """Delete all products and collections from Shopify"""
        try:
            # Get all products
            all_products = []
            if self.use_library:
                products = shopify.Product.find(limit=250)
                for product in products:
                    all_products.append(product.id)
            else:
                url = f"{self.base_url}/products.json"
                params = {'limit': 250}
                while True:
                    response = requests.get(url, headers=self.headers, params=params, timeout=30)
                    response.raise_for_status()
                    data = response.json()
                    products = data.get('products', [])
                    if not products:
                        break
                    for product in products:
                        all_products.append(product['id'])
                    link_header = response.headers.get('Link', '')
                    if link_header and 'rel="next"' in link_header:
                        import re
                        match = re.search(r'page_info=([^>]+)', link_header)
                        if match:
                            params = {'limit': 250, 'page_info': match.group(1)}
                        else:
                            break
                    else:
                        break
            
            # Delete all products
            for product_id in all_products:
                try:
                    self.delete_product(product_id)
                except Exception as e:
                    print(f"Warning: Could not delete product {product_id}: {e}")
            
            # Get and delete all collections
            collections = self.get_collections()
            for coll in collections:
                try:
                    self.delete_collection(coll['id'], coll['type'])
                except Exception as e:
                    print(f"Warning: Could not delete collection {coll['id']}: {e}")
            
            return len(all_products), len(collections)
        except Exception as e:
            raise Exception(f"Failed to delete all data: {str(e)}")

