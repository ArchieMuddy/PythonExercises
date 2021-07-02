# Code to find the minimum of 2 numbers
# Approach 1: Naive if-else

# minimum function
def minimum(a, b):
    if a<=b:
        return a
    else:
        return b

# calling code
a, b = 2, 4
print("The minimum of {} and {} is {}".format(a, b, minimum(a,b)))