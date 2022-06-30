#In python, updation and deletion of strings is not allowed as string objects are immutable.
import enum
from tokenize import String


name = "Guido Van Rossum"

#using slice:
s1 = slice(0, 3, 1)
print(name[s1])
s2 = slice(0, 6, 1)
print(name[s2])
s3 = slice(-1)
print(name[s3])

#using list or array slicing:
print(name[0: 3: 1])
print(name[:-1])

#if you want to reverse a string:
print(name[::-1])