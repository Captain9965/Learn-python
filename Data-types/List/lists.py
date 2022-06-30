#just like arrays declared in other languages. May contain integers, Strings as well as objects.
# They can store multiple data at the same time and unlike sets, they are ordered and have a definite count
#They are zero indexed

#creating a list:
from ctypes import sizeof


list = []
print(list)

#list of strings:
list = ["Lenny", "Weda"]
print(list)

#Multidimentional list:

list = [["Lenny", "Weda"], [1, 2]]
print(list)
print("--------------------------------------------------------------------------------------------------------------")
#adding elements to a list:
#1. using append():
list = []
list.append([1, 4])
list.append("four")
print(list)

#using insert():
list = ["Lenny", "Weda"]

#one can specify the index:
list.insert(0,["twenty twenty two"])
print(list)

#using extend:
list.extend(["is", "my", "birthday"])
print(list)

#element access:
print(list[1])
print(list[0:3])

#removing a specific element:
list.remove("Lenny")
print(list)

#pop the last element:
list.pop()
print(list)
#pop a specific element:
list.pop(0)
print(list)
