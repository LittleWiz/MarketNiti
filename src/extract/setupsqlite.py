import sqlite3
import os
import sys

# Define the database path (store in ../data/nifty_stocks.db)
project_root = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
db_dir = os.path.join(project_root, "data")
os.makedirs(db_dir, exist_ok=True)
db_path = os.path.join(db_dir, "nifty_stocks.db")

try:
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

    # Explicitly check if the database file was created
    if os.path.exists(db_path):
        print(f"SQLite database and tables created at: {db_path}")
    else:
        print(f"Error: Database file was not created at: {db_path}", file=sys.stderr)
except Exception as e:
    print(f"An error occurred while setting up the SQLite database: {e}", file=sys.stderr)
    sys.exit(1)