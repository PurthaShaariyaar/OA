# Required modules
import math
import os
import random
import re
import sys

# Init factors array = []
# For loop in range(1, int(n ** 0.5) + 1)
# if n % i == 0 -> append it to factors -> if inner : n//i = i -> append it to factors
# Sort factors -> if p <= len(factors) --> return factors[p - 1] else return 0

def pFactor(n, p):
  factors = []
  for i in range(1, int(n**0.5) + 1):
    if n % i == 0:
      factors.append(i)

      if n // i != i:
        factors.append(n // i)

  factors.sort()

  if p <= len(factors):
    return factors[p - 1]
  else:
    return 0

n = 20
p = 3
result = pFactor(n, p)
print(result)
