import os
import sqlite3
from src.db_utils import get_db_path, insert_stock_data

def test_insert_and_retrieve_stock_data():
    db_path = get_db_path()
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    # Insert test row
    insert_stock_data("TESTSYM.NS", "2024-01-01", 123.45)
    # Retrieve test row
    cursor.execute("SELECT stock_name, date, close FROM stock_data WHERE stock_name = ?", ("TESTSYM.NS",))
    row = cursor.fetchone()
    assert row == ("TESTSYM.NS", "2024-01-01", 123.45)
    # Clean up
    cursor.execute("DELETE FROM stock_data WHERE stock_name = ?", ("TESTSYM.NS",))
    conn.commit()
    conn.close()