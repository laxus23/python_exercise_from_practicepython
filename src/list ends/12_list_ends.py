import random


def marignal_elements(list_to_convert: list):
    """
    Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25]) and makes a new list of only
    the first and last elements of the given list. For practice, write this code inside a function.
    :return:
    """
    # a = [5, 10, 15, 20, 25]
    converted_list = [x for x in list_to_convert if x == list_to_convert[0] or x == list_to_convert[-1]]
    print(converted_list)
    # converts list by loop
    converted_list_loop = []
    for x in list_to_convert:
        if x == list_to_convert[0] or x == list_to_convert[-1]:
            converted_list_loop.append(x)
    print(converted_list_loop)


def marignal_elements_by_list_comprehension(list_to_convert: list):
    print([list_to_convert[0], list_to_convert[-1]])


def marignal_elements_by_function():
    list_to_convert = random.sample(range(10, 100), 5)
    print([list_to_convert[0], list_to_convert[len(list_to_convert) - 1]])
    print(list_to_convert)


marignal_elements(list_to_convert=[5, 2, 3, 4, 10, 15, 20, 25])
marignal_elements_by_list_comprehension(list_to_convert=[1, 3, 4, 33, 332, 22, 49])
marignal_elements_by_function()
