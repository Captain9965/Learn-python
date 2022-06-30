#Method 1: iterating through all the keys:

from typing import OrderedDict

from collections import OrderedDict
dict = {"Kenya":"Nairobi", "South Africa":"Durban", "Namibia":"Windhoek", "Tanzania":"Dodoma"}
print(dict)

print("-------------------------iterating through all the keys:----------------")
for countries in dict.keys():
    print(countries)
print("-------------------------------get an ordered dict using the function orderedDict()-----------------")
# Note that we can use orderedDict to maintain the order of keys and values in a dictionary:
dict2 = OrderedDict(dict)
print(dict2)
for countries in dict2:
    print(countries)

print("-------------------Iterate through all key, value, pairs:---------------------------------")
for country, capital in dict2.items():
    print(f"The capital city of {country} is {capital}")