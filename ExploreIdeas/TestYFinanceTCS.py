# %%
# If yfinance is not installed, uncomment the next line and run it once:
# pip install yfinance

import yfinance as yf

# Define the ticker symbol and date range
ticker = "TCS.NS"
start_date = "2025-01-01"
end_date = "2025-04-30"

# Download historical data for TCS from Yahoo Finance
data = yf.download(ticker, start=start_date, end=end_date)

# Display the fetched data and number of rows
print(data)
print(f"Number of rows fetched: {len(data)}")

# Save the data to a CSV file
data.to_csv("ExploreIdeas/TCS_2025_Jan_Apr.csv")