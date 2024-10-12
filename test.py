import ccxt

binance = ccxt.binance()

symbols = ['BNB/USDT', 'BNB/UAH']

for symbol in symbols:
    ticker = binance.fetch_ticker(symbol)
    print(f"Symbol: {symbol}")  # Print symbol with label
    print(ticker)  # Print the entire ticker dictionary
    print()  # Add an empty line for separation
