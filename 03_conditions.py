"""
TASK 3: Conditions (if / else)

Goal:
- Learn decision making in Python

Notes:
- No curly braces {}
- Indentation is VERY important
"""

# TODO 1:
# Ask the user for their age (as int)
print("What's your age?: \n")
age = input()
age = int(age)
# TODO 2:
# If age >= 18 print "You are an adult"
# Otherwise print "You are a minor"

if age >= 65:
    print("Still alive?")
elif age >= 18:
    print("Big bro")
else:
    print("Small, grow up")

# TODO 3 (optional):
# Add another condition:
# If age >= 65 print "You are retired"
