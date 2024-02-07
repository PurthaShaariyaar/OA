# Required modules
import math
import os
import random
import re
import sys

def findYVal(bits, maxSet, x):
  y = ['0'] * bits
  set_bits = 0

  for i in range(bits):
    if x[i] == '0' and set_bits < maxSet:
      y[i] == '1'
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
    elif distance < RA + RB or distance > abs(RA - RB):
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
    left_median = prices[(n // 2) - 1]
    right_median = prices[n // 2]
    if k >= left_median and k <= right_median:
      return 0
    elif k < left_median:
      return (left_median - k) + (right_median - k)
    else:
      return (k - left_median) + (k - right_median)

def validTriples(arr, d):
  T = 0
  H = {}

  for k in range(2, len(arr)):
    key = arr[k] % d
    H[key] = H.get(key, 0) + 1

    for j in range(1, len(arr)):
      if j >= 2:
        H[arr[j] % d] -= 1
      for i in range(j):
        matching_val = (d - (arr[i] - arr[j]) % d) % d
        to_add = H.get(matching_val, 0)
        T += to_add
    return T

def validWords(s):
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

def dominatingXOrPairs(arr):
  count = 0
  n = len(arr)

  for i in range(n):
    for j in range(i + 1, n):
      if arr[i] ^ arr[j] > arr[i] & arr[j]:
        count += 1

  return count

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
      expected = '1' if '0' else '0'

  return flips

def minFlipsToSecurePassword(pwd):
  flips = 0

  for i in range(0, len(pwd) - 1, 2):
    if pwd[i] != pwd[i + 1]:
      flips += 1
  return flips
