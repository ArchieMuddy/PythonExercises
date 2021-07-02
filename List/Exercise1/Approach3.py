# Swap the first and last elements of a list
# Approach 3: Use a tuple to store the first and last elements and then swap them

# Swapping function
def swapList(newList):

    #store the first and last element of the list in a tuple
    firstLast = newList[0], newList[-1]

    newList[-1], newList[0] = firstLast         #swap elements using the tuple

    return newList                              #return swapped list

#calling code
inputList =[12, 35, 9, 56, 24]
print(swapList(inputList))