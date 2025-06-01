import sqlite3
import os

def get_db_path():
    # Get the project root (parent of 'src')
    project_root = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    db_dir = os.path.join(project_root, "data")
    return os.path.join(db_dir, "nifty_stocks.db")

def insert_stock_data(stock_name, date, close):
    db_path = get_db_path()
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO stock_data (symbol, date, close) VALUES (?, ?, ?)",
        (stock_name, date, close)
    )
    conn.commit()
    conn.close()

insert_stock_data("TCS.NS", "2024-05-31", 3500.0)
