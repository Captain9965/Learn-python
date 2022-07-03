"""
    closures refer to function objects that remember values in enclosing scopes even when they are not present in memory
    unlike a plain function, they allow the function to access those captured variables through the closure's copies of their values or references.
    Illustration:

"""
import logging
logging.basicConfig(filename='example.log', level=logging.INFO)

def logger(func):
    def log_func(*args):
        logging.info(
            'Running "{}" with arguments {}'.format(func.__name__, args)
        )
        print(func(*args))
    return log_func

def add(x, y):
    return x+y
def sub(x,y):
    return (x-y) if x>y else (y-x)

add_logger = logger(add)
sub_logger = logger(sub)

add_logger(4, 6)
sub_logger(4, 6)