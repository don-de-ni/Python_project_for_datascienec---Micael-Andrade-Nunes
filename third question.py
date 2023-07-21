import yfinance as yf

def get_high_low_prices_last_5_days_gme():
    ticker_gme = yf.Ticker("GME")
    gme_data = ticker_gme.history(period="5d")
    high_low_prices_last_5_days = gme_data[['High', 'Low']]
    print(high_low_prices_last_5_days)

if __name__ == "__main__":
    get_high_low_prices_last_5_days_gme()
