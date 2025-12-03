from flask import Flask, render_template, request, jsonify, session, redirect, url_for, Response
import os
from dotenv import load_dotenv
from ss_api_client import SSActivewearClient
from shopify_client import ShopifyClient
from sync_manager import SyncManager
from scheduler import scheduler, warehouse_scheduler
from database import (init_database, save_config, get_config, get_all_config, save_sync_history, 
                      get_last_sync_id, get_sync_products, init_product_search_cache, 
                      get_search_cache_count, populate_search_cache, search_products_fts,
                      get_search_cache_last_update, clear_search_cache)
import threading
import json
import requests
from datetime import datetime, timedelta

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY', 'your-secret-key-change-this')

# CORS middleware - allow all origins for warehouse stock API
@app.after_request
def add_cors_headers(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'GET, POST, OPTIONS'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type'
    
    # Track request for system monitor (skip static files and monitor itself)
    if not request.path.startswith('/static') and not request.path.startswith('/api/system-monitor'):
        try:
            track_incoming_request(request.method, request.path, response.status_code)
        except:
            pass
    
    return response

# Forward declarations - actual implementations are at the bottom of this file
# These will be overwritten by the real implementations

_monitor_initialized = False

def track_incoming_request(method, path, status):
    global _monitor_initialized
    if not _monitor_initialized:
        return
    try:
        _track_incoming_request_impl(method, path, status)
    except:
        pass

def track_outgoing_request(target, endpoint, method, success):
    global _monitor_initialized
    if not _monitor_initialized:
        return
    try:
        _track_outgoing_request_impl(target, endpoint, method, success)
    except:
        pass

def add_system_log(log_type, message, terminal='main'):
    global _monitor_initialized
    if not _monitor_initialized:
        return
    try:
        _add_system_log_impl(log_type, message, terminal)
    except:
        pass

# Initialize database on startup
try:
    init_database()
    init_product_search_cache()
    print("Database initialized successfully")
except Exception as e:
    print(f"Database initialization error: {e}")

# Initialize Cache Manager with warming
try:
    from cache_manager import cache_manager, warm_cache
    # Warm cache with top 2000 SKUs from SQLite
    warmed_count = warm_cache(limit=2000)
    print(f"✅ Cache warmed with {warmed_count} items")
except Exception as e:
    print(f"Cache warming error: {e}")

# Cache performance stats helper
def get_cache_performance_stats():
    """Get cache performance stats for system monitor"""
    try:
        from cache_manager import cache_manager
        stats = cache_manager.get_stats()
        return {
            'hit_rate': stats.get('total_cache_hit_rate', 0),
            'memory_hits': stats.get('memory_hits', 0),
            'sqlite_hits': stats.get('sqlite_hits', 0),
            'api_calls': stats.get('api_calls', 0),
            'avg_response_ms': stats.get('avg_response_ms', 0),
            'total_queries': stats.get('total_queries', 0)
        }
    except Exception:
        return {
            'hit_rate': 0,
            'memory_hits': 0,
            'sqlite_hits': 0,
            'api_calls': 0,
            'avg_response_ms': 0,
            'total_queries': 0
        }

# Initialize system monitor logs on startup - will be called after everything is loaded

# Global sync manager instance
sync_manager = None

@app.route('/')
def index():
    return redirect(url_for('page_dashboard'))


# ==================== PAGE ROUTES ====================

@app.route('/dashboard')
def page_dashboard():
    return render_template('pages/dashboard.html', active_page='dashboard')


@app.route('/settings')
def page_settings():
    return render_template('pages/settings.html', active_page='settings')


@app.route('/sync-options')
def page_sync_options():
    return render_template('pages/sync_options.html', active_page='sync-options')


@app.route('/sync-settings')
def page_sync_settings():
    return render_template('pages/sync_settings.html', active_page='sync-settings')


@app.route('/sync')
def page_sync():
    return render_template('pages/sync.html', active_page='sync')


@app.route('/auto-sync')
def page_auto_sync():
    return render_template('pages/auto_sync.html', active_page='auto-sync')


@app.route('/product-search')
def page_product_search():
    return render_template('pages/product_search.html', active_page='product-search')

@app.route('/documentation')
def page_documentation():
    return render_template('pages/documentation.html', active_page='documentation')

@app.route('/system-monitor')
def page_system_monitor():
    return render_template('pages/system_monitor.html', active_page='system-monitor')

@app.route('/api/config', methods=['GET', 'POST'])
def config():
    """Save or retrieve configuration from database"""
    try:
        if request.method == 'POST':
            config_data = request.get_json(silent=True)
            if not config_data:
                return jsonify({'status': 'error', 'message': 'No data provided'}), 400
            
            # Get existing config to preserve values not being updated
            existing_ss = get_config('ss_config') or {}
            existing_shopify = get_config('shopify_config') or {}
            existing_sync = get_config('sync_options') or {}
            
            # Only update ss_config if credentials are provided
            if config_data.get('ss_account_number') or config_data.get('ss_api_key'):
                ss_config = {
                    'account_number': config_data.get('ss_account_number', existing_ss.get('account_number', '')).strip(),
                    'api_key': config_data.get('ss_api_key', existing_ss.get('api_key', '')).strip()
                }
                save_config('ss_config', ss_config)
                session['ss_config'] = ss_config
            
            # Only update shopify_config if credentials are provided
            if config_data.get('shopify_domain') or config_data.get('shopify_token'):
                shopify_config = {
                    'shop_domain': config_data.get('shopify_domain', existing_shopify.get('shop_domain', '')).strip(),
                    'access_token': config_data.get('shopify_token', existing_shopify.get('access_token', '')).strip()
                }
                save_config('shopify_config', shopify_config)
                session['shopify_config'] = shopify_config
            
            # Always update sync_options if provided
            if 'sync_options' in config_data:
                sync_options = config_data.get('sync_options', {})
                save_config('sync_options', sync_options)
                session['sync_options'] = sync_options
            
            session.permanent = True
            
            return jsonify({
                'status': 'success', 
                'message': 'Configuration saved successfully to database'
            })
        else:
            # Get from database, fallback to session
            ss_config = get_config('ss_config', session.get('ss_config', {}))
            shopify_config = get_config('shopify_config', session.get('shopify_config', {}))
            sync_options = get_config('sync_options', session.get('sync_options', {}))
            
            return jsonify({
                'ss_config': ss_config,
                'shopify_config': shopify_config,
                'sync_options': sync_options
            })
    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': f'Error saving configuration: {str(e)}'
        }), 500

@app.route('/api/test-connection', methods=['POST'])
def test_connection():
    """Test API connections - uses database credentials if not provided in request"""
    data = request.get_json(silent=True) or {}
    results = {'ss': False, 'shopify': False, 'messages': []}
    
    # Get S&S credentials - from request OR database
    ss_config = get_config('ss_config') or {}
    account_number = (data.get('ss_account_number', '').strip() or 
                      ss_config.get('account_number', '').strip())
    api_key = (data.get('ss_api_key', '').strip() or 
               ss_config.get('api_key', '').strip())
    
    # Test S&S Activewear
    try:
        if not account_number or not api_key:
            results['messages'].append('S&S Activewear API: Credentials not configured')
        else:
            ss_client = SSActivewearClient(account_number, api_key)
            categories = ss_client.get_categories(limit=1)
            results['ss'] = True
            results['messages'].append('S&S Activewear API: Connected successfully')
    except ValueError as e:
        results['messages'].append(f'S&S Activewear API: {str(e)}')
    except Exception as e:
        error_msg = str(e)
        if '403' in error_msg or 'Forbidden' in error_msg:
            results['messages'].append(
                f'S&S Activewear API: Authentication failed (403 Forbidden). '
                f'Please verify credentials are correct.'
            )
        else:
            results['messages'].append(f'S&S Activewear API: {error_msg}')
    
    # Get Shopify credentials - from request OR database
    shopify_config = get_config('shopify_config') or {}
    shopify_domain = (data.get('shopify_domain', '').strip() or 
                      shopify_config.get('shop_domain', '').strip())
    shopify_token = (data.get('shopify_token', '').strip() or 
                     shopify_config.get('access_token', '').strip())
    
    # Test Shopify
    try:
        if not shopify_domain or not shopify_token:
            results['messages'].append('Shopify API: Credentials not configured')
        else:
            shopify_client = ShopifyClient(shopify_domain, shopify_token)
            shop_info = shopify_client.get_shop_info()
            results['shopify'] = True
            results['messages'].append(f'Shopify: Connected to {shop_info.get("name", "store")}')
    except Exception as e:
        results['messages'].append(f'Shopify API: {str(e)}')
    
    return jsonify(results)

