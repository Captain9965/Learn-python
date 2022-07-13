"""
    the try clause is first executed. If there is no exception, only the try clause will run. 
    the exception is run, however, if there is an exception. If the exception is not handled, 
    it is passed on to the outer tries. If it is not handled, then execution stops
    Example:


"""
def try_division(x, y):
    try:
        result = x/y
        print("The answer is ", result)
    except ZeroDivisionError:
        print("You cannot divide by zero man!!")
    else:
        return result
try_division(5,2)

"""
    Raising an exception:
    use the keyword raise 
"""