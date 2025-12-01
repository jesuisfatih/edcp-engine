"""
Data Fetcher - Fetches products from S&S API and stores in local database
"""
from ss_api_client import SSActivewearClient
from database import get_db
import json
import uuid
from typing import List, Dict, Optional
from datetime import datetime

class DataFetcher:
    """Fetches and caches S&S Activewear products in local database"""
    
    def __init__(self, ss_client: SSActivewearClient, sync_id: str):
        self.ss_client = ss_client
        self.sync_id = sync_id
    
    def fetch_and_cache_products(self, filter_options: Dict) -> int:
        """
        Fetch products from S&S API based on filters and cache in local DB
        Returns: number of products cached
        """
        print(f"📥 Starting data fetch with filters: {filter_options}")
        
        # Get products from S&S API
        products = self._get_products_to_sync(filter_options)
        
        if not products:
            print("⚠️ No products found with given filters")
            return 0
        
        print(f"📦 Fetched {len(products)} products from S&S API, caching to database...")
        
        # Cache products in database
        cached_count = 0
        with get_db() as conn:
            cursor = conn.cursor()
            
            for product in products:
                try:
                    # Store full product data as JSON
                    product_json = json.dumps(product)
                    
                    cursor.execute('''
                        INSERT OR REPLACE INTO ss_products_cache 
                        (sku, style_id, part_number, brand_name, style_name, color_name, size_name, 
                         product_data, sync_id, fetched_at)
                        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, CURRENT_TIMESTAMP)
                    ''', (
                        product.get('sku', ''),
                        product.get('styleID'),
                        product.get('partNumber', ''),
                        product.get('brandName', ''),
                        product.get('styleName', ''),
                        product.get('colorName', ''),
                        product.get('sizeName', ''),
                        product_json,
                        self.sync_id
                    ))
                    cached_count += 1
                    
                    if cached_count % 100 == 0:
                        print(f"   Cached {cached_count}/{len(products)} products...")
                        conn.commit()
                
                except Exception as e:
                    print(f"⚠️ Error caching product {product.get('sku', 'N/A')}: {e}")
                    continue
            
            conn.commit()
        
        print(f"✅ Cached {cached_count} products to database")
        return cached_count
    
    def _get_products_to_sync(self, filter_options: Dict) -> List[Dict]:
        """
        Get products from S&S API with filtering
        This is similar to SyncManager._get_products_to_sync but returns raw products
        """
        all_products = []
        
        # Get all products (with pagination)
        try:
            # Use API-level filtering if possible
            style_list = filter_options.get('filter_styles', [])
            if style_list and len(style_list) > 0:
                # Filter by style IDs using API
                for style_id in style_list:
                    try:
                        style_products = self.ss_client.get_products(styleid=str(style_id), limit=5000)
                        all_products.extend(style_products)
                    except Exception as e:
                        print(f"⚠️ Error fetching products for style {style_id}: {e}")
            else:
                # Fetch all products (with limit)
                all_products = self.ss_client.get_products(limit=5000)
        except Exception as e:
            print(f"❌ Error fetching products: {e}")
            return []
        
        # Apply filters
        filtered_products = []
        
        # Filter by categories
        category_list = filter_options.get('filter_categories', [])
        if category_list:
            category_list = [str(c) for c in category_list]  # Normalize to strings
            for product in all_products:
                product_categories = product.get('categories', '')
                if product_categories:
                    product_cat_list = [c.strip() for c in str(product_categories).split(',')]
                    if any(cat in product_cat_list for cat in category_list):
                        filtered_products.append(product)
                else:
                    # If no categories, skip if category filter is active
                    pass
        else:
            filtered_products = all_products
        
        # Filter by brands
        brand_list = filter_options.get('filter_brands', [])
        if brand_list:
            filtered_products = [
                p for p in filtered_products 
                if p.get('brandName', '').strip() in [b.strip() for b in brand_list]
            ]
        
        # Filter by part numbers
        part_number_list = filter_options.get('filter_part_numbers', [])
        if part_number_list:
            filtered_products = [
                p for p in filtered_products 
                if p.get('partNumber', '').strip() in [pn.strip() for pn in part_number_list]
            ]
        
        print(f"📊 Filtered products: {len(filtered_products)} from {len(all_products)} total")
        return filtered_products
    
    def get_cached_products(self) -> List[Dict]:
        """Get all cached products from database"""
        with get_db() as conn:
            cursor = conn.cursor()
            cursor.execute('''
                SELECT product_data FROM ss_products_cache 
                WHERE sync_id = ?
                ORDER BY style_id, sku
            ''', (self.sync_id,))
            
            products = []
            for row in cursor.fetchall():
                try:
                    product = json.loads(row['product_data'])
                    products.append(product)
                except Exception as e:
                    print(f"⚠️ Error loading cached product: {e}")
                    continue
            
            return products
    
    def clear_cache(self, sync_id: Optional[str] = None):
        """Clear cached products (optionally for a specific sync_id)"""
        with get_db() as conn:
            cursor = conn.cursor()
            if sync_id:
                cursor.execute('DELETE FROM ss_products_cache WHERE sync_id = ?', (sync_id,))
            else:
                cursor.execute('DELETE FROM ss_products_cache')
            conn.commit()
            print(f"🗑️ Cleared product cache for sync_id: {sync_id or 'all'}")

