# Required modules
import math
import os
import random
import re
import sys

# Calc 2 variables inc_sum and dec_sum
# inc_sum = (j - i + 1) * (i + j) // 2
# dec_sum = (j - k + 1) * (j + k) // 2
# have an overlap = j
# assign seq_sum_tot = inc_sum + dec_sum - overlap -> return seq_sum_tot

def seqSum(i, j, k):
  inc_sum = (j - i + 1) * (i + j) // 2

  dec_sum = (j - k + 1) * (j + k) // 2

  overlap = j

  seq_sum = inc_sum + dec_sum - overlap

  return seq_sum

result = seqSum(5, 9, 6)
print(result)
