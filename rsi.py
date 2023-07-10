import yfinance as yf
import talib
import json

# Read the JSON file
with open('config.json') as file:
    data = json.load(file)

# Access the values
stock_symbol = data['stock_symbol']
rsi_period = data['rsi_period']

def rsi():
    # Define the ticker symbol for the S&P 500
    ticker = yf.Ticker(stock_symbol)

    # Download historical data for the S&P 500
    data = ticker.history(period="max", interval="1d", prepost = True)

    # Extract closing prices from the data
    close_prices = data["Close"].values

    # Calculate RSI using talib
    rsi = talib.RSI(close_prices, timeperiod=rsi_period)

    # Get the last RSI value and its corresponding date
    current_rsi = rsi[-1]
    #current_date = data.index[-1]

    return current_rsi