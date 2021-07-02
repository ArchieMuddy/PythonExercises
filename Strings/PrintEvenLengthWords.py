# This is a code to print even length words in a string

def printEvenLengthWords(inputString):
    lst = inputString.split(" ")
    for i in lst:
        if len(i)%2 == 0:
            print(i)

#calling code
inputString = "I am a good bot"
printEvenLengthWords(inputString)
