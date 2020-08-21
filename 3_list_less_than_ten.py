def less_than_ten():
    """
    Take a list, say for example this one:

    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    and write a program that prints out all the elements of the list that are less than 5.

    Extras:

    1. Instead of printing the elements one by one, make a new list that has all the elements less than 5 from this list in
    it and print out this new list.
    2. Write this in one line of Python.
    3. Ask the user for a number and return a list that
    contains only elements from the original list a that are smaller than that number given by the user.
    """
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    print('Elements of list a that are less than 5')
    for x in a:
        if x < 5:
           print(x)

def less_than_ten_new_list():
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    less_than_five = []
    for x in a:
        if x < 5:
            less_than_five.append(x)
    print(f'Elements of list a that are less than 5: {less_than_five}')


def less_than_ten_new_list_in_one_line():
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    less_than_five = [x for x in a if x < 5]
    print(f'Elements of list a that are less than 5 using list comprehension: {less_than_five}')


def return_list_by_input_number(input_number: int):
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    # input_number = int(input("Provide a number and program returns list with elements, which are smaller than "
    #                          "provided number: "))
    list_smaller_than_input_number = [x for x in a if x < input_number]
    print(list_smaller_than_input_number)


less_than_ten()
less_than_ten_new_list()
less_than_ten_new_list_in_one_line()
return_list_by_input_number(input_number=6)
