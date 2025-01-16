import yfinance as yf

def get_stock_data(stock_symbol):
    # Download stock data from Yahoo Finance
    stock = yf.Ticker(stock_symbol)
    data = stock.history(period="1d", interval="1m")  # Get 1 minute interval data for today
    return data

# Example usage
if __name__ == "__main__":
    stock_symbol = input("Enter the stock symbol (e.g., 'AAPL'): ")
    data = get_stock_data(stock_symbol)
    print(data.head())  # Print first 5 rows
