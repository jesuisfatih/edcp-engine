import sqlite3

conn = sqlite3.connect('edcp.db')
cursor = conn.cursor()

# Get table schema
cursor.execute("SELECT sql FROM sqlite_master WHERE type='table' AND name='warehouse_stock_cache'")
row = cursor.fetchone()
if row:
    print('Schema:', row[0])
else:
    print('Table does not exist')

# List all columns
cursor.execute("PRAGMA table_info(warehouse_stock_cache)")
columns = cursor.fetchall()
print('\nColumns:')
for col in columns:
    print(f'  {col[1]} ({col[2]})')

# Get sample data
cursor.execute("SELECT * FROM warehouse_stock_cache LIMIT 1")
row = cursor.fetchone()
if row:
    print('\nSample row:')
    for i, col in enumerate(columns):
        print(f'  {col[1]}: {str(row[i])[:100]}')

conn.close()

