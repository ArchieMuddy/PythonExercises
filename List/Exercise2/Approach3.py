# Swap 2 elements in a list at positions pos1 and pos2
# Approach 3: Use a tuple variable

# swapping function
def swapList(newList, pos1, pos2):
    tup = newList[pos1], newList[pos2]
    newList[pos2], newList[pos1] = tup
    return newList

# calling code
inputList = [23, 65, 19, 90]
pos1, pos2 = 1,3
print(swapList(inputList, pos1-1, pos2-1))
