# Required modules
import math
import os
import random
import re
import sys

def playSegments(coins):
    total_score = sum(coins)  # Total possible score
    player1_score = 0
    for i in range(len(coins)):
        player1_score += coins[i]
        # Maximum score Player 2 can achieve if Player 1 stops here
        player2_max_possible_score = total_score - player1_score
        if player1_score > player2_max_possible_score:
            return i + 1  # Return the number of segments Player 1 must play
    return len(coins)  # In case Player 1 needs to play all segments to win

# Example usage
coins = [1, 1, 0, 1]
print(playSegments(coins))  # Output: 2

