import yfinance as yf
def get_gme_revenue_last_5_days():
    ticker_gme = yf.Ticker("GME")
    stock_data = ticker_gme.history(period="5d")
    average_closing_price = stock_data['Close'].mean()
    shares_outstanding = ticker_gme.info['sharesOutstanding']
    revenue_last_5_days = average_closing_price * shares_outstanding
    print(f"Estimated Revenue of GameStop for the Last 5 Days: ${revenue_last_5_days:.2f}")
if __name__ == "__main__":
    get_gme_revenue_last_5_days()
