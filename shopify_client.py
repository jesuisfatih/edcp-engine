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
            
            product_input = {
                'title': product_data.get('title', 'Product'),
                'descriptionHtml': product_data.get('description', '') or '',
                'vendor': product_data.get('vendor', '') or '',
                'productType': product_data.get('product_type', '') or '',
                'tags': product_data.get('tags', '').split(',') if product_data.get('tags') else [],
                'status': product_data.get('status', 'ACTIVE').upper()
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
            
            # Step 2: Add product options
            if variants:
                # Determine option names from variants
                option_names = []
                if any(v.get('option1') for v in variants):
                    option_names.append('Color')
                if any(v.get('option2') for v in variants):
                    option_names.append('Size')
                if any(v.get('option3') for v in variants):
                    option_names.append('Style')
                
                if option_names:
                    options_mutation = """
                    mutation productOptionsUpdate($productId: ID!, $options: [ProductOptionInput!]!) {
                        productOptionsUpdate(productId: $productId, options: $options) {
                            product {
                                id
                            }
                            userErrors {
                                field
                                message
                            }
                        }
                    }
                    """
                    
                    options_input = [{'name': name} for name in option_names]
                    
                    options_response = requests.post(
                        self.graphql_url,
                        headers=self.headers,
                        json={
                            'query': options_mutation,
                            'variables': {
                                'productId': product_gid,
                                'options': options_input
                            }
                        },
                        timeout=30
                    )
                    options_response.raise_for_status()
                    time.sleep(0.2)
            
            # Step 3: Get location ID for inventory
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
                option1 = str(variant_data.get('option1', '')).strip()
                option2 = str(variant_data.get('option2', '')).strip()
                option3 = str(variant_data.get('option3', '')).strip()
                sku = str(variant_data.get('sku', '')).strip()
                
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
                    'weightUnit': variant_data.get('weight_unit', 'POUNDS').upper()
                }
                
                # CRITICAL: selectedOptions is REQUIRED for variants when product has options
                selected_options = []
                if option1:
                    selected_options.append({'name': 'Color', 'value': option1})
                if option2:
                    selected_options.append({'name': 'Size', 'value': option2})
                if option3:
                    selected_options.append({'name': 'Style', 'value': option3})
                
                # If no options, create default option to ensure variant is created
                if not selected_options:
                    print(f"Warning: Variant {sku} has no options, creating default option")
                    selected_options.append({'name': 'Default', 'value': sku if sku else f'Variant-{len(unique_variants)+1}'})
                
                variant_input['selectedOptions'] = selected_options
                
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
                
                for v in unique_variants:
                    image_url = v.pop('_image', None)
                    metafields = v.pop('_metafields', {})
                    variant_sku = v.get('sku', '')
                    if image_url and variant_sku:
                        variant_images_map[variant_sku] = image_url
                    if metafields and variant_sku:
                        variant_metafields_map[variant_sku] = metafields
                
                variant_mutation = """
                mutation productVariantCreate($productId: ID!, $variant: ProductVariantInput!) {
                    productVariantCreate(productId: $productId, variant: $variant) {
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
                        'weightUnit': variant_input.get('weightUnit', 'POUNDS')
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
                        variant_response = requests.post(
                            self.graphql_url,
                            headers=self.headers,
                            json={
                                'query': variant_mutation,
                                'variables': {
                                    'productId': product_gid,
                                    'variant': variant_payload
                                }
                            },
                            timeout=30
                        )
                        variant_response.raise_for_status()
                        variant_result = variant_response.json()
                        
                        if 'errors' in variant_result:
                            error_messages = [e.get('message', str(e)) for e in variant_result['errors']]
                            print(f"Error creating variant {variant_sku} ({idx+1}/{len(unique_variants)}): {', '.join(error_messages)}")
                            failed_count += 1
                            continue
                        
                        variant_create = variant_result.get('data', {}).get('productVariantCreate', {})
                        variant_user_errors = variant_create.get('userErrors', [])
                        
                        if variant_user_errors:
                            error_messages = [e.get('message', str(e)) for e in variant_user_errors]
                            print(f"Error creating variant {variant_sku} ({idx+1}/{len(unique_variants)}): {', '.join(error_messages)}")
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
                            if (idx + 1) % 10 == 0:
                                print(f"Progress: {idx+1}/{len(unique_variants)} variants created ({created_count} successful, {failed_count} failed)")
                        else:
                            print(f"Warning: Variant {variant_sku} created but no variant node returned")
                            failed_count += 1
                        
                        time.sleep(0.1)
                        
                    except Exception as e:
                        print(f"Exception creating variant {variant_sku} ({idx+1}/{len(unique_variants)}): {e}")
                        failed_count += 1
                        continue
                
                print(f"Variant creation complete: {created_count} successful, {failed_count} failed out of {len(unique_variants)} total")
                
                # CRITICAL: If no variants were created, this is a fatal error
                if created_count == 0:
                    raise Exception(f"CRITICAL: Failed to create any variants for product {product.get('title')}. Product created but has no variants.")
            else:
                raise Exception("CRITICAL: No variants to create. Product cannot exist without variants.")
            
            # Step 5: Add product images
            product_images = product_data.get('images', [])
            if product_images:
                print(f"Adding {len(product_images)} product-level images...")
                image_count = 0
                for idx, img_url in enumerate(product_images):
                    if not img_url or not img_url.strip():
                        continue
                    
                    image_mutation = """
                    mutation productImageCreate($productId: ID!, $image: ImageInput!) {
                        productImageCreate(productId: $productId, image: $image) {
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
                    
                    image_input = {'src': img_url.strip()}
                    
                    try:
                        image_response = requests.post(
                            self.graphql_url,
                            headers=self.headers,
                            json={
                                'query': image_mutation,
                                'variables': {
                                    'productId': product_gid,
                                    'image': image_input
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
                print(f"Adding variant-specific images for {len(variant_images_map)} variants...")
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
                        variant_gid = matching_variant.get('gid') or f"gid://shopify/ProductVariant/{matching_variant.get('id')}"
                        if not variant_gid or 'None' in variant_gid:
                            print(f"Warning: Invalid variant GID for SKU {variant_sku}, skipping image")
                            continue
                        image_mutation = """
                        mutation productImageCreate($productId: ID!, $image: ImageInput!) {
                            productImageCreate(productId: $productId, image: $image) {
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
                        
                        image_input = {
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
                                        'productId': product_gid,
                                        'image': image_input
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
                                    print(f"Successfully added variant image for SKU: {variant_sku} ({variant_image_count}/{len(variant_images_map)})")
                            time.sleep(0.15)
                        except Exception as e:
                            print(f"Warning: Could not add variant image for {variant_sku}: {e}")
                    else:
                        print(f"Warning: Could not find variant with SKU {variant_sku} for image mapping")
                print(f"Variant images complete: {variant_image_count}/{len(variant_images_map)} variant images added")
            else:
                print(f"Warning: No variant images to add (variant_images_map is empty or None)")
            
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
            
            print(f"Creating product with {variant_count} variants using GraphQL API.")
            return self._create_product_with_graphql(product_data)
            
        except Exception as e:
            raise Exception(f"Failed to create product: {str(e)}")
    
    def _create_product_with_rest(self, product_data: Dict) -> Dict:
        """DEPRECATED: REST API method - kept for fallback only (not used)"""
        raise Exception("REST API method is deprecated. Use GraphQL instead.")
    
    def update_product(self, product_id: int, product_data: Dict) -> Dict:
        """Update existing product"""
        try:
            if self.use_library:
                product = shopify.Product.find(product_id)
                
                if 'title' in product_data:
                    product.title = product_data['title']
                if 'description' in product_data:
                    product.body_html = product_data['description']
                if 'tags' in product_data:
                    product.tags = product_data['tags']
                if 'status' in product_data:
                    product.status = product_data['status']
                
                if 'variants' in product_data:
                    for variant_data in product_data['variants']:
                        variant_id = variant_data.get('id')
                        if variant_id:
                            variant = next((v for v in product.variants if v.id == variant_id), None)
                            if variant:
                                if 'price' in variant_data:
                                    variant.price = str(variant_data['price'])
                                if 'inventory_quantity' in variant_data:
                                    variant.inventory_quantity = variant_data['inventory_quantity']
                                if 'sku' in variant_data:
                                    variant.sku = variant_data['sku']
                
                product.save()
                
                return {
                    'id': product.id,
                    'status': 'updated'
                }
            else:
                # Use REST API
                payload = {'product': {}}
                
                if 'title' in product_data:
                    payload['product']['title'] = product_data['title']
                if 'description' in product_data:
                    payload['product']['body_html'] = product_data['description']
                if 'tags' in product_data:
                    payload['product']['tags'] = product_data['tags']
                if 'status' in product_data:
                    payload['product']['status'] = product_data['status']
                
                if 'variants' in product_data:
                    # First, get existing product to see current variants
                    existing_response = requests.get(
                        f"{self.base_url}/products/{product_id}.json",
                        headers=self.headers
                    )
                    existing_response.raise_for_status()
                    existing_product = existing_response.json()['product']
                    existing_variants = {v.get('id'): v for v in existing_product.get('variants', [])}
                    
                    payload['product']['variants'] = []
                    for variant_data in product_data['variants']:
                        variant_payload = {}
                        
                        # Try to match existing variant by SKU or option values
                        variant_id = None
                        variant_sku = variant_data.get('sku', '').strip()
                        variant_option1 = str(variant_data.get('option1', '')).strip()
                        variant_option2 = str(variant_data.get('option2', '')).strip()
                        
                        # Find matching existing variant - CRITICAL: Check all combinations
                        for existing_id, existing_variant in existing_variants.items():
                            existing_sku = str(existing_variant.get('sku', '')).strip()
                            existing_option1 = str(existing_variant.get('option1', '')).strip()
                            existing_option2 = str(existing_variant.get('option2', '')).strip()
                            
                            # Priority 1: Match by SKU (most reliable)
                            if variant_sku and existing_sku and variant_sku == existing_sku:
                                variant_id = existing_id
                                break
                            
                            # Priority 2: Match by option1 + option2 (both must match)
                            elif variant_option1 and variant_option2:
                                if (existing_option1 == variant_option1 and 
                                    existing_option2 == variant_option2):
                                    variant_id = existing_id
                                    break
                            
                            # Priority 3: Match by option1 only (if option2 is empty in both)
                            elif variant_option1 and not variant_option2:
                                if existing_option1 == variant_option1 and not existing_option2:
                                    variant_id = existing_id
                                    break
                            
                            # Priority 4: Match by option2 only (if option1 is empty in both)
                            elif variant_option2 and not variant_option1:
                                if existing_option2 == variant_option2 and not existing_option1:
                                    variant_id = existing_id
                                    break
                        
                        # If found, update existing variant
                        if variant_id:
                            variant_payload['id'] = variant_id
                            if 'price' in variant_data:
                                variant_payload['price'] = str(variant_data['price'])
                            if 'inventory_quantity' in variant_data:
                                variant_payload['inventory_quantity'] = variant_data['inventory_quantity']
                            if 'sku' in variant_data:
                                variant_payload['sku'] = variant_data['sku']
                            if 'option1' in variant_data:
                                variant_payload['option1'] = variant_data['option1']
                            if 'option2' in variant_data:
                                variant_payload['option2'] = variant_data['option2']
                            if 'option3' in variant_data:
                                variant_payload['option3'] = variant_data['option3']
                        else:
                            # New variant - add all fields
                            if 'price' in variant_data:
                                variant_payload['price'] = str(variant_data['price'])
                            if 'inventory_quantity' in variant_data:
                                variant_payload['inventory_quantity'] = variant_data['inventory_quantity']
                            if 'sku' in variant_data:
                                variant_payload['sku'] = variant_data['sku']
                            if 'option1' in variant_data:
                                variant_payload['option1'] = variant_data['option1']
                            if 'option2' in variant_data:
                                variant_payload['option2'] = variant_data['option2']
                            if 'option3' in variant_data:
                                variant_payload['option3'] = variant_data['option3']
                        
                        payload['product']['variants'].append(variant_payload)
                
                response = requests.put(
                    f"{self.base_url}/products/{product_id}.json",
                    headers=self.headers,
                    json=payload
                )
                response.raise_for_status()
                
                return {
                    'id': product_id,
                    'status': 'updated'
                }
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

