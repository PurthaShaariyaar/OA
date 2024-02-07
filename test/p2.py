# Required modules
import math
import os
import random
import re
import sys
from collections import deque

def getQueryResults(N, queries):
  good_array = [2**i for i in range(64) if (N >> i) & 1]
  answers = []

  for l, r, m in queries:
    l -= 1
    r -= 1
    product = 1
    for i in range(l, r + 1):
      product = (product * good_array[i]) % m
    answers.append(product)
  return answers

def scoreDifference(n, numSeq):
  sequence = deque(numSeq)
  first_score, second_score = 0, 0

  reverse = False

  for i in range(n):
    if reverse:
      num = sequence.pop()
    else:
      num = sequence.popleft()

    if i % 2 == 0:
      first_score += num
    else:
      second_score += num

    if num % 2 == 0:
      reverse = not reverse

  return first_score - second_score

def getFinalData(data, updates):
  n = len(data)

  negation_marks = [0] * (n + 1)

  for l, r in updates:
    negation_marks[l - 1] += 1
    negation_marks[r] -= 1

  negation_effect = 0
  for i in range(n):
    negation_effect += negation_marks[i]
    if negation_effect % 2 != 0:
      data[i] -= data[i]

  return data

def getTotalEfficiency(skills):
    skills.sort()

    sum_efficiencies = 0
    expected_sum = skills[0] + skills[-1]  # Sum of the first and last elements

    i, j = 0, len(skills) - 1
    while i < j:
        current_sum = skills[i] + skills[j]
        efficiency = skills[i] * skills[j]

        if current_sum != expected_sum:
            return -1

        sum_efficiencies += efficiency

        i += 1
        j -= 1

    return sum_efficiencies

def minFlipsToSecurePassword(pwd):
  flips = 0

  for i in range(0, len(pwd) - 1, 2):
    if pwd[i] != pwd[i + 1]:
      flips += 1
  return flips

def sentTimes(numberOfPorts, transmissionTime, packetIds):
  port_availability = [0] * numberOfPorts
  final_ports = []

  current_time = 1
  for packetId in packetIds:
    desired_port = packetId % numberOfPorts

    while current_time < port_availability[desired_port]:
      desired_port = (desired_port + 1) % numberOfPorts

    port_availability[desired_port] = max(current_time, port_availability[desired_port]) + transmissionTime

    final_ports.append(desired_port)
    current_time += 1
  return final_ports


# TEST 1

N = 26
queries = [
    [1, 2, 1009],
    [3, 3, 5]
]

output = getQueryResults(N, queries)
print(output)

# TEST 2
n = 5
numSeq = [3, 6, 2, 3, 5]
print(scoreDifference(n, numSeq))

# TEST 3
data = [1, -4, -5, 2]
updates = [[2, 4], [1, 2]]
print(getFinalData(data, updates))

# TEST 4
skills = [1, 2, 3, 2]
print(getTotalEfficiency(skills))

# TEST 5
pwd = "1110011000"
print(minFlipsToSecurePassword(pwd))

# TEST 6
numberOfPorts = 3
transmissionTime = 2
packetIds = [4, 7, 10, 6]
print(sentTimes(numberOfPorts, transmissionTime, packetIds))
