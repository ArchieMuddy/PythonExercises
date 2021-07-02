# Swap 2 elements in the list placed at pos1 and pos2
# Approach 1: Swap using comma variables

#Swapping function
def swapList(newList, pos1, pos2):
    newList[pos1], newList[pos2] = newList[pos2], newList[pos1]
    return newList

#calling function
inputList = [23, 65, 19, 90]
pos1, pos2 = 1,3

print(swapList(inputList, pos1-1, pos2-1))