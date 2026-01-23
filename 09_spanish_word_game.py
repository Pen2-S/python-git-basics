"""
TASK 9: Mini Game 🎮 Spanish Word Quiz

Goal:
- Build a small interactive game
- Combine random selection, input, and conditions

Game rules:
1. Select ONE random Spanish word
2. Select TWO additional random English translations (wrong ones)
3. Shuffle the options
4. Ask the user to choose the correct translation

Example:
What is the correct translation for "que"?

1) who
2) that
3) when

Your answer: 2
Correct! 🎉
"""

import json
import random


# TODO 1:
# Load the JSON file (same as Task 8)


# TODO 2:
# Select ONE random word (this is the correct answer)
# Example:
#   {"spanish": "que", "english": "that"}


# TODO 3:
# Extract the Spanish word from the selected word
# Extract the correct English translation
# Example:
#   spanish_word = "que"
#   correct_translation = "that"


# TODO 4:
# Select TWO MORE random English translations
# Make sure they are NOT the correct one
# If any of selected matches the correct translation, re-select
# Example:
#   {"spanish": "con", "english": "with"}
#   {"spanish": "como", "english": "how"}


# TODO 5:
# Extract the wrong English translations
# Example:
#   wrong_translation1 = "with"
#   wrong_translation2 = "how"


# TODO 6:
# Combine correct + wrong translations into a list
# Shuffle the list


# TODO 7:
# Print the Spanish word and numbered options (1, 2, 3) with translations
# The numbers should be 1, 2, 3 NOT 0, 1, 2
# Example:
# What is the correct translation for "que"?
# 1) who
# 2) that
# 3) when


# TODO 8:
# Ask the user for their answer as a number (1, 2, or 3)
# Convert input to integer


# TODO 7:
# Check if the answer is correct
# Hint:
# - Use the user's input to get the selected translation from the list
# - List indices start at 0, so adjust accordingly
# Print:
# - "Correct! 🎉"
# - or "Wrong 😅"
