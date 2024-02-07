# Required modules
import math
import os
import random
import re
import sys

# Find len of start assign to n
# Init tasks to tuple of start[i], end[i] by for looping through n
# Sort the tasks with key lambda x: x[1] > init machines arr
# For loop through all tasks > init found to False > inner for loop range of len(machines)
# For each machine check if machines[i] <= task[0] > if so machines[i] = task[1] > found = True > break
# If not found append task[1] to machines
# Return length of machines

def getMinMachines(start, end):
  n = len(start)

  tasks = [(start[i], end[i]) for i in range(n)]

  tasks.sort(key=lambda x: x[1])

  machines = []

  for t in tasks:
    found = False
    for i in range(len(machines)):
      if machines[i] <= t[0]:
        machines[i] = t[1]
        found = True
        break

    if not found:
      machines.append(t[1])

  return len(machines)

start = [1, 8, 3, 9, 6]
end = [7, 9, 6, 14, 7]
result = getMinMachines(start, end)
print(result)
