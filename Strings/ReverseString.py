# Code to reverse a string in Python

def reverseString(inputString):
    reversedString = inputString[:0:-1]
    return reversedString

inputString = input("Enter a String")
reverseString = reverseString(inputString)
print(reverseString)