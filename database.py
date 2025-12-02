import sqlite3
import json
from typing import Optional, Dict, Any
from contextlib import contextmanager
import os

DB_PATH = 'edcp.db'

@contextmanager
def get_db():
    """Get database connection with context manager"""
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    try:
        yield conn
        conn.commit()
    except Exception:
        conn.rollback()
        raise
    finally:
        conn.close()

def init_database():
    """Initialize database with required tables"""
    with get_db() as conn:
        cursor = conn.cursor()
        
        # Configuration table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS config (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                key TEXT UNIQUE NOT NULL,
                value TEXT NOT NULL,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        
        # Sync history table
        cursor.execute('''
                CREATE TABLE IF NOT EXISTS sync_history (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    sync_id TEXT UNIQUE NOT NULL,
                    started_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    completed_at TIMESTAMP,
                    status TEXT,
                    total_products INTEGER,
                    created INTEGER,
                    updated INTEGER,
                    errors INTEGER,
                    message TEXT,
                    sync_options TEXT
                )
        ''')
        
        # Check if sync_id column exists, if not add it (for existing databases)
        try:
            cursor.execute("PRAGMA table_info(sync_history)")
            columns = [row[1] for row in cursor.fetchall()]
            if 'sync_id' not in columns:
                try:
                    cursor.execute('ALTER TABLE sync_history ADD COLUMN sync_id TEXT')
                    conn.commit()
                except Exception as e:
                    print(f"Warning: Could not add sync_id column: {e}")
        except Exception as e:
            print(f"Warning: Could not check sync_history columns: {e}")
        
        # Sync products table - track which products were created/updated
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS sync_products (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                sync_id TEXT NOT NULL,
                shopify_product_id INTEGER NOT NULL,
                shopify_variant_id INTEGER,
                sku TEXT NOT NULL,
                action TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                created_by_api INTEGER DEFAULT 1,
                FOREIGN KEY (sync_id) REFERENCES sync_history(sync_id)
            )
        ''')
        
        # Add created_by_api column if it doesn't exist (for existing databases)
        try:
            cursor.execute("PRAGMA table_info(sync_products)")
            columns = [row[1] for row in cursor.fetchall()]
            if 'created_by_api' not in columns:
                cursor.execute('ALTER TABLE sync_products ADD COLUMN created_by_api INTEGER DEFAULT 1')
                conn.commit()
        except Exception as e:
            print(f"Warning: Could not add created_by_api column: {e}")
        
        # NEW ARCHITECTURE: Products cache table - stores S&S products locally
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS ss_products_cache (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                sku TEXT UNIQUE NOT NULL,
                style_id INTEGER,
                part_number TEXT,
                brand_name TEXT,
                style_name TEXT,
                color_name TEXT,
                size_name TEXT,
                product_data TEXT NOT NULL,
                fetched_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                sync_id TEXT,
                FOREIGN KEY (sync_id) REFERENCES sync_history(sync_id)
            )
        ''')
        
        # ===== NEW ARCHITECTURE: Persistent Mapping Tables =====
        
        # Style to Shopify Product mapping (CRITICAL for idempotent sync)
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS style_shopify_products (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                style_id TEXT NOT NULL,
                part_index INTEGER DEFAULT 0,
                shopify_product_id INTEGER NOT NULL,
                shopify_handle TEXT,
                shopify_gid TEXT,
                variant_count INTEGER DEFAULT 0,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                last_synced_at TIMESTAMP,
                snapshot_hash TEXT,
                UNIQUE(style_id, part_index)
            )
        ''')
        
        # SKU to Shopify Variant mapping
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS sku_shopify_variants (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                sku TEXT UNIQUE NOT NULL,
                style_id TEXT NOT NULL,
                shopify_variant_id INTEGER NOT NULL,
                shopify_product_id INTEGER NOT NULL,
                shopify_gid TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        
        # Style snapshots for change detection
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS style_snapshots (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                style_id TEXT NOT NULL,
                snapshot_hash TEXT NOT NULL,
                variant_count INTEGER,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                snapshot_data TEXT
            )
        ''')
        
        # Variants table - grouped variants for Shopify products
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS product_variants (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                product_group_id TEXT NOT NULL,
                sku TEXT NOT NULL,
                color_name TEXT,
                size_name TEXT,
                price TEXT,
                inventory_quantity INTEGER,
                barcode TEXT,
                weight REAL,
                weight_unit TEXT,
                variant_image_url TEXT,
                variant_metafields TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                UNIQUE(product_group_id, sku)
            )
        ''')
        
        # Product groups table - groups variants by styleID
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS product_groups (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                group_id TEXT UNIQUE NOT NULL,
                style_id INTEGER,
                title TEXT NOT NULL,
                description TEXT,
                vendor TEXT,
                product_type TEXT,
                base_category TEXT,
                product_images TEXT,
                product_metafields TEXT,
                tags TEXT,
                collections TEXT,
                status TEXT DEFAULT 'pending',
                shopify_product_id INTEGER,
                sync_id TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                synced_at TIMESTAMP
            )
        ''')
        
        # Product images table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS product_images (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                product_group_id TEXT NOT NULL,
                image_url TEXT NOT NULL,
                image_type TEXT,
                variant_sku TEXT,
                sort_order INTEGER DEFAULT 0,
                FOREIGN KEY (product_group_id) REFERENCES product_groups(group_id)
            )
        ''')
        
        # Create indexes for faster lookups
        cursor.execute('CREATE INDEX IF NOT EXISTS idx_sync_products_sync_id ON sync_products(sync_id)')
        cursor.execute('CREATE INDEX IF NOT EXISTS idx_sync_products_sku ON sync_products(sku)')
        cursor.execute('CREATE INDEX IF NOT EXISTS idx_sync_history_sync_id ON sync_history(sync_id)')
        cursor.execute('CREATE INDEX IF NOT EXISTS idx_ss_products_cache_sku ON ss_products_cache(sku)')
        cursor.execute('CREATE INDEX IF NOT EXISTS idx_ss_products_cache_style_id ON ss_products_cache(style_id)')
        cursor.execute('CREATE INDEX IF NOT EXISTS idx_product_variants_group_id ON product_variants(product_group_id)')
        cursor.execute('CREATE INDEX IF NOT EXISTS idx_product_groups_group_id ON product_groups(group_id)')
        cursor.execute('CREATE INDEX IF NOT EXISTS idx_product_groups_style_id ON product_groups(style_id)')
        cursor.execute('CREATE INDEX IF NOT EXISTS idx_product_images_group_id ON product_images(product_group_id)')
        
        conn.commit()

def save_config(key: str, value: Any):
    """Save configuration to database"""
    with get_db() as conn:
        cursor = conn.cursor()
        value_json = json.dumps(value) if not isinstance(value, str) else value
        cursor.execute('''
            INSERT OR REPLACE INTO config (key, value, updated_at)
            VALUES (?, ?, CURRENT_TIMESTAMP)
        ''', (key, value_json))
        conn.commit()

def get_config(key: str, default: Any = None) -> Any:
    """Get configuration from database"""
    with get_db() as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT value FROM config WHERE key = ?', (key,))
        row = cursor.fetchone()
        if row:
            try:
                return json.loads(row['value'])
            except:
                return row['value']
        return default

def get_all_config() -> Dict[str, Any]:
    """Get all configuration"""
    with get_db() as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT key, value FROM config')
        rows = cursor.fetchall()
        config = {}
        for row in rows:
            try:
                config[row['key']] = json.loads(row['value'])
            except:
                config[row['key']] = row['value']
        return config

def save_sync_history(sync_id: str, status: str, total: int, created: int, updated: int, errors: int, message: str, sync_options: dict = None):
    """Save sync history"""
    with get_db() as conn:
        cursor = conn.cursor()
        # Update sync_state table if exists
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS sync_history (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                sync_id TEXT UNIQUE,
                started_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                completed_at TIMESTAMP,
                status TEXT,
                total_products INTEGER,
                created INTEGER,
                updated INTEGER,
                errors INTEGER,
                message TEXT,
                sync_options TEXT
            )
        ''')
        cursor.execute('''
            INSERT OR REPLACE INTO sync_history (sync_id, status, total_products, created, updated, errors, message, sync_options, completed_at)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, CURRENT_TIMESTAMP)
        ''', (sync_id, status, total, created, updated, errors, message, json.dumps(sync_options or {})))
        conn.commit()

