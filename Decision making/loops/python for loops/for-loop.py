"""A pythonic for loop is used to loop over an iterator while in other 
    languages, it is used to loop over a condition
"""
# a gotcha:
num_list = [2, 4, 6, 8]
squares = (n**2 for n in num_list)

#returns true:
print(16 in squares)
#returns false:
print(16 in squares)

doubles = (n*2 for n in num_list)
print(list(doubles))
#getting a weird answer 0 instead of 40 :
print(sum(doubles))

"""
this is due to the fact that a for loop in python is really a foreach loop, which instead of working on an index, works on the element itself

"""
#lets try looping using indices:
print("---------------------------------------------looping using indices----------------------------------------------")
i = 0
while i < len(num_list):
    print(num_list[i])
    i +=1

#python uses iterators instead for looping:
#the iter function can be used to extract an iterator from an iteratable:
print("----------------------------------------using next with an iteratable:---------------------------------------------")
names = ("Lenny", "Japheth", "Weda")
print(iter(names))

iteratable_obj = iter(names)
print(next(iteratable_obj))
print(next(iteratable_obj))

#once an item is used up in an iterator, it is deleted from memory!
print("-----------------------------------using a custom for loop:-------------------------------------------------------------")
#custom for loop:
def forloop(iteratable):
    _iter = iter(iteratable)
    finished_loop = False

    while not finished_loop:
        try:
            next_item = next(_iter)
        except StopIteration:
            finished_loop = True
        else:
            print(next_item)

forloop(names)

"""
    The solution to the gotchas is to do the operation before converting the iteratable to a list, as 
    this involves iterating over the object, thus exhausting the interatable.

"""