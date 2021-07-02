# Swap the first and last elements of the list
# Approach 2: Don;t use the len function. Instead use list[-1] to access the last element of the list

#swap function
def swapList(newList):

    newList[0], newList[-1] = newList[-1], newList[0]       #swapping logic without temp variable

    return newList

#calling code
inputList = [12, 35, 9, 56, 24]
print(swapList((inputList)))