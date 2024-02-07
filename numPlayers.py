# Required modules
import math
import os
import random
import re
import sys

# Sort the scores in reverse order using .sort(reverse=True)
# Assign k = min(k, len(scores)) > assign curr_rank = 1 and level_up_count = 0
# For loop range(k) > 2 if statements: 1 if scores[i] > 0 -> level_up_count += 1
# 2nd if statement if i < k - 1 and scores[i] != scores[i + 1] -> curr_rank += 1
# Return level_up_count

def numPlayers(k, scores):
    # Filter out players with a score of 0
    filtered_scores = [score for score in scores if score > 0]

    # Sort the scores in descending order
    sorted_scores = sorted(filtered_scores, reverse=True)

    # Initialize the count of players who can level up
    can_level_up = 0

    # Iterate through the sorted scores and count how many players can level up
    for i, score in enumerate(sorted_scores):
        # The rank of the current player is i + 1 (due to zero-based indexing)
        # If the rank is within the cutoff, increase the count
        if i < k or sorted_scores[i] == sorted_scores[k-1]:
            can_level_up += 1
        else:
            break  # No need to check further if rank is beyond cutoff

    return can_level_up


# Example usage:
k_value = 3
player_scores = [100, 50, 50, 25]
result = numPlayers(k_value, player_scores)
print(result)
