# Required modules
import math
import os
import random
import re
import sys

# Assign y = ['0'] * bits so all 0s in bit length
# Assign set_bits = 0
# For loop i in range(bits) -> if x[i] == '0' and set_bits < maxSet -> y[i] = '1' and incr set_bits += 1
# For loop done -> create y_str = ''.join(y) -> return y_str

def findYValue(bits, maxSet, x):
  y = ['0'] * bits

  set_bits = 0

  for i in range(bits):
    if x[i] == '0' and set_bits < maxSet:
      y[i] = '1'
      set_bits += 1

  y_str = ''.join(y)

  return y_str

bits = 3
maxSet = 1
x = "101"

print(findYValue(bits, maxSet, x))
