import sqlite3
import pandas as pd

# Database path
db_path = '/root/.openclaw/workspace/tgss.db'
excel_path = '/root/.openclaw/workspace/tgss.xlsx'

# Connect and get all tables
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Get all table names
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()

print(f"Tables found: {tables}")

# Export each table to Excel
with pd.ExcelWriter(excel_path, engine='openpyxl') as writer:
    for table in tables:
        table_name = table[0]
        print(f"Exporting: {table_name}")
        df = pd.read_sql_query(f"SELECT * FROM {table_name}", conn)
        df.to_excel(writer, sheet_name=table_name[:31], index=False)

conn.close()
print(f"Done! Saved to: {excel_path}")
