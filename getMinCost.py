# Required modules
import math
import os
import random
import re
import sys

# Get length of arr > calc initCost > assign minCost = initCost
# For loop i to n - 1 > assign cost = init cost - ...
# Update minCost and cost to min of whichever > return minCost

def getMinCost(arr):
  n = len(arr)

  initCost = sum((arr[i] - arr[i+1])**2 for i in range(n - 1))

  minCost = initCost

  for i in range(n - 1):
    cost = initCost - (arr[i] - arr[i + 1])**2 + (arr[i] - arr[i + 1]//2)**2 + (arr[i + 1]//2 - arr[i + 1])**2
    minCost = min(minCost, cost)
  return minCost

arr = [1, 3, 5, 2, 10]
result = getMinCost(arr)
print(result)
