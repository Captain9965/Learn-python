"""
    These are lambda/anonymous functions...can have any numer of arguments but can only have only one expression:


"""

square = lambda x: x * x

print (square(10))

#list comprehension with lambda functions:
a = [(lambda x: x*x)(x) for x in range(5)]
print(a)