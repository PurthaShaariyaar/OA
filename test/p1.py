# Required modules
import math
import os
import random
import re
import sys

def findYValue(bits, maxSet, x):
  y = ['0'] * bits

  set_bits = 0

  for i in range(bits):
    if x[i] == '0' and set_bits < maxSet:
      y[i] = '1'
      set_bits += 1

  y_str = ''.join(y)

  return y_str

def circles(circlePairs):
  def determine_relationship(xA, yA, RA, xB, yB, RB):
    distance = abs(xA - xB) if yA == yB else abs(yA - yB)

    if distance == 0 and RA == RB:
      return 'Concentric'
    elif distance == RA + RB or distance == abs(RA - RB):
      return 'Touching'
    elif distance < RA + RB and distance > abs(RA - RB):
      return 'Intersecting'
    elif distance + min(RA, RB) < max(RA, RB):
      return 'Disjoint-Inside'
    else:
      return 'Disjoint-Outside'

  results = []
  for pair in circlePairs:
    xA, yA, RA, xB, yB, RB = map(int, pair.split())
    relationships = determine_relationship(xA, yA, RA, xB, yB, RB)
    results.append(relationships)

  return results

def minMoves(prices, k):
  prices.sort()
  n = len(prices)

  if n % 2 == 1:
    median = prices[n // 2]
    return abs(k - median)
  else:
    left_median = [(n // 2) - 1]
    right_median = [n // 2]
    if k >= left_median and k <= right_median:
      return 0
    elif k < left_median:
      return (left_median - k) + (right_median - k)
    else:
      return (k - left_median) + (k - right_median)

def countValidTriplets(arr, d):
    T = 0
    H = {}

    for k in range(2, len(arr)):
      key = arr[k] % d
      H[key] = H.get(key, 0) + 1

    for j in range(1, len(arr)):
      if j >= 2:
        H[arr[j] % d] -= 1
      for i in range(j):
        matching_val = (d - (arr[i] + arr[j]) % d) % d
        to_add = H.get(matching_val, 0)
        T += to_add
    return T

def numValidWords(s):

  def is_valid_word(word):
    vowels = set("aeiouAEIOU")
    consonants = set("bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ")

    has_alpha = any(char.isalnum() for char in word)
    has_vowel = any(char in vowels for char in word)
    has_consonant = any(char in consonants for char in word)

    return has_alpha and has_vowel and has_consonant and len(word) >= 3

  words = s.split()
  valid_word_count = sum(is_valid_word(word) for word in words)
  return valid_word_count

def dominatingXorPairs(arr):
  n = len(arr)
  count = 0

  for i in range(n):
    for j in range(i + 1, n):
      if arr[i] ^ arr[j] > arr[i] & arr[j]:
        count += 1
  return count

def playSegments(coins):
  total_score = sum(coins)
  player1_score = 0

  for i in range(len(coins)):
    player1_score += coins[i]
    player2_score = total_score - player1_score
    if player1_score > player2_score:
      return i + 1
  return len(coins)

def sameSubtring(s, t, K):
  cost = 0
  left_pointer = 0
  max_length = 0

  for right_pointer in range(len(s)):
    cost += abs(ord(s[right_pointer]) - ord(t[right_pointer]))

    while cost > K:
      cost -= abs(ord(s[left_pointer]) - ord(t[left_pointer]))
      left_pointer += 1

    max_length = max(max_length, right_pointer - left_pointer + 1)

  return max_length

def pthFactor(n, p):
  factors = set()
  for i in range(1, int(n**0.5)  + 1):
    if n % i == 0:
      factors.add(i)
      factors.add(n // i)

  factors = sorted(list(factors))

  if p <= len(factors):
    return factors[p - 1]
  else:
    return 0

def getSequenceSum(i, j, k):
  inc_sum = ((j - i + 1) * (i + j)) // 2
  dec_sum = ((j - k + 1) * (j + k)) // 2

  total_sum = inc_sum + dec_sum - j
  return total_sum

def minimumFlips(target):
  flips = 0
  expected = '0'

  for char in target:
    if char != expected:
      flips += 1
      expected = '1' if expected == '0' else '0'
  return flips

def numPlayers(k, scores):
  filtered_scores = [score for score in scores if score > 0]

  sorted_scores = sorted(filtered_scores, reverse=True)

  can_level_up = 0

  for i, score in enumerate(scores):
    if i < k or sorted_scores[i] == sorted_scores[k - 1]:
      can_level_up += 1
    else:
      return 0
  return can_level_up

def romanizer(numbers):
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

  def int_to_roman(num):
    roman = ''
    for i in range(len(val)):
      while num >= val[i]:
        num -= val[i]
        roman += syb[i]
    return roman

  result = [int_to_roman(num) for num in numbers]
  return result


# TEST 1

bits = 3
maxSet = 1
x = "101"
print(findYValue(bits, maxSet, x))

# TEST 2

circlePairs = ["3 0 10 5 0 3", "0 1 4 0 1 5"]
print(circles(circlePairs))

# TEST 3

prices = [4, 2, 1, 4, 7]
k = 3
print(minMoves(prices, k))

# TEST 4

# Example usage:
arr = [3, 3, 4, 7, 8]
d = 5
result = countValidTriplets(arr, d)
print(result)

# TEST 5

# Example usage:
input_string = "Hello, this is a test string with valid words like apple and 123."
result = numValidWords(input_string)
print(result)

# TEST 6

arr = [4, 3, 5, 2]
print(dominatingXorPairs(arr))  # Output: 4

# TEST 7
coins = [1, 1, 0, 1]
print(playSegments(coins))  # Output: 2

# TEST 8

s = "adpgki"
t = "cdmxki"
K = 6
result = sameSubtring(s, t, K)
print(result)

# TEST 9

# Example usage
n = 20
p = 3
print(pthFactor(n, p))  # Output should be 4 as per the corrected explanation


# TEST 10
i, j, k = 5, 9, 6
print(getSequenceSum(i, j, k))

# TEST 11
target = "1010"
result = minimumFlips(target)
print(result)

# TEST 12
k_value = 3
player_scores = [100, 50, 50, 25]
result = numPlayers(k_value, player_scores)
print(result)

# TEST 13
numbers = [1, 2, 3, 4, 5]
result = romanizer(numbers)
print(result)
