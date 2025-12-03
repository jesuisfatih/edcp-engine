from ss_api_client import SSActivewearClient
from database import get_config

config = get_config('ss_config')
client = SSActivewearClient(config['account_number'], config['api_key'])

# Try different approaches to find American Apparel 2001CVC
print("=== Searching for American Apparel 2001CVC ===")

# Approach 1: Search all products and filter
print("\nFetching products from American Apparel brand...")
products = client.get_products(limit=100)

# Find products with "2001" in style name
matches = [p for p in products if '2001' in str(p.get('styleName', ''))]
print(f"Found {len(matches)} products with '2001' in style name")

for p in matches[:10]:
    print(f"  Style ID: {p.get('styleID')}, Style: {p.get('styleName')}, Brand: {p.get('brandName')}")
    
# Also check the product search cache
print("\n=== Checking search cache ===")
import sqlite3
conn = sqlite3.connect('edcp.db')
cursor = conn.cursor()
cursor.execute("SELECT style_id, style_name, brand_name FROM product_search_cache WHERE style_name LIKE '%2001%' LIMIT 10")
rows = cursor.fetchall()
for row in rows:
    print(f"  Style ID: {row[0]}, Style: {row[1]}, Brand: {row[2]}")
conn.close()
