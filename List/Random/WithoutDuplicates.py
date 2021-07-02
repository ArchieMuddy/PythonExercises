# This code takes a list and lists all the elements of this list without duplicates
# Approach: Take a list --> put it in a set (which removes duplicates --> Print the elements of the set

# Initialize list
lst = [1, 1, 2, 3, 4, 4, 4, 5, 6, 6, 6, 6, 6]
s = set(lst)

print("[", end="")
for i in s:
    print(i, end = ", ")

print("\b \b" + "]")