@app.route('/api/sync/start', methods=['POST'])
def start_sync():
    """Start synchronization process"""
    global sync_manager
    
    config_data = request.get_json(silent=True) or {}
    
    # Get sync_options from request, fallback to database, then session
    sync_options = config_data.get('sync_options', {})
    if not sync_options:
        sync_options = get_config('sync_options', {})
    if not sync_options:
        sync_options = session.get('sync_options', {})
    
    # Get credentials from request, fallback to database, then session
    account_number = (config_data.get('ss_account_number', '').strip() or 
                     get_config('ss_config', {}).get('account_number', '') or
                     session.get('ss_config', {}).get('account_number', '')).strip()
    api_key = (config_data.get('ss_api_key', '').strip() or 
              get_config('ss_config', {}).get('api_key', '') or
              session.get('ss_config', {}).get('api_key', '')).strip()
    shopify_domain = (config_data.get('shopify_domain', '').strip() or 
                     get_config('shopify_config', {}).get('shop_domain', '') or
                     session.get('shopify_config', {}).get('shop_domain', '')).strip()
    shopify_token = (config_data.get('shopify_token', '').strip() or 
                    get_config('shopify_config', {}).get('access_token', '') or
                    session.get('shopify_config', {}).get('access_token', '')).strip()
    
    try:
        if not account_number or not api_key:
            return jsonify({
                'status': 'error',
                'message': 'S&S Activewear Account Number and API Key are required'
            }), 400
        
        if not shopify_domain or not shopify_token:
            return jsonify({
                'status': 'error',
                'message': 'Shopify Domain and Access Token are required'
            }), 400
        
        ss_client = SSActivewearClient(account_number, api_key)
        shopify_client = ShopifyClient(shopify_domain, shopify_token)
        
        # Debug: Log sync options
        print(f"Sync options: {sync_options}")
        print(f"Filter categories: {sync_options.get('filter_categories')}")
        print(f"Filter styles: {sync_options.get('filter_styles')}")
        print(f"Filter brands: {sync_options.get('filter_brands')}")
        print(f"Filter warehouses: {sync_options.get('filter_warehouses')}")
        
        # CRITICAL: Warn if no warehouse filter (will cause duplicate variants!)
        warehouse_filter = sync_options.get('filter_warehouses', [])
        if not warehouse_filter:
            print("⚠️ WARNING: No warehouse filter selected! This may cause duplicate variant errors!")
            print("⚠️ Recommendation: Select a specific warehouse/location before syncing")
        
        sync_manager = SyncManager(ss_client, shopify_client, sync_options)
        
        # Start sync in background thread
        thread = threading.Thread(target=sync_manager.start_sync)
        thread.daemon = True
        thread.start()
        
        return jsonify({
            'status': 'success',
            'message': 'Synchronization started',
            'sync_id': sync_manager.sync_id
        })
    except Exception as e:
        import traceback
        error_detail = traceback.format_exc()
        print(f"Sync start error: {error_detail}")
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 400

@app.route('/api/sync/status', methods=['GET'])
def sync_status():
    """Get synchronization status with all details for UI"""
    global sync_manager
    
    if sync_manager is None:
        # Return last sync info from database if available
        return jsonify({
            'status': 'success',
            'is_running': False,
            'progress': 0,
            'message': 'No sync in progress',
            'stats': {'total': 0, 'created': 0, 'updated': 0, 'errors': 0},
            'errors': [],
            'logs': [],
            'created_products': [],
            'current_product': None,
            'step': None,
            'last_sync': None
        })
    
    # Determine if sync is actually running
    is_running = sync_manager.status == 'running'
    
    # Get current product info
    current_product_info = None
    if sync_manager.current_product:
        current_product_info = {
            'sku': sync_manager.current_product.get('sku', 'N/A'),
            'title': f"{sync_manager.current_product.get('brandName', '')} {sync_manager.current_product.get('styleName', '')} {sync_manager.current_product.get('colorName', '')}".strip(),
            'styleName': sync_manager.current_product.get('styleName', ''),
            'index': sync_manager.current_index,
            'total': sync_manager.stats.get('total', 0)
        }
    
    # Format logs for frontend
    formatted_logs = []
    logs = getattr(sync_manager, 'logs', [])
    for log in logs[-100:]:  # Last 100 logs
        if isinstance(log, dict):
            formatted_logs.append(f"[{log.get('timestamp', '')}] {log.get('message', '')}")
        else:
            formatted_logs.append(str(log))
    
    # Last sync stats for completed syncs
    last_sync = None
    if sync_manager.status in ('completed', 'error'):
        last_sync = {
            'total': sync_manager.stats.get('total', 0),
            'created': sync_manager.stats.get('created', 0),
            'updated': sync_manager.stats.get('updated', 0),
            'errors': sync_manager.stats.get('errors', 0),
            'timestamp': datetime.now().isoformat()
        }
    
    return jsonify({
        'status': 'success',
        'is_running': is_running,
        'sync_status': sync_manager.status,
        'progress': sync_manager.progress,
        'message': sync_manager.message,
        'stats': sync_manager.stats,
        'errors': sync_manager.errors[-10:],  # Last 10 errors
        'current_product': current_product_info,
        'current_index': sync_manager.current_index,
        'total': sync_manager.stats.get('total', 0),
        'step': getattr(sync_manager, 'step', None),
        'step_progress': getattr(sync_manager, 'step_progress', None),
        'logs': formatted_logs,  # Formatted string logs
        'created_products': getattr(sync_manager, 'created_products', []),
        'last_sync': last_sync
    })

@app.route('/api/sync/stop', methods=['POST'])
def stop_sync():
    """Stop synchronization"""
    global sync_manager
    
    if sync_manager:
        sync_manager.stop()
        return jsonify({'status': 'success', 'message': 'Sync stopped'})
    
    return jsonify({'status': 'error', 'message': 'No sync in progress'})

@app.route('/api/sync/clear-snapshots', methods=['POST'])
def clear_snapshots():
    """Clear all style snapshots to force resync"""
    try:
        from database import get_db
        with get_db() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT COUNT(*) FROM style_snapshots")
            count = cursor.fetchone()[0]
            cursor.execute("DELETE FROM style_snapshots")
            conn.commit()
        
        return jsonify({
            'status': 'success',
            'message': f'{count} snapshot(s) cleared',
            'cleared': count
        })
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500

@app.route('/api/products/count', methods=['POST'])
def products_count():
    """Get count of products based on filters - NO Shopify needed"""
    try:
        data = request.get_json(silent=True) or {}
        
        # Get credentials from database
        ss_config = get_config('ss_config') or session.get('ss_config', {})
        account_number = ss_config.get('account_number', '')
        api_key = ss_config.get('api_key', '')
        
        if not account_number or not api_key:
            return jsonify({
                'status': 'error',
                'message': 'S&S API credentials not configured'
            }), 400
        
        ss_client = SSActivewearClient(account_number, api_key)
        
        sync_options = data.get('sync_options', {})
        
        # Get filter parameters
        style_ids = sync_options.get('filter_styles', [])
        category_ids = sync_options.get('filter_categories', [])
        brand_ids = sync_options.get('filter_brands', [])
        warehouse_codes = sync_options.get('filter_warehouses', [])
        
        # Build style ID parameter for API
        style_param = None
        if style_ids:
            if isinstance(style_ids, list) and style_ids:
                style_param = ','.join(str(s) for s in style_ids if s)
            elif style_ids:
                style_param = str(style_ids)
        
        # Fetch products from S&S API (DO NOT pass warehouse - causes 404 errors!)
        products = []
        try:
            if style_param:
                # Batch style IDs to avoid URL too long
                all_style_ids = [str(s) for s in style_ids if s]
                for i in range(0, len(all_style_ids), 50):
                    batch = all_style_ids[i:i+50]
                    batch_param = ','.join(batch)
                    batch_products = ss_client.get_products(styleid=batch_param, limit=5000)
                    if batch_products:
                        products.extend(batch_products)
            else:
                products = ss_client.get_products(limit=5000) or []
        except Exception as api_err:
            print(f"API Error in products_count: {api_err}")
            products = []
        
        # Filter by warehouse in Python (check if product has stock in selected warehouse)
        if warehouse_codes and products:
            warehouse_set = set(warehouse_codes)
            filtered = []
            for p in products:
                product_warehouses = [wh.get('warehouseAbbr') for wh in p.get('warehouses', [])]
                if any(wh in warehouse_set for wh in product_warehouses):
                    filtered.append(p)
            products = filtered
        
        # Filter by categories if specified (skip if styles already selected)
        if category_ids and products and not style_ids:
            cat_list = [str(c).strip() for c in category_ids if c]
            filtered = []
            for p in products:
                p_cats = str(p.get('categories', '')).split(',')
                p_cats = [c.strip() for c in p_cats if c.strip()]
                if any(cat in p_cats for cat in cat_list):
                    filtered.append(p)
            products = filtered
        
        # Filter by brands (can be IDs or names)
        if brand_ids and products:
            brand_list = [str(b).strip() for b in brand_ids if b]
            if brand_list:
                # Check if these are IDs (numeric) or names
                if brand_list[0].isdigit():
                    # Brand IDs - compare as strings (S&S returns brandID as string)
                    brand_id_set = set(brand_list)
                    products = [p for p in products if str(p.get('brandID') or '') in brand_id_set]
                else:
                    # Brand names
                    products = [p for p in products if p.get('brandName', '').strip() in brand_list]
        
        # Count unique styles
        unique_styles = set(p.get('styleID') for p in products if p.get('styleID'))
        
        return jsonify({
            'status': 'success',
            'count': len(products),
            'style_count': len(unique_styles)
        })
    except Exception as e:
        import traceback
        traceback.print_exc()
        response = jsonify({
            'status': 'error',
            'message': str(e),
            'count': 0
        })
        response.headers['Content-Length'] = str(len(response.get_data()))
        return response, 400

