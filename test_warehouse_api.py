"""Test script to check S&S API warehouse data structure"""

from ss_api_client import SSActivewearClient
from database import get_config
import json

# Get credentials
ss_config = get_config('ss_config')
client = SSActivewearClient(
    ss_config['account_number'],
    ss_config['api_key']
)

# Fetch sample products
print("Fetching sample products...")
products = client.get_products(limit=10)

print(f"\nFound {len(products)} products")
print("\nSample product fields:")
if products:
    sample = products[0]
    for key in sample.keys():
        if 'warehouse' in key.lower() or 'location' in key.lower() or key == 'qty':
            print(f"  {key}: {sample.get(key)}")

print("\nAll keys:")
print(list(products[0].keys()) if products else "No products")

# Try warehouse filter
print("\n\nTesting warehouse filter...")
try:
    ca_products = client.get_products(warehouses="CA", limit=5)
    print(f"CA warehouse: {len(ca_products)} products")
except Exception as e:
    print(f"Error: {e}")

