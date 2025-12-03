import sqlite3
conn = sqlite3.connect("edcp.db")
c = conn.cursor()
# Check for products with multiple sizes
c.execute("""
SELECT style_id, color_name, COUNT(DISTINCT size_name) as size_count 
FROM warehouse_stock_cache 
WHERE color_name != '' 
GROUP BY style_id, color_name 
HAVING size_count > 1 
LIMIT 10
""")
print("Products with multiple sizes:")
for r in c.fetchall():
    print(r)

# Get sample with different sizes
c.execute("""
SELECT sku, color_name, size_name, warehouse_code, quantity 
FROM warehouse_stock_cache 
WHERE style_id = (
    SELECT style_id FROM warehouse_stock_cache 
    WHERE color_name != '' 
    GROUP BY style_id, color_name 
    HAVING COUNT(DISTINCT size_name) > 3 
    LIMIT 1
)
AND warehouse_code = 'NV'
LIMIT 20
""")
print("\nSample sizes with NV stock:")
for r in c.fetchall():
    print(r)
