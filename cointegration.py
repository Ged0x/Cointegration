import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

# Define the ticker symbol for the company
ticker_symbol = 'AAPL'  # Example: Apple Inc.

# Fetch financial data from Yahoo Finance
financials = yf.Ticker(ticker_symbol)

# Get quarterly revenue data
revenue_data = financials.quarterly_financials.loc['Total Revenue']

# Convert revenue data to DataFrame
revenue_df = pd.DataFrame(revenue_data)


# Convert index to datetime
revenue_df.index = pd.to_datetime(revenue_df.index)

# Sort data by date
revenue_df.sort_index(inplace=True)
print(revenue_df)

# Interpolate revenue data to make it continuous
interp_func = interp1d(revenue_df.index, revenue_df['Total Revenue'], kind='linear')

#date range
date_range = pd.date_range(start=revenue_df.index.min(), end=revenue_df.index.max(), freq='D')

# Define a function to convert datetime to numerical values
def datetime_to_numeric(dates):
    return dates.map(pd.Timestamp.timestamp)

# Interpolate revenue data to make it continuous
interp_func = interp1d(datetime_to_numeric(revenue_df.index), revenue_df['Total Revenue'], kind='linear')

# Define a range of dates for interpolation
date_range = pd.date_range(start=revenue_df.index.min(), end=revenue_df.index.max(), freq='D')

# Interpolate revenue for each date in the range
revenue_interpolated = interp_func(datetime_to_numeric(date_range))

# Plot derivative of revenue over time
plt.figure(figsize=(10, 6))
plt.plot(date_range, revenue_interpolated, marker='o', linestyle='-')
plt.xlabel('Date')
plt.ylabel('Revenue Interpolated')
plt.title('Interpolated Revenue Over Time')
# Format y-axis tick labels as integers
plt.gca().get_yaxis().set_major_formatter(plt.FuncFormatter(lambda x, loc: "{:,}".format(int(x))))
plt.grid(True)
plt.show()
