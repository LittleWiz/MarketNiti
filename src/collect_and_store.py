import yfinance as yf
import time
from datetime import datetime, timedelta
from stock_list import get_nifty_symbols
from db_utils import insert_stock_data

START_DATE = (datetime.now() - timedelta(days=365*1)).strftime("%Y-%m-%d")
END_DATE = datetime.now().strftime("%Y-%m-%d")
TIMEOUT_BETWEEN_REQUESTS = 2  # seconds

def fetch_and_store():
    symbols = get_nifty_symbols()
    for symbol in symbols:
        print(f"Fetching {symbol}...")
        try:
            data = yf.download(symbol, start=START_DATE, end=END_DATE, progress=False)
            if data.empty:
                print(f"No data for {symbol}")
                continue
            for date, row in data.iterrows():
                # Use 'Close' column for close price
                insert_stock_data(symbol, date.strftime("%Y-%m-%d"), float(row['Close']))
            print(f"Stored data for {symbol}")
        except Exception as e:
            print(f"Error fetching {symbol}: {e}")
        time.sleep(TIMEOUT_BETWEEN_REQUESTS)

if __name__ == "__main__":
    fetch_and_store()