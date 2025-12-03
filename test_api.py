from ss_api_client import SSActivewearClient
from database import get_config

cfg = get_config('ss_config')
print("Config:", cfg)

client = SSActivewearClient(cfg['account_number'], cfg['api_key'])

# Test with style ID
try:
    print("Testing styleid=11987, warehouses=DS")
    result = client.get_products(styleid='11987', warehouses='DS', limit=5)
    print('Result count:', len(result) if result else 0)
    if result:
        print('First item:', result[0].get('sku'), result[0].get('styleName'))
except Exception as e:
    print('Error:', e)

# Test without warehouse filter
try:
    print("\nTesting styleid=11987 without warehouse filter")
    result = client.get_products(styleid='11987', limit=5)
    print('Result count:', len(result) if result else 0)
    if result:
        print('First item:', result[0].get('sku'), result[0].get('styleName'))
except Exception as e:
    print('Error:', e)