@app.route('/api/preview', methods=['POST'])
def preview():
    """Preview products before sync - uses same filtering logic as sync"""
    try:
        data = request.get_json(silent=True) or {}
        
        # Get credentials from database
        ss_config = get_config('ss_config') or {}
        account_number = ss_config.get('account_number', '').strip()
        api_key = ss_config.get('api_key', '').strip()
        
        if not account_number or not api_key:
            return jsonify({
                'status': 'error',
                'message': 'S&S API credentials not configured',
                'products': [],
                'count': 0
            }), 400
        
        ss_client = SSActivewearClient(account_number, api_key)
        
        # Get filter options - can be from filter_options or sync_options
        filter_options = data.get('filter_options', {})
        sync_options = data.get('sync_options', {})
        
        # Use sync_options if available, otherwise use filter_options
        if sync_options:
            category_ids = sync_options.get('filter_categories', [])
            style_ids = sync_options.get('filter_styles', [])
            brand_names = sync_options.get('filter_brands', [])
        else:
            category_ids = filter_options.get('categories', [])
            style_ids = filter_options.get('styles', [])
            brand_names = filter_options.get('brands', [])
        
        # Normalize category IDs
        if isinstance(category_ids, list):
            category_list = [str(cid).strip() for cid in category_ids if cid]
        elif isinstance(category_ids, str):
            category_list = [c.strip() for c in category_ids.split(',') if c.strip()]
        else:
            category_list = [str(category_ids).strip()] if category_ids else []
        
        # Normalize style IDs
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
        
        # Normalize brand names
        if isinstance(brand_names, list):
            brand_list = [str(b).strip() for b in brand_names if b and not str(b).strip().isdigit()]
        elif isinstance(brand_names, str):
            brand_list = [b.strip() for b in brand_names.split(',') if b.strip() and not b.strip().isdigit()]
        else:
            brand_list = [str(brand_names).strip()] if brand_names and not str(brand_names).isdigit() else []
        
        # Get products - USE STYLE FILTER AT API LEVEL!
        print(f"Preview: Fetching products with filters - Categories: {category_list}, Styles: {style_list}, Brands: {brand_list}")
        
        # Build style parameter for API
        style_param = None
        if style_list:
            style_param = ','.join(str(s) for s in style_list)
        
        # Fetch with style filter if available (much more efficient!)
        if style_param:
            products = ss_client.get_products(styleid=style_param, limit=10000)
            print(f"Preview: Fetched {len(products)} products for styles: {style_param}")
        else:
            products = ss_client.get_products(limit=5000)
            print(f"Preview: Fetched {len(products)} products (no style filter)")
        
        # Filter by categories - ONLY if no style filter was used
        # (style filter is more specific, category would over-filter)
        if category_list and not style_param:
            filtered = []
            for product in products:
                product_cats = product.get('categories', '')
                if product_cats:
                    product_cat_list = [c.strip() for c in str(product_cats).split(',') if c.strip()]
                    if any(cat in product_cat_list for cat in category_list):
                        filtered.append(product)
            products = filtered
            print(f"Preview: After category filter: {len(products)} products")
        elif style_param:
            print(f"Preview: Skipping category filter (style filter already applied)")
        
        # Filter by brands (can be IDs or names)
        if brand_list:
            # Check if these are IDs (numeric) or names
            if brand_list[0].isdigit():
                # These are brand IDs - filter by brandID (S&S API returns brandID as string!)
                brand_id_strs = set(brand_list)  # Keep as strings
                products = [p for p in products if str(p.get('brandID') or p.get('brandId') or '') in brand_id_strs]
            else:
                # These are brand names - filter by brandName
                products = [p for p in products if p.get('brandName', '').strip() in brand_list]
            print(f"Preview: After brand filter: {len(products)} products")
        
        # Remove duplicates
        seen_skus = set()
        unique_products = []
        for product in products:
            sku = product.get('sku')
            if sku and sku not in seen_skus:
                seen_skus.add(sku)
                unique_products.append(product)
        
        # Limit to 50 for preview
        preview_products = unique_products[:50]
        
        response = jsonify({
            'status': 'success',
            'products': preview_products,
            'count': len(unique_products),
            'preview_count': len(preview_products)
        })
        response.headers['Content-Length'] = str(len(response.get_data()))
        return response
    except Exception as e:
        import traceback
        error_detail = traceback.format_exc()
        print(f"Preview error: {error_detail}")
        response = jsonify({
            'status': 'error',
            'message': str(e),
            'detail': error_detail
        })
        response.headers['Content-Length'] = str(len(response.get_data()))
        return response, 400

@app.route('/api/test-endpoints', methods=['POST'])
def test_endpoints():
    """Test access to different API endpoints"""
    try:
        ss_client = SSActivewearClient(
            request.json.get('ss_account_number'),
            request.json.get('ss_api_key')
        )
        
        results = ss_client.test_endpoint_access()
        
        return jsonify({
            'status': 'success',
            'results': results
        })
    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 400

@app.route('/api/categories', methods=['POST'])
def get_categories():
    """Get all categories from S&S Activewear"""
    try:
        # Get credentials from database or session
        ss_config = get_config('ss_config') or session.get('ss_config', {})
        account_number = ss_config.get('account_number', '')
        api_key = ss_config.get('api_key', '')
        
        if not account_number or not api_key:
            return jsonify({
                'status': 'error',
                'message': 'S&S API credentials not configured'
            }), 400
        
        ss_client = SSActivewearClient(account_number, api_key)
        categories = ss_client.get_categories()
        
        return jsonify({
            'status': 'success',
            'categories': categories
        })
    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 400

@app.route('/api/styles', methods=['POST'])
def get_styles():
    """Get styles filtered by categories"""
    try:
        data = request.get_json(silent=True) or {}
        
        # Get credentials from database
        ss_config = get_config('ss_config') or session.get('ss_config', {})
        account_number = ss_config.get('account_number', '')
        api_key = ss_config.get('api_key', '')
        
        if not account_number or not api_key:
            return jsonify({
                'status': 'error',
                'message': 'S&S API credentials not configured'
            }), 400
        
        ss_client = SSActivewearClient(account_number, api_key)
        
        category_ids = data.get('category_ids', [])
        if isinstance(category_ids, str):
            category_ids = [c.strip() for c in category_ids.split(',') if c.strip()]
        elif not isinstance(category_ids, list):
            category_ids = []
        
        # Get all styles first (this is faster than getting products)
        try:
            all_styles = ss_client.get_styles(limit=1000)
        except Exception as e:
            return jsonify({
                'status': 'error',
                'message': f'Failed to fetch styles: {str(e)}'
            }), 400
        
        # Organize styles by category
        styles_by_category = {}
        category_map = {}  # Map category IDs to names
        
        # Get category names
        try:
            categories = ss_client.get_categories()
            for cat in categories:
                category_map[str(cat.get('categoryID'))] = cat.get('name', 'Unknown')
        except:
            pass
        
        # Build styles list
        styles_list = []
        if category_ids:
            # Filter by selected categories
            seen_ids = set()
            for style in all_styles:
                style_cats = style.get('categories', '')
                if style_cats:
                    style_cat_list = [c.strip() for c in str(style_cats).split(',')]
                    for cat_id in category_ids:
                        if str(cat_id) in style_cat_list and style.get('styleID') not in seen_ids:
                            styles_list.append(style)
                            seen_ids.add(style.get('styleID'))
                            break
        else:
            # Return all styles (limited)
            styles_list = all_styles[:500]
        
        return jsonify({
            'status': 'success',
            'styles': styles_list,
            'total': len(styles_list)
        })
    except Exception as e:
        import traceback
        error_detail = traceback.format_exc()
        response = jsonify({
            'status': 'error',
            'message': str(e),
            'detail': error_detail
        })
        response.headers['Content-Length'] = str(len(response.get_data()))
        return response, 400

@app.route('/api/warehouses', methods=['POST'])
def get_warehouses():
    """Get list of warehouses with stock info"""
    try:
        # Get credentials from database
        ss_config = get_config('ss_config') or session.get('ss_config', {})
        account_number = ss_config.get('account_number', '')
        api_key = ss_config.get('api_key', '')
        
        if not account_number or not api_key:
            return jsonify({
                'status': 'error',
                'message': 'S&S API credentials not configured'
            }), 400
        
        ss_client = SSActivewearClient(account_number, api_key)
        warehouses = ss_client.get_warehouses()
        
        return jsonify({
            'status': 'success',
            'warehouses': warehouses
        })
    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 500

