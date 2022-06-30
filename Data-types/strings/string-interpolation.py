
#string interpolation is the process of substituting values of variables in placeholders in a string:
string1 = "lenny"
string2 = "Weda"
# 1.. using the % operator:
print("%s %s %d" % (string1, string2, 7))

#2. using the format function. It lets us concatenate elements within a string through positional formatting:
print("My name is {} {}".format(string1, string2))
#3. one can use variable names inside the curly braces and substitute in any order:
print("My name is {n1} {n2}".format(n2 = string2, n1 = string1))

#4. using the f-string( literal string interpolation )
print(f"My name is {string1} {string2}")
# it can also be used to do some arithmetic:
a = 10
b = 2
c = 3
print(f"{a} * {b} * {c}")

#string template class
from string import Template
n= Template("My name is $name1 $name2")
print(n.substitute(name1 = string1, name2 = string2))

