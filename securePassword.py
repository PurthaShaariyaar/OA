# Required modules
import math
import os
import random
import re
import sys
from collections import Counter

# Init changes_needed = 0
# for loop range(0, len(pwd), 2) -> substring = pwd[i:i+2]
# init count_0 = substring.count('0') and count_1 = substring.count('1')
# updated changes_needed += min(count_0, count_1) -> return changes_needed

def minFlipsToSecurePassword(pwd):
    # Initialize a counter for the flips
    flips = 0

    # Iterate through the string in steps of 2
    for i in range(0, len(pwd) - 1, 2):
        # If two consecutive characters are the same, no flip is needed
        # If they are different, increment the flip counter
        if pwd[i] != pwd[i+1]:
            flips += 1

    return flips

# Example usage
pwd = "1110011000"
print(minFlipsToSecurePassword(pwd))


# Example usage:
pwd = "1110011000"
result = min_changes_to_secure_password(pwd)
print(result)

