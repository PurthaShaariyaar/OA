# Required modules
import math
import os
import random
import re
import sys

# Sort skills in reverse order > assign totEff = 0 and leftP, rightP = 0, len(skills) -1
# While loop as long as l < r: update currEff as product of skills[leftp] * skills[rightP]
# Update totEff += currEff > update leftP += 1 and rightP -=1 > if l == r return -1
# Return totEff

def getTotalEfficiency(skills):
    # Sort the skills array
    skills.sort()

    # Initialize variables for sum of efficiencies and expected sum of skills for each team
    sum_efficiencies = 0
    expected_sum = skills[0] + skills[-1]  # Sum of the first and last elements

    # Iterate through the sorted list to form pairs and calculate efficiency
    i, j = 0, len(skills) - 1
    while i < j:
        # Calculate current sum and efficiency of the pair
        current_sum = skills[i] + skills[j]
        efficiency = skills[i] * skills[j]

        # If the current sum doesn't match the expected sum, return -1
        if current_sum != expected_sum:
            return -1

        # Add the current efficiency to the total sum of efficiencies
        sum_efficiencies += efficiency

        # Move towards the center of the list
        i += 1
        j -= 1

    # Return the total sum of efficiencies
    return sum_efficiencies

# Example usage
skills = [1, 2, 3, 2]
print(getTotalEfficiency(skills))

