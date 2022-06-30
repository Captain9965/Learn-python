"""
    In python, functions are treated as first class objects. First class objects in a language are handled uniformly throughout.
    they may be stored in data structures, passed as arguments and used in control structures.
    Properties of first class functions:
        1. A function is a instance of Object Type
        2. One can store the function in an object
        3. The function can be passed as a parameter to another function
        4. One can return the function from a function
        5. One can store them in data structures such as hash_tables, lists
    And inner function is a funcion that is defined inside another function and hence it can access data members only within the function
    in which it was defined.
Example:

"""
def OuterFunction(text):
    text = text
    def innerFunction(text):
        print(text)
    innerFunction(text)
def changeOutervarWithIteratable():
    s = ['Lenny']
    def changewithInner():
        s[0] = 'Weda'
        print(s)
    #this is changed with 
    changewithInner()
    print(s)



if __name__ == '__main__':
    OuterFunction("Lenny")
#One must however call the outer function first!
    print("-------changing the value of the outer function-------------------")
    changeOutervarWithIteratable()




