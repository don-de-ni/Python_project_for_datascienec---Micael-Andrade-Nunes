import yfinance as yf
import mplfinance as mpf
def plot_gme_candlestick_chart():
    ticker_gme = yf.Ticker("GME")
    stock_data = ticker_gme.history(period="5d")
    mpf.plot(stock_data, type='candle', volume=True, title="GameStop (GME) Candlestick Chart - Last 5 Days")
if __name__ == "__main__":
    plot_gme_candlestick_chart()
