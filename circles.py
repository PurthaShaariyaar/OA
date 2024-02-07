# Required modules
import math
import os
import random
import re
import sys

# 1 Helper fcn with params (xA, yA, RA, xB, yB, RB) -> determine relationship
  # distance = abs(xA - xB) if yA == yB else abs(yA - yB)
  # run each check (memorize)
# Init results arr
# For pair in circlePairs -> assign (xA, yA, RA, xB, yB, RB) = map(int, pair.split())
# Call helper fcn -> assign val to relationships -> append relationships to results
# Return results

def circles(circlePairs):
  def determine_relationship(xA, yA, RA, xB, yB, RB):
    distance = abs(xA - xB) if yA == yB else abs(yA - yB)

    if distance == 0 and RA == RB:
      return "Concentric"
    # Check for touching circles
    elif distance == RA + RB or distance == abs(RA - RB):
      return "Touching"
    # Check for intersecting circles
    elif distance < RA + RB and distance > abs(RA - RB):
      return "Intersecting"
    # Check for disjoint-inside
    elif distance + min(RA, RB) < max(RA, RB):
      return "Disjoint-Inside"
    # Otherwise, they are disjoint-outside
    else:
      return "Disjoint-Outside"

  results = []
  for pair in circlePairs:
    xA, yA, RA, xB, yB, RB = map(int, pair.split())
    relationship = determine_relationship(xA, yA, RA, xB, yB, RB)
    results.append(relationship)
  return results



circlePairs = ["3 0 10 5 0 3", "0 1 4 0 1 5"]
print(circles(circlePairs))
