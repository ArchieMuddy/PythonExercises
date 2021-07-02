# Swap the first and last elements of a list
#Approach 1: Use the length function and swap the first and last elements

# Swap Function
def SwapList(newList):
    size = len(newList)                #Find the length

    temp = newList[0]
    newList[0] = newList[size-1]       #swapping logic
    newList[size-1] = temp

    return(newList)                    #return swapped list
                                       #End of Function

# main code
newList = [12, 35, 9, 56, 24]
newList = SwapList(newList)
print(newList)
