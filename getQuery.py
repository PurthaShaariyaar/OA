# Required modules
import math
import os
import random
import re
import sys

def getQueryResults(N, queries):
    # Convert N to its binary representation to find powers of 2
    goodArray = [2**i for i in range(64) if (N >> i) & 1]
    answers = []

    for l, r, m in queries:
        # Adjust indices to 0-based
        l -= 1
        r -= 1
        product = 1
        for i in range(l, r + 1):
            product = (product * goodArray[i]) % m
        answers.append(product)

    return answers

# Example
N = 26
queries = [
    [1, 2, 1009],
    [3, 3, 5]
]

output = getQueryResults(N, queries)
print(output)
