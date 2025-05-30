# %%

# Install the required package
# pip install nsepy

from nsepy import get_history 
from datetime import date

# Fetch historical data for INFY from 2005-01-01 to 2025-05-30
data = get_history(
    symbol="INFY",
    start=date(2025, 1, 1),
    end=date(2025, 5, 29)
)

print(data)
print(f"Number of rows fetched: {len(data)}")
# Save the data to a CSV file
data.to_csv("INFY.csv")