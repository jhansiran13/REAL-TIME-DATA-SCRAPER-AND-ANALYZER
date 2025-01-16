import matplotlib.pyplot as plt

def plot_stock_data(stock_data):
    # Plot the closing price and moving averages
    plt.figure(figsize=(12, 6))
    plt.plot(stock_data['Close'], label='Closing Price', color='blue')
    plt.plot(stock_data['MA_50'], label='50-Day Moving Average', color='red')
    plt.plot(stock_data['MA_200'], label='200-Day Moving Average', color='green')
    
    # Highlight buy/sell signals
    plt.plot(stock_data[stock_data['Position'] == 1].index,
             stock_data['MA_50'][stock_data['Position'] == 1],
             '^', markersize=10, color='g', lw=0, label='Buy Signal')
    plt.plot(stock_data[stock_data['Position'] == -1].index,
             stock_data['MA_50'][stock_data['Position'] == -1],
             'v', markersize=10, color='r', lw=0, label='Sell Signal')

    plt.title('Stock Price with Moving Averages and Buy/Sell Signals')
    plt.legend(loc='best')
    plt.show()

# Example usage
if __name__ == "__main__":
    from data_analyzer import analyze_stock_data
    from stock_scraper import get_stock_data

    stock_symbol = input("Enter the stock symbol (e.g., 'AAPL'): ")
    data = get_stock_data(stock_symbol)
    analyzed_data = analyze_stock_data(data)
    plot_stock_data(analyzed_data)
