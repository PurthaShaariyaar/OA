# Required modules
import math
import os
import random
import re
import sys

def getFinalData(data, updates):
    n = len(data)
    # Create an auxiliary array to mark negations
    negation_marks = [0] * (n + 1)

    # Apply updates in the form of marking negations
    for l, r in updates:
        negation_marks[l-1] += 1  # Start negation
        negation_marks[r] -= 1  # End negation

    # Apply negation marks to data
    negation_effect = 0
    for i in range(n):
        negation_effect += negation_marks[i]
        # If negation_effect is odd, negate the current element
        if negation_effect % 2 != 0:
            data[i] = -data[i]

    return data

# The corrected example usage
data = [1, -4, -5, 2]
updates = [[2, 4], [1, 2]]
print(getFinalData(data, updates))


initial_data = [1, -4, -5, 2]
updates = [[2, 4], [1, 2]]
result = getFinalData(initial_data, updates)
print(result)
