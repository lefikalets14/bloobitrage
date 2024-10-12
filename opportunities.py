import json

def calculate_profit_potential(buy_price, sell_price, fees=0.001):
    initial_investment = 1
    buy_amount = initial_investment / buy_price
    effective_buy_amount = buy_amount * (1 - fees)
    
    received_amount = effective_buy_amount * sell_price
    effective_received_amount = received_amount * (1 - fees)
    
    profit = effective_received_amount - initial_investment
    profit_percentage = (profit / initial_investment) * 100
    
    return profit_percentage

def load_basket_from_file():
    with open('basket.json', 'r') as f:
        basket = json.load(f)
    return basket

def find_arbitrage_opportunities(basket, min_profit_percentage=0.5):
    opportunities = []
    for i in range(len(basket)):
        for j in range(i + 1, len(basket)):
            buy_pair = basket[i]
            sell_pair = basket[j]
            buy_price = buy_pair[1]['last']
            sell_price = sell_pair[1]['last']
            
            profit_potential = calculate_profit_potential(buy_price, sell_price)
            
            if profit_potential >= min_profit_percentage:
                opportunities.append((buy_pair[0], sell_pair[0], profit_potential))
    
    return opportunities

def display_opportunities(opportunities, min_profit_percentage, max_display=5):
    sorted_opportunities = sorted(opportunities, key=lambda x: x[2], reverse=True)
    print(f"Top {max_display} arbitrage opportunities with {min_profit_percentage}% or greater profit potential:")
    for opportunity in sorted_opportunities[:max_display]:
        buy_pair, sell_pair, profit_potential = opportunity
        print(f"Buy {buy_pair} at {buy_pair.split('/')[1]}, sell {sell_pair} at {sell_pair.split('/')[1]}, profit potential: {profit_potential:.2f}%")

if __name__ == "__main__":
    basket = load_basket_from_file()
    min_profit_percentage = 0.5
    opportunities = find_arbitrage_opportunities(basket, min_profit_percentage)
    display_opportunities(opportunities, min_profit_percentage)
