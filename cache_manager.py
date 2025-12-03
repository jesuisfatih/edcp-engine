"""
EDCP Cache Manager - High Performance Caching System

Bu modül tüm SKU/ürün sorgularını önbellek üzerinden yönetir.
3 katmanlı cache mimarisi:
1. In-Memory Cache (< 1ms) - En sık erişilen veriler
2. SQLite Cache (< 50ms) - Tüm ürün verileri
3. S&S API (2-10s) - Sadece cache miss durumunda

Performans hedefleri:
- %95+ cache hit oranı
- Ortalama yanıt süresi < 100ms
- Kullanıcı bekleme süresi minimize
"""

import threading
import time
import json
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Any, Tuple
from functools import lru_cache
from collections import OrderedDict
import sqlite3

# ============================================================================
# IN-MEMORY CACHE (Layer 1) - Ultra Fast
# ============================================================================

class LRUCache:
    """Thread-safe LRU Cache with TTL support"""
    
    def __init__(self, max_size: int = 10000, ttl_seconds: int = 300):
        self.max_size = max_size
        self.ttl_seconds = ttl_seconds
        self.cache: OrderedDict = OrderedDict()
        self.timestamps: Dict[str, float] = {}
        self.lock = threading.RLock()
        self.hits = 0
        self.misses = 0
    
    def get(self, key: str) -> Optional[Any]:
        with self.lock:
            if key not in self.cache:
                self.misses += 1
                return None
            
            # Check TTL
            if time.time() - self.timestamps[key] > self.ttl_seconds:
                del self.cache[key]
                del self.timestamps[key]
                self.misses += 1
                return None
            
            # Move to end (most recently used)
            self.cache.move_to_end(key)
            self.hits += 1
            return self.cache[key]
    
    def set(self, key: str, value: Any):
        with self.lock:
            if key in self.cache:
                self.cache.move_to_end(key)
            else:
                if len(self.cache) >= self.max_size:
                    # Remove oldest
                    oldest_key = next(iter(self.cache))
                    del self.cache[oldest_key]
                    del self.timestamps[oldest_key]
            
            self.cache[key] = value
            self.timestamps[key] = time.time()
    
    def delete(self, key: str):
        with self.lock:
            if key in self.cache:
                del self.cache[key]
                del self.timestamps[key]
    
    def clear(self):
        with self.lock:
            self.cache.clear()
            self.timestamps.clear()
    
    def get_stats(self) -> Dict:
        with self.lock:
            total = self.hits + self.misses
            hit_rate = (self.hits / total * 100) if total > 0 else 0
            return {
                'size': len(self.cache),
                'max_size': self.max_size,
                'hits': self.hits,
                'misses': self.misses,
                'hit_rate': round(hit_rate, 2),
                'ttl_seconds': self.ttl_seconds
            }


# ============================================================================
# UNIFIED CACHE MANAGER
# ============================================================================

