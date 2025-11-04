import sqlite3


# Connect to SQLite database (creates one if not exists)
conn = sqlite3.connect("sales_data.db")

# Create a cursor to execute SQL commands
cursor = conn.cursor()

# Create a table named 'sales'
cursor.execute("""
CREATE TABLE IF NOT EXISTS sales (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product TEXT,
    quantity INTEGER,
    price REAL
);
""")

# Insert some sample data
sample_data = [
    ("Laptop", 5, 60000),
    ("Mouse", 15, 500),
    ("Keyboard", 10, 1500),
    ("Monitor", 7, 10000),
    ("Headphones", 12, 1200)
]

cursor.executemany("INSERT INTO sales (product, quantity, price) VALUES (?, ?, ?)", sample_data)

# Commit and close
conn.commit()
conn.close()

print("✅ Database and table created successfully with sample data!")

import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# Connect to the database
conn = sqlite3.connect("sales_data.db")

# SQL query to summarize total quantity and revenue by product
query = """
SELECT 
    product, 
    SUM(quantity) AS total_qty, 
    SUM(quantity * price) AS revenue
FROM sales
GROUP BY product;
"""

# Load data into a pandas DataFrame
df = pd.read_sql_query(query, conn)

# Close connection
conn.close()

# Print results
print("📊 Basic Sales Summary:")
print(df)

# Plot bar chart for revenue by product
df.plot(kind="bar", x="product", y="revenue", legend=False)
plt.title("Revenue by Product")
plt.xlabel("Product")
plt.ylabel("Revenue (₹)")
plt.tight_layout()
conn = sqlite3.connect("sales_data.db")
print("\n📦 Data stored in 'sales' table:")
print(conn.execute("SELECT * FROM sales").fetchall())
conn.close()
plt.show()

