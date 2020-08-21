import random


def common_elements_of_lists():
    """
    Take two lists, say for example these two:

      a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89] b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13] and write a program
      that returns a list that contains only the elements that are common between the lists (without duplicates).
      Make sure your program works on two lists of different sizes.

    Extras:

    1. Randomly generate two lists to test this
    2. Write this in one line of Python (don’t worry if you can’t figure this out at this point - we’ll get to it soon)
    """
    list_a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    list_b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    common_elements_list = list(set(list_a).intersection(set(list_b)))
    print(f'Common elements of lists: {common_elements_list}')


def common_elements_of_randomly_generate_lists(range_number_list_a: int, range_number_list_b: int):
    """
        1. Randomly generate two lists to test this
    """
    list_a = list(range(1, random.randint(2,range_number_list_a)))
    list_b = list(range(1, random.randint(2,range_number_list_b)))
    print (f'\nlist_a = {list_a}, \nlist_b = {list_b}')
    common_elements_list = list(set(list_a).intersection(set(list_b)))
    print(f'Common elements using randomly generate lists: {common_elements_list}')


def common_elements_of_lists_using_for(range_number_list_a: int, range_number_list_b: int):
    list_a = list(range(1, random.randint(2, range_number_list_a)))
    list_b = list(range(1, random.randint(2, range_number_list_b)))
    list_c = []
    for num in list_a:
        if num in list_b and num not in list_c:
            list_c.append(num)
    print(f'Common elements using for loop: {list_c}')


common_elements_of_lists()
common_elements_of_randomly_generate_lists(range_number_list_a=15, range_number_list_b=16)
common_elements_of_lists_using_for(range_number_list_a=5, range_number_list_b=7)
