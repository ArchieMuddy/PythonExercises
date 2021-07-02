# Approaches for finding the length of a list
# Approach1: Naive method

#Initializing List
inputList = [1, 4, 5, 7, 8]

# Printing list
print("The list is: {}".format(inputList))

#finding the length using a loop and a counter
counter = 0
for i in inputList:
    counter+=1

print("The length of the list is " + str(counter))