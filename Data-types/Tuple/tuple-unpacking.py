#demonstration:
tp = ("Lenny", "Weda", 25)
print(tp)

print("--------------------------unpacking the tuple--------------------------")
(first_name, second_name, age) = tp
print(f"The first name is {first_name} and the age is {age}")

print("--------------------------unpacking using the * -----------------------")
*names, age = ("Lenny", "Weda", "Orengo", 25)
print(f"The first arguments are {names} and the last one is {age}")

print("-----------------------unpacking using a function--------------------")
def multiply(x, y):
    return x*y
tp2 = (10, 3)

print(multiply(*tp2))