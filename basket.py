import ccxt
import json
import os

def save_basket_to_file(basket):
    with open('basket.json', 'w') as f:
        json.dump(basket, f, indent=4)

async def fetch_and_store_basket_pairs():
    exchange = ccxt.binance()
    base_currency = input("Enter the basket commander (base currency): ").upper()
    try:
        tickers = exchange.fetch_tickers()
        pairs = {symbol: tickers[symbol] for symbol in tickers if base_currency in symbol}
        
        # Filter out pairs with missing last price information
        filtered_pairs = {symbol: pairs[symbol] for symbol in pairs if 'last' in pairs[symbol] and pairs[symbol]['last'] is not None}
        
        # Sort pairs by last price in ascending order
        sorted_pairs = sorted(filtered_pairs.items(), key=lambda x: x[1]['last'])

        # Save to basket.json
        if os.path.exists('basket.json'):
            os.remove('basket.json')
        save_basket_to_file(sorted_pairs)

        print(f"Basket for {base_currency} saved successfully.")
    except Exception as e:
        print(f"Error fetching pairs: {e}")

if __name__ == "__main__":
    import asyncio
    asyncio.run(fetch_and_store_basket_pairs())
