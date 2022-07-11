"""
    whenever an object is created in python, the operators __new__ and __init__ are called.New is called when the object is 
    created while __init__ is called when the object is being initialized.

    Demonstration:

"""
# Python program to 
# demonstrate __new__
  
# don't forget the object specified as base
class A(object):
    def __new__(cls):
         print("Creating instance")
         return super(A, cls).__new__(cls)
  
    def __init__(self):
        print("Init is called")
  
A()