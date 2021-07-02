# swap 2 elements in a list at positions pos1 and pos2
# Approach 2: Using the inbuilt list.pop function

def swapList(newList, pos1, pos2):
    epos1 = newList.pop(pos1)
    epos2 = newList.pop(pos2-1)
    newList.insert(pos1, epos2)
    newList.insert(pos2, epos1)
    return newList

# calling function
inputList = [23, 65, 19, 90]
pos1, pos2 = 1,3
print(swapList(inputList, pos1-1, pos2-1))
