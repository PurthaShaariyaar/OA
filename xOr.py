# Required modules
import math
import os
import random
import re
import sys

# Init n = len(arr) and count to 0
# n^2 2 for loops i(n) and j(i + 1, n)
# main formula arr[i] ^ arr[j] > arr[i] and arr[i] ^ arr[j] > arr[j] -> update count += 1
# return count

def dominatingXorPairs(arr):
    n = len(arr)
    count = 0

    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] ^ arr[j] > arr[i] & arr[j]:
                count += 1

    return count

# Example usage
arr = [4, 3, 5, 2]
result = dominatingXorPairs(arr)
print(result)

