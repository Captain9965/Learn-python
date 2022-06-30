#in python, strings are arrays of bytes representing unicode characters, hence, python doesnt have a character data-type but
# instead a character is simply a string of length 1
# There are several methods that can be used to concatenate strings:
# 
# 1. using the + operator:

string1 = "Lenny"
string2 = "Weda" 

name = string1 + " " + string2
print(name)

# 2. using the join operator: it returns a string in which the elements of the sequence have been joined by an str seperator:
print("".join([string1, string2]))
#inserting a space:
print(" ".join([string1, string2]))
#inserting a comma:
print(" ,".join([string1, string2]))