class CacheManager:
    """
    Merkezi Cache Yöneticisi
    
    Tüm SKU/ürün sorguları bu sınıf üzerinden geçer.
    3 katmanlı cache sistemi ile maksimum performans sağlar.
    """
    
    _instance = None
    _lock = threading.Lock()
    
    def __new__(cls):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
                    cls._instance._initialized = False
        return cls._instance
    
    def __init__(self):
        if self._initialized:
            return
        
        # Layer 1: In-Memory Caches
        self.sku_cache = LRUCache(max_size=50000, ttl_seconds=600)  # 10 min TTL
        self.style_cache = LRUCache(max_size=5000, ttl_seconds=600)
        self.warehouse_cache = LRUCache(max_size=100000, ttl_seconds=300)  # 5 min TTL
        self.product_cache = LRUCache(max_size=10000, ttl_seconds=600)
        
        # Statistics
        self.stats = {
            'total_queries': 0,
            'memory_hits': 0,
            'sqlite_hits': 0,
            'api_calls': 0,
            'avg_response_ms': 0,
            'last_full_sync': None
        }
        self.stats_lock = threading.Lock()
        
        # Background sync state
        self.sync_in_progress = False
        self.last_sync_time = None
        
        self._initialized = True
        print("✅ CacheManager initialized with 3-layer caching")
    
    # ========================================================================
    # LAYER 1: Memory Cache Operations
    # ========================================================================
    
    def _memory_get_sku(self, sku: str) -> Optional[Dict]:
        """Get SKU from memory cache"""
        return self.sku_cache.get(f"sku:{sku}")
    
    def _memory_set_sku(self, sku: str, data: Dict):
        """Store SKU in memory cache"""
        self.sku_cache.set(f"sku:{sku}", data)
    
    def _memory_get_style(self, style_id: str) -> Optional[List[Dict]]:
        """Get style products from memory cache"""
        return self.style_cache.get(f"style:{style_id}")
    
    def _memory_set_style(self, style_id: str, data: List[Dict]):
        """Store style products in memory cache"""
        self.style_cache.set(f"style:{style_id}", data)
    
    def _memory_get_warehouse_stock(self, sku: str) -> Optional[Dict]:
        """Get warehouse stock from memory cache"""
        return self.warehouse_cache.get(f"wh:{sku}")
    
    def _memory_set_warehouse_stock(self, sku: str, data: Dict):
        """Store warehouse stock in memory cache"""
        self.warehouse_cache.set(f"wh:{sku}", data)
    
    # ========================================================================
    # LAYER 2: SQLite Cache Operations
    # ========================================================================
    
    def _sqlite_get_sku(self, sku: str) -> Optional[Dict]:
        """Get SKU from SQLite warehouse_stock_cache"""
        try:
            from database import get_db
            with get_db() as conn:
                cursor = conn.cursor()
                # SKU data is in warehouse_stock_cache, not product_search_cache
                cursor.execute('''
                    SELECT sku, style_id, color_name, size_name
                    FROM warehouse_stock_cache 
                    WHERE sku = ? LIMIT 1
                ''', (sku,))
                row = cursor.fetchone()
                if row:
                    return {
                        'sku': row['sku'],
                        'style_id': row['style_id'],
                        'color_name': row['color_name'],
                        'size_name': row['size_name']
                    }
        except Exception as e:
            print(f"SQLite SKU lookup error: {e}")
        return None
    
    def _sqlite_get_style(self, style_id: str) -> Optional[List[Dict]]:
        """Get style data from SQLite product_search_cache"""
        try:
            from database import get_db
            with get_db() as conn:
                cursor = conn.cursor()
                # product_search_cache stores style-level info, not individual products
                cursor.execute('''
                    SELECT style_id, style_name, brand_name, title, base_price, 
                           image_url, variant_count, color_count, size_count, colors, sizes
                    FROM product_search_cache 
                    WHERE style_id = ?
                ''', (style_id,))
                row = cursor.fetchone()
                if row:
                    return [{
                        'style_id': row['style_id'],
                        'style_name': row['style_name'],
                        'brand_name': row['brand_name'],
                        'title': row['title'],
                        'base_price': row['base_price'],
                        'image_url': row['image_url'],
                        'variant_count': row['variant_count'],
                        'color_count': row['color_count'],
                        'size_count': row['size_count'],
                        'colors': row['colors'],
                        'sizes': row['sizes']
                    }]
        except Exception as e:
            print(f"SQLite style lookup error: {e}")
        return None
    
    def _sqlite_get_warehouse_stock(self, sku: str) -> Optional[Dict]:
        """Get warehouse stock from SQLite"""
        try:
            from database import get_db
            with get_db() as conn:
                cursor = conn.cursor()
                cursor.execute('''
                    SELECT sku, style_id, color_name, size_name, 
                           warehouse_code, warehouse_name, quantity, price
                    FROM warehouse_stock_cache 
                    WHERE sku = ?
                ''', (sku,))
                rows = cursor.fetchall()
                if rows:
                    warehouses = []
                    for row in rows:
                        warehouses.append({
                            'code': row['warehouse_code'],
                            'name': row['warehouse_name'],
                            'qty': row['quantity'],
                            'price': row['price']
                        })
                    return {
                        'sku': sku,
                        'style_id': rows[0]['style_id'],
                        'color_name': rows[0]['color_name'],
                        'size_name': rows[0]['size_name'],
                        'warehouses': warehouses
                    }
        except Exception as e:
            print(f"SQLite warehouse lookup error: {e}")
        return None
    
    def _sqlite_search_products(self, query: str, limit: int = 50, offset: int = 0) -> tuple:
        """Full-text search in SQLite cache - returns (results, total)"""
        try:
            from database import search_products_fts
            return search_products_fts(query, limit, offset)
        except Exception as e:
            print(f"SQLite search error: {e}")
            return [], 0
    
    # ========================================================================
    # LAYER 3: S&S API Operations (Fallback)
    # ========================================================================
    
    def _api_get_sku(self, sku: str) -> Optional[Dict]:
        """Fetch SKU from S&S API"""
        try:
            from database import get_config
            ss_config = get_config('ss_config') or {}
            if not ss_config.get('account_number') or not ss_config.get('api_key'):
                return None
            
            from ss_api_client import SSActivewearClient
            client = SSActivewearClient(
                account_number=ss_config['account_number'],
                api_key=ss_config['api_key']
            )
            
            products = client.get_products(partnumber=sku)
            if products:
                return products[0]
        except Exception as e:
            print(f"API SKU lookup error: {e}")
        return None
    
    def _api_get_style(self, style_id: str) -> Optional[List[Dict]]:
        """Fetch style products from S&S API"""
        try:
            from database import get_config
            ss_config = get_config('ss_config') or {}
            if not ss_config.get('account_number') or not ss_config.get('api_key'):
                return None
            
            from ss_api_client import SSActivewearClient
            client = SSActivewearClient(
                account_number=ss_config['account_number'],
                api_key=ss_config['api_key']
            )
            
            products = client.get_products(styleid=style_id)
            return products if products else None
        except Exception as e:
            print(f"API style lookup error: {e}")
        return None
    
    def _fetch_style_from_api_and_cache(self, style_id: str) -> Dict[str, Dict]:
        """
        Fetch style products from S&S API and cache them
        Used as fallback when cache is empty
        
        Returns: {sku: {sku, style_id, color_name, size_name, warehouses}}
        """
        try:
            from database import get_config, update_warehouse_stock
            ss_config = get_config('ss_config') or {}
            if not ss_config.get('account_number') or not ss_config.get('api_key'):
                print("⚠️ S&S API credentials not configured")
                return {}
            
            from ss_api_client import SSActivewearClient
            client = SSActivewearClient(
                account_number=ss_config['account_number'],
                api_key=ss_config['api_key']
            )
            
            # Fetch all products for this style
            products = client.get_products(styleid=str(style_id))
            if not products:
                print(f"⚠️ No products found for style {style_id}")
                return {}
            
            print(f"📦 API returned {len(products)} products for style {style_id}")
            
            result = {}
            for item in products:
                sku = item.get('sku', '')
                if not sku:
                    continue
                
                warehouses = item.get('warehouses', [])
                price = item.get('customerPrice') or item.get('piecePrice') or 0
                color_name = item.get('colorName', '')
                size_name = item.get('sizeName', '')
                
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
                
                # Cache'e kaydet
                if warehouse_list:
                    try:
                        update_warehouse_stock(
                            sku=sku,
                            warehouse_data=warehouse_list,
                            style_id=str(style_id),
                            color_name=color_name,
                            size_name=size_name
                        )
                    except Exception as e:
                        print(f"⚠️ Error caching SKU {sku}: {e}")
                
                result[sku] = {
                    'sku': sku,
                    'style_id': str(style_id),
                    'color_name': color_name,
                    'size_name': size_name,
                    'warehouses': warehouse_list
                }
            
            print(f"✅ Cached {len(result)} SKUs for style {style_id}")
            return result
            
        except Exception as e:
            print(f"API fetch and cache error for style {style_id}: {e}")
            return {}
    
    # ========================================================================
    # UNIFIED QUERY METHODS (Cache-First)
    # ========================================================================
    
    def get_sku(self, sku: str, use_api_fallback: bool = True) -> Tuple[Optional[Dict], str]:
        """
        Get SKU data with 3-layer cache lookup
        
        Returns: (data, source) where source is 'memory', 'sqlite', 'api', or 'miss'
        """
        start_time = time.time()
        
        with self.stats_lock:
            self.stats['total_queries'] += 1
        
        # Layer 1: Memory Cache
        data = self._memory_get_sku(sku)
        if data:
            self._update_stats(start_time, 'memory')
            return data, 'memory'
        
        # Layer 2: SQLite Cache
        data = self._sqlite_get_sku(sku)
        if data:
            self._memory_set_sku(sku, data)  # Promote to memory
            self._update_stats(start_time, 'sqlite')
            return data, 'sqlite'
        
        # Layer 3: S&S API (if allowed)
        if use_api_fallback:
            data = self._api_get_sku(sku)
            if data:
                self._memory_set_sku(sku, data)
                self._update_stats(start_time, 'api')
                return data, 'api'
        
        self._update_stats(start_time, 'miss')
        return None, 'miss'
    
    def get_style(self, style_id: str, use_api_fallback: bool = True) -> Tuple[Optional[List[Dict]], str]:
        """
        Get all products for a style with 3-layer cache lookup
        
        Returns: (data, source) where source is 'memory', 'sqlite', 'api', or 'miss'
        """
        start_time = time.time()
        
        with self.stats_lock:
            self.stats['total_queries'] += 1
        
        # Layer 1: Memory Cache
        data = self._memory_get_style(style_id)
        if data:
            self._update_stats(start_time, 'memory')
            return data, 'memory'
        
        # Layer 2: SQLite Cache
        data = self._sqlite_get_style(style_id)
        if data:
            self._memory_set_style(style_id, data)  # Promote to memory
            self._update_stats(start_time, 'sqlite')
            return data, 'sqlite'
        
        # Layer 3: S&S API (if allowed)
        if use_api_fallback:
            data = self._api_get_style(style_id)
            if data:
                self._memory_set_style(style_id, data)
                self._update_stats(start_time, 'api')
                return data, 'api'
        
        self._update_stats(start_time, 'miss')
        return None, 'miss'
    
    def get_warehouse_stock(self, sku: str, use_api_fallback: bool = True) -> Tuple[Optional[Dict], str]:
        """
        Get warehouse stock for SKU with 3-layer cache lookup
        
        Returns: (data, source) where source is 'memory', 'sqlite', 'api', or 'miss'
        """
        start_time = time.time()
        
        with self.stats_lock:
            self.stats['total_queries'] += 1
        
        # Layer 1: Memory Cache
        data = self._memory_get_warehouse_stock(sku)
        if data:
            self._update_stats(start_time, 'memory')
            return data, 'memory'
        
        # Layer 2: SQLite Cache
        data = self._sqlite_get_warehouse_stock(sku)
        if data:
            self._memory_set_warehouse_stock(sku, data)  # Promote to memory
            self._update_stats(start_time, 'sqlite')
            return data, 'sqlite'
        
        # Layer 3: S&S API (if allowed) - fetch and cache
        if use_api_fallback:
            sku_data = self._api_get_sku(sku)
            if sku_data and sku_data.get('warehouses'):
                data = {
                    'sku': sku,
                    'style_id': str(sku_data.get('styleID', '')),
                    'color_name': sku_data.get('colorName', ''),
                    'size_name': sku_data.get('sizeName', ''),
                    'warehouses': [
                        {
                            'code': wh.get('warehouseAbbr', ''),
                            'name': wh.get('warehouseName', ''),
                            'qty': wh.get('qty', 0),
                            'price': sku_data.get('customerPrice', sku_data.get('piecePrice', 0))
                        }
                        for wh in sku_data.get('warehouses', [])
                    ]
                }
                self._memory_set_warehouse_stock(sku, data)
                
                # Also save to SQLite for persistence
                self._save_warehouse_stock_to_sqlite(data)
                
                self._update_stats(start_time, 'api')
                return data, 'api'
        
        self._update_stats(start_time, 'miss')
        return None, 'miss'
    
    def search_products(self, query: str, limit: int = 50, offset: int = 0) -> tuple:
        """
        Search products - uses SQLite FTS for speed
        
        Memory cache is not used for search as queries are too varied
        Returns: (results_list, total_count)
        """
        start_time = time.time()
        
        with self.stats_lock:
            self.stats['total_queries'] += 1
        
        results, total = self._sqlite_search_products(query, limit, offset)
        self._update_stats(start_time, 'sqlite' if results else 'miss')
        return results, total
    
    def get_warehouse_stock_by_style(self, style_id: str, use_api_fallback: bool = True) -> Dict[str, Dict]:
        """
        Get warehouse stock for all SKUs in a style
        WITH API FALLBACK if cache is empty
        
        Returns: {sku: {sku, style_id, color_name, size_name, warehouses}}
        """
        start_time = time.time()
        
        with self.stats_lock:
            self.stats['total_queries'] += 1
        
        try:
            from database import get_db
            with get_db() as conn:
                cursor = conn.cursor()
                cursor.execute('''
                    SELECT sku, style_id, color_name, size_name,
                           warehouse_code, warehouse_name, quantity, price
                    FROM warehouse_stock_cache
                    WHERE style_id = ?
                    ORDER BY sku
                ''', (str(style_id),))
                rows = cursor.fetchall()
                
                # Cache'de veri varsa döndür
                if rows:
                    # Group by SKU
                    result = {}
                    for row in rows:
                        sku = row['sku']
                        if sku not in result:
                            result[sku] = {
                                'sku': sku,
                                'style_id': row['style_id'],
                                'color_name': row['color_name'],
                                'size_name': row['size_name'],
                                'warehouses': []
                            }
                        result[sku]['warehouses'].append({
                            'code': row['warehouse_code'],
                            'name': row['warehouse_name'],
                            'qty': row['quantity'],
                            'price': row['price']
                        })
                    
                    self._update_stats(start_time, 'sqlite')
                    return result
                
                # Cache boş - API FALLBACK
                if use_api_fallback:
                    print(f"⚠️ Cache miss for style {style_id} - falling back to API")
                    result = self._fetch_style_from_api_and_cache(style_id)
                    if result:
                        self._update_stats(start_time, 'api')
                        return result
                
                self._update_stats(start_time, 'miss')
                return {}
                
        except Exception as e:
            print(f"Error getting warehouse stock by style: {e}")
            self._update_stats(start_time, 'miss')
            return {}
    
    # ========================================================================
    # BATCH OPERATIONS (for bulk queries)
    # ========================================================================
    
    def get_skus_batch(self, skus: List[str]) -> Dict[str, Dict]:
        """
        Batch get multiple SKUs - optimized for bulk operations
        
        Returns: {sku: data}
        """
        results = {}
        missing_skus = []
        
        # First pass: check memory cache
        for sku in skus:
            data = self._memory_get_sku(sku)
            if data:
                results[sku] = data
            else:
                missing_skus.append(sku)
        
        if not missing_skus:
            return results
        
        # Second pass: batch query SQLite
        try:
            from database import get_db
            with get_db() as conn:
                cursor = conn.cursor()
                placeholders = ','.join(['?' for _ in missing_skus])
                cursor.execute(f'''
                    SELECT sku, product_data FROM product_search_cache
                    WHERE sku IN ({placeholders})
                ''', missing_skus)
                
                for row in cursor.fetchall():
                    if row['product_data']:
                        data = json.loads(row['product_data'])
                        results[row['sku']] = data
                        self._memory_set_sku(row['sku'], data)
                        missing_skus.remove(row['sku'])
        except Exception as e:
            print(f"Batch SQLite lookup error: {e}")
        
        return results
    
    # ========================================================================
    # CACHE MANAGEMENT
    # ========================================================================
    
    def _save_warehouse_stock_to_sqlite(self, data: Dict):
        """Save warehouse stock to SQLite for persistence"""
        try:
            from database import update_warehouse_stock
            update_warehouse_stock(
                sku=data['sku'],
                warehouse_data=data['warehouses'],
                style_id=data.get('style_id'),
                color_name=data.get('color_name'),
                size_name=data.get('size_name')
            )
        except Exception as e:
            print(f"Error saving warehouse stock to SQLite: {e}")
    
    def _update_stats(self, start_time: float, source: str):
        """Update performance statistics"""
        elapsed_ms = (time.time() - start_time) * 1000
        
        with self.stats_lock:
            if source == 'memory':
                self.stats['memory_hits'] += 1
            elif source == 'sqlite':
                self.stats['sqlite_hits'] += 1
            elif source == 'api':
                self.stats['api_calls'] += 1
            
            # Update rolling average
            total = self.stats['total_queries']
            if total > 1:
                self.stats['avg_response_ms'] = (
                    (self.stats['avg_response_ms'] * (total - 1) + elapsed_ms) / total
                )
            else:
                self.stats['avg_response_ms'] = elapsed_ms
    
    def get_stats(self) -> Dict:
        """Get comprehensive cache statistics"""
        with self.stats_lock:
            total = self.stats['total_queries']
            memory_rate = (self.stats['memory_hits'] / total * 100) if total > 0 else 0
            sqlite_rate = (self.stats['sqlite_hits'] / total * 100) if total > 0 else 0
            api_rate = (self.stats['api_calls'] / total * 100) if total > 0 else 0
            cache_hit_rate = memory_rate + sqlite_rate
            
            return {
                'total_queries': total,
                'memory_hits': self.stats['memory_hits'],
                'sqlite_hits': self.stats['sqlite_hits'],
                'api_calls': self.stats['api_calls'],
                'memory_hit_rate': round(memory_rate, 2),
                'sqlite_hit_rate': round(sqlite_rate, 2),
                'api_rate': round(api_rate, 2),
                'total_cache_hit_rate': round(cache_hit_rate, 2),
                'avg_response_ms': round(self.stats['avg_response_ms'], 2),
                'last_full_sync': self.stats['last_full_sync'],
                'memory_caches': {
                    'sku': self.sku_cache.get_stats(),
                    'style': self.style_cache.get_stats(),
                    'warehouse': self.warehouse_cache.get_stats(),
                    'product': self.product_cache.get_stats()
                }
            }
    
    def warm_cache(self, style_ids: List[str] = None, limit: int = 1000):
        """
        Warm up memory cache from SQLite
        
        Called on server startup or after a full sync
        """
        print("🔥 Warming up memory cache...")
        start_time = time.time()
        warmed = 0
        
        try:
            from database import get_db
            with get_db() as conn:
                cursor = conn.cursor()
                
                # Warm style cache from product_search_cache
                try:
                    cursor.execute('''
                        SELECT style_id, style_name, brand_name, title, base_price, 
                               image_url, variant_count, color_count, size_count
                        FROM product_search_cache
                        ORDER BY ROWID DESC LIMIT ?
                    ''', (limit,))
                    
                    for row in cursor.fetchall():
                        style_data = {
                            'style_id': row['style_id'],
                            'style_name': row['style_name'],
                            'brand_name': row['brand_name'],
                            'title': row['title'],
                            'base_price': row['base_price'],
                            'image_url': row['image_url'],
                            'variant_count': row['variant_count']
                        }
                        self.product_cache.set(f"product:{row['style_id']}", style_data)
                        warmed += 1
                except Exception as e:
                    print(f"Style cache warming error: {e}")
                
                # Warm warehouse cache with most recently accessed SKUs
                try:
                    cursor.execute('''
                        SELECT DISTINCT sku FROM warehouse_stock_cache
                        ORDER BY ROWID DESC LIMIT ?
                    ''', (limit,))
                    
                    for row in cursor.fetchall():
                        sku = row['sku'] if isinstance(row, dict) else row[0]
                        data = self._sqlite_get_warehouse_stock(sku)
                        if data:
                            self._memory_set_warehouse_stock(sku, data)
                            warmed += 1
                except Exception as e:
                    print(f"Warehouse cache warming error: {e}")
        
        except Exception as e:
            print(f"Error warming cache: {e}")
        
        elapsed = time.time() - start_time
        print(f"✅ Cache warmed: {warmed} items in {elapsed:.2f}s")
        return warmed
    
    def clear_memory_cache(self):
        """Clear all memory caches"""
        self.sku_cache.clear()
        self.style_cache.clear()
        self.warehouse_cache.clear()
        self.product_cache.clear()
        print("🗑️ Memory caches cleared")
    
    def invalidate_sku(self, sku: str):
        """Invalidate a specific SKU from all caches"""
        self.sku_cache.delete(f"sku:{sku}")
        self.warehouse_cache.delete(f"wh:{sku}")
    
    def invalidate_style(self, style_id: str):
        """Invalidate a style from cache"""
        self.style_cache.delete(f"style:{style_id}")


