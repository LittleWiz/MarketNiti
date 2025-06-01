import sqlite3
import os
import time
from datetime import datetime, timedelta
import yfinance as yf

# Helper to get DB path (reuse logic from db_utils.py)
def get_db_path():
    # Go up four levels to reach the project root
    project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
    db_dir = os.path.join(project_root, "data")
    os.makedirs(db_dir, exist_ok=True)  # Ensure the directory exists
    return os.path.join(db_dir, "nifty_stocks.db")

def get_all_symbols():
    db_path = get_db_path()
    conn = sqlite3.connect(db_path, timeout=30)
    cursor = conn.cursor()
    cursor.execute("SELECT symbol FROM stock")
    symbols = [row[0] for row in cursor.fetchall()]
    conn.close()
    return symbols

def get_last_date(symbol):
    db_path = get_db_path()
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT MAX(date) FROM stock_data WHERE symbol = ?", (symbol,))
    result = cursor.fetchone()
    conn.close()
    return result[0]  # Returns None if no data

def insert_stock_data(symbol, date, close):
    db_path = get_db_path()
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute(
        "INSERT OR IGNORE INTO stock_data (symbol, date, close) VALUES (?, ?, ?)",
        (symbol, date, close)
    )
    conn.commit()
    conn.close()

def fetch_and_update():
    symbols = get_all_symbols()
    for symbol in symbols:
        try:
            last_date = get_last_date(symbol)
            if last_date:
                # Start from the next day
                start_date = (datetime.strptime(last_date, "%Y-%m-%d") + timedelta(days=1)).strftime("%Y-%m-%d")
            else:
                # If no data, fetch last 20 years
                start_date = (datetime.now() - timedelta(days=365*20)).strftime("%Y-%m-%d")

            # Always fetch up to today, but yfinance will only return up to the last trading day
            data = yf.download(symbol, start=start_date, end=datetime.now().strftime("%Y-%m-%d"), interval="1d", progress=False)
            if data.empty:
                print(f"No new data for {symbol}")
                continue

            # Only insert rows with date > last_date
            for date, row in data.iterrows():
                close_date = date.strftime("%Y-%m-%d")
                if last_date is not None and close_date <= last_date:
                    continue  # Skip already present or duplicate dates
                close_price = float(row['Close'])
                insert_stock_data(symbol, close_date, close_price)
                print(f"Inserted {symbol} {close_date} {close_price}")
            else:
                # If no new rows were inserted, print up-to-date message
                if last_date is not None and all(date.strftime("%Y-%m-%d") <= last_date for date in data.index):
                    print(f"{symbol}: Already up to date.")
        except Exception as e:
            print(f"Error updating {symbol}: {e}")
        time.sleep(1)  # Be polite to Yahoo Finance

if __name__ == "__main__":
    project_root = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    db_dir = os.path.join(project_root, "data")
    db_path = os.path.join(db_dir, "nifty_stocks.db")
    fetch_and_update()