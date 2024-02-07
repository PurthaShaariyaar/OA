# Required modules
import math
import os
import random
import re
import sys

# Get total sum of quantity (sum fcn) > assign runningSum = 0 and minMoves to inf
# Iterate through quantity and add all q values to runningSum
# if runningSum == totalSum//2 > return totalSum - runningSum * 2
# Update minMoves to min of (minMoves, abs(runningSum - totalSum // 2 *2))
# Return minMoves

def getMinimumMoves(quantity):
    total_sum = sum(quantity)
    prefix_sums = [0] * (len(quantity) + 1)
    for i in range(1, len(quantity) + 1):
        prefix_sums[i] = prefix_sums[i-1] + quantity[i-1]

    def find_moves_for_partition(target):
        # This function would calculate the minimum moves for a given target partition sum
        # Implement binary search and logic to calculate moves based on the target sum
        pass

    # Start binary search
    left, right = 0, total_sum // 2
    min_moves = float('inf')
    while left <= right:
        mid = (left + right) // 2
        moves = find_moves_for_partition(mid)
        min_moves = min(min_moves, moves)
        # Adjust left or right based on the condition to narrow down the search
        # This part depends on the specific logic of how you calculate moves and compare partitions

    return min_moves

quantity = [1, 2, 3, 4, 5]
result = getMinimumMoves(quantity)
print(result)
