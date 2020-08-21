def check_if_string_is_palindrome(input_string: str):
    """
    Ask the user for a string and print out whether this string is a palindrome or not. (A palindrome is a string
    that reads the same forwards and backwards.)
    """
    # input_string = input("Please provide a string: ")
    if input_string == input_string[::-1]:
        print('This string is a palindrome')
    else:
        print("This string isn't a palindrome")


check_if_string_is_palindrome("ada")
