# Required modules
import math
import os
import random
import re
import sys

# Assign 2 arrays: 1 with int vals and another with symbols
# Need a helper fcn
# Assign roman nums to an empty string and assign i = 0
# While loop as long as num > 0 -> for loop _ in range(num // val[i])
# Add all syb to roman_num += then decrement num -= val[i] -> increment i += 1
# Return roman_num -> assign result to call helper fcn for each num in nums -> return result


def romanizer(nums):
  def int_to_roman(num):
    val = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4,
            1
        ]
    syb = [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV",
            "I"
        ]
    roman_num = ''
    i = 0
    while num > 0:
      for _ in range(num // val[i]):
        roman_num += syb[i]
        num -= val[i]
      i += 1
    return roman_num

  result = [int_to_roman(num) for num in nums]
  return result

numbers = [1, 2, 3, 4, 5]
result = romanizer(numbers)
print(result)
