# Swap the first and last elements of a list
# Approach 4: Use the * operand

inputList =[12, 35, 9, 56, 24]

first, *remaining, last = inputList     #stores first element in first, last element in last and remaining element in *remaining

newList = last, *remaining, first       #swap first and last
print(newList)