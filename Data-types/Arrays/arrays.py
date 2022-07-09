"""
    These are collections of items stored at contiguous memory locations and they 
    can only store one type of element.
"""
#Creating an array:
import array as arr

def printarray(a):
    for i in a:
        print(i, end=" ")
    pass

#creating an array of integer type:
a = arr.array('i', [1, 2, 3, 4])

#printing the array items:
printarray(a)
#the time complexity for creating arrays is 0(1)
#one can add elements using the insert() or append() method:
a.insert(0,19)
print("----------------------Inserting a 19 at position 1:----------------------")
printarray(a)