@app.route('/api/brands', methods=['POST'])
def get_brands():
    """Get brands filtered by styles - organized by style"""
    try:
        data = request.get_json(silent=True) or {}
        
        # Get credentials from database
        ss_config = get_config('ss_config') or session.get('ss_config', {})
        account_number = ss_config.get('account_number', '')
        api_key = ss_config.get('api_key', '')
        
        if not account_number or not api_key:
            return jsonify({
                'status': 'error',
                'message': 'S&S API credentials not configured'
            }), 400
        
        ss_client = SSActivewearClient(account_number, api_key)
        
        style_ids = data.get('style_ids', [])
        if isinstance(style_ids, str):
            style_ids = [int(s.strip()) for s in style_ids.split(',') if s.strip()]
        elif isinstance(style_ids, list):
            style_ids = [int(sid) for sid in style_ids if sid]
        
        # Get all brands
        try:
            all_brands = ss_client.get_brands()
        except Exception as e:
            return jsonify({
                'status': 'error',
                'message': f'Failed to fetch brands: {str(e)}'
            }), 400
        
        # Get styles to organize brands
        brands_by_style = {}
        style_map = {}  # Map styleID to style info
        
        if style_ids:
            try:
                styles = ss_client.get_styles(limit=1000)
                for style in styles:
                    style_id = style.get('styleID')
                    if style_id and style_id in style_ids:
                        brand_name = style.get('brandName')
                        if brand_name:
                            if brand_name not in brands_by_style:
                                brands_by_style[brand_name] = []
                            brands_by_style[brand_name].append({
                                'styleID': style_id,
                                'styleName': style.get('styleName', ''),
                                'partNumber': style.get('partNumber', '')
                            })
                        style_map[style_id] = style
            except Exception as e:
                pass
        
        return jsonify({
            'status': 'success',
            'brands': all_brands,
            'total': len(all_brands)
        })
    except Exception as e:
        import traceback
        error_detail = traceback.format_exc()
        return jsonify({
            'status': 'error',
            'message': str(e),
            'detail': error_detail
        }), 400

@app.route('/api/auto-sync/status', methods=['GET'])
def auto_sync_status():
    """Get automatic sync status"""
    return jsonify(scheduler.get_status())

@app.route('/api/auto-sync/start', methods=['POST'])
def auto_sync_start():
    """Start automatic sync scheduler"""
    try:
        data = request.get_json(silent=True) or {}
        config = {
            'ss_account_number': data.get('ss_account_number'),
            'ss_api_key': data.get('ss_api_key'),
            'shopify_domain': data.get('shopify_domain'),
            'shopify_token': data.get('shopify_token')
        }
        sync_options = data.get('sync_options', {})
        auto_sync_options = data.get('auto_sync_options', {})
        require_approval = data.get('require_approval', True)
        interval_hours = data.get('interval_hours', 12)
        
        # Merge auto_sync_options into sync_options for scheduler
        if auto_sync_options:
            sync_options.update(auto_sync_options)
        
        scheduler.interval_hours = interval_hours
        scheduler.auto_sync_options = auto_sync_options  # Store separately for status
        scheduler.start(config, sync_options, require_approval)
        
        return jsonify({
            'status': 'success',
            'message': 'Automatic sync scheduler started'
        })
    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 400

@app.route('/api/auto-sync/stop', methods=['POST'])
def auto_sync_stop():
    """Stop automatic sync scheduler"""
    scheduler.stop()
    return jsonify({
        'status': 'success',
        'message': 'Automatic sync scheduler stopped'
    })

@app.route('/api/auto-sync/approve', methods=['POST'])
def auto_sync_approve():
    """Approve pending automatic sync"""
    if scheduler.approve_pending_sync():
        return jsonify({
            'status': 'success',
            'message': 'Sync approved and started'
        })
    else:
        return jsonify({
            'status': 'error',
            'message': 'No pending sync to approve'
        }), 400

@app.route('/api/sync/current-product', methods=['GET'])
def get_current_product():
    """Get currently syncing product"""
    global sync_manager
    
    if sync_manager and sync_manager.status == 'running':
        return jsonify({
            'status': 'success',
            'current_product': getattr(sync_manager, 'current_product', None),
            'current_index': getattr(sync_manager, 'current_index', 0),
            'total': sync_manager.stats.get('total', 0)
        })
    
    return jsonify({
        'status': 'idle',
        'current_product': None
    })

@app.route('/api/sync/rollback-last', methods=['POST'])
def rollback_last_sync():
    """Rollback last sync - delete created products, revert updated products"""
    try:
        # Get credentials from database
        shopify_config = get_config('shopify_config') or session.get('shopify_config', {})
        shopify_domain = shopify_config.get('shop_domain', '').strip()
        shopify_token = shopify_config.get('access_token', '').strip()
        
        if not shopify_domain or not shopify_token:
            return jsonify({
                'status': 'error',
                'message': 'Shopify credentials required'
            }), 400
        
        shopify_client = ShopifyClient(shopify_domain, shopify_token)
        last_sync_id = get_last_sync_id()
        
        if not last_sync_id:
            return jsonify({
                'status': 'error',
                'message': 'No sync history found'
            }), 404
        
        sync_products = get_sync_products(last_sync_id)
        if not sync_products:
            return jsonify({
                'status': 'error',
                'message': 'No products found in last sync'
            }), 404
        
        deleted = 0
        errors = []
        
        seen_product_ids = set()  # Track products we've already deleted
        
        for product_record in sync_products:
            # Only delete products created by API (created_by_api = 1)
            if product_record.get('created_by_api', 1) != 1:
                continue
                
            product_id = product_record['shopify_product_id']
            
            # Skip if we've already deleted this product
            if product_id in seen_product_ids:
                continue
                
            try:
                if product_record['action'] == 'created':
                    # Delete created product
                    shopify_client.delete_product(product_id)
                    deleted += 1
                    seen_product_ids.add(product_id)
                elif product_record['action'] == 'updated':
                    # Note: We can't fully revert updates without storing old data
                    # For now, we'll just log it
                    errors.append(f"Product {product_record['sku']} was updated (cannot auto-revert)")
            except Exception as e:
                error_msg = str(e)
                # Ignore 404 errors (product already deleted)
                if '404' not in error_msg and 'not found' not in error_msg.lower():
                    errors.append(f"Error processing {product_record['sku']}: {str(e)}")
        
        return jsonify({
            'status': 'success',
            'message': f'Rolled back {deleted} created products',
            'deleted': deleted,
            'errors': errors
        })
    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 400

@app.route('/api/shopify/delete-all', methods=['POST'])
def delete_all_shopify_data():
    """
    Delete ONLY products created by our system - SAFE OPERATION
    Only deletes products that exist in our style_shopify_products mapping table
    """
    try:
        data = request.get_json(silent=True) or {}
        
        # Get credentials from database
        shopify_config = get_config('shopify_config') or session.get('shopify_config', {})
        shopify_domain = shopify_config.get('shop_domain', '').strip()
        shopify_token = shopify_config.get('access_token', '').strip()
        delete_products = data.get('delete_products', True)
        delete_collections = data.get('delete_collections', True)
        
        if not shopify_domain or not shopify_token:
            return jsonify({
                'status': 'error',
                'message': 'Shopify credentials not configured'
            }), 400
        
        shopify_client = ShopifyClient(shopify_domain, shopify_token)
        deleted_products = 0
        deleted_collections = 0
        errors = []
        skipped_products = 0
        
        if delete_products:
            try:
                # GÜVENLI SİLME: Sadece bizim oluşturduğumuz ürünleri sil
                # style_shopify_products tablosundaki mapping'leri kullan
                from database import get_db
                
                our_product_ids = set()
                with get_db() as conn:
                    cursor = conn.cursor()
                    cursor.execute('SELECT DISTINCT shopify_product_id FROM style_shopify_products')
                    for row in cursor.fetchall():
                        our_product_ids.add(row['shopify_product_id'])
                
                if not our_product_ids:
                    return jsonify({
                        'status': 'success',
                        'message': 'Silinecek ürün bulunamadı (mapping tablosu boş)',
                        'deleted_products': 0,
                        'skipped_products': 0
                    })
                
                add_system_log('INFO', f"Silinecek ürün sayısı: {len(our_product_ids)} (sadece bizim oluşturduklarımız)", 'main')
                
                for product_id in our_product_ids:
                    try:
                        shopify_client.delete_product(product_id)
                        deleted_products += 1
                        
                        # Mapping'den de sil
                        with get_db() as conn:
                            cursor = conn.cursor()
                            cursor.execute('DELETE FROM style_shopify_products WHERE shopify_product_id = ?', (product_id,))
                            cursor.execute('DELETE FROM sku_shopify_variants WHERE shopify_product_id = ?', (product_id,))
                        
                    except Exception as e:
                        errors.append(f"Error deleting product {product_id}: {str(e)}")
                    
                add_system_log('SUCCESS', f"Toplam {deleted_products} ürün silindi", 'main')
                
            except Exception as e:
                errors.append(f"Error during safe delete: {str(e)}")
        
        # Collections için de sadece bizim oluşturduklarımızı sil (eğer mapping varsa)
        # Şimdilik collection silme devre dışı - güvenlik için
        if delete_collections:
            add_system_log('WARNING', "Collection silme şimdilik devre dışı - güvenlik için", 'main')
        
        return jsonify({
            'status': 'success',
            'message': f'Sadece bizim oluşturduğumuz {deleted_products} ürün silindi',
            'deleted_products': deleted_products,
            'skipped_products': skipped_products,
            'errors': errors
        })
    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 400


