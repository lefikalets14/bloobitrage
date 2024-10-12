import asyncio
from basket import fetch_and_store_basket_pairs
from opportunities import load_basket_from_file, find_arbitrage_opportunities, display_opportunities

async def main():
    await fetch_and_store_basket_pairs()
    basket = load_basket_from_file()
    min_profit_percentage = 0.5
    opportunities = find_arbitrage_opportunities(basket, min_profit_percentage)
    display_opportunities(opportunities, min_profit_percentage)

if __name__ == "__main__":
    asyncio.run(main())
