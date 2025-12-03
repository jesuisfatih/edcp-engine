from ss_api_client import SSActivewearClient
from database import get_config
import requests
import base64
import json

config = get_config('ss_config')
print(f"Using account: {config['account_number'][:4]}...")

creds = base64.b64encode(f"{config['account_number']}:{config['api_key']}".encode()).decode()
headers = {'Authorization': f'Basic {creds}', 'Accept': 'application/json'}

# Get inventory API response
resp = requests.get('https://api.ssactivewear.com/v2/inventory/?style=2001', headers=headers)
items = resp.json()[:2]

print('\n=== INVENTORY API FIELDS ===')
if items:
    for k in sorted(items[0].keys()):
        print(f'  {k}: {str(items[0][k])[:80]}')

# Get products API response for comparison
resp2 = requests.get('https://api.ssactivewear.com/v2/products/?style=2001', headers=headers)
products = resp2.json()[:2]

print('\n=== PRODUCTS API FIELDS ===')
if products:
    for k in sorted(products[0].keys()):
        print(f'  {k}: {str(products[0][k])[:80]}')

