# Required modules
import math
import os
import random
import re
import sys
from collections import deque
import heapq

def getMinMachines(start, end):
  tasks = sorted(zip(start, end))
  machines = []

  for s, e in tasks:
    if machines and machines[0] <= s:
      heapq.heappop(machines)
    heapq.heappush(machines, e)

  return len(machines)

def getMinCost(arr):
  original_cost = sum((arr[i] - arr[i + 1])**2 for i in range(len(arr) - 1))
  min_cost_after_insertion = float('inf')

  for i in range(len(arr) - 1):
    optimal_insert_value = (arr[i] + arr[i + 1]) // 2
    new_cost = original_cost - (arr[i] - arr[i+1])**2 + (arr[i] - optimal_insert_value)**2 + (optimal_insert_value - arr[i+1])**2
    min_cost_after_insertion = min(min_cost_after_insertion, new_cost)
  return min_cost_after_insertion



# TEST 1
start = [1, 8, 3, 9, 6]
end = [7, 9, 6, 14, 7]
print(getMinMachines(start, end))  # Output: 3

# TEST 2
arr = [1, 3, 5, 2, 10]
getMinCost(arr)
