"""
Data Fetcher - Fetches products from S&S API and stores in local database
"""
from ss_api_client import SSActivewearClient
from database import get_db
import json
from typing import List, Dict, Optional
import time


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
        print(f"[fetch] Starting data fetch with filters: {filter_options}")

        # Get products from S&S API
        products = self._get_products_to_sync(filter_options)

        if not products:
            print("[fetch] No products found with given filters")
            return 0

        print(f"[fetch] Fetched {len(products)} products, caching to database...")

        # Enrich with style details
        style_ids = sorted({p.get("styleID") for p in products if p.get("styleID")})
        style_lookup = {}
        category_lookup = {}
        if style_ids:
            try:
                styleid_param = ",".join([str(sid) for sid in style_ids])
                styles = self.ss_client.get_styles(styleid=styleid_param, limit=None)
                for s in styles or []:
                    sid = s.get("styleID")
                    if sid is not None:
                        style_lookup[int(sid)] = s
                print(f"[fetch] Enriched styles fetched: {len(style_lookup)}")
            except Exception as e:
                print(f"[fetch] Warning: could not fetch style details: {e}")
        # Category lookup for human-friendly tags/collections
        try:
            categories = self.ss_client.get_categories()
            for c in categories or []:
                cid = c.get("categoryID")
                if cid is not None:
                    category_lookup[str(cid)] = c.get("name", "").strip()
            print(f"[fetch] Category lookup loaded: {len(category_lookup)}")
        except Exception as e:
            print(f"[fetch] Warning: could not fetch categories: {e}")

        def normalize_image(path: Optional[str]) -> Optional[str]:
            """Build full URL and prefer large size; return None if empty."""
            if not path:
                return None
            url = str(path).strip()
            if not url:
                return None
            full = url if url.startswith("http") else f"https://www.ssactivewear.com/{url.lstrip('/')}"
            return full.replace("_fm", "_fl")

        # Cache products in database
        cached_count = 0
        with get_db() as conn:
            cursor = conn.cursor()

            for product in products:
                try:
                    enriched = dict(product)

                    # Merge style-level fields
                    style_data = (
                        style_lookup.get(int(enriched.get("styleID")))
                        if enriched.get("styleID") is not None
                        else {}
                    )
                    if style_data:
                        for key in [
                            "description",
                            "baseCategory",
                            "categories",
                            "catalogPageNumber",
                            "sustainableStyle",
                            "styleImage",
                            "brandImage",
                        ]:
                            if style_data.get(key) is not None and (enriched.get(key) in (None, "", [])):
                                enriched[key] = style_data.get(key)

                    # Normalize images with fallback
                    front = normalize_image(enriched.get("colorFrontImage"))
                    side = normalize_image(enriched.get("colorSideImage"))
                    back = normalize_image(enriched.get("colorBackImage"))
                    if not front:
                        front = side or back
                    enriched["colorFrontImage"] = front
                    enriched["colorSideImage"] = side
                    enriched["colorBackImage"] = back
                    enriched["styleImage"] = normalize_image(enriched.get("styleImage"))

                    # Category names list for tags/collections
                    cat_names = []
                    cats_raw = enriched.get("categories")
                    if cats_raw:
                        if isinstance(cats_raw, list):
                            cat_ids = [str(c).strip() for c in cats_raw if str(c).strip()]
                        else:
                            cat_ids = [c.strip() for c in str(cats_raw).split(",") if c.strip()]
                        for cid in cat_ids:
                            name = category_lookup.get(str(cid))
                            if name:
                                cat_names.append(name)
                    if cat_names:
                        enriched["categoryNames"] = cat_names

                    # Store full product data as JSON
                    product_json = json.dumps(enriched)

                    cursor.execute(
                        """
                        INSERT OR REPLACE INTO ss_products_cache
                        (sku, style_id, part_number, brand_name, style_name, color_name, size_name,
                         product_data, sync_id, fetched_at)
                        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, CURRENT_TIMESTAMP)
                    """,
                        (
                            enriched.get("sku", ""),
                            enriched.get("styleID"),
                            enriched.get("partNumber", ""),
                            enriched.get("brandName", ""),
                            enriched.get("styleName", ""),
                            enriched.get("colorName", ""),
                            enriched.get("sizeName", ""),
                            product_json,
                            self.sync_id,
                        ),
                    )
                    cached_count += 1

                    if cached_count % 100 == 0:
                        print(f"[fetch] Cached {cached_count}/{len(products)} products...")
                        conn.commit()

                except Exception as e:
                    print(f"[fetch] Error caching product {product.get('sku', 'N/A')}: {e}")
                    continue

            conn.commit()

        print(f"[fetch] Cached {cached_count} products to database")
        return cached_count

    def _get_products_to_sync(self, filter_options: Dict) -> List[Dict]:
        """
        Get products from S&S API with filtering
        Uses the same logic as SyncManager._get_products_to_sync for consistency
        """
        # Normalize filters (same as sync_manager)
        category_ids = filter_options.get("filter_categories", [])
        if isinstance(category_ids, list):
            category_list = [str(cid).strip() for cid in category_ids if cid]
        elif isinstance(category_ids, str):
            category_list = [c.strip() for c in category_ids.split(",") if c.strip()]
        else:
            category_list = [str(category_ids).strip()] if category_ids else []

        style_ids = filter_options.get("filter_styles", [])
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
            for sid in style_ids.split(","):
                sid = sid.strip()
                if sid and sid.isdigit():
                    style_list.append(int(sid))
        else:
            style_list = [int(style_ids)] if style_ids and str(style_ids).isdigit() else []

        brand_filters = filter_options.get("filter_brands", [])
        brand_names = []
        if isinstance(brand_filters, list):
            for bf in brand_filters:
                bf_str = str(bf).strip()
                if bf_str and not bf_str.isdigit():
                    brand_names.append(bf_str)
        elif isinstance(brand_filters, str):
            brand_names = [b.strip() for b in brand_filters.split(",") if b.strip() and not b.strip().isdigit()]
        else:
            brand_names = [str(brand_filters).strip()] if brand_filters and not str(brand_filters).isdigit() else []

        print(f"=== DATA FETCHER FILTERING DEBUG ===")
        print(f"Categories: {category_list}")
        print(f"Styles: {style_list}")
        print(f"Brands: {brand_names}")

        all_products = []

        # CRITICAL: Use API-level filtering for styles (much more efficient)
        if style_list:
            print(f"Using API-level filtering for {len(style_list)} styles...")
            styleid_param = ",".join([str(sid) for sid in style_list])
            print(f"Fetching products with styleid={styleid_param}")

            try:
                products = self.ss_client.get_products(styleid=styleid_param, limit=5000)
                print(f"API returned {len(products)} products for selected styles")
                all_products = products
            except Exception as e:
                print(f"Error with styleid filter: {e}")
                # Fallback: get all and filter in memory
                print("Falling back to memory filtering...")
                products = self.ss_client.get_products(limit=5000)
                filtered = []
                for product in products:
                    product_style_id = product.get("styleID")
                    if product_style_id:
                        try:
                            if int(product_style_id) in style_list:
                                filtered.append(product)
                        except Exception:
                            pass
                all_products = filtered
                print(f"Memory filter found {len(all_products)} products")
        else:
            # No style filter, get all products
            print("No style filter, fetching all products...")
            all_products = self.ss_client.get_products(limit=5000)
            print(f"Fetched {len(all_products)} products")

        # CRITICAL FIX: If styles were selected, SKIP category filter
        if category_list and all_products:
            if style_list:
                print(f"SKIPPING category filter - already filtered by {len(style_list)} styles")
                print(f"  Selected categories: {category_list} (will be ignored)")
            else:
                # Only apply category filter if no style filter was used
                print(f"Filtering {len(all_products)} products by {len(category_list)} categories...")
                filtered = []
                for product in all_products:
                    product_cats = product.get("categories", "")
                    if product_cats:
                        if isinstance(product_cats, list):
                            product_cat_list = [str(c).strip() for c in product_cats if c]
                        else:
                            product_cat_list = [c.strip() for c in str(product_cats).split(",") if c.strip()]

                        matched = False
                        for cat in category_list:
                            cat_str = str(cat).strip()
                            if cat_str in product_cat_list:
                                matched = True
                                break
                            try:
                                if int(cat_str) in [int(c) for c in product_cat_list if c.isdigit()]:
                                    matched = True
                                    break
                            except Exception:
                                pass

                        if matched:
                            filtered.append(product)

                all_products = filtered
                print(f"After category filter: {len(all_products)} products")

        # Filter by brands if selected
        if brand_names and all_products:
            print(f"Filtering {len(all_products)} products by {len(brand_names)} brands...")
            filtered = []
            for product in all_products:
                product_brand = product.get("brandName", "").strip()
                if product_brand in brand_names:
                    filtered.append(product)
            all_products = filtered
            print(f"After brand filter: {len(all_products)} products")

        # Remove duplicates by SKU
        seen_skus = set()
        unique_products = []
        for product in all_products:
            sku = product.get("sku")
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
            if all_products:
                sample = all_products[0]
                print(f"  Sample product categories: {sample.get('categories')}")
                print(f"  Sample product styleID: {sample.get('styleID')}")
                print(f"  Sample product brand: {sample.get('brandName')}")

        return unique_products

    def get_cached_products(self) -> List[Dict]:
        """Get all cached products from database"""
        with get_db() as conn:
            cursor = conn.cursor()
            cursor.execute(
                """
                SELECT product_data FROM ss_products_cache
                WHERE sync_id = ?
                ORDER BY style_id, sku
            """,
                (self.sync_id,),
            )

            products = []
            for row in cursor.fetchall():
                try:
                    product = json.loads(row["product_data"])
                    products.append(product)
                except Exception as e:
                    print(f"?? Error loading cached product: {e}")
                    continue

            return products

    def clear_cache(self, sync_id: Optional[str] = None):
        """Clear cached products (optionally for a specific sync_id)"""
        with get_db() as conn:
            cursor = conn.cursor()
            if sync_id:
                cursor.execute("DELETE FROM ss_products_cache WHERE sync_id = ?", (sync_id,))
            else:
                cursor.execute("DELETE FROM ss_products_cache")
            conn.commit()
            print(f"??? Cleared product cache for sync_id: {sync_id or 'all'}")
