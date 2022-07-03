"""
    used to end execution of a function. 
    If used without an expression, a special value called None is returned.

"""

#returning multiple values using an object:
class Test:
    def __init__(self):
        self.name = 'Lenny'
        self.age = 19

def return_obj():
    return Test()
#returning multiple values using a tuple:
def return_tuple():
     name = 'Lenny'
     age = 19
     return name, age

def return_list():
    name = 'Lenny'
    age = 19
    return [name, age]
def return_dict():
    return {"name": 'Lenny', "age": 19}

t = return_obj()
print("----------------returning multiple values with objects:-------------------")
print(t.name , t.age)
print("----------------returning multiple values with a tuple:-------------------")
#unpack the values:
name, age = return_tuple()
print(name, age)
print("----------------returning a list------------------------------")
list = return_list()
print(list[0], list[1])
print("-----------------returning a dictionary------------------------")
dict = return_dict()
print(dict.get("name"), dict.get("age"))

