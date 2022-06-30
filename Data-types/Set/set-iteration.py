from timeit import default_timer as timer
import itertools
import random

#function under evaluation:
def test_for_loop(test_set):
    for val in test_set:
        _ = val
def test_enumeration(test_set):
    for i, val in enumerate(test_set):
        _ = val
def test_indexed_list(test_set):
    test_list = list(test_set)
    for id in range(len(test_list)):
        _ = test_list[id]
def test_list_constructor(test_set):
    list(val for val in test_set)
def test_set_comprehension(test_set):
    [val for val in test_set]
def test_set_map_lambda(test_set):
    [map(lambda val : val, test_set)]
def test_iterator(test_set):
    for val in iter(test_set):
        _ = val
def test_iterator_while(test_set):
    iter_gen = iter(test_set)
    while True:
        try: 
            next(iter_gen)
        except StopIteration:
            break
#driver function:
if __name__ == '__main__':
    random.seed(21)
    for _ in range(5):
        test_set = set()

        #generating a set of random numbers:
        for r in range(int(1e6)):
            k = random.random()
            test_set.add(k)
        # print("-------------------Test for loop--------------------------")
        # start = timer()
        # test_for_loop(test_set)
        # end = timer()
        # print(str(end - start))
        # print("------------------------Test enumeration-------------------")
        # start = timer()
        # test_enumeration(test_set)
        # end = timer()
        # print(str(end - start))

        # print("------------------Iterating over a set as and indexed list---------")
        # start = timer()
        # test_indexed_list(test_set)
        # end = timer()
        # print(str(end - start))

        # print("---------------------Iterating over a set using comprehension and list constructor-initializer--------------")
        # start = timer()
        # test_list_constructor(test_set)
        # end = timer()
        # print(str(end - start))

        # print("----------------------------Iterate using set comprehension----------------------")
        # start = timer()
        # test_set_comprehension(test_set)
        # end = timer()
        # print(str(end- start))

        # print("------------------Iterate using map, lambda and list comprehension-------------------")
        # start = timer()
        # test_set_map_lambda(test_set)
        # end = timer()
        # print(str(end - start))

        # print("-------------------------Iterate using iterator:-----------------------------------")
        # start = timer()
        # test_iterator(test_set)
        # end = timer()
        # print(str(end - start))

        print("-----------------Using iterator and while loop:-----------------------------------------")
        start = timer()
        test_iterator_while(test_set)
        end = timer()
        print(str(end - start))
#verdict:
"""
Among the loops, a simple for loop iteration and a simple looping over iterators works best
But for overall perfomance, using map with lambda over set or iterator of set gives the best perfomance

"""