# This is a code to capitalize the first and last character of each word in a string
def Capitalize(inputString):
    lst = inputString.split(" ")
    count = 0
    for i in lst:
        if (len(i)==1) or (len(i)==2):
            lst[count] = i.upper()
        else:
            firstchar, rem, lastchar = i[0], i[1:-1], i[-1]
            firstchar = firstchar.upper()
            lastchar = lastchar.upper()
            lst[count] = firstchar + rem + lastchar
        count+=1
    newString = " ".join(lst)
    return newString

#calling code
inputString = "I am a good bot"
print(Capitalize(inputString))
