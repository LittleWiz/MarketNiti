import sqlite3
import os

def get_db_path():
    """Return the path to the SQLite database."""
    db_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data")
    return os.path.join(db_dir, "nifty_stocks.db")

def check_table_exists(db_path, table_name="stock_data"):
    """Check if the specified table exists in the SQLite database."""
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute(
        "SELECT name FROM sqlite_master WHERE type='table' AND name=?;",
        (table_name,)
    )
    result = cursor.fetchone()
    conn.close()
    if result:
        print(f"Table '{table_name}' exists.")
        return True
    else:
        print(f"Table '{table_name}' does NOT exist.")
        return False

def print_table_schema(db_path, table_name="stock_data"):
    """Print the schema (columns) of the specified table."""
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute(f"PRAGMA table_info({table_name});")
    columns = cursor.fetchall()
    conn.close()
    if columns:
        print(f"Schema for table '{table_name}':")
        for col in columns:
            print(f"  {col[1]} ({col[2]})")
    else:
        print(f"No schema found for table '{table_name}'.")

if __name__ == "__main__":
    db_path = get_db_path()
    if check_table_exists(db_path):
        print_table_schema(db_path)