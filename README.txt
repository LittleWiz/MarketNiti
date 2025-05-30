_____________________________________________________________________________________________
MARKET NITI
_____________________________________________________________________________________________

Requirements:
- Collect daily close price data for 150 NIFTY stocks over the last 10 years.
- Store the data in a SQLite database for further analysis.

Description:
Market Niti is a project focused on gathering, processing, and storing historical stock data for NIFTY index companies. The system fetches daily close prices using the yfinance package and stores them in a structured SQLite database. The project is designed to be extensible, allowing new stocks to be added easily.

Project Structure:
MarketNiti/
│
├── data/                  # Stores raw and processed data (CSV, DB files, etc.)
│   └── nifty_stocks.db    # SQLite database file
│
├── notebooks/             # Jupyter or Python notebooks for exploration/analysis
│
├── src/                   # Main source code for data collection, processing, etc.
│   ├── setupsqlite.py         # Script to set up the SQLite database and table
│   ├── db_utils.py            # Database helper functions (insert, connect, etc.)
│   ├── stock_list.py          # List and mapping of NIFTY stock symbols
│   ├── collect_and_store.py   # Main script to fetch and store data for all stocks
│   ├── check_sqlite_setup.py  # Script to verify database and table structure
│   └── ...                    # Other modules (visualization, analysis, etc.)
│
├── tests/                 # Unit and integration tests
│
├── ExploreIdeas/          # For quick experiments and scratch scripts
│
├── README.txt
├── TODO.md
├── requirements.txt       # List of dependencies (nsepy, yfinance, etc.)
└── .gitignore             # Git ignore file

Usage:
1. Install dependencies listed in requirements.txt:
   pip install -r requirements.txt

2. Set up the SQLite database and table:
   python src/setupsqlite.py

3. (Optional) Verify the database and table structure:
   python src/check_sqlite_setup.py

4. Update src/stock_list.py to include all desired NIFTY stock symbols.

5. Fetch and store historical data for all stocks:
   python src/collect_and_store.py

6. Use the data in data/nifty_stocks.db for analysis, modeling, or visualization.

Notes:
- Only the stock name, date, and close price are stored in the database.
- To add new stocks, update the list in src/stock_list.py.
- A delay is included between requests to avoid being blocked by Yahoo Finance.
- Use a SQLite browser (e.g., DB Browser for SQLite) to inspect the database visually.
- For quick experiments, use the ExploreIdeas/ folder.
- Refer to code comments and TODO.md for further development tasks.