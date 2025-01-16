import pandas as pd
import numpy as np
def analyze_stock_data(stock_data):
    # Calculate the moving average of the 'Close' price
    stock_data['MA_50'] = stock_data['Close'].rolling(window=50).mean()
    stock_data['MA_200'] = stock_data['Close'].rolling(window=200).mean()
    
    # Example: detect when the stock price crosses the moving average
    stock_data['Signal'] = 0
    stock_data['Signal'][50:] = np.where(stock_data['Close'][50:] > stock_data['MA_50'][50:], 1, 0)
    stock_data['Position'] = stock_data['Signal'].diff()

    return stock_data

# Example usage
if __name__ == "__main__":
    from stock_scraper import get_stock_data

    stock_symbol = input("Enter the stock symbol (e.g., 'AAPL'): ")
    data = get_stock_data(stock_symbol)
    analyzed_data = analyze_stock_data(data)
    print(analyzed_data.tail())  # Print the last few rows of the analysis
def check_alerts(stock_data, price_threshold):
    latest_price = stock_data['Close'].iloc[-1]
    if latest_price > price_threshold:
        print(f"ALERT: {stock_data.name} price is above {price_threshold}!")
    else:
        print(f"Price is below {price_threshold}, no alert.")
