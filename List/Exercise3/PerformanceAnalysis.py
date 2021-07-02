#Performace analysis of different approaches for finding the length of a list

from operator import length_hint
import time

#Initializing List
inputList = list(range(1, 1000000))

# Printing list
print("The list is: {}".format(inputList))

#finding the length using a loop and a counter
start_time_naive = time.process_time_ns()
counter = 0
for i in inputList:
    counter+=1
end_time_naive = time.process_time_ns()
print("The length of the list is " + str(counter))
print("Time taken by naive method is {}".format((end_time_naive-start_time_naive)))

#finding the length using the len() function
start_time_len = time.time_ns()
length = len(inputList)
end_time_len = time.time_ns()
print("The length of the list is " + str(length))
print("Time taken by naive method is {}".format((end_time_len-start_time_len)))

# using length_hint()
start_time_len_hint = time.time_ns()
length = length_hint(inputList)
end_time_len_hint = time.time_ns()
print("The length of the list is: " + str(length))
print("Time taken by naive method is {}".format((end_time_len_hint-start_time_len_hint)))