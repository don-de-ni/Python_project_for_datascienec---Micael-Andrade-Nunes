import yfinance as yf
import mplfinance as mpf
def plot_tesla_candlestick_chart():
    ticker_tesla = yf.Ticker("TSLA")
    stock_data = ticker_tesla.history(period="5d")
    mpf.plot(stock_data, type='candle', volume=True, title="Tesla (TSLA) Candlestick Chart - Last 5 Days")
if __name__ == "__main__":
    plot_tesla_candlestick_chart()
