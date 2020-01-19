# Greedy approach!
# Trying out a greedy approach should be one of the first ways you try to break down a new question.
# Suppose we could come up with the answer in one pass through the input, by simply updating the 'best answer so far' as we went

def get_max_profit(stock_prices):
    if len(stock_prices) < 2:
        raise ValueError('Getting a profit requires at least 2 prices')

    max_profit = stock_prices[1]-stock_prices[0]
    min_price = stock_prices[0]

    for current_time in range(1, len(stock_prices)):
        current_price = stock_prices[current_time]

        potential_profit = current_price-min_price
        max_profit = max(max_profit, potential_profit)
        min_price = min(min_price, current_price)

    return max_profit


print(get_max_profit([10]))
