# A set is an unordered collection of data type that is iteratable, mutable and has no duplicate elements.
#set initialization:

st = set()
print(st)
print("-----------------------------Initializing a set of strings--------------------------")
#creating a set of strings:
print(set("Lenny"))

#creating a set from a list:
st = set(["Lenny", "Weda", "Orengo", "Lenny"])
print(st)
print("------------------Adding elements using add-------------------------------")
st.add("Kevin")
print(st)
st.add(("Calvin", "Jack"))
print(st)
# accessing a set because a set cannot be accessed using indexes:
print("-----------------------------Accessing elements of a set-----------------------")
for i in st:
    print(i, end= " ")
#removing elements from a set, if not a member, it raises a key error:
print("\n------------------------------using remove() to remove an element-----------")
st.remove('Lenny')
print(st)

# The discard method does not raise a key error when the element is not found, it does nothing:
print("--------------------------using discard() method------------------------------")
st.discard("Lenny")
print(st)

#since a set is unordered, there is no way to know which element will be popped:
print("---------------------------using the pop() method-------------------------------")
st.pop()
print(st)

#The clear method pops all objects from the set
print("-------------------------------using the clear() method--------------------------")
st.clear()
print(st)