@app.route('/api/search-products', methods=['POST'])
def search_products():
    """Fast product search using FTS5 cache - CACHE-FIRST"""
    try:
        import time
        start_time = time.time()
        
        data = request.get_json(silent=True) or {}
        query = data.get('query', '').strip()
        limit = data.get('limit', 50)
        offset = data.get('offset', 0)
        
        if not query or len(query) < 2:
            return jsonify({
                'status': 'error',
                'message': 'Search query must be at least 2 characters'
            }), 400
        
        # Search in FTS cache (milliseconds!)
        results, total = search_products_fts(query, limit, offset)
        
        elapsed_ms = (time.time() - start_time) * 1000
        add_system_log('CACHE', f"Search '{query[:20]}': {len(results)} sonuç, {elapsed_ms:.1f}ms", 'cache')
        
        return jsonify({
            'status': 'success',
            'total': total,
            'results': results,
            'hasMore': offset + limit < total,
            'cached': True,
            'response_time_ms': round(elapsed_ms, 2)
        })
        
    except Exception as e:
        import traceback
        traceback.print_exc()
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 500


@app.route('/api/search-cache/status', methods=['GET'])
def search_cache_status():
    """Get search cache status"""
    try:
        count = get_search_cache_count()
        last_update = get_search_cache_last_update()
        
        return jsonify({
            'status': 'success',
            'count': count,
            'lastUpdate': last_update,
            'isEmpty': count == 0
        })
    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 500


@app.route('/api/search-cache/rebuild', methods=['POST'])
def rebuild_search_cache():
    """Rebuild search cache from S&S API"""
    try:
        # Get S&S API config
        ss_config = get_config('ss_config') or session.get('ss_config', {})
        if not ss_config.get('account_number') or not ss_config.get('api_key'):
            return jsonify({
                'status': 'error',
                'message': 'S&S API credentials not configured'
            }), 400
        
        ss_client = SSActivewearClient(
            account_number=ss_config['account_number'],
            api_key=ss_config['api_key']
        )
        
        # Clear existing cache
        clear_search_cache()
        
        # Fetch all products from API
        print("Fetching products from S&S API for search cache...")
        all_products = ss_client.get_products(limit=50000)
        print(f"Fetched {len(all_products)} products")
        
        # Populate cache
        inserted = populate_search_cache(all_products)
        print(f"Inserted {inserted} styles into search cache")
        
        return jsonify({
            'status': 'success',
            'message': f'Cache rebuilt with {inserted} styles',
            'count': inserted
        })
        
    except Exception as e:
        import traceback
        traceback.print_exc()
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 500


@app.route('/api/image-proxy')
def image_proxy():
    """Proxy S&S images to avoid CORS issues"""
    from flask import Response
    
    image_url = request.args.get('url', '')
    if not image_url:
        return '', 404
    
    # Only allow S&S images
    if not image_url.startswith('https://www.ssactivewear.com/'):
        return '', 403
    
    try:
        # Get S&S credentials for auth
        ss_config = get_config('ss_config') or {}
        account_number = ss_config.get('account_number', '')
        api_key = ss_config.get('api_key', '')
        
        headers = {}
        if account_number and api_key:
            import base64
            credentials = base64.b64encode(f"{account_number}:{api_key}".encode()).decode()
            headers['Authorization'] = f'Basic {credentials}'
        
        response = requests.get(image_url, headers=headers, timeout=10, stream=True)
        
        if response.status_code == 200:
            return Response(
                response.content,
                content_type=response.headers.get('Content-Type', 'image/jpeg')
            )
        else:
            return '', response.status_code
    except Exception as e:
        print(f"Image proxy error: {e}")
        return '', 500


@app.route('/api/product-detail/<style_id>', methods=['GET'])
def get_product_detail(style_id):
    """Get detailed product information including all variants and metafields"""
    try:
        # Get S&S API config
        ss_config = get_config('ss_config') or session.get('ss_config', {})
        if not ss_config.get('account_number') or not ss_config.get('api_key'):
            return jsonify({
                'status': 'error',
                'message': 'S&S API credentials not configured'
            }), 400
        
        ss_client = SSActivewearClient(
            account_number=ss_config['account_number'],
            api_key=ss_config['api_key']
        )
        
        # Fetch products for this style
        products = ss_client.get_products(styleid=style_id, limit=2000)
        
        if not products:
            return jsonify({
                'status': 'error',
                'message': f'No products found for style {style_id}'
            }), 404
        
        # Build comprehensive product data
        base_product = products[0]
        
        # Collect all images
        all_images = {}
        for product in products:
            color = product.get('colorName', 'Default')
            if color not in all_images:
                all_images[color] = []
            
            for img_field in ['colorFrontImage', 'colorSideImage', 'colorBackImage', 
                              'colorDirectSideImage', 'colorOnModelFrontImage', 'colorOnModelBackImage']:
                img_url = product.get(img_field)
                if img_url:
                    if not img_url.startswith('http'):
                        img_url = f"https://www.ssactivewear.com/{img_url.lstrip('/')}"
                    if img_url not in all_images[color]:
                        all_images[color].append(img_url)
        
        # Build variants list
        variants = []
        for product in products:
            # Get inventory from warehouses
            total_inventory = 0
            warehouse_inventory = {}
            warehouses = product.get('warehouses', [])
            if isinstance(warehouses, list):
                for wh in warehouses:
                    wh_name = wh.get('warehouseAbbr', 'Unknown')
                    qty = wh.get('qty', 0)
                    warehouse_inventory[wh_name] = qty
                    total_inventory += qty
            
            variants.append({
                'sku': product.get('sku', ''),
                'gtin': product.get('gtin', ''),
                'colorName': product.get('colorName', ''),
                'sizeName': product.get('sizeName', ''),
                'colorCode': product.get('colorCode', ''),
                'sizeCode': product.get('sizeCode', ''),
                'piecePrice': product.get('piecePrice', 0),
                'casePrice': product.get('casePrice', 0),
                'dozenPrice': product.get('dozenPrice', 0),
                'salePrice': product.get('salePrice'),
                'customerPrice': product.get('customerPrice'),
                'caseQty': product.get('caseQty', 0),
                'weight': product.get('pieceWeight', 0),
                'inventory': total_inventory,
                'warehouseInventory': warehouse_inventory
            })
        
        # Extract all metafields from base product
        metafields = {}
        skip_fields = ['sku', 'gtin', 'colorName', 'sizeName', 'piecePrice', 'warehouses', 
                       'colorFrontImage', 'colorSideImage', 'colorBackImage', 'styleImage']
        
        for key, value in base_product.items():
            if key not in skip_fields and value is not None and value != '':
                if not isinstance(value, (list, dict)):
                    metafields[key] = value
        
        # Calculate price range
        prices = [v['piecePrice'] for v in variants if v['piecePrice'] > 0]
        min_price = min(prices) if prices else 0
        max_price = max(prices) if prices else 0
        
        # Get unique colors and sizes
        colors = sorted(list(set(v['colorName'] for v in variants if v['colorName'])))
        sizes = sorted(list(set(v['sizeName'] for v in variants if v['sizeName'])))
        
        result = {
            'styleID': style_id,
            'styleName': base_product.get('styleName', ''),
            'brandName': base_product.get('brandName', ''),
            'title': base_product.get('title', base_product.get('styleName', '')),
            'description': base_product.get('description', ''),
            'minPrice': min_price,
            'maxPrice': max_price,
            'images': all_images,
            'colors': colors,
            'sizes': sizes,
            'variants': variants,
            'metafields': metafields,
            'totalVariants': len(variants)
        }
        
        return jsonify({
            'status': 'success',
            'product': result
        })
        
    except Exception as e:
        import traceback
        traceback.print_exc()
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 500


