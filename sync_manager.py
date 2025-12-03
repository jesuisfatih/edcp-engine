from ss_api_client import SSActivewearClient
from shopify_client import ShopifyClient
from data_fetcher import DataFetcher
from variant_grouper import VariantGrouper

# NEW ARCHITECTURE imports
from shopify_gateway import ShopifyGateway
from sync_orchestrator import SyncOrchestrator
from database import init_database

# Cache invalidation
def invalidate_synced_styles(style_ids: list):
    """Invalidate cache for synced styles to force fresh data"""
    try:
        from cache_manager import cache_manager
        for style_id in style_ids:
            cache_manager.invalidate_style(str(style_id))
        print(f"✅ Invalidated cache for {len(style_ids)} synced styles")
    except Exception as e:
        print(f"Cache invalidation error: {e}")

from typing import Dict, List, Optional
import time
import uuid
from datetime import datetime
from database import save_sync_state, get_sync_state, save_sync_product, save_sync_history
import requests
import json

class SyncManager:
    """Manages synchronization between S&S Activewear and Shopify"""
    
    def __init__(self, ss_client: SSActivewearClient, 
                 shopify_client: ShopifyClient, 
                 sync_options: Dict):
        self.ss_client = ss_client
        self.shopify_client = shopify_client
        self.sync_options = sync_options
        self.sync_id = str(uuid.uuid4())
        self.status = 'idle'  # idle, running, paused, completed, error
        self.progress = 0
        self.message = ''
        self.stats = {
            'total': 0,
            'processed': 0,
            'created': 0,
            'updated': 0,
            'skipped': 0,
            'errors': 0
        }
        self.errors = []
        self._stop_flag = False
        self.current_product = None
        self.current_index = 0
        # Log system for detailed operation tracking
        self.logs = []  # List of log entries: {'timestamp': str, 'level': str, 'message': str, 'data': dict}
        self.created_products = []  # List of created products with Shopify links: {'title': str, 'shopify_id': int, 'shopify_url': str, 'handle': str}
        # Extract shop domain for building product URLs
        self.shop_domain = shopify_client.shop_domain.replace('https://', '').replace('http://', '').split('/')[0]
    
    def _add_log(self, level: str, message: str, data: dict = None):
        """Add a log entry with timestamp"""
        log_entry = {
            'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'level': level,  # 'info', 'success', 'warning', 'error', 'step'
            'message': message,
            'data': data or {}
        }
        self.logs.append(log_entry)
        
        # Also track in system monitor
        try:
            from app import add_system_log
            log_type_map = {
                'info': 'INFO', 'success': 'SUCCESS', 'warning': 'WARNING',
                'error': 'ERROR', 'step': 'SYNC'
            }
            add_system_log(log_type_map.get(level, 'SYNC'), message, 'main')
        except:
            pass
        # Keep only last 1000 logs to prevent memory issues
        if len(self.logs) > 1000:
            self.logs = self.logs[-1000:]
        # Also print to console for debugging
        print(f"[{log_entry['timestamp']}] [{level.upper()}] {message}")
    
    def stop(self):
        """Stop synchronization"""
        self._stop_flag = True
        self.status = 'paused'
        self.message = 'Sync stopped by user'
    
    def start_sync(self):
        """Start synchronization process - NEW ARCHITECTURE: Fetch -> Cache -> Group -> Sync"""
        self.status = 'running'
        self.message = 'Starting synchronization...'
        self.progress = 0
        self.current_product = None
        self.current_index = 0
        self.step = 'init'
        self.step_progress = 0
        self.step = None
        self.step_progress = 0
        # Clear logs and created products for new sync
        self.logs = []
        self.created_products = []
        self._add_log('step', '🚀 Aktarım başlatılıyor...', {'step': 'init'})
        
        try:
            # Inventory-only mode: just update qty on Shopify using cached products
            if self.sync_options.get('inventory_only'):
                self.message = 'Inventory-only sync: fetching products...'
                fetcher = DataFetcher(self.ss_client, self.sync_id)
                products = fetcher._get_products_to_sync(self.sync_options)
                sku_qty = {}
                for p in products:
                    sku = p.get('sku')
                    if sku:
                        sku_qty[sku] = p.get('qty', 0) or 0
                # Choose locations: from sync_options or primary
                loc_ids = self.sync_options.get('inventory_location_ids')
                if loc_ids and isinstance(loc_ids, str):
                    loc_ids = [l.strip() for l in loc_ids.split(',') if l.strip()]
                if not loc_ids:
                    loc_ids = None
                self.message = f'Updating inventory for {len(sku_qty)} SKUs...'
                result = self.shopify_client.update_inventory_bulk(sku_qty, location_ids=loc_ids)
                self.status = 'completed'
                self.progress = 100
                self.message = f"Inventory sync done: {result.get('updated',0)} updated, {len(result.get('failed',[]))} failed"
                # Log failures for visibility
                if result.get('failed'):
                    print(f"[inventory] Failed entries: {result['failed'][:10]}")
                save_sync_history(
                    self.sync_id,
                    self.status,
                    len(sku_qty),
                    0,
                    0,
                    len(result.get('failed', [])),
                    self.message,
                    self.sync_options
                )
                return

            # STEP 1: Fetch products from S&S API and cache in local database
            self.message = 'Fetching products from S&S Activewear...'
            self.progress = 5
            self.step = 'fetch'
            self.step_progress = 5
            self._add_log('step', '📥 S&S Activewear API\'den ürünler çekiliyor...', {'step': 'fetch'})
            
            try:
                data_fetcher = DataFetcher(self.ss_client, self.sync_id)
                cached_count = data_fetcher.fetch_and_cache_products(self.sync_options)
                
                if cached_count == 0:
                    self.status = 'completed'
                    filter_info = []
                    if self.sync_options.get('filter_categories'):
                        cats = self.sync_options.get('filter_categories')
                        filter_info.append(f"Kategoriler: {cats if isinstance(cats, list) else str(cats)}")
                    if self.sync_options.get('filter_styles'):
                        styles = self.sync_options.get('filter_styles')
                        filter_info.append(f"Stiller: {styles if isinstance(styles, list) else str(styles)}")
                    if self.sync_options.get('filter_brands'):
                        brands = self.sync_options.get('filter_brands')
                        filter_info.append(f"Markalar: {brands if isinstance(brands, list) else str(brands)}")
                    if self.sync_options.get('filter_warehouses'):
                        warehouses = self.sync_options.get('filter_warehouses')
                        filter_info.append(f"Depolar: {warehouses if isinstance(warehouses, list) else str(warehouses)}")
                    
                    filter_msg = '. '.join(filter_info) if filter_info else 'Filtre yok'
                    self.message = f'Ürün bulunamadı. Seçilen filtreler: {filter_msg}. Lütfen filtreleri kontrol edin veya farklı filtreler deneyin.'
                    self._add_log('warning', f'⚠️ {self.message}')
                    self.progress = 100
                    self.step_progress = 100
                    return
                
                self.progress = 20
                self.step_progress = 20
                self.message = f'Cached {cached_count} products to local database'
                self._add_log('success', f'✅ {cached_count} ürün veritabanına kaydedildi')
                
            except Exception as e:
                error_msg = str(e)
                if '403' in error_msg or 'Forbidden' in error_msg:
                    self.status = 'error'
                    self.message = (
                        f'Authentication failed while fetching products. '
                        f'Please verify your API credentials are correct and active. '
                        f'Error: {error_msg}'
                    )
                    self._add_log('error', f'❌ Kimlik doğrulama hatası: {error_msg}')
                    self.errors.append({
                        'error': f'Authentication failed: {error_msg}',
                        'timestamp': datetime.now().isoformat()
                    })
                    return
                else:
                    self.status = 'error'
                    self.message = f'Error fetching products: {str(e)}'
                    self._add_log('error', f'❌ Ürün çekme hatası: {error_msg}')
                    self.errors.append({
                        'error': str(e),
                        'timestamp': datetime.now().isoformat()
                    })
                    return
            
            # STEP 2: Group products by styleID
            self.message = 'Grouping products by styleID...'
            self.progress = 25
            self.step = 'group'
            self.step_progress = 25
            self._add_log('step', '📦 Ürünler styleID\'ye göre gruplanıyor...', {'step': 'group'})
            
            try:
                grouper = VariantGrouper(self.sync_id, self.sync_options)
                groups_count = grouper.group_products()
                
                if groups_count == 0:
                    self.status = 'error'
                    self.message = 'No product groups created'
                    self._add_log('error', '❌ Ürün grubu oluşturulamadı')
                    return
                
                self.progress = 30
                self.message = f'Created {groups_count} product groups'
                self._add_log('success', f'✅ {groups_count} ürün grubu oluşturuldu')
                
            except Exception as e:
                self.status = 'error'
                self.message = f'Error grouping products: {str(e)}'
                self._add_log('error', f'❌ Gruplama hatası: {str(e)}')
                self.errors.append({
                    'error': str(e),
                    'timestamp': datetime.now().isoformat()
                })
                return
            
            # STEP 3: Get product groups from database and sync to Shopify
            self.message = 'Syncing product groups to Shopify...'
            self.progress = 35
            self.step = 'sync'
            self.step_progress = 35
            self._add_log('step', '🔄 NEW ARCHITECTURE: Style-based sync başlatılıyor...', {'step': 'sync'})
            
            # Initialize database (create new architecture tables)
            init_database()
            
            # Create Shopify Gateway
            shopify_gateway = ShopifyGateway(
                shop_domain=self.shopify_client.shop_domain,
                access_token=self.shopify_client.access_token
            )
            
            # NOT: Otomatik silme KALDIRILDI - Güvenlik için
            # Artık sadece CREATE/UPDATE yapılıyor, silme işlemi manuel tetiklenmeli
            self._add_log('info', '🔒 Güvenli mod: Mevcut ürünler korunuyor, sadece güncelleme/oluşturma yapılacak')
            
            # Create Sync Orchestrator (with sync_options for arbitraj pricing etc.)
            # Pass self as parent for real-time stats updates
            orchestrator = SyncOrchestrator(
                sync_id=self.sync_id,
                shopify_gateway=shopify_gateway,
                log_callback=self._add_log,
                sync_options=self.sync_options,
                parent_sync_manager=self  # Enable real-time stats updates
            )
            
            # Execute sync with new architecture
            sync_stats = orchestrator.sync_all_styles()
            
            # Update our stats
            self.stats['created'] = sync_stats.get('products_created', 0)
            self.stats['updated'] = sync_stats.get('products_updated', 0)
            self.stats['errors'] = sync_stats.get('errors', 0)
            
            self._add_log('step', '✅ NEW ARCHITECTURE sync complete', {'stats': sync_stats})
            
            # Invalidate cache for synced styles
            synced_styles = list(set(p.get('styleID') for p in self._cached_products if p.get('styleID'))) if hasattr(self, '_cached_products') else []
            if synced_styles:
                invalidate_synced_styles(synced_styles)
            
            # NEW ARCHITECTURE is the ONLY way - no fallback
            self.status = 'completed'
            self.progress = 100
            
            self._add_log('success', f'🎉 NEW ARCHITECTURE complete: {sync_stats.get("products_created", 0)} created, {sync_stats.get("errors", 0)} errors')
            
            # Save sync results
            save_sync_history(
                self.sync_id,
                self.status,
                self.stats['total'],
                self.stats['created'],
                self.stats['updated'],
                self.stats['errors'],
                self.message,
                json.dumps(self.sync_options)
            )
            
            return  # EXIT - no old fallback
            
            product_groups = grouper.get_product_groups(status='pending')
            total_groups = len(product_groups)
            self.stats['total'] = total_groups
            
            if total_groups == 0:
                self.status = 'completed'
                self.message = 'No product groups to sync'
                self.progress = 100
                return
            
            processed_groups = 0
            
            for group in product_groups:
                if self._stop_flag:
                    self.status = 'stopped'
                    self.message = 'Sync stopped by user'
                    break
                
                processed_groups += 1
                self.current_index = processed_groups - 1
                
                # Update progress
                progress_pct = 35 + int(processed_groups / total_groups * 60)
                self.progress = progress_pct
                
                group_id = group['group_id']
                product_name = group.get('title', 'Unknown Product')
                
                # Update current product info for UI display
                self.current_product = {
                    'sku': group_id,
                    'styleName': product_name,
                    'brandName': group.get('vendor', ''),
                    'colorName': '',
                    'title': product_name,
                    'index': processed_groups - 1,
                    'total': total_groups
                }
                
                self.message = f'Processing {processed_groups}/{total_groups}: {product_name}'
                self._add_log('info', f'📋 İşleniyor ({processed_groups}/{total_groups}): {product_name}', {
                    'group_id': group_id,
                    'product_name': product_name,
                    'progress': processed_groups,
                    'total': total_groups
                })
                
                try:
                    # Get variants and images for this group
                    variants = grouper.get_variants_for_group(group_id)
                    images = grouper.get_images_for_group(group_id)
                    
                    print(f"📋 Group {group_id}: {len(variants)} variants, {len(images)} images from database")
                    
                    if not variants or len(variants) == 0:
                        print(f"❌ ERROR: Group {group_id} has NO variants! Skipping...")
                        self.stats['errors'] += 1
                        self.errors.append({
                            'sku': group_id,
                            'error': 'No variants found in database for this group',
                            'timestamp': datetime.now().isoformat()
                        })
                        continue
                    
                    # Build Shopify product data
                    product_data = self._build_product_data_from_group(group, variants, images)
                    
                    # CRITICAL: Validate product_data before sending
                    if not product_data.get('variants') or len(product_data['variants']) == 0:
                        print(f"❌ ERROR: Product data has NO variants after building! Skipping...")
                        self.stats['errors'] += 1
                        continue
                    
                    # Sync to Shopify
                    self._sync_product_from_group(group_id, product_data, variants)
                    
                    # Update group status
                    self._update_group_status(group_id, 'synced')
                    
                    self.stats['processed'] += len(variants)
                
                except Exception as e:
                    self.stats['errors'] += len(variants) if 'variants' in locals() else 1
                    error_msg = str(e)
                    self.errors.append({
                        'sku': group_id,
                        'error': error_msg,
                        'timestamp': datetime.now().isoformat()
                    })
                    # Update group status to error
                    self._update_group_status(group_id, 'error')
                
                # Rate limiting
                time.sleep(0.5)
            
            # Clear current product when done
            self.current_product = None
            self.current_index = 0
            
            self.status = 'completed'
            self.progress = 100
            self.message = f'Sync completed: {self.stats["created"]} created, {self.stats["updated"]} updated, {self.stats["errors"]} errors'
            self._add_log('success', f'🎉 Aktarım tamamlandı! {self.stats["created"]} oluşturuldu, {self.stats["updated"]} güncellendi, {self.stats["errors"]} hata', {
                'stats': self.stats,
                'created_products_count': len(self.created_products)
            })
            # Save final state
            save_sync_state(self.sync_id, self.status, 100, total_groups, total_groups, self.stats)
            # Save sync history
            save_sync_history(
                self.sync_id,
                self.status,
                self.stats.get('total', 0),
                self.stats.get('created', 0),
                self.stats.get('updated', 0),
                self.stats.get('errors', 0),
                self.message,
                self.sync_options
            )
        
        except Exception as e:
            self.status = 'error'
            self.message = f'Sync failed: {str(e)}'
            self.errors.append({
                'error': str(e),
                'timestamp': datetime.now().isoformat()
            })
            # Save error state
            save_sync_state(self.sync_id, self.status, self.progress, self.current_index, self.stats.get('total', 0), self.stats)
            # Save sync history
            save_sync_history(
                self.sync_id,
                self.status,
                self.stats.get('total', 0),
                self.stats.get('created', 0),
                self.stats.get('updated', 0),
                self.stats.get('errors', 0),
                self.message,
                self.sync_options
            )
    
    def _get_products_to_sync(self) -> List[Dict]:
        """Get products to sync based on options - OPTIMIZED with API-level filtering"""
        try:
            # Normalize filters
            category_ids = self.sync_options.get('filter_categories', [])
            if isinstance(category_ids, list):
                category_list = [str(cid).strip() for cid in category_ids if cid]
            elif isinstance(category_ids, str):
                category_list = [c.strip() for c in category_ids.split(',') if c.strip()]
            else:
                category_list = [str(category_ids).strip()] if category_ids else []
            
            style_ids = self.sync_options.get('filter_styles', [])
            if isinstance(style_ids, list):
                style_list = []
                for sid in style_ids:
                    if sid:
                        try:
                            style_list.append(int(sid))
                        except (ValueError, TypeError):
                            pass
            elif isinstance(style_ids, str):
                style_list = []
                for sid in style_ids.split(','):
                    sid = sid.strip()
                    if sid and sid.isdigit():
                        style_list.append(int(sid))
            else:
                style_list = [int(style_ids)] if style_ids and str(style_ids).isdigit() else []
            
            brand_filters = self.sync_options.get('filter_brands', [])
            brand_names = []
            if isinstance(brand_filters, list):
                for bf in brand_filters:
                    bf_str = str(bf).strip()
                    if bf_str and not bf_str.isdigit():
                        brand_names.append(bf_str)
            elif isinstance(brand_filters, str):
                brand_names = [b.strip() for b in brand_filters.split(',') if b.strip() and not b.strip().isdigit()]
            else:
                brand_names = [str(brand_filters).strip()] if brand_filters and not str(brand_filters).isdigit() else []
            
            print(f"=== PRODUCT FILTERING DEBUG ===")
            print(f"Categories: {category_list}")
            print(f"Styles: {style_list}")
            print(f"Brands: {brand_names}")
            
            all_products = []
            
            # OPTIMIZATION: If styles are selected, use API-level filtering with styleid parameter (batched)
            # Get warehouse filter
            warehouse_codes = self.sync_options.get('filter_warehouses', [])
            warehouse_param = ','.join(warehouse_codes) if warehouse_codes else None
            print(f"Warehouse filter: {warehouse_param or 'ALL (no filter)'}")
            
            if style_list:
                print(f"Using API-level filtering for {len(style_list)} styles (batched)...")
                def chunks(lst, n):
                    for i in range(0, len(lst), n):
                        yield lst[i:i+n]
                batched_products = []
                for batch in chunks(style_list, 50):
                    styleid_param = ','.join([str(sid) for sid in batch])
                    print(f"Fetching products with styleid batch size={len(batch)}, warehouses={warehouse_param}")
                    try:
                        # CRITICAL: Pass warehouse filter to API!
                        products = self.ss_client.get_products(styleid=styleid_param, warehouses=warehouse_param, limit=5000)
                        print(f"API returned {len(products)} products for batch")
                        batched_products.extend(products)
                    except Exception as e:
                        print(f"Error with styleid batch {batch}: {e}")
                        continue
                all_products = batched_products
            else:
                # No style filter, get all products
                print(f"No style filter, fetching all products with warehouses={warehouse_param}...")
                all_products = self.ss_client.get_products(warehouses=warehouse_param, limit=5000)
                print(f"Fetched {len(all_products)} products")
            
            # Filter by categories if selected (after style filter)
            # CRITICAL FIX: Products from styleid filter already match the styles
            # If styles were selected, we should SKIP category filter (styles already filtered by category)
            # Only apply category filter if NO styles were selected
            if category_list and all_products:
                # If we already filtered by styles, skip category filter (redundant and causes issues)
                if style_list:
                    print(f"SKIPPING category filter - already filtered by {len(style_list)} styles")
                    print(f"  Selected categories: {category_list} (will be ignored)")
                    print(f"  Reason: Styles are already filtered by categories, applying category filter would remove all products")
                else:
                    # Only apply category filter if no style filter was used
                    print(f"Filtering {len(all_products)} products by {len(category_list)} categories...")
                    print(f"Looking for categories: {category_list}")
                    filtered = []
                    sample_cats = []
                    for idx, product in enumerate(all_products[:5]):  # Sample first 5
                        sample_cats.append(f"Product {idx}: categories={product.get('categories')}, type={type(product.get('categories'))}")
                    print(f"Sample product categories: {sample_cats}")
                    
                    for product in all_products:
                        product_cats = product.get('categories', '')
                        if product_cats:
                            # Handle both string and list formats
                            if isinstance(product_cats, list):
                                product_cat_list = [str(c).strip() for c in product_cats if c]
                            else:
                                product_cat_list = [c.strip() for c in str(product_cats).split(',') if c.strip()]
                            
                            # Debug: print first product's category list
                            if len(filtered) == 0:
                                print(f"DEBUG: First product category list: {product_cat_list}")
                                print(f"DEBUG: Looking for: {category_list}")
                            
                            # Check if any selected category matches (as string)
                            # Try both exact match and string contains
                            matched = False
                            for cat in category_list:
                                cat_str = str(cat).strip()
                                # Exact match
                                if cat_str in product_cat_list:
                                    matched = True
                                    break
                                # Try as integer match (in case categories are stored as ints)
                                try:
                                    if int(cat_str) in [int(c) for c in product_cat_list if c.isdigit()]:
                                        matched = True
                                        break
                                except:
                                    pass
                            
                            if matched:
                                filtered.append(product)
                        else:
                            # If no categories field, skip category filter (include product)
                            # This might be needed if some products don't have categories
                            if not category_list:  # Only include if no category filter
                                filtered.append(product)
                    
                    all_products = filtered
                    print(f"After category filter: {len(all_products)} products")
                    
                    # If no products after category filter, show warning
                    if len(all_products) == 0 and len(filtered) == 0:
                        print("WARNING: Category filter removed all products!")
                        print(f"  Selected categories: {category_list}")
                        print(f"  Sample product had categories: {sample_cats[0] if sample_cats else 'N/A'}")
            
            # Filter by brands if selected
            if brand_names and all_products:
                print(f"Filtering {len(all_products)} products by {len(brand_names)} brands...")
                filtered = []
                for product in all_products:
                    product_brand = product.get('brandName', '').strip()
                    if product_brand in brand_names:
                        filtered.append(product)
                all_products = filtered
                print(f"After brand filter: {len(all_products)} products")
            
            # Remove duplicates by SKU
            seen_skus = set()
            unique_products = []
            for product in all_products:
                sku = product.get('sku')
                if sku and sku not in seen_skus:
                    seen_skus.add(sku)
                    unique_products.append(product)
            
            print(f"=== FINAL RESULT ===")
            print(f"Total unique products: {len(unique_products)}")
            
            if not unique_products:
                print("ERROR: No products found after all filters!")
                print(f"  Category filter: {category_list}")
                print(f"  Style filter: {style_list}")
                print(f"  Brand filter: {brand_names}")
                # Show sample product for debugging
                if all_products:
                    sample = all_products[0]
                    print(f"  Sample product categories: {sample.get('categories')}")
                    print(f"  Sample product styleID: {sample.get('styleID')}")
                    print(f"  Sample product brand: {sample.get('brandName')}")
                return []
            
            return unique_products
        except Exception as e:
            error_msg = str(e)
            print(f"Error in _get_products_to_sync: {error_msg}")
            if '403' in error_msg or 'Forbidden' in error_msg:
                raise Exception(
                    f"Authentication failed while fetching filtered products. "
                    f"Please verify your API Key has access to products endpoint. "
                    f"Original error: {error_msg}"
                )
            raise
        
        # Check if filtering by category (old method)
        if self.sync_options.get('filter_categories'):
            category_ids = self.sync_options.get('filter_categories')
            if isinstance(category_ids, list):
                category_ids = ','.join([str(cid) for cid in category_ids if cid])
            elif isinstance(category_ids, str):
                category_ids = category_ids
            
            if category_ids:
                try:
                    # Get all products and filter by category
                    all_products = []
                    # Get styles for each category
                    for cat_id in category_ids.split(','):
                        cat_id = cat_id.strip()
                        if cat_id:
                            # Get styles in this category by checking products
                            # Since API doesn't directly support category->products,
                            # we'll get all products and filter
                            products = self.ss_client.get_products()
                            for product in products:
                                if product.get('categories'):
                                    product_cats = [c.strip() for c in product['categories'].split(',')]
                                    if cat_id in product_cats:
                                        all_products.append(product)
                    
                    # Remove duplicates based on SKU
                    seen_skus = set()
                    unique_products = []
                    for product in all_products:
                        sku = product.get('sku')
                        if sku and sku not in seen_skus:
                            seen_skus.add(sku)
                            unique_products.append(product)
                    
                    return unique_products
                except Exception as e:
                    error_msg = str(e)
                    if '403' in error_msg or 'Forbidden' in error_msg:
                        raise Exception(
                            f"Authentication failed while fetching products by category. "
                            f"Please verify your API Key has access to products endpoint. "
                            f"Original error: {error_msg}"
                        )
                    raise
        
        # Check if filtering by style
        if self.sync_options.get('filter_style'):
            style = self.sync_options.get('filter_style')
            try:
                return self.ss_client.get_products(style=style)
            except Exception as e:
                error_msg = str(e)
                if '403' in error_msg or 'Forbidden' in error_msg:
                    raise Exception(
                        f"Authentication failed while fetching products by style. "
                        f"Please verify your API Key has access to products endpoint. "
                        f"Original error: {error_msg}"
                    )
                raise
        
        # Check if filtering by SKU/GTIN
        if self.sync_options.get('filter_sku'):
            sku_filter = self.sync_options.get('filter_sku')
            try:
                return self.ss_client.get_products(product_filter=sku_filter)
            except Exception as e:
                error_msg = str(e)
                if '403' in error_msg or 'Forbidden' in error_msg:
                    raise Exception(
                        f"Authentication failed while fetching products by SKU. "
                        f"Please verify your API Key has access to products endpoint. "
                        f"Original error: {error_msg}"
                    )
                raise
        
        # Check if filtering by part number
        if self.sync_options.get('filter_partnumber'):
            partnumber = self.sync_options.get('filter_partnumber')
            warehouses = self.sync_options.get('filter_warehouses')
            try:
                return self.ss_client.get_products(partnumber=partnumber, warehouses=warehouses)
            except Exception as e:
                error_msg = str(e)
                if '403' in error_msg or 'Forbidden' in error_msg:
                    raise Exception(
                        f"Authentication failed while fetching products by part number. "
                        f"Please verify your API Key has access to products endpoint. "
                        f"Original error: {error_msg}"
                    )
                raise
        
        # Check if filtering by brand
        if self.sync_options.get('filter_brand'):
            # Get styles by brand first
            try:
                styles = self.ss_client.get_styles(search=self.sync_options.get('filter_brand'))
                if styles:
                    style_ids = [str(s['styleID']) for s in styles]
                    return self.ss_client.get_products(styleid=','.join(style_ids))
            except Exception as e:
                error_msg = str(e)
                if '403' in error_msg or 'Forbidden' in error_msg:
                    raise Exception(
                        f"Authentication failed while fetching products by brand. "
                        f"Please verify your API Key has access to styles and products endpoints. "
                        f"Original error: {error_msg}"
                    )
                raise
        
        # Get all products
        if self.sync_options.get('sync_all_products', True):
            try:
                return self.ss_client.get_all_products()
            except Exception as e:
                error_msg = str(e)
                if '403' in error_msg or 'Forbidden' in error_msg:
                    raise Exception(
                        f"Authentication failed while fetching all products. "
                        f"This might indicate:\n"
                        f"1. API Key doesn't have access to products endpoint\n"
                        f"2. Rate limiting is blocking requests\n"
                        f"3. API Key permissions are limited\n\n"
                        f"Try using filters (Brand, Style, Category, or Part Number) instead of 'Sync All Products'.\n"
                        f"Contact api@ssactivewear.com for full API access.\n\n"
                        f"Original error: {error_msg}"
                    )
                raise
        
        return []
    
    def _build_product_data_from_group(self, group: Dict, variants: List[Dict], images: List[Dict]) -> Dict:
        """Build Shopify product data from database group"""
        print(f"🔨 Building product data for group: {group.get('title', 'N/A')}")
        print(f"   Variants from DB: {len(variants)}")
        print(f"   Images from DB: {len(images)}")
        
        # Build variants list
        def _normalize_weight_unit(unit):
            """Convert stored weight units into Shopify's expected enum values"""
            if not unit:
                return 'POUNDS'
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
            return mapping.get(str(unit).strip().lower(), 'POUNDS')
        variant_list = []
        variant_images_map = {}
        
        for idx, variant in enumerate(variants):
            # CRITICAL: Ensure option1 and option2 are never empty
            color_name = (variant.get('color_name') or '').strip()
            size_name = (variant.get('size_name') or '').strip()
            sku = (variant.get('sku') or '').strip()
            
            # Fallback if empty
            if not color_name:
                color_name = f"Color-{sku}" if sku else f"Color-{idx+1}"
            if not size_name:
                size_name = f"Size-{sku}" if sku else f"Size-{idx+1}"
            
            variant_data = {
                'sku': sku,
                'price': variant.get('price', '0'),
                'inventory_quantity': variant.get('inventory_quantity'),
                'option1': color_name,  # Color
                'option2': size_name,    # Size
                'barcode': variant.get('barcode'),
                'weight': variant.get('weight', 0) or 0,
                'weight_unit': _normalize_weight_unit(variant.get('weight_unit', 'lb'))
            }
            
            # Add variant image
            variant_image_url = (variant.get('variant_image_url') or '').strip()
            if variant_image_url:
                variant_data['image'] = variant_image_url
                variant_images_map[sku] = variant_image_url
                print(f"   Variant {idx+1} (SKU: {sku}) has image: {variant_image_url[:50]}...")
            else:
                print(f"   ⚠️ Variant {idx+1} (SKU: {sku}) has NO image")
            
            # Add variant metafields
            if variant.get('variant_metafields'):
                variant_data['metafields'] = variant['variant_metafields']
            
            variant_list.append(variant_data)
        
        print(f"✅ Built {len(variant_list)} variants (with images: {len(variant_images_map)})")
        
        # Build product images
        product_images = [img['image_url'] for img in images if img.get('image_type') == 'product' and img.get('image_url')]
        print(f"✅ Built {len(product_images)} product images")
        
        if not product_images:
            print(f"⚠️ WARNING: No product images found in database for group {group.get('group_id')}")
        
        # Build collections (if needed)
        collections = []
        if self.sync_options.get('sync_collections', True):
            create_if_not_exists = self.sync_options.get('create_collections', True)
            
            # Add category collections
            if group.get('base_category'):
                try:
                    if create_if_not_exists:
                        coll = self.shopify_client.find_or_create_collection(
                            group['base_category'],
                            handle=group['base_category'].lower().replace(' ', '-').replace('&', 'and')
                        )
                        collections.append(coll['id'])
                except Exception:
                    pass
            
            # Add brand collection
            if group.get('vendor') and self.sync_options.get('create_brand_collections', True):
                try:
                    if create_if_not_exists:
                        coll = self.shopify_client.find_or_create_collection(
                            group['vendor'],
                            handle=group['vendor'].lower().replace(' ', '-').replace('&', 'and')
                        )
                        collections.append(coll['id'])
                except Exception:
                    pass
            # Add category name collections if available in metafields
            if isinstance(group.get('product_metafields'), dict):
                cat_names = group['product_metafields'].get('categoryNames') or group['product_metafields'].get('categorynames')
                if cat_names and create_if_not_exists:
                    for cname in cat_names:
                        try:
                            coll = self.shopify_client.find_or_create_collection(
                                cname,
                                handle=cname.lower().replace(' ', '-').replace('&', 'and')
                            )
                            collections.append(coll['id'])
                        except Exception:
                            pass
        
        # CRITICAL VALIDATION: Must have at least 1 variant
        if not variant_list or len(variant_list) == 0:
            raise Exception(f"CRITICAL ERROR: Product {group.get('title')} has NO variants! Cannot create product without variants.")
        
        # Build product data
        product_data = {
            'title': group.get('title', 'Product'),
            'description': group.get('description', '') or '',
            'vendor': group.get('vendor', ''),
            'product_type': group.get('product_type', ''),
            'tags': group.get('tags', ''),
            'status': 'active' if self.sync_options.get('set_active', True) else 'draft',
            'images': product_images if product_images else [],  # Ensure it's a list
            'variants': variant_list,  # CRITICAL: Must have variants
            'collections': collections,
            'metafields': group.get('product_metafields', {}) if isinstance(group.get('product_metafields'), dict) else {}
        }
        
        # CRITICAL DEBUG: Log what we're sending to Shopify
        print(f"📦 Final product data for Shopify:")
        print(f"   Title: {product_data['title']}")
        print(f"   Variants: {len(product_data['variants'])}")
        print(f"   Images: {len(product_data['images'])}")
        print(f"   Metafields: {len(product_data.get('metafields', {}))}")
        print(f"   Collections: {len(product_data['collections'])}")
        
        # Validate variant data
        for idx, v in enumerate(product_data['variants']):
            if not v.get('option1') and not v.get('option2'):
                print(f"⚠️ WARNING: Variant {idx+1} (SKU: {v.get('sku', 'N/A')}) has no options!")
            if not v.get('sku'):
                print(f"⚠️ WARNING: Variant {idx+1} has no SKU!")
            if not v.get('price'):
                print(f"⚠️ WARNING: Variant {idx+1} (SKU: {v.get('sku', 'N/A')}) has no price!")
        
        return product_data
    
    def _sync_product_from_group(self, group_id: str, product_data: Dict, variants: List[Dict]):
        """Sync a product group to Shopify"""
        product_title = product_data.get('title', '')
        
        # Search for existing product
        existing_product = None
        if product_title:
            existing_product = self.shopify_client.get_product_by_title(product_title)
        
        if existing_product:
            # Update existing product
            if self.sync_options.get('update_existing', True):
                self.shopify_client.update_product(existing_product['id'], product_data)
                self.stats['updated'] += 1
                # Post-update validation
                try:
                    refreshed = self.shopify_client.get_product_by_title(product_title)
                    if refreshed:
                        print(f"[validate] Updated product {product_title}: variants={len(refreshed.get('variants', []))}, images={len(refreshed.get('images', [])) if isinstance(refreshed.get('images'), list) else 'n/a'}")
                except Exception as e:
                    print(f"[validate] Warning fetching updated product {product_title}: {e}")
                
                # Save to database for rollback
                shopify_variants = existing_product.get('variants', [])
                if shopify_variants:
                    for variant in shopify_variants:
                        variant_id = variant.get('id') if isinstance(variant, dict) else None
                        variant_sku = variant.get('sku', '') if isinstance(variant, dict) else ''
                        if variant_id and variant_sku:
                            save_sync_product(self.sync_id, existing_product['id'], variant_id, variant_sku, 'updated')
        else:
            # Create new product
            if self.sync_options.get('create_new', True):
                print(f"🆕 Creating NEW product: {product_data['title']}")
                print(f"   Variants to create: {len(product_data.get('variants', []))}")
                print(f"   Images to add: {len(product_data.get('images', []))}")
                
                result = self.shopify_client.create_product(product_data)
                
                if result.get('status') == 'exists':
                    # Product already exists, update it
                    print(f"⚠️ Product already exists, updating: {result['id']}")
                    self.shopify_client.update_product(result['id'], product_data)
                    self.stats['updated'] += 1
                else:
                    # New product created
                    print(f"✅ Product created successfully: ID={result.get('id')}, Variants created: {len(result.get('variants', []))}")
                    self.stats['created'] += 1
                    
                    # Save to database for rollback
                    shopify_variants = result.get('variants', [])
                    if shopify_variants:
                        print(f"   Saving {len(shopify_variants)} variants to sync history...")
                        for variant in shopify_variants:
                            variant_id = variant.get('id') if isinstance(variant, dict) else None
                            variant_sku = variant.get('sku', '') if isinstance(variant, dict) else ''
                            if variant_id and variant_sku:
                                save_sync_product(self.sync_id, result['id'], variant_id, variant_sku, 'created')
                    else:
                        print(f"⚠️ WARNING: Product created but no variants returned from Shopify!")
                    
                    # Update group with Shopify product ID
                    self._update_group_shopify_id(group_id, result['id'])
    
    def _update_group_status(self, group_id: str, status: str):
        """Update product group status in database"""
        from database import get_db
        with get_db() as conn:
            cursor = conn.cursor()
            cursor.execute('''
                UPDATE product_groups 
                SET status = ?, synced_at = CURRENT_TIMESTAMP
                WHERE group_id = ?
            ''', (status, group_id))
            conn.commit()
    
    def _update_group_shopify_id(self, group_id: str, shopify_product_id: int):
        """Update product group with Shopify product ID"""
        from database import get_db
        with get_db() as conn:
            cursor = conn.cursor()
            cursor.execute('''
                UPDATE product_groups 
                SET shopify_product_id = ?
                WHERE group_id = ?
            ''', (shopify_product_id, group_id))
            conn.commit()
    
    def _sync_product_group(self, ss_products: List[Dict]):
        """Sync a group of products (same styleID) as one Shopify product with variants"""
        if not ss_products:
            return
        
        # Use first product as base for product info
        base_product = ss_products[0]
        style_id = base_product.get('styleID')
        
        # Build product data first to get the title
        product_data = self._build_shopify_product_data_with_variants(ss_products)
        product_title = product_data.get('title', '')
        
        # CRITICAL FIX: Search by title FIRST (much faster than SKU search)
        # This prevents "variant already exists" errors by finding existing products quickly
        existing_product = None
        if product_title:
            existing_product = self.shopify_client.get_product_by_title(product_title)
        
        # Fallback: If title search fails, try SKU search (but only for first product to avoid rate limiting)
        if not existing_product and ss_products:
            first_sku = ss_products[0].get('sku')
            if first_sku:
                try:
                    existing_product = self.shopify_client.get_product_by_sku(first_sku)
                except Exception as e:
                    print(f"SKU search failed (rate limited?): {e}, continuing with title-based product")
        
        # Remove the duplicate product_data build below since we already built it above
        
        if existing_product:
            # Update existing product with all variants
            if self.sync_options.get('update_existing', True):
                self._add_log('info', f'🔄 Mevcut ürün güncelleniyor: {product_title}', {
                    'product_id': existing_product['id'],
                    'variants_count': len(product_data.get('variants', []))
                })
                self.shopify_client.update_product(existing_product['id'], product_data)
                self.stats['updated'] += 1
                self._add_log('success', f'✅ Ürün güncellendi: {product_title}', {
                    'product_id': existing_product['id'],
                    'shopify_url': f"https://{self.shop_domain}/admin/products/{existing_product['id']}"
                })
                try:
                    refreshed = self.shopify_client.get_product_by_title(product_title)
                    if refreshed:
                        print(f"[validate] Updated product {product_title}: variants={len(refreshed.get('variants', []))}, images={len(refreshed.get('images', [])) if isinstance(refreshed.get('images'), list) else 'n/a'}")
                except Exception as e:
                    print(f"[validate] Warning fetching updated product {product_title}: {e}")
                # Save to database for rollback
                variants = existing_product.get('variants', [])
                if variants:
                    for variant in variants:
                        variant_id = variant.get('id') if isinstance(variant, dict) else None
                        variant_sku = variant.get('sku', '') if isinstance(variant, dict) else ''
                        if variant_id and variant_sku:
                            save_sync_product(self.sync_id, existing_product['id'], variant_id, variant_sku, 'updated')
            else:
                self.stats['skipped'] += len(ss_products)
        else:
            # Create new product with all variants
            if self.sync_options.get('create_new', True):
                # Note: Shopify now supports up to 2048 variants per product (GraphQL API)
                try:
                    result = self.shopify_client.create_product(product_data)
                    
                    # Check if product already exists (create_product might return existing product)
                    if result.get('status') == 'exists':
                        # Product already exists, update it instead
                        print(f"Product already exists, updating instead: {result['id']}")
                        self.shopify_client.update_product(result['id'], product_data)
                        self.stats['updated'] += 1
                        # Save to database for rollback
                        variants = result.get('variants', [])
                        if variants:
                            for variant in variants:
                                variant_id = variant.get('id') if isinstance(variant, dict) else None
                                variant_sku = variant.get('sku', '') if isinstance(variant, dict) else ''
                                if variant_id and variant_sku:
                                    save_sync_product(self.sync_id, result['id'], variant_id, variant_sku, 'updated')
                    else:
                        # New product created
                        self.stats['created'] += 1
                        product_id = result.get('id')
                        product_handle = result.get('handle', '')
                        shopify_url = f"https://{self.shop_domain}/admin/products/{product_id}"
                        product_url = f"https://{self.shop_domain}/products/{product_handle}" if product_handle else shopify_url
                        
                        self._add_log('success', f'✅ Yeni ürün oluşturuldu: {product_title}', {
                            'product_id': product_id,
                            'variants_count': len(result.get('variants', [])),
                            'shopify_url': shopify_url,
                            'product_url': product_url
                        })
                        
                        # Store created product with link
                        self.created_products.append({
                            'title': product_title,
                            'shopify_id': product_id,
                            'shopify_url': shopify_url,
                            'product_url': product_url,
                            'handle': product_handle,
                            'variants_count': len(result.get('variants', []))
                        })
                        
                        try:
                            refreshed = self.shopify_client.get_product_by_title(product_title)
                            if refreshed:
                                print(f"[validate] Created product {product_title}: variants={len(refreshed.get('variants', []))}, images={len(refreshed.get('images', [])) if isinstance(refreshed.get('images'), list) else 'n/a'}")
                        except Exception as e:
                            print(f"[validate] Warning fetching created product {product_title}: {e}")
                
                        # Save to database for rollback
                        # Handle both dict and list formats for variants
                        variants = result.get('variants', [])
                        if isinstance(variants, list):
                            for variant in variants:
                                variant_id = variant.get('id') if isinstance(variant, dict) else getattr(variant, 'id', None)
                                variant_sku = variant.get('sku', '') if isinstance(variant, dict) else getattr(variant, 'sku', '')
                                if variant_id and variant_sku:
                                    save_sync_product(self.sync_id, result['id'], variant_id, variant_sku, 'created')
                
                # Add to collections if needed
                    if self.sync_options.get('sync_collections', True) and product_data.get('collections'):
                        for coll_id in product_data['collections']:
                            self.shopify_client.add_product_to_collection(result['id'], coll_id)
                except Exception as e:
                    error_msg = str(e)
                    # If error is about variant already existing, try to find product by title and update
                    if 'variant' in error_msg.lower() and 'already exists' in error_msg.lower():
                        # Try to find product by title from product_data
                        product_title = product_data.get('title', '')
                        if product_title:
                            try:
                                import requests
                                # Rate limiting: Add delay before search
                                time.sleep(0.5)
                                
                                # Search for product by title
                                search_response = requests.get(
                                    f"{self.shopify_client.base_url}/products.json",
                                    headers=self.shopify_client.headers,
                                    params={'title': product_title, 'limit': 10},
                                    timeout=30
                                )
                                if search_response.status_code == 200:
                                    search_products = search_response.json().get('products', [])
                                    for search_product in search_products:
                                        if search_product.get('title', '').strip().lower() == product_title.strip().lower():
                                            # Found existing product, update it
                                            print(f"Found existing product by title after error, updating: {search_product['id']}")
                                            self.shopify_client.update_product(search_product['id'], product_data)
                                            self.stats['updated'] += 1
                                            # Save to database
                                            variants = search_product.get('variants', [])
                                            if variants:
                                                for variant in variants:
                                                    variant_id = variant.get('id')
                                                    variant_sku = variant.get('sku', '')
                                                    if variant_id and variant_sku:
                                                        save_sync_product(self.sync_id, search_product['id'], variant_id, variant_sku, 'updated')
                                            return  # Success, exit
                            except Exception as search_error:
                                print(f"Error searching for product by title: {search_error}")
                    
                    # If we get here, the error couldn't be resolved
                    raise
            else:
                self.stats['skipped'] += len(ss_products)
    
    def _sync_product(self, ss_product: Dict):
        """Sync a single product from S&S to Shopify (legacy method, kept for compatibility)"""
        self._sync_product_group([ss_product])
    
    def _build_shopify_product_data_with_variants(self, ss_products: List[Dict]) -> Dict:
        """Build Shopify product data with multiple variants from S&S products"""
        if not ss_products:
            return {}
        
        # Use first product as base
        base_product = ss_products[0]
        
        # Build title (without color/size - that goes in variants)
        title_parts = []
        if base_product.get('brandName'):
            title_parts.append(base_product['brandName'])
        if base_product.get('styleName'):
            title_parts.append(base_product['styleName'])
        
        title = ' '.join(title_parts) if title_parts else base_product.get('sku', 'Product')
        
        # Build description from first product
        description = base_product.get('description', '')
        if not description and base_product.get('styleID'):
            styles = self.ss_client.get_styles(styleid=str(base_product['styleID']))
            if styles and styles[0].get('description'):
                description = styles[0]['description']
        
        # Build images from all products (unique images)
        images = []
        if self.sync_options.get('update_images', True):
            base_url = "https://www.ssactivewear.com/"
            image_size = self.sync_options.get('image_size', '_fl')
            seen_images = set()
            
            for ss_product in ss_products:
                # Primary front image
                if ss_product.get('colorFrontImage'):
                    img_url = base_url + ss_product['colorFrontImage'].replace('_fm', image_size)
                    if img_url not in seen_images:
                        images.append(img_url)
                        seen_images.add(img_url)
                elif ss_product.get('styleImage'):
                    styles = self.ss_client.get_styles(styleid=str(ss_product.get('styleID', '')))
                    if styles and styles[0].get('styleImage'):
                        img_url = base_url + styles[0]['styleImage'].replace('_fm', image_size)
                        if img_url not in seen_images:
                            images.append(img_url)
                            seen_images.add(img_url)
                
                # Additional images
                for img_field in ['colorSideImage', 'colorBackImage', 'colorDirectSideImage', 
                                 'colorOnModelFrontImage', 'colorOnModelSideImage', 'colorOnModelBackImage', 
                                 'colorSwatchImage']:
                    if ss_product.get(img_field):
                        img_url = base_url + ss_product[img_field].replace('_fm', image_size)
                        if img_url not in seen_images:
                            images.append(img_url)
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
            if base_product.get('sustainableStyle'):
                tags.append('Sustainable')
        
        # Build collections (same as before)
        collections = []
        if self.sync_options.get('sync_collections', True):
            create_if_not_exists = self.sync_options.get('create_collections', True)
            
            # Get category collections from first product
            if base_product.get('categories'):
                category_ids = base_product['categories'].split(',')
                for cat_id in category_ids:
                    cat_id = cat_id.strip()
                    if cat_id:
                        try:
                            categories = self.ss_client.get_categories(category_ids=cat_id)
                            if categories:
                                if create_if_not_exists:
                                    coll = self.shopify_client.find_or_create_collection(
                                        categories[0]['name'],
                                        handle=categories[0]['name'].lower().replace(' ', '-').replace('&', 'and')
                                    )
                                    collections.append(coll['id'])
                                else:
                                    existing_collections = self.shopify_client.get_collections()
                                    for existing in existing_collections:
                                        if existing['title'].lower() == categories[0]['name'].lower():
                                            collections.append(existing['id'])
                                            break
                        except Exception:
                            pass
            
            # Brand collection
            if base_product.get('brandName') and self.sync_options.get('create_brand_collections', True):
                try:
                    if create_if_not_exists:
                        coll = self.shopify_client.find_or_create_collection(
                            base_product['brandName'],
                            handle=base_product['brandName'].lower().replace(' ', '-').replace('&', 'and')
                        )
                        collections.append(coll['id'])
                    else:
                        existing_collections = self.shopify_client.get_collections()
                        for existing in existing_collections:
                            if existing['title'].lower() == base_product['brandName'].lower():
                                collections.append(existing['id'])
                                break
                except Exception:
                    pass
            
            # Base category collection
            if base_product.get('baseCategory'):
                try:
                    if create_if_not_exists:
                        coll = self.shopify_client.find_or_create_collection(
                            base_product['baseCategory'],
                            handle=base_product['baseCategory'].lower().replace(' ', '-').replace('&', 'and')
                        )
                        collections.append(coll['id'])
                    else:
                        existing_collections = self.shopify_client.get_collections()
                        for existing in existing_collections:
                            if existing['title'].lower() == base_product['baseCategory'].lower():
                                collections.append(existing['id'])
                                break
                except Exception:
                    pass
        
        # Build variants from all products with images
        price_field = self.sync_options.get('price_field', 'customerPrice')
        variants = []
        base_url = "https://www.ssactivewear.com/"
        image_size = self.sync_options.get('image_size', '_fl')
        
        # Track unique variant combinations to avoid duplicates
        seen_variants = set()
        seen_option_combinations = set()  # Track option combinations separately (Shopify doesn't allow duplicates)
        
        for ss_product in ss_products:
            price = ss_product.get(price_field)
            if not price or price == 0:
                price = ss_product.get('customerPrice', ss_product.get('piecePrice', '0'))
            
            # Get variant-specific image (color front image)
            variant_image = None
            if ss_product.get('colorFrontImage'):
                variant_image = base_url + ss_product['colorFrontImage'].replace('_fm', image_size)
            
            # Get color and size - ensure they are not empty
            color_name = ss_product.get('colorName', '').strip()
            size_name = ss_product.get('sizeName', '').strip()
            sku = ss_product.get('sku', '')
            
            # CRITICAL FIX: If size is missing or empty, we MUST use SKU to ensure uniqueness
            # Otherwise, all variants with same color but different sizes will be seen as duplicates
            if not size_name or size_name == '' or size_name.lower() == 'default':
                # Use SKU to make it unique - this ensures each variant is different
                size_name = f"Size-{sku}" if sku else f"Size-{len(variants)}"
                print(f"WARNING: Missing size for SKU {sku}, using fallback: {size_name}")
            
            # If color is missing, use SKU as fallback to ensure uniqueness
            if not color_name or color_name == '' or color_name.lower() == 'default':
                color_name = f"Color-{sku}" if sku else f"Color-{len(variants)}"
                print(f"WARNING: Missing color for SKU {sku}, using fallback: {color_name}")
            
            # CRITICAL: Shopify doesn't allow duplicate option combinations (option1 + option2)
            # Check if this option combination already exists BEFORE adding variant
            option_key = (color_name, size_name)
            if option_key in seen_option_combinations:
                # Make it unique by appending SKU to size
                if sku and not size_name.endswith(sku):
                    size_name = f"{size_name}-{sku[:6]}"  # Append first 6 chars of SKU
                    print(f"Warning: Duplicate option combination detected. Modified size to: {size_name} for SKU: {sku}")
                    # Update option_key with new size_name
                    option_key = (color_name, size_name)
                else:
                    # If already modified or no SKU, skip this variant
                    print(f"Skipping duplicate variant - Color: {color_name}, Size: {size_name}, SKU: {sku}")
                    continue
            
            seen_option_combinations.add(option_key)
            
            # Create unique key for variant (color + size + SKU combination)
            variant_key = (color_name, size_name, sku)
            
            # Skip if this exact variant combination already exists
            if variant_key in seen_variants:
                print(f"Warning: Duplicate variant skipped - Color: {color_name}, Size: {size_name}, SKU: {sku}")
                continue
            
            seen_variants.add(variant_key)
            
            variant = {
                'sku': ss_product.get('sku', ''),
                'price': str(price),
                'inventory_quantity': ss_product.get('qty', 0) if self.sync_options.get('update_inventory', True) else None,
                'option1': color_name,  # Color as option1
                'option2': size_name,    # Size as option2
                'barcode': ss_product.get('gtin', '') or None,
                'weight': ss_product.get('unitWeight', 0) or 0,
                'weight_unit': 'lb'
            }
            
            # Add variant image if available
            if variant_image:
                variant['image'] = variant_image
            
            # Add variant-specific metafields
            variant_metafields = {}
            variant_metafield_fields = [
                'colorName', 'colorCode', 'colorPriceCodeName', 'colorGroup', 'colorGroupName',
                'colorFamilyID', 'colorFamily', 'sizeName', 'sizeCode', 'sizeOrder', 
                'sizePriceCodeName', 'qty', 'gtin', 'yourSku'
            ]
            for field in variant_metafield_fields:
                if ss_product.get(field) is not None:
                    variant_metafields[field] = ss_product[field]
            
            if variant_metafields:
                variant['metafields'] = variant_metafields
            
            # Set inventory management
            inventory_management = self.sync_options.get('inventory_management', 'shopify')
            if inventory_management == 'not_managed':
                variant['inventory_management'] = None
                variant['inventory_policy'] = 'continue'
            
            variants.append(variant)
        
        # Build metafields from S&S API data (CRITICAL: Store all product information)
        metafields = {}
        if base_product:
            # Store all S&S API fields as metafields
            metafield_fields = [
                'styleID', 'partNumber', 'brandName', 'styleName', 'title',
                'baseCategory', 'catalogPageNumber', 'newStyle', 'comparableGroup',
                'companionGroup', 'sustainableStyle', 'colorCode', 'colorPriceCodeName',
                'colorGroup', 'colorGroupName', 'colorFamilyID', 'colorFamily',
                'sizeCode', 'sizeOrder', 'sizePriceCodeName', 'caseQty', 'unitWeight',
                'mapPrice', 'piecePrice', 'dozenPrice', 'casePrice', 'salePrice',
                'customerPrice', 'saleExpiration', 'noeRetailing', 'caseWeight',
                'caseWidth', 'caseLength', 'caseHeight', 'PolyPackQty', 'countryOfOrigin'
            ]
            
            for field in metafield_fields:
                if base_product.get(field) is not None:
                    metafields[field] = base_product[field]
            
            # Store categories as comma-separated string
            if base_product.get('categories'):
                metafields['categories'] = base_product['categories']
        
        # CRITICAL VALIDATION: Must have at least 1 variant
        if not variants or len(variants) == 0:
            raise Exception(f"CRITICAL ERROR: Product {title} has NO variants! Cannot create product without variants. Check product data: {len(ss_products)} S&S products processed.")
        
        # CRITICAL VALIDATION: Check variant data structure
        for idx, v in enumerate(variants):
            if not v.get('option1') and not v.get('option2'):
                print(f"WARNING: Variant {idx+1} (SKU: {v.get('sku', 'N/A')}) has no options!")
            if not v.get('sku'):
                print(f"WARNING: Variant {idx+1} has no SKU!")
            if not v.get('price'):
                print(f"WARNING: Variant {idx+1} (SKU: {v.get('sku', 'N/A')}) has no price!")
        
        # Build product data
        # Note: Shopify requires 'options' to match variant option names
        # We'll let Shopify auto-detect from variant option1/option2
        product_data = {
            'title': title,
            'description': description or '',  # Ensure description is not None
            'vendor': base_product.get('brandName', ''),
            'product_type': base_product.get('baseCategory', ''),
            'tags': ', '.join(tags) if tags else '',
            'status': 'active' if self.sync_options.get('set_active', True) else 'draft',
            'images': images if images else [],  # Ensure images is a list
            'variants': variants,
            'collections': collections,
            'metafields': metafields  # Add metafields
            # Don't specify 'options' - Shopify will auto-detect from variants
        }
        
        # Detailed logging
        variant_images_count = sum(1 for v in variants if v.get('image'))
        variant_metafields_count = sum(1 for v in variants if v.get('metafields'))
        
        print(f"✅ Built product data: {title}")
        print(f"   - Variants: {len(variants)} (with images: {variant_images_count}, with metafields: {variant_metafields_count})")
        print(f"   - Product images: {len(images)}")
        print(f"   - Product metafields: {len(metafields)}")
        print(f"   - Collections: {len(collections)}")
        
        return product_data
    
    def _build_shopify_product_data(self, ss_product: Dict) -> Dict:
        """Convert S&S product data to Shopify format"""
        # Build title
        title_parts = []
        if ss_product.get('brandName'):
            title_parts.append(ss_product['brandName'])
        if ss_product.get('styleName'):
            title_parts.append(ss_product['styleName'])
        if ss_product.get('colorName'):
            title_parts.append(ss_product['colorName'])
        
        title = ' '.join(title_parts) if title_parts else ss_product.get('sku', 'Product')
        
        # Build description
        description = ss_product.get('description', '')
        if not description and ss_product.get('styleID'):
            # Try to get style description
            styles = self.ss_client.get_styles(styleid=str(ss_product['styleID']))
            if styles and styles[0].get('description'):
                description = styles[0]['description']
        
        # Build images - FIXED: Include ALL available images
        images = []
        if self.sync_options.get('update_images', True):
            base_url = "https://www.ssactivewear.com/"
            image_size = self.sync_options.get('image_size', '_fl')
            
            # Primary front image (highest priority)
            if ss_product.get('colorFrontImage'):
                images.append(base_url + ss_product['colorFrontImage'].replace('_fm', image_size))
            elif ss_product.get('styleImage'):
                styles = self.ss_client.get_styles(styleid=str(ss_product.get('styleID', '')))
                if styles and styles[0].get('styleImage'):
                    images.append(base_url + styles[0]['styleImage'].replace('_fm', image_size))
            
            # Additional product images
            if ss_product.get('colorSideImage'):
                images.append(base_url + ss_product['colorSideImage'].replace('_fm', image_size))
            if ss_product.get('colorBackImage'):
                images.append(base_url + ss_product['colorBackImage'].replace('_fm', image_size))
            if ss_product.get('colorDirectSideImage'):
                images.append(base_url + ss_product['colorDirectSideImage'].replace('_fm', image_size))
            
            # On-model images (if available)
            if ss_product.get('colorOnModelFrontImage'):
                images.append(base_url + ss_product['colorOnModelFrontImage'].replace('_fm', image_size))
            if ss_product.get('colorOnModelSideImage'):
                images.append(base_url + ss_product['colorOnModelSideImage'].replace('_fm', image_size))
            if ss_product.get('colorOnModelBackImage'):
                images.append(base_url + ss_product['colorOnModelBackImage'].replace('_fm', image_size))
            
            # Color swatch (small but useful)
            if ss_product.get('colorSwatchImage'):
                images.append(base_url + ss_product['colorSwatchImage'].replace('_fm', image_size))
        
        # Build tags
        tags = []
        if self.sync_options.get('sync_tags', True):
            if ss_product.get('brandName'):
                tags.append(ss_product['brandName'])
            if ss_product.get('colorName'):
                tags.append(ss_product['colorName'])
            if ss_product.get('colorFamily'):
                tags.append(ss_product['colorFamily'])
            if ss_product.get('baseCategory'):
                tags.append(ss_product['baseCategory'])
            if ss_product.get('sustainableStyle'):
                tags.append('Sustainable')
        
        # Build collections
        collections = []
        if self.sync_options.get('sync_collections', True):
            create_if_not_exists = self.sync_options.get('create_collections', True)
            
            # Get category collections
            if ss_product.get('categories'):
                category_ids = ss_product['categories'].split(',')
                for cat_id in category_ids:
                    cat_id = cat_id.strip()
                    if cat_id:
                        try:
                            categories = self.ss_client.get_categories(category_ids=cat_id)
                            if categories:
                                if create_if_not_exists:
                                    coll = self.shopify_client.find_or_create_collection(
                                        categories[0]['name'],
                                        handle=categories[0]['name'].lower().replace(' ', '-').replace('&', 'and')
                                    )
                                    collections.append(coll['id'])
                                else:
                                    # Only use existing collections
                                    existing_collections = self.shopify_client.get_collections()
                                    for existing in existing_collections:
                                        if existing['title'].lower() == categories[0]['name'].lower():
                                            collections.append(existing['id'])
                                            break
                        except Exception:
                            pass  # Skip if category not found
            
            # Brand collection
            if ss_product.get('brandName') and self.sync_options.get('create_brand_collections', True):
                try:
                    if create_if_not_exists:
                        coll = self.shopify_client.find_or_create_collection(
                            ss_product['brandName'],
                            handle=ss_product['brandName'].lower().replace(' ', '-').replace('&', 'and')
                        )
                        collections.append(coll['id'])
                    else:
                        existing_collections = self.shopify_client.get_collections()
                        for existing in existing_collections:
                            if existing['title'].lower() == ss_product['brandName'].lower():
                                collections.append(existing['id'])
                                break
                except Exception:
                    pass
            
            # Base category collection
            if ss_product.get('baseCategory'):
                try:
                    if create_if_not_exists:
                        coll = self.shopify_client.find_or_create_collection(
                            ss_product['baseCategory'],
                            handle=ss_product['baseCategory'].lower().replace(' ', '-').replace('&', 'and')
                        )
                        collections.append(coll['id'])
                    else:
                        existing_collections = self.shopify_client.get_collections()
                        for existing in existing_collections:
                            if existing['title'].lower() == ss_product['baseCategory'].lower():
                                collections.append(existing['id'])
                                break
                except Exception:
                    pass
        
        # Get price field from options
        price_field = self.sync_options.get('price_field', 'customerPrice')
        price = ss_product.get(price_field)
        if not price or price == 0:
            # Fallback to customerPrice or piecePrice
            price = ss_product.get('customerPrice', ss_product.get('piecePrice', '0'))
        
        # Build variant
        variant = {
            'sku': ss_product.get('sku', ''),
            'price': str(price),
            'inventory_quantity': ss_product.get('qty', 0) if self.sync_options.get('update_inventory', True) else None,
            'option1': ss_product.get('sizeName', 'Default'),
            'barcode': ss_product.get('gtin', ''),
            'weight': ss_product.get('unitWeight', 0),
            'weight_unit': 'lb'
        }
        
        # Set inventory management
        inventory_management = self.sync_options.get('inventory_management', 'shopify')
        if inventory_management == 'not_managed':
            variant['inventory_management'] = None
            variant['inventory_policy'] = 'continue'
        
        # Build product data
        product_data = {
            'title': title,
            'description': description,
            'vendor': ss_product.get('brandName', ''),
            'product_type': ss_product.get('baseCategory', ''),
            'tags': ', '.join(tags) if tags else '',
            'status': 'active' if self.sync_options.get('set_active', True) else 'draft',
            'images': images,
            'variants': [variant],
            'collections': collections
        }
        
        return product_data

