# Required modules
import math
import os
import random
import re
import sys


from collections import deque

def calculateScoreDifference(n, numSeq):
    # Initialize deque from the sequence
    sequence = deque(numSeq)
    # Scores initialization
    first_score, second_score = 0, 0
    # Flag to indicate the direction of removal (False for front, True for back)
    reverse = False

    for i in range(n):
        if reverse:
            num = sequence.pop()  # Remove from the back
        else:
            num = sequence.popleft()  # Remove from the front

        # Alternating turns
        if i % 2 == 0:  # First player's turn
            first_score += num
        else:  # Second player's turn
            second_score += num

        # Toggle the reverse flag if the number is even
        if num % 2 == 0:
            reverse = not reverse

    return first_score - second_score

# Example usage
n = 5
numSeq = [3, 6, 2, 3, 5]
print(calculateScoreDifference(n, numSeq))

n = 5
numSeq = [3, 6, 2, 3, 5]
result = scoreDifference(n, numSeq)
print(result)  # Output: 1
