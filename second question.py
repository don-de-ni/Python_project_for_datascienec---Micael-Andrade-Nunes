import yfinance as yf
def get_tesla_revenue_last_5_days():
    # Create a ticker object for Tesla (TSLA)
    ticker_tesla = yf.Ticker("TSLA")
    # Get historical stock data for the last 5 days
    stock_data = ticker_tesla.history(period="5d")
    # Calculate the average closing price for the last 5 days
    average_closing_price = stock_data['Close'].mean()
    # Get the number of shares outstanding from financials
    shares_outstanding = ticker_tesla.info['sharesOutstanding']
    # Calculate the estimated revenue for the last 5 days
    revenue_last_5_days = average_closing_price * shares_outstanding
    # Display the estimated revenue for the last 5 days
    print(f"Estimated Revenue of Tesla for the Last 5 Days: ${revenue_last_5_days:.2f}")
if __name__ == "__main__":
    get_tesla_revenue_last_5_days()


