_____________________________________________________________________________________________
MARKET NITI
_____________________________________________________________________________________________

Requirements:
- Collect daily close price data for 150 NIFTY stocks over the last 10+ years.
- Store the data in a SQLite database for further analysis and visualization.

Description:
Market Niti is a project focused on gathering, processing, and storing historical stock data for NIFTY index companies. The system fetches daily close prices using the yfinance package and stores them in a structured SQLite database. The project is designed to be extensible, allowing new stocks to be added easily and supporting further analysis and visualization.

Project Structure:
MarketNiti/
│
├── data/                        # Stores raw and processed data (CSV, DB files, etc.)
│   └── nifty_stocks.db          # SQLite database file
│
├── notebooks/                   # Jupyter or Python notebooks for exploration/analysis
│
├── src/
│   ├── calculate/
│   │   └── performance_calculator.py   # Calculates stock performance metrics
│   │
│   ├── extract/
│   │   ├── daily/
│   │   │   └── daily_update.py         # Script for daily data updates
│   │   │
│   │   ├── history/
│   │   │   └── history_load.py         # Script to fetch and store historical data
│   │   │
│   │   ├── check_sqlite_setup.py       # Script to verify database and table structure
│   │   ├── db_utils.py                 # Database helper functions (insert, connect, etc.)
│   │   ├── run_first_time_setup.py     # Automates first-time setup and data load
│   │   ├── setupsqlite.py              # Script to set up the SQLite database and tables
│   │   ├── stock_list.py               # List and mapping of NIFTY stock symbols
│   │   └── stock_master_data.py        # Inserts stock master data (name, category)
│   │
│   └── ...                            # Other modules (visualization, analysis, etc.)
│
├── tests/                             # Unit and integration tests
│
├── ExploreIdeas/                      # For quick experiments and scratch scripts
│
├── README.txt
├── TODO.md
├── requirements.txt                   # List of dependencies (nsepy, yfinance, etc.)
└── .gitignore                         # Git ignore file

Usage:
1. Install dependencies listed in requirements.txt:
   pip install -r requirements.txt

2. Run the first-time setup script to initialize the database, verify structure, insert stock master data, and fetch historical data:
   python src/extract/run_first_time_setup.py

   This script will:
   - Set up the SQLite database and tables
   - Verify the database and table structure
   - Insert stock master data (symbols, names, categories)
   - Fetch and store historical data for all stocks

3. (Optional) For daily updates, use:
   python src/extract/daily/daily_update.py

4. For further analysis, use the data in data/nifty_stocks.db with your own scripts or notebooks.

Development & Roadmap:
- See TODO.md for planned features and ongoing tasks, including:
  - Automating daily data updates
  - Handling missing data and errors
  - Adding new columns for extended analysis
  - Data visualization scripts
  - Unit and integration tests

Notes:
- Only the stock symbol, name, category, date, and close price are stored in the database by default.
- To add new stocks, update the list in src/extract/stock_list.py and src/extract/stock_master_data.py.
- A delay is included between requests to avoid being blocked by Yahoo Finance.
- Use a SQLite browser (e.g., DB Browser for SQLite) to inspect the database visually.
- For quick experiments, use the ExploreIdeas/ folder.
- Refer to code comments and TODO.md for further development tasks and ideas.

Contributing:
- Contributions are welcome. Please see TODO.md for open tasks or suggest improvements via pull requests.

License:
- This project is for educational and research purposes. Please review the LICENSE file for more information.
