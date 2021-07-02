# Swap the first and last elements in a list
# Approach 5: Use inbuilt list.pop() function

def swapList(newList):
    first = newList.pop(0)
    last = newList.pop(-1)

    newList.insert(0, last)
    newList.append(first)

    return newList

# calling function
inputList = [12, 35, 9, 56, 24]
print(swapList(inputList))