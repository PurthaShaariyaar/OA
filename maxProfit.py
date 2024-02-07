# Required modules
import math
import os
import random
import re
import sys

def getMaximumProfit(price, profit):
    n = len(price)
    if n < 3:
        return -1  # Not enough days for a valid triplet

    # Step 1: Preprocess for maximum future profit
    max_future_profit = [0] * n
    max_profit_so_far = profit[-1]
    for i in range(n - 2, -1, -1):
        max_future_profit[i] = max(max_profit_so_far, profit[i + 1])
        max_profit_so_far = max(max_profit_so_far, profit[i])

    # Step 2: Iterate through each day to find the best triplet
    max_total_profit = -1
    min_price_so_far = price[0]
    for j in range(1, n - 1):
        if price[j] > min_price_so_far:  # There's a lower price before day j
            # Calculate profit if bought at min_price_so_far and sold at price[j]
            profit_if_sold_today = profit[j] - (price[j] - min_price_so_far)
            # Update max total profit considering the future profit as well
            max_total_profit = max(max_total_profit, profit_if_sold_today + max_future_profit[j])
        # Update min price seen so far
        min_price_so_far = min(min_price_so_far, price[j])

    return max_total_profit if max_total_profit > 0 else -1

price = [2, 3, 1, 5, 9]
profit = [1, 2, 6, 1, 5]
result = getMaximumProfit(price, profit)
print(result)
