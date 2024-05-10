# Cointegration
performs cointegration analysis and implements a basic pairs trading strategy using financial data fetched from Yahoo Finance.


The code provided performs cointegration analysis and implements a basic pairs trading strategy using financial data fetched from Yahoo Finance. Here's a brief description of the steps:

1.Import Libraries: The code imports necessary libraries such as yfinance, numpy, pandas, scipy, matplotlib, and statsmodels.
2.Define Tickers: Two tickers, ^XAU and ^GSPC, are defined for gold and S&P 500 index, respectively.
3.Download Data: Historical adjusted close prices of the defined tickers are downloaded from Yahoo Finance starting from January 3, 2000.
4.Data Preprocessing: The downloaded data is preprocessed by resetting indexes, forward filling missing values, and merging the dataframes on the 'Date' column.
5.Normalization: Data is normalized using MinMaxScaler to ensure comparability.
6.Pearson Correlation Coefficient: The Pearson correlation coefficient and its associated p-value are calculated to measure the linear correlation between the two time series.
7.Cointegration Test: The cointegration test is performed using the Engle-Granger two-step cointegration test from statsmodels. This test determines whether there exists a long-term relationship between the two time series.
8.Pairs Trading Strategy: If the cointegration test indicates that the series are cointegrated (p-value < 0.05), a basic pairs trading strategy is implemented. This involves taking long and short positions on the two assets based on their spread.
9.Visualization: The normalized time series data are plotted along with the calculated Pearson correlation coefficient.
Output: The results of the Pearson correlation coefficient, cointegration test statistic, p-value, and any trading actions taken are printed.![Figure_cointegration](https://github.com/Ged0x/Cointegration/assets/143278786/2496d9f9-44da-4c9d-ab0a-ab1b01771fac)
