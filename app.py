from flask import Flask, render_template, request, jsonify, session, redirect, url_for
import os
from dotenv import load_dotenv
from ss_api_client import SSActivewearClient
from shopify_client import ShopifyClient
from sync_manager import SyncManager
from scheduler import scheduler
from database import (init_database, save_config, get_config, get_all_config, save_sync_history, 
                      get_last_sync_id, get_sync_products, init_product_search_cache, 
                      get_search_cache_count, populate_search_cache, search_products_fts,
                      get_search_cache_last_update, clear_search_cache)
import threading
import json
import requests
from datetime import datetime

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY', 'your-secret-key-change-this')

# Initialize database on startup
try:
    init_database()
    init_product_search_cache()
    print("Database initialized successfully")
except Exception as e:
    print(f"Database initialization error: {e}")

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
        
        # Get products directly from S&S (no SyncManager needed)
        style_ids = sync_options.get('filter_styles', [])
        category_ids = sync_options.get('filter_categories', [])
        brand_names = sync_options.get('filter_brands', [])
        warehouse_codes = sync_options.get('filter_warehouses', [])
        
        # Build style ID parameter
        if style_ids:
            if isinstance(style_ids, list):
                style_param = ','.join(str(s) for s in style_ids if s)
            else:
                style_param = str(style_ids)
        else:
            style_param = None
        
        # Build warehouse parameter
        warehouse_param = ','.join(warehouse_codes) if warehouse_codes else None
        
        # Fetch products
        products = ss_client.get_products(
            styleid=style_param,
            warehouses=warehouse_param,
            limit=5000
        )
        
        # Filter by categories if specified
        if category_ids:
            cat_list = [str(c).strip() for c in category_ids if c]
            filtered = []
            for p in products:
                p_cats = str(p.get('categories', '')).split(',')
                p_cats = [c.strip() for c in p_cats if c.strip()]
                if any(cat in p_cats for cat in cat_list):
                    filtered.append(p)
            products = filtered
        
        # Filter by brands if specified
        if brand_names:
            brand_list = [str(b).strip() for b in brand_names if b]
            products = [p for p in products if p.get('brandName', '').strip() in brand_list]
        
        # Count unique styles
        unique_styles = set(p.get('styleID') for p in products if p.get('styleID'))
        
        response = jsonify({
            'status': 'success',
            'count': len(products),
            'style_count': len(unique_styles)
        })
        response.headers['Content-Length'] = str(len(response.get_data()))
        return response
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
        
        # Filter by brands
        if brand_list:
            filtered = []
            for product in products:
                product_brand = product.get('brandName', '').strip()
                if product_brand in brand_list:
                    filtered.append(product)
            products = filtered
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
    """Delete all products, collections from Shopify - DANGEROUS OPERATION"""
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
        
        if delete_products:
            try:
                # Get all products and delete them
                page_info = None
                page_count = 0
                while page_count < 100:  # Safety limit
                    url = f"{shopify_client.base_url}/products.json"
                    params = {'limit': 250}
                    if page_info:
                        params['page_info'] = page_info
                    
                    response = requests.get(url, headers=shopify_client.headers, params=params, timeout=30)
                    if response.status_code != 200:
                        break
                    
                    data = response.json()
                    products = data.get('products', [])
                    if not products:
                        break
                    
                    for product in products:
                        try:
                            shopify_client.delete_product(product['id'])
                            deleted_products += 1
                        except Exception as e:
                            errors.append(f"Error deleting product {product.get('title', 'Unknown')}: {str(e)}")
                    
                    # Check for next page
                    link_header = response.headers.get('Link', '')
                    if link_header and 'rel="next"' in link_header:
                        import re
                        match = re.search(r'page_info=([^>]+)', link_header)
                        if match:
                            page_info = match.group(1)
                        else:
                            break
                    else:
                        break
                    
                    page_count += 1
            except Exception as e:
                errors.append(f"Error fetching products: {str(e)}")
        
        if delete_collections:
            try:
                collections = shopify_client.get_collections()
                for collection in collections:
                    try:
                        shopify_client.delete_collection(collection['id'], collection.get('type', 'custom'))
                        deleted_collections += 1
                    except Exception as e:
                        errors.append(f"Error deleting collection {collection.get('title', 'Unknown')}: {str(e)}")
            except Exception as e:
                errors.append(f"Error fetching collections: {str(e)}")
        
        return jsonify({
            'status': 'success',
            'message': f'Deleted {deleted_products} products and {deleted_collections} collections',
            'deleted_products': deleted_products,
            'deleted_collections': deleted_collections,
            'errors': errors
        })
    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 400


@app.route('/api/search-products', methods=['POST'])
def search_products():
    """Fast product search using FTS5 cache"""
    try:
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
        
        return jsonify({
            'status': 'success',
            'total': total,
            'results': results,
            'hasMore': offset + limit < total,
            'cached': True
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


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
