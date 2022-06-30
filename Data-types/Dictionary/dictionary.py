"""
A dictionary is an unordered collection of data values, used to store data like a map
"""
#creating a dictionary:
dict = {}
print(dict)

# assigning values:
dict = {"Name": "Paul", "Age": 35, "Hobby": "Soccer"}
print(dict)

print("-----------------Adding elements to the dictionary---------------------")
# adding elements to the dict:
dict["Status"] = "married"
print(dict)

print("-----------------------updating the keys----------------------")
dict["Name"] = "Kennedy"
print(dict)

#element access, N/B get() is preferrably used because it does not raise a key error
print("------------------------Element access--------------------------")
print(dict["Hobby"])
print(dict.get("Age"))

#removing elements from a dictionary, pop requires the key as the argument:
print("------------------------Removing elements from a dictionary---------------------")
dict.pop("Name")
print(dict)

#using pop_item(), it removes the last key-value pair
print("------------------------using popitem-----------------------------------------")
dict.popitem()
print(dict)



