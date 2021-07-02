# Finding the length of a list
# Approach 2: length_hint() from the operator class method

from operator import length_hint

# initialize list
inputList = [1, 4, 5, 7, 8]
print(inputList)

# using length_hint()
length = length_hint(inputList)
print("The length of the list is: " + str(length))