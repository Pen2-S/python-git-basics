"""
TASK 4: Loops

Goal:
- Learn for and while loops
- Understand repetition

Notes:
- range(start, stop)
- stop is NOT included
"""

# TODO 1:
# Use a for-loop to print numbers from 1 to 5
print("==========For===============")
numbers = range(1, 6)
for x in numbers:
    print(x)


# TODO 2:
# Use a while-loop to do the same thing
print("==========While==============")
i=1
while i < 6:
    print(i)
    i+=1
# TODO 3 (optional):
# Print only even numbers from 1 to 20
print("=========EN=================")
i=1
while i <= 20:
    if i % 2 == 0:
        print(i)
    else:
        pass
    i+=1
    
