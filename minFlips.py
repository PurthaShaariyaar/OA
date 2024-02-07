# Required modules
import math
import os
import random
import re
import sys

# Init flips = 0 and assign curr = '0' * len(target)
# For loop range(len(target)) -> if curr[i] != target[i] -> incr flips by 1 -> update all next curr nums
# return flips
# Need helper fcn -> flip(char): return '0' if char == '1' else '1'

def minimumFlips(target):
    flips = 0
    current = "0" * len(target)  # Initial string of zeros

    for i in range(len(target)):
        if current[i] != target[i]:
            flips += 1
            current = current[:i] + flip(current[i]) + current[i+1:]

    return flips

def flip(char):
    return "0" if char == "1" else "1"

# Example usage:
target = "00110"
result = minimumFlips(target)
print(result)
