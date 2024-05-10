import yfinance as yf
import numpy as np
import pandas as pd
from scipy.stats import pearsonr
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt
from statsmodels.tsa.stattools import coint

ticker1 = "^XAU"
ticker2 = "^GSPC"

# Download data
df1 = yf.download(ticker1, start="2000-01-03", progress=False)["Adj Close"]
df2 = yf.download(ticker2, start="2000-01-03", progress=False)["Adj Close"]

# Reset index
df1 = df1.reset_index()
df2 = df2.reset_index()

# Forward fill missing values in df2 (fill up weekends with previous value)
df2['Adj Close'] = df2['Adj Close'].ffill()

# Merge dataframes on Date
merged_df = pd.merge(df1, df2, on='Date', suffixes=('_df1', '_df2'))

# Print the merged DataFrame
print("Merged DataFrame:")
print(merged_df)

# Extract values
df1_values = merged_df['Adj Close_df1'].values
df2_values = merged_df['Adj Close_df2'].values

# Normalize data
scaler = MinMaxScaler()
df1_normalized = scaler.fit_transform(df1_values.reshape(-1, 1)).flatten()
df2_normalized = scaler.fit_transform(df2_values.reshape(-1, 1)).flatten()

# Calculate Pearson correlation coefficient
corr_coefficient, p_value = pearsonr(df1_normalized, df2_normalized)

print("\nPearson correlation coefficient between df1 and df2 (after normalization):", corr_coefficient)
print("P-value:", p_value)

# Perform cointegration test
cointegration_test_result = coint(df1_normalized, df2_normalized)
print("\nCointegration Test:")
print("Cointegration test statistic:", cointegration_test_result[0])
print("P-value:", cointegration_test_result[1])
print("Critical values:", cointegration_test_result[2])

# Check if the series are cointegrated
if cointegration_test_result[1] < 0.05:  # Adjust significance level as needed
    print("The series are cointegrated.")
    spread = df1_normalized - df2_normalized  # Calculate spread
    mean_spread = np.mean(spread)
    std_spread = np.std(spread)

    # Define entry and exit thresholds (e.g., ±1 standard deviation)
    entry_threshold = mean_spread - 1 * std_spread
    exit_threshold = mean_spread

    # Initialize positions
    position_df1 = 0
    position_df2 = 0
    trades = []

    # Implement trading strategy
    for i in range(len(spread)):
        if spread[i] < entry_threshold and position_df1 == 0:
            # Buy df1 and short df2
            position_df1 = 1
            position_df2 = -1
            trades.append(('Buy df1', 'Short df2'))
        elif spread[i] > exit_threshold and position_df1 != 0:
            # Exit positions
            position_df1 = 0
            position_df2 = 0
            trades.append(('Exit', 'Exit'))


    print("\nTrades:")
    for trade in trades:
        print(trade)
else:
    print("The series are not cointegrated. Pairs trading strategy cannot be applied.")


plt.figure(figsize=(8, 6))


plt.plot(np.arange(len(df1_normalized)), df1_normalized, label=f'{ticker1} (Normalized)', color='blue')
plt.plot(np.arange(len(df2_normalized)), df2_normalized, label=f'{ticker2} (Normalized)', color='red', alpha=0.5)

plt.title("Line Graph of df1 vs df2 (Normalized)")
plt.xlabel("Index")
plt.ylabel("Normalized Values")
plt.legend()


plt.text(0.1, 0.9, f'Pearson Correlation Coefficient: {corr_coefficient:.2f}', transform=plt.gca().transAxes, fontsize=10)

plt.show()
