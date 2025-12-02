#Arrays Problem #2: Best Time to Buy & Sell Stock
#prices = [7,1,5,3,6,4]
# output = 5   # Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5

def maxProfit(prices):
    min_price = float('inf')   # lowest price seen so far
    max_profit = 0             # best profit found

    for price in prices:
        min_price = min(min_price, price)
        profit = price - min_price
        max_profit = max(max_profit, profit)

    return max_profit

# Example usage:
prices = [7, 1, 5, 3, 6, 4]
result = maxProfit(prices)
print(result)  # Output: 5