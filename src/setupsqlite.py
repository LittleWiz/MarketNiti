import sqlite3
import os

# Define the database path (store in ../data/nifty_stocks.db)
db_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data")
os.makedirs(db_dir, exist_ok=True)
db_path = os.path.join(db_dir, "nifty_stocks.db")

# Connect to the SQLite database (it will be created if it doesn't exist)
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Create the table for storing stock master data
cursor.execute("""
CREATE TABLE IF NOT EXISTS stock (
    symbol TEXT PRIMARY KEY,
    name TEXT,
    category TEXT
)
""")

# Create the table for storing daily stock data
cursor.execute("""
CREATE TABLE IF NOT EXISTS stock_data (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    symbol TEXT NOT NULL,
    date TEXT NOT NULL,
    close REAL,
    FOREIGN KEY(symbol) REFERENCES stock(symbol)
)
""")

conn.commit()
conn.close()
print(f"SQLite database and tables created at: {db_path}")