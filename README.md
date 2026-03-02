 Asset Volatility & Returns Analysis

This is a Python script I wrote to programmatically fetch historical stock data, calculate daily logarithmic returns, and compute annualised volatility. 

Coming from a background in corporate finance forecasting (heavily reliant on Excel and simple discrete returns), I built this to transition my modeling into a Python/pandas environment and apply more rigorous, continuous mathematics to market data.

The Math

To make the time-series data stationary and mathematically time-additive, the script converts raw adjusted closing prices into continuous log returns before calculating risk.

1. Logarithmic Returns:
r_t = ln({P_t}/{P_{t-1})

2. Annualised Volatility:
Assuming geometric Brownian motion and 252 trading days in a year, daily standard deviation is scaled by the square root of time to find the annualised volatility (sigma):
sigma_{annual} = sigma_{daily} /times /sqrt{252}

Tools Used
Python (Core logic)
yfinance (Data ingestion from Yahoo Finance)
pandas & numpy (Vectorised math and data manipulation)
matplotlib(Time-series visualisation)

Usage

The main logic is contained in the `analyse_asset_volatility()` function. You can run it for any ticker symbol to get a quick printout of the risk metrics and a plot of the stationary returns.

python
from volatility_scanner import analyse_asset_volatility

# Example: Check Apple's volatility over the past year
analyse_asset_volatility("AAPL", period="1y")
