import sqlite3
import os

def get_db_path():
    """Return the path to the SQLite database."""
    db_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data")
    return os.path.join(db_dir, "nifty_stocks.db")

def get_all_table_names(db_path):
    """Return a list of all table names in the SQLite database."""
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = [row[0] for row in cursor.fetchall()]
    conn.close()
    return tables

def print_table_schema(db_path, table_name):
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
    table_names = get_all_table_names(db_path)
    if not table_names:
        print("No tables found in the database.")
    else:
        for table in table_names:
            print_table_schema(db_path, table)
            print()