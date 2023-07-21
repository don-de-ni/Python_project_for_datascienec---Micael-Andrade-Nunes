#First question

import yfinance as yf
def get_high_low_prices_last_5_days():
    # Create a ticker object for Tesla (TSLA)
    ticker_tesla = yf.Ticker("TSLA")
    # Get historical data for Tesla for the last 5 days
    tesla_data = ticker_tesla.history(period="5d")
    # Select only the columns for high and low prices
    high_low_prices_last_5_days = tesla_data[['High', 'Low']]
    # Display the high and low price columns for the last 5 days
    print(high_low_prices_last_5_days)
if __name__ == "__main__":
    get_high_low_prices_last_5_days()




