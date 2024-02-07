# Required modules
import math
import os
import random
import re
import sys

# Init T = 0 and H = {} dict
# For loop k in range(2, len(arr)) -> update key = arr[k] % d -> update H[key] = H.get(key, 0) + 1
# For loop j(1, len(arr)) -> if j >= 2: H[arr[j] % d] -= 1
    # Inner for loop i(j) -> matching_val = (d - (arr[i] + arr[j]) % d) % d
    # update to_add = H.get(matching_val, 0) -> update T += to_get
# Return T

def count_valid_triplets(arr, d):
    T = 0  # Total possibilities
    H = {}  # Counts all possible (arr[k]) % d = Key from index k

    # Preprocessing step: Build the dictionary
    for k in range(2, len(arr)):
        key = arr[k] % d
        H[key] = H.get(key, 0) + 1

    # Iterate through pairs (i, j)
    for j in range(1, len(arr)):
        if j >= 2:
            H[arr[j] % d] -= 1  # When j increments, it reduces options for arr[k]
        for i in range(j):
            matching_val = (d - (arr[i] + arr[j]) % d) % d
            to_add = H.get(matching_val, 0)
            T += to_add

    return T

# Example usage:
arr = [3, 3, 4, 7, 8]
d = 5
result = count_valid_triplets(arr, d)
print(result)
