import ccxt

# Get a list of all exchange classes
exchanges = ccxt.exchanges

# Print the exchange names
for exchange_id in exchanges:
    print(exchange_id)
