#Ways of iterating over list elements:
list = []
for i in range(5):
    list.append(i*20)

#1. using a for loop:
print("--------------------------For loop:---------------------------------------------")
for ls in list:
    print(ls)
#2. using for loop and range:
length = len(list)
print("-----------------------for loop and range:---------------------------------------")
for i in range(length):
    print(list[i])
#using a while loop:
print("--------------------------------using while loop:----------------------------------")
i = 0
while (i< length):
    print(list[i])
    i+=1
# 3. using list comprehension:
print("------------------------------list comprehension:-------------------------------------")
[print(i) for i in list]
 #5. using enumerate:
print("------------------------using enumerate:------------------------------------------")

for i, val in enumerate(list):
    print(f"{i}, {val}")

print("----------------------------using numpy------------------------------")
#using numpy especially when using very large n-dimensional lists:
import numpy as np
#creating an array using the arrange method:
arr = np.arange(0, 9, 1)
print(arr)

#shape arrays with 3 rows and 3 columns:
arr = arr.reshape(3, 3)
print(arr)

#numpy iteration:
print("---------------------------------numpy iteration-------------------")
for i in np.nditer(arr):
    print(i)


