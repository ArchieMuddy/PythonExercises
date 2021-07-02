# Code to check whether a string entered by the user is a palindrome or not

# function to check palindrome
def checkPalindrome(inputString):
    if inputString[0] == inputString[-1]:
        if (len(inputString) == 1) or (len(inputString) == 2):
            return 1
        else:
            x = checkPalindrome(inputString[1 : len(inputString) - 1])
            return x
    else:
        return 0

#calling code
inputString = input("Enter the string")
x = checkPalindrome(inputString)
if x==1:
    print("{0} is a palindrome".format(inputString))
else:
    print("{0} is not a palindrome".format(inputString))