# ============================================================================
# SINGLETON INSTANCE
# ============================================================================

# Global cache manager instance
cache_manager = CacheManager()


# ============================================================================
# CONVENIENCE FUNCTIONS
# ============================================================================

def get_sku_cached(sku: str, use_api: bool = True) -> Optional[Dict]:
    """Convenience function to get SKU with caching"""
    data, source = cache_manager.get_sku(sku, use_api)
    return data

def get_style_cached(style_id: str, use_api: bool = True) -> Optional[List[Dict]]:
    """Convenience function to get style products with caching"""
    data, source = cache_manager.get_style(style_id, use_api)
    return data

def get_warehouse_stock_cached(sku: str, use_api: bool = True) -> Optional[Dict]:
    """Convenience function to get warehouse stock with caching"""
    data, source = cache_manager.get_warehouse_stock(sku, use_api)
    return data

def search_products_cached(query: str, limit: int = 50, offset: int = 0) -> tuple:
    """Convenience function to search products - returns (results, total)"""
    return cache_manager.search_products(query, limit, offset)

def get_cache_stats() -> Dict:
    """Get cache statistics"""
    return cache_manager.get_stats()

def warm_cache(limit: int = 1000) -> int:
    """Warm up memory cache"""
    return cache_manager.warm_cache(limit=limit)

