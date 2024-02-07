# Required modules
import math
import os
import random
import re
import sys


# Sort prices and get len of prices assign n
# If n % 2 == odd number -> then median = prices[n // 2] -> return abs(k - median)
# Else get leftP = prices[(n // 2) - 1] and rightP = [n // 2]
  # if k >= leftP and k <= rightP: return 0
  # elif k < leftP: return (leftP - k) + (rightP - k)
  # else: return (k - leftP) + (k - rightP)

def getMinimumMoves(prices, k):
  prices.sort()
  n = len(prices)

  if n % 2 == 1:
    median = prices[n // 2]
    return abs(k - median)
  else:
    left_median = prices[(n // 2) - 1]
    right_median = prices[n // 2]

    if k >= left_median and k <= right_median:
      return 0
    elif k < left_median:
      return (left_median - k) + (right_median - k)
    else:
      return (k - left_median) + (k - right_median)

# Example usage
prices = [4, 2, 1, 4, 7]
k = 3
print(getMinimumMoves(prices, k))
