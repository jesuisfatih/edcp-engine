import sqlite3

# Test the style name lookup
conn = sqlite3.connect('/opt/edcp/edcp.db')
conn.row_factory = sqlite3.Row
cursor = conn.cursor()

style_id = "2001CVC"

print(f"Looking up style: {style_id}")
print(f"Is digit: {style_id.isdigit()}")

# Case-insensitive search
cursor.execute(
    "SELECT style_id FROM product_search_cache WHERE UPPER(style_name) = UPPER(?) LIMIT 1",
    (style_id,)
)
row = cursor.fetchone()

if row:
    print(f"Found! Style ID: {row['style_id']}")
else:
    print("Not found!")
    
    # Debug: show what's in the cache
    cursor.execute("SELECT style_id, style_name FROM product_search_cache WHERE style_name LIKE '%2001%' LIMIT 5")
    rows = cursor.fetchall()
    print("\nSimilar entries:")
    for r in rows:
        print(f"  {r['style_id']}: {r['style_name']}")

conn.close()