def save_sync_product(sync_id: str, shopify_product_id: int, shopify_variant_id: int, sku: str, action: str, created_by_api: int = 1):
    """Save individual product sync record"""
    with get_db() as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS sync_products (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                sync_id TEXT NOT NULL,
                shopify_product_id INTEGER NOT NULL,
                shopify_variant_id INTEGER,
                sku TEXT NOT NULL,
                action TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                created_by_api INTEGER DEFAULT 1
            )
        ''')
        cursor.execute('''
            INSERT INTO sync_products (sync_id, shopify_product_id, shopify_variant_id, sku, action, created_by_api)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (sync_id, shopify_product_id, shopify_variant_id, sku, action, created_by_api))
        conn.commit()

def get_last_sync_id():
    """Get the last sync ID"""
    with get_db() as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT sync_id FROM sync_history ORDER BY started_at DESC LIMIT 1')
        row = cursor.fetchone()
        return row['sync_id'] if row else None

def get_sync_products(sync_id: str):
    """Get all products from a sync"""
    with get_db() as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM sync_products WHERE sync_id = ?', (sync_id,))
        products = []
        for row in cursor.fetchall():
            product_dict = dict(row)
            # Ensure created_by_api exists (default to 1 for backward compatibility)
            if 'created_by_api' not in product_dict:
                product_dict['created_by_api'] = 1
            products.append(product_dict)
        return products

