# This is a code to remove the ith character from a string

def removeithcharacter(inputString, i):
    beforei, ithchar, afteri = inputString[0:i-1], inputString[i-1], inputString[i:]
    newString = beforei + afteri
    return newString

inputString = "HelloWorld"
i = 5
print((removeithcharacter(inputString, i)))