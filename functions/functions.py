"""
    keyword arguments: they allow the caller to specify the argument name with values so that the caller doesnt need to remember the 
    order of parameters
    Example:

"""
def student(firstname, lastname):
    print(firstname, lastname)
    return
#driver code:
student(firstname="Lenny", lastname="Weda")
print("--------------------arguments in any order-----------------------")
student(lastname="Weda", firstname="Lenny")
""" Variable length arguments: Can be used in advance when we do not know the number of arguments that will be passed to out function
"""
def print_arguments(*argv):
    for arg in argv:
        print(arg, end=" ")
print("----------------------variable length arguments:------------------------")
print_arguments("Lenny", 1, 4, 5)

def print_keyword_arguments(**kwargs):
    for key, value in kwargs.items():
        print("Key: ", key ," value: ", value)
print("----------------variable keyword arguments:-----------------------------")
print_keyword_arguments(name = "Lenny", age = "unknown", hobby = "coding")
