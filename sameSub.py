# Required modules
import math
import os
import random
import re
import sys

# Init n = len(s), max_length, current_cost and left_pointer = 0
# for right_pointer in range(n) -> update current_cost += abs val of s and t of [right_pointer]
# inner while loop as long as current_cost > K -> update current_cost -= abs val of s and t of [left_pointer]
# calc max_length = max(max_length, right_pointer - left_pointer + 1)
# lastly return max_length

def sameSub(s, t, K):
  n = len(s)
  max_length = 0
  current_cost = 0
  left_pointer = 0

  for right_pointer in range(n):
    current_cost += abs(ord(s[right_pointer]) - ord(t[right_pointer]))

    while current_cost > K:
      current_cost -= abs(ord(s[left_pointer]) - ord(t[left_pointer]))
      left_pointer += 1

    max_length = max(max_length, right_pointer - left_pointer + 1)

  return max_length

# Example usage:
s = "adpgki"
t = "cdmxki"
K = 6
result = sameSub(s, t, K)
print(result)
