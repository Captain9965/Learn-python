"""
frozenset() takes an iteratable object as input and makes it immutable.
Since they are immutable, they are mainly used as keys in dictionary or elements in other sets
Illustration:

"""
Student = {"Name": "Lenny", "Age": 21, "Job Description": "Firmware Engineer"}

key = frozenset(Student)

print("The frozen set of the object Student is ->", key)