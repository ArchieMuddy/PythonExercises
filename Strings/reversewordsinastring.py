# This is a code to revers the order of all words in the string

inputString = input("Enter a String")
lst = list(inputString.split(" "))
length = len(lst)
lst = lst [length: :-1]
newString = " ".join(lst)
print(newString)