@app.route('/api/quick-import', methods=['POST'])
def quick_import():
    """Quick import a single style to Shopify"""
    try:
        data = request.get_json(silent=True) or {}
        style_id = data.get('style_id')
        warehouse = data.get('warehouse')
        
        if not style_id:
            return jsonify({'status': 'error', 'message': 'style_id required'}), 400
        
        # Get configs
        ss_config = get_config('ss_config') or {}
        shopify_config = get_config('shopify_config') or {}
        
        if not ss_config.get('account_number') or not ss_config.get('api_key'):
            return jsonify({'status': 'error', 'message': 'S&S API credentials not configured'}), 400
        
        if not shopify_config.get('shop_domain') or not shopify_config.get('access_token'):
            return jsonify({'status': 'error', 'message': 'Shopify credentials not configured'}), 400
        
        # Fetch products for this style (warehouse filter not supported with styleid)
        ss_client = SSActivewearClient(
            account_number=ss_config['account_number'],
            api_key=ss_config['api_key']
        )
        
        # Fetch without warehouse filter - API doesn't support styleid + Warehouses together
        products = ss_client.get_products(styleid=str(style_id), limit=2000)
        
        if not products:
            return jsonify({'status': 'error', 'message': 'No products found'}), 404
        
        # Filter by warehouse locally if specified
        if warehouse:
            filtered_products = []
            for p in products:
                warehouses_list = p.get('warehouses', [])
                # Check if product has stock in selected warehouse
                for wh in warehouses_list:
                    if wh.get('warehouseAbbr') == warehouse and wh.get('qty', 0) > 0:
                        filtered_products.append(p)
                        break
            products = filtered_products if filtered_products else products
        
        # Import using sync orchestrator
        from shopify_gateway import ShopifyGateway
        from style_builder import StyleBuilder
        from domain_models import Style, StyleVariant, StyleImage
        from database import init_database
        import uuid
        
        init_database()
        
        gateway = ShopifyGateway(
            shop_domain=shopify_config['shop_domain'],
            access_token=shopify_config['access_token']
        )
        
        # Build style manually
        base = products[0]
        sync_id = str(uuid.uuid4())
        
        # Store products in cache first
        from database import get_db
        with get_db() as conn:
            cursor = conn.cursor()
            for product in products:
                cursor.execute('''
                    INSERT OR REPLACE INTO ss_products_cache
                    (sync_id, sku, style_id, product_data, fetched_at)
                    VALUES (?, ?, ?, ?, datetime('now'))
                ''', (sync_id, product.get('sku', ''), str(style_id), json.dumps(product)))
            conn.commit()
        
        # Build style using StyleBuilder
        builder = StyleBuilder(sync_id)
        style = builder.build_style_from_group(str(style_id))
        
        if not style:
            return jsonify({'status': 'error', 'message': 'Could not build style'}), 500
        
        # Create product using gateway
        parts = style.split_into_parts()
        if not parts:
            return jsonify({'status': 'error', 'message': 'No parts to create'}), 500
        
        style_part = parts[0]
        product_id, product_gid, created_variants = gateway.create_product_with_variants(style_part)
        
        # Update metafields - CRITICAL: Store all S&S API data
        if style.metafields:
            metafield_success = gateway.update_metafields(product_gid, style.metafields)
            print(f"   📝 Metafields updated: {len(style.metafields)} fields, success: {metafield_success}")
        
        # Build Shopify URL
        shop_domain = shopify_config['shop_domain'].replace('https://', '').replace('http://', '').split('/')[0]
        shopify_url = f"https://{shop_domain}/admin/products/{product_id}"
        
        return jsonify({
            'status': 'success',
            'product_id': product_id,
            'variants_created': len(created_variants),
            'metafields_count': len(style.metafields) if style.metafields else 0,
            'shopify_url': shopify_url
        })
        
    except Exception as e:
        import traceback
        traceback.print_exc()
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 500


# ===== WAREHOUSE STOCK API =====
# These endpoints power the Shopify product page warehouse stock table

@app.route('/api/warehouse-stock/sku/<sku>', methods=['GET'])
def get_warehouse_stock_sku(sku):
    """Get warehouse stock for a specific SKU - for Shopify App Proxy"""
    try:
        from database import get_warehouse_stock_by_sku
        
        stock_data = get_warehouse_stock_by_sku(sku)
        
        # Return JSONP if callback provided (for cross-domain)
        callback = request.args.get('callback')
        
        response_data = {
            'status': 'success',
            'sku': sku,
            'warehouses': stock_data,
            'updated_at': stock_data[0]['updated_at'] if stock_data else None
        }
        
        if callback:
            return f"{callback}({json.dumps(response_data)})", 200, {'Content-Type': 'application/javascript'}
        
        return jsonify(response_data)
        
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500


@app.route('/api/warehouse-stock/by-sku/<sku>', methods=['GET'])
def get_warehouse_stock_by_sku_endpoint(sku):
    """Get warehouse stock by SKU - CACHE-FIRST implementation"""
    try:
        from cache_manager import cache_manager
        import time
        start_time = time.time()
        
        # 1. Cache'den SKU bilgisini al (3-layer: Memory -> SQLite -> API)
        sku_data, source = cache_manager.get_warehouse_stock(sku, use_api_fallback=True)
        
        if not sku_data:
            add_system_log('WARNING', f"SKU {sku} cache miss - API fallback", 'cache')
            return jsonify({
                'status': 'error',
                'message': f'SKU {sku} bulunamadı',
                'sku': sku
            }), 404
        
        style_id = sku_data.get('style_id')
        elapsed_ms = (time.time() - start_time) * 1000
        add_system_log('CACHE', f"SKU {sku} -> style {style_id} ({source}, {elapsed_ms:.1f}ms)", 'cache')
        
        if not style_id:
            return jsonify({
                'status': 'error',
                'message': f'SKU {sku} için style_id bulunamadı',
                'sku': sku
            }), 404
        
        # 2. Style ID ile tüm varyantları getir (cache-first WITH API FALLBACK)
        stock_data = cache_manager.get_warehouse_stock_by_style(style_id, use_api_fallback=True)
        
        total_elapsed = (time.time() - start_time) * 1000
        
        if not stock_data:
            add_system_log('WARNING', f"Style {style_id}: Cache ve API'de bulunamadı", 'cache')
        else:
            add_system_log('SUCCESS', f"Style {style_id}: {len(stock_data)} SKU, toplam {total_elapsed:.1f}ms", 'cache')
        
        callback = request.args.get('callback')
        response_data = {
            'status': 'success',
            'requested_sku': sku,
            'style_id': style_id,
            'skus': stock_data,
            'total_skus': len(stock_data),
            'source': source,
            'response_time_ms': round(total_elapsed, 2)
        }
        
        if callback:
            return f"{callback}({json.dumps(response_data)})", 200, {'Content-Type': 'application/javascript'}
        
        return jsonify(response_data)
        
    except Exception as e:
        import traceback
        traceback.print_exc()
        return jsonify({'status': 'error', 'message': str(e)}), 500


@app.route('/api/warehouse-stock/style/<style_id>', methods=['GET'])
def get_warehouse_stock_style(style_id):
    """Get all warehouse stock for a style - with real-time fallback"""
    try:
        from database import get_warehouse_stock_by_style, update_warehouse_stock
        
        # 1. İlk önce cache'e bak
        stock_data = get_warehouse_stock_by_style(style_id)
        
        # 2. Cache boşsa veya color/size eksikse, anlık API sorgusu yap
        needs_realtime = False
        if not stock_data:
            needs_realtime = True
        else:
            # İlk SKU'yu kontrol et - color_name boşsa veriler eksik demek
            first_sku = next(iter(stock_data.values()), None)
            if first_sku and not first_sku.get('color_name'):
                needs_realtime = True
        
        if needs_realtime:
            # S&S API'den anlık veri çek
            ss_config = get_config('ss_config') or {}
            if ss_config.get('account_number') and ss_config.get('api_key'):
                try:
                    ss_client = SSActivewearClient(
                        account_number=ss_config['account_number'],
                        api_key=ss_config['api_key']
                    )
                    
                    # Products API'den style'a ait ürünleri çek (style ID veya style name ile)
                    products = None
                    
                    # Önce styleid ile dene
                    if style_id.isdigit():
                        products = ss_client.get_products(styleid=str(style_id))
                    
                    # Sonuç yoksa style name ile dene
                    if not products and not style_id.isdigit():
                        try:
                            products = ss_client.get_products(style=style_id)
                        except:
                            pass
                    
                    if products:
                        # Veriyi işle ve cache'e yaz
                        stock_data = {}
                        for item in products:
                            sku = item.get('sku', '')
                            if not sku:
                                continue
                            
                            warehouses = item.get('warehouses', [])
                            if not warehouses:
                                continue
                            
                            price = item.get('customerPrice') or item.get('piecePrice') or 0
                            color_name = item.get('colorName', '')
                            size_name = item.get('sizeName', '')
                            
                            # Warehouse listesi oluştur
                            warehouse_list = []
                            for wh in warehouses:
                                code = wh.get('warehouseAbbr', '')
                                if code:
                                    warehouse_list.append({
                                        'code': code,
                                        'name': wh.get('warehouseName', code),
                                        'qty': wh.get('qty', 0),
                                        'price': price
                                    })
                            
                            # Cache'e kaydet (arka planda)
                            if warehouse_list:
                                update_warehouse_stock(
                                    sku=sku,
                                    warehouse_data=warehouse_list,
                                    style_id=str(style_id),
                                    color_name=color_name,
                                    size_name=size_name
                                )
                            
                            # Response için hazırla
                            stock_data[sku] = {
                                'sku': sku,
                                'color_name': color_name,
                                'size_name': size_name,
                                'warehouses': warehouse_list
                            }
                        
                        print(f"📡 Real-time fetch for style {style_id}: {len(stock_data)} SKUs")
                except Exception as api_error:
                    print(f"⚠️ Real-time API error for style {style_id}: {api_error}")
                    # Hata olsa bile cache'deki veriyi dön
        
        callback = request.args.get('callback')
        
        response_data = {
            'status': 'success',
            'style_id': style_id,
            'skus': stock_data,
            'total_skus': len(stock_data),
            'source': 'realtime' if needs_realtime else 'cache'
        }
        
        if callback:
            return f"{callback}({json.dumps(response_data)})", 200, {'Content-Type': 'application/javascript'}
        
        return jsonify(response_data)
        
    except Exception as e:
        import traceback
        traceback.print_exc()
        return jsonify({'status': 'error', 'message': str(e)}), 500


