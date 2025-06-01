import sqlite3
import pandas as pd
from datetime import datetime, timedelta

DB_PATH = r"D:\Projects\MarketNiti\data\nifty_stocks.db"
TABLE_NAME = "stock_data"

def get_stock_symbols_with_category(db_path=DB_PATH):
    """Fetch all unique stock symbols, names, and categories from the stock table."""
    conn = sqlite3.connect(db_path)
    symbols = pd.read_sql_query("SELECT symbol, name, category FROM stock", conn)
    conn.close()
    return symbols

def get_stock_data(symbol, db_path=DB_PATH):
    """Fetch daily stock data for a given symbol."""
    conn = sqlite3.connect(db_path)
    df = pd.read_sql_query(
        f"SELECT date, close FROM {TABLE_NAME} WHERE symbol = ? ORDER BY date ASC",
        conn, params=(symbol,)
    )
    conn.close()
    df['date'] = pd.to_datetime(df['date'])
    return df

def get_price_on_or_before(df, target_date):
    sub = df[df['date'] <= target_date]
    if sub.empty:
        return None
    return sub.iloc[-1]['close']

def calculate_performance(df, as_of_date=None):
    if df.empty:
        return None
    if as_of_date is None:
        as_of_date = df['date'].max()
    last_price = get_price_on_or_before(df, as_of_date)
    if last_price is None:
        return None

    result = {'Last': last_price}

    # 1-day difference
    prev_trading = df[df['date'] < as_of_date]
    if not prev_trading.empty:
        prev_date = prev_trading['date'].max()
        prev_price = get_price_on_or_before(df, prev_date)
        result['1d'] = ((last_price - prev_price) / prev_price) * 100 if prev_price else None
    else:
        result['1d'] = None

    # Month-to-date (MTD)
    mtd_start = as_of_date.replace(day=1)
    mtd_price = get_price_on_or_before(df, mtd_start)
    result['Mtd'] = ((last_price - mtd_price) / mtd_price) * 100 if mtd_price else None

    # Year-to-date (YTD)
    ytd_start = as_of_date.replace(month=1, day=1)
    ytd_price = get_price_on_or_before(df, ytd_start)
    result['Ytd'] = ((last_price - ytd_price) / ytd_price) * 100 if ytd_price else None

    # Yearly changes
    for years in [1, 2, 5, 10, 20]:
        try:
            past_date = as_of_date.replace(year=as_of_date.year - years)
        except ValueError:
            past_date = as_of_date - timedelta(days=365 * years)
        past_price = get_price_on_or_before(df, past_date)
        result[f'{years}y'] = ((last_price - past_price) / past_price) * 100 if past_price else None

    return result

def prepare_performance_summary(db_path=DB_PATH):
    symbols_df = get_stock_symbols_with_category(db_path)
    summary = []
    for _, row in symbols_df.iterrows():
        symbol = row['symbol']
        company_name = row['name']
        category = row['category']
        try:
            df = get_stock_data(symbol, db_path)
            perf = calculate_performance(df)
            if perf is None:
                continue
            perf_row = {'Company': company_name, 'Category': category}
            perf_row.update(perf)
            summary.append(perf_row)
        except Exception as e:
            print(f"Error processing {company_name} ({symbol}): {e}")
            continue
    columns = ['Company', 'Category', 'Last', 'Mtd', 'Ytd', '1d', '1y', '2y', '5y', '10y', '20y']
    return pd.DataFrame(summary, columns=columns)

# Example usage:
df_summary = prepare_performance_summary()
print(df_summary)