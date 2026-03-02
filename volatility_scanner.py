import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def analyse_asset_volatility(ticker: str, period: str = "1y"):
    """
    Fetches historical market data, calculates continuous logarithmic returns, 
    and computes the annualised volatility for a given financial asset.
    
    Parameters:
    ticker (str): The stock ticker symbol (e.g., 'AAPL', 'NVDA').
    period (str): The time period to analyze (default is 1 year).
    
    Returns:
    None: Prints the volatility metrics and displays a visualization.
    """
    print(f"--- Initiating Volatility Analysis for {ticker} ---")
    
    # 1. Telemetry Acquisition
    # Fetch the data, ensuring corporate actions (splits/dividends) are adjusted for
    data = yf.download(ticker, period=period, auto_adjust=True, progress=False)
    
    if data.empty:
        print(f"Error: Could not retrieve data for {ticker}.")
        return
        
    position = data['Close']
    
    # 2. Continuous Transformation (Velocity)
    # Calculate daily logarithmic returns to ensure time-additivity and stationarity
    velocity = np.log(position / position.shift(1)).dropna()
    
    # 3. Energy Measurement (Amplitude)
    # Calculate standard deviation and scale it using the square root of time
    daily_vol_series = velocity.std()
    
    # Extract the raw float value (handling pandas Series format)
    if isinstance(daily_vol_series, pd.Series):
        daily_vol = daily_vol_series.iloc[0]
    else:
        daily_vol = daily_vol_series
        
    annual_vol = daily_vol * np.sqrt(252)
    
    # 4. Output Metrics
    print(f"Data Points Analysed: {len(velocity)} trading days")
    print(f"Daily Volatility:     {daily_vol:.4f} ({daily_vol * 100:.2f}%)")
    print(f"Annualised Risk:      {annual_vol:.4f} ({annual_vol * 100:.2f}%)\n")
    
    # 5. Signal Visualization
    plt.figure(figsize=(10, 5))
    plt.plot(velocity, color='teal', linewidth=1)
    plt.title(f"{ticker} - Stationary Log Returns (Velocity)")
    plt.xlabel("Date")
    plt.ylabel("Logarithmic Return")
    plt.axhline(0, color='red', linestyle='--', linewidth=1.5, alpha=0.7)
    plt.grid(alpha=0.3)
    plt.tight_layout()
    plt.show()

# --- Execution ---
# Now you can test any asset with just one line of code!
analyse_asset_volatility("AAPL", period="1y")
analyse_asset_volatility("TSLA", period="1y")
