def e3(gold_prices):
    min_price = gold_prices[0]
    max_profit = 0
    for i in gold_prices[1:]:
        profit = i - min_price
        max_profit = max(max_profit, profit)
        min_price = min(min_price, i)
    return max_profit
        
gold_prices_1 = [100, 120, 140, 160, 180, 200, 220]
gold_prices_2 = [200, 180, 220, 160, 240, 260, 210]
gold_prices_3 = [250, 230, 210, 190, 170, 150, 130]
gold_prices_4 = [200, 200, 200, 200, 200, 200, 200]
gold_prices_5 = [150, 160, 155, 170, 180, 175, 165]

print(e3(gold_prices_1))
print(e3(gold_prices_2))
print(e3(gold_prices_3))
print(e3(gold_prices_4))
print(e3(gold_prices_5))