# Global warehouse sync state
warehouse_sync_state = {
    'is_running': False,
    'started_at': None,
    'progress': 0,
    'total': 0,
    'error': None
}

def _run_warehouse_sync_background():
    """Background task for warehouse stock sync - Uses Products API for full data"""
    global warehouse_sync_state
    import time
    
    try:
        from database import update_warehouse_stock, update_warehouse_sync_status
        
        warehouse_sync_state['is_running'] = True
        warehouse_sync_state['started_at'] = datetime.now().isoformat()
        warehouse_sync_state['progress'] = 0
        warehouse_sync_state['error'] = None
        
        start_time = time.time()
        
        # Log start
        add_system_log('CACHE', '🚀 Warehouse cache güncellemesi başlatıldı', 'cache')
        add_system_log('SCHEDULER', '📦 Background sync başladı', 'scheduler')
        
        # Get S&S credentials
        ss_config = get_config('ss_config') or {}
        if not ss_config.get('account_number') or not ss_config.get('api_key'):
            warehouse_sync_state['error'] = 'S&S API not configured'
            warehouse_sync_state['is_running'] = False
            add_system_log('ERROR', 'S&S API yapılandırılmamış!', 'cache')
            return
        
        ss_client = SSActivewearClient(
            account_number=ss_config['account_number'],
            api_key=ss_config['api_key']
        )
        
        add_system_log('API', '→ S&S Products API çağrılıyor...', 'ss')
        
        # Fetch PRODUCTS from S&S (includes colorName, sizeName, price AND warehouses)
        print("📦 Fetching all products from S&S API (background)...")
        print("⚠️ This may take several minutes for the full catalog...")
        
        # Get all products in one call (API returns everything)
        all_products = ss_client.get_products()
        
        if not all_products:
            warehouse_sync_state['error'] = 'No products returned'
            warehouse_sync_state['is_running'] = False
            return
        
        warehouse_sync_state['total'] = len(all_products)
        print(f"📦 Processing {len(all_products)} products with full data...")
        
        # Process each product
        total_skus = 0
        warehouse_codes = set()
        
        for i, item in enumerate(all_products):
            sku = item.get('sku', '')
            if not sku:
                continue
            
            warehouses = item.get('warehouses', [])
            if not warehouses:
                continue
            
            # Get price (prioritize customerPrice, then piecePrice, then dozenPrice)
            price = item.get('customerPrice') or item.get('piecePrice') or item.get('dozenPrice') or 0
            
            # Prepare warehouse data with full product info
            warehouse_list = []
            for wh in warehouses:
                code = wh.get('warehouseAbbr', '')
                if code:
                    warehouse_codes.add(code)
                    warehouse_list.append({
                        'code': code,
                        'name': wh.get('warehouseName', code),
                        'qty': wh.get('qty', 0),
                        'price': price
                    })
            
            if warehouse_list:
                # Now we have full product data including colorName, sizeName, price
                update_warehouse_stock(
                    sku=sku,
                    warehouse_data=warehouse_list,
                    style_id=str(item.get('styleID', '')),
                    color_name=item.get('colorName', ''),
                    size_name=item.get('sizeName', '')
                )
                total_skus += 1
            
            # Update progress every 1000 items
            if i % 1000 == 0:
                warehouse_sync_state['progress'] = i
                print(f"   Processed {i}/{len(all_products)} products...")
        
        duration = int(time.time() - start_time)
        update_warehouse_sync_status(total_skus, len(warehouse_codes), duration)
        
        warehouse_sync_state['progress'] = warehouse_sync_state['total']
        warehouse_sync_state['is_running'] = False
        
        print(f"✅ Warehouse sync complete: {total_skus} SKUs, {len(warehouse_codes)} warehouses, {duration}s")
        
    except Exception as e:
        import traceback
        traceback.print_exc()
        warehouse_sync_state['error'] = str(e)
        warehouse_sync_state['is_running'] = False


@app.route('/api/warehouse-stock/sync', methods=['POST'])
def sync_warehouse_stock():
    """Start warehouse stock sync in background - won't block server"""
    global warehouse_sync_state
    
    if warehouse_sync_state['is_running']:
        return jsonify({
            'status': 'already_running',
            'message': 'Warehouse sync already in progress',
            'progress': warehouse_sync_state['progress'],
            'total': warehouse_sync_state['total']
        })
    
    # Start background thread
    sync_thread = threading.Thread(target=_run_warehouse_sync_background, daemon=True)
    sync_thread.start()
    
    return jsonify({
        'status': 'started',
        'message': 'Warehouse sync started in background. Check /api/warehouse-stock/status for progress.'
    })


@app.route('/api/warehouse-stock/status', methods=['GET'])
def warehouse_stock_status():
    """Get warehouse stock sync status"""
    global warehouse_sync_state
    try:
        from database import get_warehouse_sync_status
        db_status = get_warehouse_sync_status()
        scheduler_status = warehouse_scheduler.get_status()
        return jsonify({
            'status': 'success',
            'sync': db_status,
            'scheduler': scheduler_status,
            'current_sync': {
                'is_running': warehouse_sync_state['is_running'],
                'started_at': warehouse_sync_state['started_at'],
                'progress': warehouse_sync_state['progress'],
                'total': warehouse_sync_state['total'],
                'error': warehouse_sync_state['error']
            }
        })
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500


@app.route('/api/warehouse-stock/scheduler/start', methods=['POST'])
def start_warehouse_scheduler():
    """Start warehouse stock scheduler (runs every 2 hours)"""
    try:
        ss_config = get_config('ss_config') or {}
        if not ss_config.get('account_number') or not ss_config.get('api_key'):
            return jsonify({'status': 'error', 'message': 'S&S API not configured'}), 400
        
        warehouse_scheduler.start(ss_config)
        return jsonify({'status': 'success', 'message': 'Warehouse scheduler started'})
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500


@app.route('/api/warehouse-stock/scheduler/stop', methods=['POST'])
def stop_warehouse_scheduler():
    """Stop warehouse stock scheduler"""
    try:
        warehouse_scheduler.stop()
        return jsonify({'status': 'success', 'message': 'Warehouse scheduler stopped'})
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500


# ===== SHOPIFY APP PROXY ENDPOINT =====
# This endpoint is called from Shopify storefront via App Proxy
# URL: https://your-store.myshopify.com/apps/warehouse/stock?sku=XXX

@app.route('/apps/warehouse/stock', methods=['GET'])
def shopify_warehouse_proxy():
    """Shopify App Proxy endpoint for warehouse stock"""
    try:
        from database import get_warehouse_stock_by_sku, get_warehouse_stock_by_style
        
        sku = request.args.get('sku')
        style_id = request.args.get('style_id')
        
        if sku:
            stock_data = get_warehouse_stock_by_sku(sku)
            result = {
                'sku': sku,
                'warehouses': stock_data
            }
        elif style_id:
            stock_data = get_warehouse_stock_by_style(style_id)
            result = {
                'style_id': style_id,
                'skus': stock_data
            }
        else:
            return jsonify({'error': 'sku or style_id required'}), 400
        
        # Shopify App Proxy returns content-type based on extension
        # For .js it expects JavaScript, for .json it expects JSON
        response = jsonify(result)
        response.headers['Access-Control-Allow-Origin'] = '*'
        return response
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500


# ==================== SYSTEM MONITOR ====================

# Global system monitor state
system_monitor = {
    'start_time': datetime.now(),
    'total_requests': 0,
    'success_count': 0,
    'error_count': 0,
    'incoming_requests': [],
    'outgoing_requests': [],
    'logs': {
        'main': [],
        'ss': [],
        'shopify': [],
        'cache': [],
        'scheduler': []
    },
    'last_db_query': None,
    'scheduler_running': False,
    'last_cache_update': None
}

