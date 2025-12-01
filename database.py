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

