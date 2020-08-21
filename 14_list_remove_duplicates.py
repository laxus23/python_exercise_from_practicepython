def remove_duplicates_from_list(list_a: list):
    """
    Write a program (function!) that takes a list and returns a new list that contains all the elements of the first
    list minus all the duplicates.

    Extras:

    Write two different functions to do this - one using a loop and constructing a list, and another using sets.
    Go back and do Exercise 5 using sets, and write the solution for that in a different function.
    :return:
    """
    list_a_without_duplicates = []
    for x in list_a:
        if x not in list_a_without_duplicates:
            list_a_without_duplicates.append(x)
    print(list_a_without_duplicates)


def remove_duplicates_from_list_by_set(list_a: list):
    """
    Function return a sets of list.
    :param list_a: list
    :return: print set of list_a
    """
    set_without_duplicates = set(list_a)
    print(set_without_duplicates)


remove_duplicates_from_list(list_a=[1, 1, 2, 2, 3, 5, 6, 7, 7, 22, 22, 33, 33, 44, 55, 55])
remove_duplicates_from_list_by_set(list_a=[1, 1, 2, 2, 3, 5, 6, 7, 7, 22, 22, 33, 33, 44, 55, 55])
