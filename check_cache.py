import sqlite3
conn = sqlite3.connect('edcp.db')
cursor = conn.cursor()

# Check for 2001CVC
cursor.execute("SELECT style_id, style_name, brand_name FROM product_search_cache WHERE style_name = '2001CVC' LIMIT 1")
row = cursor.fetchone()
print('2001CVC result:', row)

# Check for similar
cursor.execute("SELECT style_id, style_name, brand_name FROM product_search_cache WHERE style_name LIKE '%2001%' LIMIT 5")
rows = cursor.fetchall()
print('\nSimilar styles:')
for r in rows:
    print(f"  {r}")

# Now test with style ID 10485
cursor.execute("SELECT COUNT(*) FROM warehouse_stock_cache WHERE style_id = '10485'")
count = cursor.fetchone()[0]
print(f'\nWarehouse stock cache for style 10485: {count} records')

conn.close()
