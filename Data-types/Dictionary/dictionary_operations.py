#creating a dictionary:
from copy import copy


dict = {}
print(dict)

# assigning values:
dict = {"Name": "Paul", "Age": 35, "Hobby": "Soccer"}
print(dict)

print("-------------getting the values in a list:-----------------------")
print(dict.values())

print("--------------------getting the keys:----------------------------")
print(dict.keys())

print("-------------------deleting an entry from a dict using del:----------------")
del dict["Age"]
print(dict)
print("-------------------------copy the dictionary----------------------------")
dict2 = dict
print(dict2)

print("--------------------finding the number of entries-------------------------")
print(len(dict))

print("-------------------------------safely updating values without exceptions----------------------")
dict.update({"Name":"Kennedy"})
print(dict)
print("--------------------------------safely copying elements using copy()------------------")
dict3 = copy(dict)
print(dict3)
print("----------------------clearing the dict--------------------------")
dict.clear()
print(dict)