def get_sync_products_for_sync(sync_id: str):
    """Get all products from a sync (alias for get_sync_products)"""
    return get_sync_products(sync_id)

def save_sync_state(sync_id: str, status: str, progress: int, current_index: int, total: int, stats: dict, sync_options: dict = None):
    """Save current sync state for resuming"""
    with get_db() as conn:
        cursor = conn.cursor()
        # Create sync_state table if not exists
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS sync_state (
                sync_id TEXT PRIMARY KEY,
                status TEXT,
                progress INTEGER,
                current_index INTEGER,
                total INTEGER,
                stats TEXT,
                sync_options TEXT,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        cursor.execute('''
            INSERT OR REPLACE INTO sync_state (sync_id, status, progress, current_index, total, stats, sync_options, updated_at)
            VALUES (?, ?, ?, ?, ?, ?, ?, CURRENT_TIMESTAMP)
        ''', (sync_id, status, progress, current_index, total, json.dumps(stats), json.dumps(sync_options or {})))
        conn.commit()

def get_sync_state(sync_id: str):
    """Get saved sync state"""
    with get_db() as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM sync_state WHERE sync_id = ?', (sync_id,))
        row = cursor.fetchone()
        if row:
            return {
                'sync_id': row['sync_id'],
                'status': row['status'],
                'progress': row['progress'],
                'current_index': row['current_index'],
                'total': row['total'],
                'stats': json.loads(row['stats']) if row['stats'] else {},
                'sync_options': json.loads(row['sync_options']) if row['sync_options'] else {}
            }
        return None


# ==================== PRODUCT SEARCH CACHE (FTS5) ====================

def init_product_search_cache():
    """Initialize FTS5 virtual table for fast product search"""
    with get_db() as conn:
        cursor = conn.cursor()
        
        # Main products table for search
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS product_search_cache (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                style_id TEXT UNIQUE NOT NULL,
                style_name TEXT,
                brand_name TEXT,
                title TEXT,
                base_price REAL,
                image_url TEXT,
                variant_count INTEGER DEFAULT 0,
                color_count INTEGER DEFAULT 0,
                size_count INTEGER DEFAULT 0,
                colors TEXT,
                sizes TEXT,
                product_data TEXT,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        
        # FTS5 virtual table for fast full-text search
        cursor.execute('''
            CREATE VIRTUAL TABLE IF NOT EXISTS product_search_fts USING fts5(
                style_id,
                style_name,
                brand_name,
                title,
                colors,
                content='product_search_cache',
                content_rowid='id'
            )
        ''')
        
        # Triggers to keep FTS in sync
        cursor.execute('''
            CREATE TRIGGER IF NOT EXISTS product_search_ai AFTER INSERT ON product_search_cache BEGIN
                INSERT INTO product_search_fts(rowid, style_id, style_name, brand_name, title, colors)
                VALUES (new.id, new.style_id, new.style_name, new.brand_name, new.title, new.colors);
            END
        ''')
        
        cursor.execute('''
            CREATE TRIGGER IF NOT EXISTS product_search_ad AFTER DELETE ON product_search_cache BEGIN
                INSERT INTO product_search_fts(product_search_fts, rowid, style_id, style_name, brand_name, title, colors)
                VALUES ('delete', old.id, old.style_id, old.style_name, old.brand_name, old.title, old.colors);
            END
        ''')
        
        cursor.execute('''
            CREATE TRIGGER IF NOT EXISTS product_search_au AFTER UPDATE ON product_search_cache BEGIN
                INSERT INTO product_search_fts(product_search_fts, rowid, style_id, style_name, brand_name, title, colors)
                VALUES ('delete', old.id, old.style_id, old.style_name, old.brand_name, old.title, old.colors);
                INSERT INTO product_search_fts(rowid, style_id, style_name, brand_name, title, colors)
                VALUES (new.id, new.style_id, new.style_name, new.brand_name, new.title, new.colors);
            END
        ''')
        
        conn.commit()
        print("Product search cache initialized")


def get_search_cache_count():
    """Get number of products in search cache"""
    with get_db() as conn:
        cursor = conn.cursor()
        try:
            cursor.execute('SELECT COUNT(*) FROM product_search_cache')
            return cursor.fetchone()[0]
        except:
            return 0


def get_search_cache_last_update():
    """Get last update time of search cache"""
    with get_db() as conn:
        cursor = conn.cursor()
        try:
            cursor.execute('SELECT MAX(updated_at) FROM product_search_cache')
            result = cursor.fetchone()[0]
            return result
        except:
            return None


def populate_search_cache(products: list):
    """Populate search cache from S&S API products (grouped by style)"""
    with get_db() as conn:
        cursor = conn.cursor()
        
        # Group products by style
        styles_dict = {}
        for product in products:
            style_id = str(product.get('styleID') or product.get('style', 'unknown'))
            
            if style_id not in styles_dict:
                styles_dict[style_id] = {
                    'style_id': style_id,
                    'style_name': product.get('styleName', ''),
                    'brand_name': product.get('brandName', ''),
                    'title': product.get('title', product.get('styleName', '')),
                    'base_price': product.get('piecePrice') or product.get('customerPrice') or product.get('casePrice', 0),
                    'image_url': None,
                    'variants': [],
                    'colors': set(),
                    'sizes': set()
                }
                
                # Get primary image
                for img_field in ['colorFrontImage', 'colorSideImage', 'colorBackImage', 'styleImage']:
                    img_url = product.get(img_field)
                    if img_url:
                        if not img_url.startswith('http'):
                            img_url = f"https://www.ssactivewear.com/{img_url.lstrip('/')}"
                        styles_dict[style_id]['image_url'] = img_url
                        break
            
            styles_dict[style_id]['variants'].append(product)
            if product.get('colorName'):
                styles_dict[style_id]['colors'].add(product['colorName'])
            if product.get('sizeName'):
                styles_dict[style_id]['sizes'].add(product['sizeName'])
        
        # Insert into cache
        inserted = 0
        for style_id, data in styles_dict.items():
            try:
                colors_str = ', '.join(sorted(data['colors']))
                sizes_str = ', '.join(sorted(data['sizes']))
                
                cursor.execute('''
                    INSERT OR REPLACE INTO product_search_cache 
                    (style_id, style_name, brand_name, title, base_price, image_url, 
                     variant_count, color_count, size_count, colors, sizes, updated_at)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, CURRENT_TIMESTAMP)
                ''', (
                    style_id,
                    data['style_name'],
                    data['brand_name'],
                    data['title'],
                    data['base_price'],
                    data['image_url'],
                    len(data['variants']),
                    len(data['colors']),
                    len(data['sizes']),
                    colors_str,
                    sizes_str
                ))
                inserted += 1
            except Exception as e:
                print(f"Error inserting style {style_id}: {e}")
        
        conn.commit()
        return inserted


def search_products_fts(query: str, limit: int = 50, offset: int = 0):
    """Fast full-text search using FTS5"""
    with get_db() as conn:
        cursor = conn.cursor()
        
        # Escape special FTS characters and prepare query
        clean_query = query.replace('"', '').replace("'", "").strip()
        
        if not clean_query:
            return [], 0
        
        # Use FTS5 MATCH with prefix search
        fts_query = f'"{clean_query}"* OR {clean_query}*'
        
        try:
            # Count total matches
            cursor.execute('''
                SELECT COUNT(*) FROM product_search_cache c
                WHERE c.id IN (
                    SELECT rowid FROM product_search_fts WHERE product_search_fts MATCH ?
                )
            ''', (fts_query,))
            total = cursor.fetchone()[0]
            
            # Get matching products
            cursor.execute('''
                SELECT c.*, bm25(product_search_fts) as rank
                FROM product_search_cache c
                JOIN product_search_fts f ON c.id = f.rowid
                WHERE product_search_fts MATCH ?
                ORDER BY rank
                LIMIT ? OFFSET ?
            ''', (fts_query, limit, offset))
            
            results = []
            for row in cursor.fetchall():
                results.append({
                    'styleID': row['style_id'],
                    'styleName': row['style_name'],
                    'brandName': row['brand_name'],
                    'title': row['title'],
                    'basePrice': row['base_price'],
                    'image': row['image_url'],
                    'variantCount': row['variant_count'],
                    'colorCount': row['color_count'],
                    'sizeCount': row['size_count']
                })
            
            return results, total
            
        except Exception as e:
            print(f"FTS search error: {e}")
            # Fallback to LIKE search if FTS fails
            return search_products_like(query, limit, offset)


def search_products_like(query: str, limit: int = 50, offset: int = 0):
    """Fallback LIKE search (slower but always works)"""
    with get_db() as conn:
        cursor = conn.cursor()
        
        search_pattern = f'%{query}%'
        
        # Count total
        cursor.execute('''
            SELECT COUNT(*) FROM product_search_cache 
            WHERE style_id LIKE ? OR style_name LIKE ? OR brand_name LIKE ? 
                  OR title LIKE ? OR colors LIKE ?
        ''', (search_pattern,) * 5)
        total = cursor.fetchone()[0]
        
        # Get results
        cursor.execute('''
            SELECT * FROM product_search_cache 
            WHERE style_id LIKE ? OR style_name LIKE ? OR brand_name LIKE ? 
                  OR title LIKE ? OR colors LIKE ?
            ORDER BY 
                CASE 
                    WHEN style_name LIKE ? THEN 1
                    WHEN title LIKE ? THEN 2
                    ELSE 3
                END
            LIMIT ? OFFSET ?
        ''', (search_pattern,) * 5 + (f'{query}%', f'{query}%', limit, offset))
        
        results = []
        for row in cursor.fetchall():
            results.append({
                'styleID': row['style_id'],
                'styleName': row['style_name'],
                'brandName': row['brand_name'],
                'title': row['title'],
                'basePrice': row['base_price'],
                'image': row['image_url'],
                'variantCount': row['variant_count'],
                'colorCount': row['color_count'],
                'sizeCount': row['size_count']
            })
        
        return results, total


def clear_search_cache():
    """Clear the product search cache"""
    with get_db() as conn:
        cursor = conn.cursor()
        cursor.execute('DELETE FROM product_search_cache')
        conn.commit()