def _add_system_log_impl(log_type, message, terminal='main'):
    """Add a log entry to the system monitor"""
    entry = {
        'time': datetime.now().strftime('%H:%M:%S'),
        'type': log_type,
        'message': message,
        'terminal': terminal
    }
    
    # Add to specific terminal log
    if terminal in system_monitor['logs']:
        system_monitor['logs'][terminal].insert(0, entry)
        # Keep only last 100 logs per terminal
        if len(system_monitor['logs'][terminal]) > 100:
            system_monitor['logs'][terminal] = system_monitor['logs'][terminal][:100]
    
    # Also add to main log
    if terminal != 'main':
        system_monitor['logs']['main'].insert(0, entry)
        if len(system_monitor['logs']['main']) > 200:
            system_monitor['logs']['main'] = system_monitor['logs']['main'][:200]

def _track_incoming_request_impl(method, path, status):
    """Track incoming API request"""
    entry = {
        'method': method,
        'path': path,
        'status': status,
        'time': datetime.now().strftime('%H:%M:%S')
    }
    system_monitor['incoming_requests'].insert(0, entry)
    system_monitor['total_requests'] += 1
    if status < 400:
        system_monitor['success_count'] += 1
    else:
        system_monitor['error_count'] += 1
    # Keep only last 50
    if len(system_monitor['incoming_requests']) > 50:
        system_monitor['incoming_requests'] = system_monitor['incoming_requests'][:50]
    
    # Add log entry
    log_type = 'SUCCESS' if status < 400 else 'ERROR'
    _add_system_log_impl(log_type, f"← {method} {path} [{status}]", 'main')

def _track_outgoing_request_impl(target, endpoint, method, success):
    """Track outgoing API request"""
    entry = {
        'target': target,
        'endpoint': endpoint[:50] + '...' if len(endpoint) > 50 else endpoint,
        'method': method,
        'success': success,
        'time': datetime.now().strftime('%H:%M:%S')
    }
    system_monitor['outgoing_requests'].insert(0, entry)
    # Keep only last 50
    if len(system_monitor['outgoing_requests']) > 50:
        system_monitor['outgoing_requests'] = system_monitor['outgoing_requests'][:50]

# Mark monitor as initialized
_monitor_initialized = True

# Initialize system monitor logs on startup
def _init_system_monitor():
    """Add initial logs on server startup"""
    _add_system_log_impl('INFO', '🚀 Sunucu başlatıldı', 'main')
    _add_system_log_impl('INFO', 'Veritabanı bağlantısı aktif', 'cache')
    _add_system_log_impl('INFO', 'Sistem izleme modülü hazır', 'main')
    
    # Check configs
    ss_config = get_config('ss_config') or {}
    shopify_config = get_config('shopify_config') or {}
    
    if ss_config.get('account_number'):
        _add_system_log_impl('SUCCESS', 'S&S API kimlik bilgileri yapılandırılmış', 'ss')
    else:
        _add_system_log_impl('WARNING', 'S&S API kimlik bilgileri eksik', 'ss')
    
    if shopify_config.get('shop_domain'):
        shop = shopify_config.get('shop_domain', '').replace('https://', '').split('/')[0]
        _add_system_log_impl('SUCCESS', f"Shopify bağlantısı: {shop}", 'shopify')
    else:
        _add_system_log_impl('WARNING', 'Shopify kimlik bilgileri eksik', 'shopify')
    
    _add_system_log_impl('INFO', 'Scheduler durumu kontrol ediliyor...', 'scheduler')

# Run initialization
try:
    _init_system_monitor()
except Exception as e:
    print(f"System monitor init error: {e}")

@app.route('/api/system-monitor/status')
def get_system_monitor_status():
    """Get real-time system monitor status"""
    try:
        from database import get_db
        
        # Calculate uptime
        uptime = datetime.now() - system_monitor['start_time']
        hours, remainder = divmod(int(uptime.total_seconds()), 3600)
        minutes, seconds = divmod(remainder, 60)
        uptime_str = f"{hours:02d}:{minutes:02d}:{seconds:02d}"
        
        # Get cached SKUs count
        cached_skus = 0
        try:
            with get_db() as conn:
                cursor = conn.cursor()
                cursor.execute("SELECT COUNT(DISTINCT sku) FROM warehouse_stock_cache")
                result = cursor.fetchone()
                cached_skus = result[0] if result else 0
                system_monitor['last_db_query'] = datetime.now().strftime('%H:%M:%S')
                
                # Don't log every cache query - too noisy
                pass
        except Exception as db_err:
            add_system_log('ERROR', f"DB hatası: {str(db_err)}", 'cache')
        
        # Check connections
        ss_config = get_config('ss_config') or {}
        shopify_config = get_config('shopify_config') or {}
        
        ss_connected = bool(ss_config.get('account_number') and ss_config.get('api_key'))
        shopify_connected = bool(shopify_config.get('shop_domain') and shopify_config.get('access_token'))
        
        # Check scheduler status
        scheduler_running = warehouse_scheduler is not None and getattr(warehouse_scheduler, 'running', False)
        
        # Calculate next cache update (every 2 hours)
        if system_monitor.get('last_cache_update'):
            from datetime import timedelta
            next_update = system_monitor['last_cache_update'] + timedelta(hours=2)
            remaining = next_update - datetime.now()
            if remaining.total_seconds() > 0:
                hours_left, remainder = divmod(int(remaining.total_seconds()), 3600)
                mins_left, secs_left = divmod(remainder, 60)
                next_cache_str = f"{hours_left:02d}:{mins_left:02d}:{secs_left:02d}"
                cache_progress = 100 - (remaining.total_seconds() / 7200 * 100)
            else:
                next_cache_str = "Şimdi"
                cache_progress = 100
        else:
            next_cache_str = "Bekliyor"
            cache_progress = 0
        
        # Check if sync is running
        active_syncs = 1 if sync_manager and sync_manager.status == 'running' else 0
        
        return jsonify({
            'status': 'success',
            'connections': {
                'ss_api': ss_connected,
                'shopify_api': shopify_connected,
                'database': True,
                'scheduler': scheduler_running
            },
            'stats': {
                'total_requests': system_monitor['total_requests'],
                'success_count': system_monitor['success_count'],
                'error_count': system_monitor['error_count'],
                'cached_skus': cached_skus,
                'active_syncs': active_syncs,
                'queue_size': 0
            },
            'timers': {
                'next_cache_update': next_cache_str,
                'cache_progress': cache_progress,
                'server_uptime': uptime_str,
                'last_db_query': system_monitor.get('last_db_query', '--')
            },
            'cache_performance': get_cache_performance_stats(),
            'incoming_requests': system_monitor['incoming_requests'][:20],
            'outgoing_requests': system_monitor['outgoing_requests'][:20],
            'logs': {
                'main': system_monitor['logs'].get('main', [])[:30],
                'ss': system_monitor['logs'].get('ss', [])[:30],
                'shopify': system_monitor['logs'].get('shopify', [])[:30],
                'cache': system_monitor['logs'].get('cache', [])[:30],
                'scheduler': system_monitor['logs'].get('scheduler', [])[:30]
            }
        })
        
    except Exception as e:
        import traceback
        traceback.print_exc()
        return jsonify({'status': 'error', 'message': str(e)}), 500

@app.route('/api/system-monitor/log', methods=['POST'])
def add_monitor_log():
    """Add a log entry from external sources"""
    try:
        data = request.get_json(silent=True) or {}
        log_type = data.get('type', 'INFO')
        message = data.get('message', '')
        terminal = data.get('terminal', 'main')
        
        add_system_log(log_type, message, terminal)
        return jsonify({'status': 'success'})
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500


# ==================== CACHE STATS API ====================

@app.route('/api/cache/stats')
def get_cache_stats():
    """Get comprehensive cache statistics"""
    try:
        from cache_manager import cache_manager
        stats = cache_manager.get_stats()
        
        # Log to system monitor
        add_system_log('CACHE', f"Cache stats: {stats['total_cache_hit_rate']}% hit rate, {stats['avg_response_ms']:.1f}ms avg", 'cache')
        
        return jsonify({
            'status': 'success',
            'stats': stats
        })
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500

@app.route('/api/cache/warm', methods=['POST'])
def warm_cache_endpoint():
    """Warm up the memory cache"""
    try:
        data = request.get_json(silent=True) or {}
        limit = data.get('limit', 2000)
        
        from cache_manager import warm_cache
        count = warm_cache(limit=limit)
        
        add_system_log('CACHE', f"Cache warmed: {count} items", 'cache')
        
        return jsonify({
            'status': 'success',
            'warmed_count': count
        })
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500

@app.route('/api/cache/clear', methods=['POST'])
def clear_cache_endpoint():
    """Clear memory caches"""
    try:
        from cache_manager import cache_manager
        cache_manager.clear_memory_cache()
        
        add_system_log('CACHE', "Memory cache cleared", 'cache')
        
        return jsonify({'status': 'success', 'message': 'Memory cache cleared'})
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
