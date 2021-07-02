# Find maximum of 2 numbers

def maximum(a, b):
    if a >= b:
        print("a is greater")
        return a
    else:
        print("b is greater")
        return b

# driver code
a, b = 2, 4
print("The maximum of the 2 numbers is " + str(maximum(a, b)))