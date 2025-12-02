"""Helper method for ShopifyGateway - Delete all products"""

def delete_all_products(gateway) -> int:
    """
    Delete ALL products from Shopify
    Returns: number of products deleted
    """
    graphql_url = f"{gateway.shop_domain}/admin/api/{gateway.api_version}/graphql.json"
    
    deleted_count = 0
    
    try:
        # Get all products using GraphQL
        query = """
        query {
            products(first: 250) {
                edges {
                    node {
                        id
                    }
                }
            }
        }
        """
        
        resp = requests.post(graphql_url, headers=gateway.headers, json={'query': query}, timeout=30)
        
        if resp.status_code == 200:
            result = resp.json()
            products_edges = result.get('data', {}).get('products', {}).get('edges', [])
            
            for edge in products_edges:
                node = edge.get('node', {})
                product_gid = node.get('id', '')
                product_id = product_gid.replace('gid://shopify/Product/', '')
                
                if product_id:
                    delete_url = f"{gateway.base_url}/products/{product_id}.json"
                    del_resp = requests.delete(delete_url, headers=gateway.headers, timeout=30)
                    
                    if del_resp.status_code in [200, 204]:
                        deleted_count += 1
                    
                    time.sleep(0.2)
        
        return deleted_count
    except Exception as e:
        print(f"Error deleting products: {e}")
        return deleted_count

