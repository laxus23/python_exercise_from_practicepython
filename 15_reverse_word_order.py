def reverse_word_order():
    """
    Write a program (using functions!) that asks the user for a long string containing multiple words. Print back to
    the user the same string, except with the words in backwards order. For example, say I type the string: :return:
    """
    user_input = input("Provide a string to reverse:\n")
    list_with_split_word = user_input.split()[::-1]
    reverse_word = ''
    for x in list_with_split_word:
        reverse_word += x + ' '
    print(reverse_word)


def reverse_word_order_2():
    user_input = input("Provide a string to reverse:\n")
    print(' '.join(user_input.split()[::-1]))


reverse_word_order()
reverse_word_order_2()
