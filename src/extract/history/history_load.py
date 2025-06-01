import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from stock_list import get_nifty_symbols
from db_utils import insert_stock_data

import yfinance as yf
import time
from datetime import datetime, timedelta

START_DATE = (datetime.now() - timedelta(days=365*20)).strftime("%Y-%m-%d")
END_DATE = datetime.now().strftime("%Y-%m-%d")
TIMEOUT_BETWEEN_REQUESTS = 2  # seconds

def fetch_and_store():
    symbols = get_nifty_symbols()
    total_stocks = len(symbols)
    print(f"Total stocks to fetch: {total_stocks}")
    estimated_time_sec = total_stocks * TIMEOUT_BETWEEN_REQUESTS
    print(f"Estimated minimum time (with {TIMEOUT_BETWEEN_REQUESTS}s delay per stock): "
          f"{estimated_time_sec // 60} min {estimated_time_sec % 60} sec (not including download time)")
    start_time = time.time()
    for idx, symbol in enumerate(symbols, 1):
        print(f"[{idx}/{total_stocks}] Fetching {symbol}...")
        try:
            data = yf.download(symbol, start=START_DATE, end=END_DATE, progress=False)
            if data.empty:
                print(f"No data for {symbol}")
                continue
            for date, row in data.iterrows():
                insert_stock_data(symbol, date.strftime("%Y-%m-%d"), float(row['Close']))
            print(f"Stored data for {symbol}")
        except Exception as e:
            print(f"Error fetching {symbol}: {e}")
        time.sleep(TIMEOUT_BETWEEN_REQUESTS)
        elapsed = time.time() - start_time
        remaining = ((total_stocks - idx) * TIMEOUT_BETWEEN_REQUESTS) + (total_stocks - idx) * (elapsed / idx)
        print(f"Elapsed: {int(elapsed // 60)}m {int(elapsed % 60)}s | "
              f"Approx. remaining: {int(remaining // 60)}m {int(remaining % 60)}s")
    print("All stocks processed.")

if __name__ == "__main__":
    fetch_and_store()