"""
     In python, all objects are instances of the class object.
     Hence, the object class is the base class for all other classes.
     In the case of multiple inheritance, a given attribute is first searched in the current class. If it is not found, it is then
     searched for in the parent classes. The order that is followed is called linearization and is 
     found out using a set of rules called Method Resolution Order(MRO). 
     To view the MRO of a class, use the method mro() which returns a list or the __mro__ attribute which returns a tupe
"""

class class1:
    def m(self):
        print("In class 1")
class class2(class1):
    def m(self):
        print("In class 2")
        super().m()
class class3(class2):
    def m(self):
        print("In class 3")
        super().m()
class class4(class3):
    def m(self):
        print("In class 4")
        super().m()

if __name__ == "__main__":
    print(class4.mro())
    print(class4.__mro__)