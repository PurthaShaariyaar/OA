# Required modules
import math
import os
import random
import re
import sys

# Assign vowels and consonants to each of their sets
# Check each char for has_alpha, has_vowel and has_consonant
# return has_alpha and has_vowel and has_consonant and len(word) >= 3
# Need helper fcn num_valid_words(s): assign words = s.split
# Assign valid_word_count = sum(is_valid_words)
# return valid_word_count

def is_valid_word(word):
  vowels = set("aeiouAEIOU")
  consonants = set("bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ")

  has_alpha = any(char.isalnum() for char in word)
  has_vowel = any(char in vowels for char in word)
  has_consonant = any(char in consonants for char in word)

  return has_alpha and has_vowel and has_consonant and len(word) >= 3

def num_valid_words(s):
  words = s.split()
  valid_word_count = sum(is_valid_word(word) for word in words)
  return valid_word_count


# Example usage:
input_string = "Hello, this is a test string with valid words like apple and 123."
result = num_valid_words(input_string)
print(result)

