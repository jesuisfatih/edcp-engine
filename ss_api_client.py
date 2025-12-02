import requests
from requests.auth import HTTPBasicAuth
from typing import List, Dict, Optional
import time

class SSActivewearClient:
    """Client for S&S Activewear REST API"""
    
    BASE_URL = "https://api.ssactivewear.com/v2"
    
    def __init__(self, account_number: str, api_key: str, proxy: Optional[Dict] = None):
        # Ensure account_number is string (some APIs require this)
        self.account_number = str(account_number).strip() if account_number else ""
        self.api_key = str(api_key).strip() if api_key else ""
        
        if not self.account_number or not self.api_key:
            raise ValueError("Account Number and API Key are required")
        
        self.auth = HTTPBasicAuth(self.account_number, self.api_key)
        self.session = requests.Session()
        self.session.auth = self.auth
        
        # Set proxy if provided (for regional restrictions)
        if proxy:
            self.session.proxies = {
                'http': proxy.get('http'),
                'https': proxy.get('https')
            }
        
        # Set user agent to avoid blocking
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        })
    
    def _make_request(self, endpoint: str, params: Optional[Dict] = None) -> List[Dict]:
        """Make API request with error handling"""
        url = f"{self.BASE_URL}/{endpoint.lstrip('/')}"
        
        try:
            response = self.session.get(url, params=params, timeout=120)  # Increased timeout for large requests
            
            # Provide more detailed error messages
            if response.status_code == 403:
                # Check if it's a regional/IP restriction
                error_details = ""
                try:
                    error_data = response.json()
                    if isinstance(error_data, dict):
                        error_details = error_data.get('message', '')
                except:
                    pass
                
                # Check response headers for clues
                cf_ray = response.headers.get('CF-Ray', '')
                server = response.headers.get('Server', '')
                
                regional_hint = ""
                if 'cloudflare' in server.lower() or cf_ray:
                    regional_hint = (
                        f"\n\n⚠️ BÖLGESEL KISITLAMA OLABİLİR:\n"
                        f"• IP adresiniz engellenmiş olabilir\n"
                        f"• Coğrafi kısıtlama olabilir\n"
                        f"• VPN veya proxy kullanmayı deneyin\n"
                        f"• api@ssactivewear.com'a IP adresinizi bildirin"
                    )
                
                raise Exception(
                    f"403 Forbidden - Authentication failed. Please check:\n"
                    f"1. Account Number is correct: {self.account_number[:3]}...\n"
                    f"2. API Key is correct and active\n"
                    f"3. API Key has not expired\n"
                    f"4. API Key has access to '{endpoint}' endpoint\n"
                    f"5. Contact api@ssactivewear.com if you need a new API key{regional_hint}"
                )
            elif response.status_code == 401:
                raise Exception(
                    f"401 Unauthorized - Invalid credentials. Please verify your Account Number and API Key."
                )
            elif response.status_code == 429:
                raise Exception(
                    f"429 Too Many Requests - Rate limit exceeded. Please wait and try again later."
                )
            
            response.raise_for_status()
            
            data = response.json()
            if isinstance(data, list):
                return data
            elif isinstance(data, dict):
                return [data]
            return []
        except requests.exceptions.HTTPError as e:
            if e.response.status_code == 403:
                # Check for regional restrictions
                cf_ray = e.response.headers.get('CF-Ray', '')
                server = e.response.headers.get('Server', '')
                
                regional_hint = ""
                if 'cloudflare' in server.lower() or cf_ray:
                    regional_hint = (
                        f"\n\n⚠️ BÖLGESEL KISITLAMA OLABİLİR:\n"
                        f"• IP adresiniz engellenmiş olabilir\n"
                        f"• Coğrafi kısıtlama olabilir\n"
                        f"• VPN veya proxy kullanmayı deneyin"
                    )
                
                raise Exception(
                    f"403 Forbidden - Authentication failed. Please check:\n"
                    f"1. Account Number: {self.account_number[:3]}... (first 3 digits shown)\n"
                    f"2. API Key is correct and active\n"
                    f"3. API Key has access to requested endpoint\n"
                    f"4. Contact api@ssactivewear.com for API key support{regional_hint}"
                )
            raise Exception(f"API request failed: {str(e)}")
        except requests.exceptions.RequestException as e:
            raise Exception(f"API request failed: {str(e)}")
    
    def test_endpoint_access(self) -> Dict:
        """Test access to different endpoints to identify restrictions"""
        results = {
            'categories': False,
            'brands': False,
            'styles': False,
            'products': False,
            'errors': {}
        }
        
        # Test Categories
        try:
            self.get_categories(limit=1)
            results['categories'] = True
        except Exception as e:
            results['errors']['categories'] = str(e)
        
        # Test Brands
        try:
            self.get_brands()
            results['brands'] = True
        except Exception as e:
            results['errors']['brands'] = str(e)
        
        # Test Styles
        try:
            self.get_styles(limit=1)
            results['styles'] = True
        except Exception as e:
            results['errors']['styles'] = str(e)
        
        # Test Products
        try:
            self.get_products(limit=1)
            results['products'] = True
        except Exception as e:
            results['errors']['products'] = str(e)
        
        return results
    
    def get_categories(self, category_ids: Optional[str] = None, 
                      fields: Optional[str] = None, limit: Optional[int] = None) -> List[Dict]:
        """Get categories"""
        params = {}
        if fields:
            params['fields'] = fields
        
        endpoint = "categories/"
        if category_ids:
            endpoint = f"categories/{category_ids}"
        
        categories = self._make_request(endpoint, params)
        
        if limit:
            categories = categories[:limit]
        
        return categories
    
    def get_brands(self, brand_ids: Optional[str] = None, 
                  mediatype: str = "json") -> List[Dict]:
        """Get brands"""
        params = {'mediatype': mediatype}
        
        endpoint = "Brands/"
        if brand_ids:
            endpoint = f"Brands/{brand_ids}"
        
        return self._make_request(endpoint, params)
    
    def get_styles(self, style_filter: Optional[str] = None,
                  search: Optional[str] = None,
                  styleid: Optional[str] = None,
                  partnumber: Optional[str] = None,
                  fields: Optional[str] = None,
                  limit: Optional[int] = None) -> List[Dict]:
        """Get styles"""
        params = {}
        
        if search:
            params['search'] = search
        if styleid:
            params['styleid'] = styleid
        if partnumber:
            params['partnumber'] = partnumber
        if fields:
            params['fields'] = fields
        
        endpoint = "styles/"
        if style_filter:
            endpoint = f"styles/{style_filter}"
        
        styles = self._make_request(endpoint, params)
        
        if limit:
            styles = styles[:limit]
        
        return styles

    def get_specs(self, style: Optional[str] = None,
                  specid: Optional[str] = None,
                  fields: Optional[str] = None,
                  limit: Optional[int] = None) -> List[Dict]:
        """Get specs for styles"""
        params = {}
        if style:
            params['style'] = style
        if specid:
            endpoint = f"specs/{specid}"
        else:
            endpoint = "specs/"
        if fields:
            params['fields'] = fields
        specs = self._make_request(endpoint, params)
        if limit:
            specs = specs[:limit]
        return specs
    
    def get_products(self, product_filter: Optional[str] = None,
                    style: Optional[str] = None,
                    styleid: Optional[str] = None,
                    partnumber: Optional[str] = None,
                    warehouses: Optional[str] = None,
                    fields: Optional[str] = None,
                    limit: Optional[int] = None,
                    offset: int = 0) -> List[Dict]:
        """Get products with pagination support"""
        params = {}
        
        if style:
            params['style'] = style
        if styleid:
            params['styleid'] = styleid
        if partnumber:
            params['partnumber'] = partnumber
        if warehouses:
            params['Warehouses'] = warehouses
        if fields:
            params['fields'] = fields
        
        endpoint = "products/"
        if product_filter:
            endpoint = f"products/{product_filter}"
        
        products = self._make_request(endpoint, params)
        
        # Apply pagination
        if offset:
            products = products[offset:]
        if limit:
            products = products[:limit]
        
        return products
    
    def get_inventory(self, product_filter: Optional[str] = None,
                     style: Optional[str] = None,
                     styleid: Optional[str] = None,
                     partnumber: Optional[str] = None,
                     warehouses: Optional[str] = None) -> List[Dict]:
        """Get inventory information"""
        params = {}
        
        if style:
            params['style'] = style
        if styleid:
            params['styleid'] = styleid
        if partnumber:
            params['partnumber'] = partnumber
        if warehouses:
            params['Warehouses'] = warehouses
        
        endpoint = "inventory/"
        if product_filter:
            endpoint = f"inventory/{product_filter}"
        
        return self._make_request(endpoint, params)
    
    def get_warehouses(self) -> List[Dict]:
        """
        Get list of all warehouses with inventory
        Returns: List of warehouse info with stock counts
        """
        try:
            # Get inventory summary by warehouse
            inventory = self.get_inventory()
            
            # Group by warehouse
            warehouse_stock = {}
            for item in inventory:
                warehouse = item.get('warehouse', 'Unknown')
                qty = item.get('qty', 0) or 0
                
                if warehouse not in warehouse_stock:
                    warehouse_stock[warehouse] = {
                        'code': warehouse,
                        'name': warehouse,
                        'total_stock': 0,
                        'product_count': 0
                    }
                
                warehouse_stock[warehouse]['total_stock'] += qty
                warehouse_stock[warehouse]['product_count'] += 1
            
            # Convert to list and sort by stock
            warehouses = sorted(
                warehouse_stock.values(),
                key=lambda x: x['total_stock'],
                reverse=True
            )
            
            return warehouses
        except:
            # Fallback: return common warehouses
            return [
                {'code': 'CA', 'name': 'California', 'total_stock': 0, 'product_count': 0},
                {'code': 'TX', 'name': 'Texas', 'total_stock': 0, 'product_count': 0},
                {'code': 'NY', 'name': 'New York', 'total_stock': 0, 'product_count': 0}
            ]
    
    def get_specs(self, spec_filter: Optional[str] = None,
                 style: Optional[str] = None,
                 fields: Optional[str] = None) -> List[Dict]:
        """Get product specifications"""
        params = {}
        
        if style:
            params['style'] = style
        if fields:
            params['fields'] = fields
        
        endpoint = "specs/"
        if spec_filter:
            endpoint = f"specs/{spec_filter}"
        
        return self._make_request(endpoint, params)
    
    def get_all_products(self, batch_size: int = 100, 
                        callback: Optional[callable] = None) -> List[Dict]:
        """Get all products in batches"""
        all_products = []
        offset = 0
        max_retries = 3
        retry_delay = 2
        
        while True:
            retries = 0
            batch = None
            
            while retries < max_retries:
                try:
                    batch = self.get_products(limit=batch_size, offset=offset)
                    break  # Success, exit retry loop
                except Exception as e:
                    error_msg = str(e)
                    if '403' in error_msg or 'Forbidden' in error_msg:
                        # Don't retry on authentication errors
                        raise Exception(
                            f"Authentication failed while fetching products (offset {offset}). "
                            f"Please verify your API credentials. Original error: {error_msg}"
                        )
                    elif '429' in error_msg or 'Too Many Requests' in error_msg:
                        # Rate limiting - wait longer and retry
                        retries += 1
                        if retries < max_retries:
                            wait_time = retry_delay * retries
                            time.sleep(wait_time)
                            continue
                        else:
                            raise Exception(f"Rate limit exceeded after {max_retries} retries")
                    else:
                        # Other errors - retry once
                        retries += 1
                        if retries < max_retries:
                            time.sleep(retry_delay)
                            continue
                        else:
                            raise
            
            if not batch:
                break
            
            all_products.extend(batch)
            
            if callback:
                callback(len(all_products), len(batch))
            
            if len(batch) < batch_size:
                break
            
            offset += batch_size
            time.sleep(0.5)  # Rate limiting
        
        return all_products
