"""
TASK 2: Variables & Input

Goal:
- Learn variables
- Read user input
- Convert types

Notes:
- input() ALWAYS returns a string
- int() converts string to number
"""

# TODO 1:
# Ask the user for their name and store it in a variable
name = input("Name:\n")

# TODO 2:
# Ask the user for their age
# Convert it to an integer
age = input("Age: \n")
age = int(age)

# TODO 3:
# Print a greeting:
# Example: "Hello Alex, next year you will be 26"
print(f"Hello {name}, next year you will be {age+1}")

