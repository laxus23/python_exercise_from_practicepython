def odd_or_even(user_number: int, num: int, check: int):
    """
    Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to
    the user. Hint: how does an even / odd number react differently when divided by 2?

    Extras:

    1. If the number is a multiple of 4, print out a different message.
    2. Ask the user for two numbers: one number to check (
    call it num) and one number to divide by (check). If check divides evenly into num, tell that to the user. If not,
    print a different appropriate message.
    """
    if user_number % 2 == 0:
        if user_number % 4 == 0:
            print(f'Your number is {user_number} and this is even number and it is a multiple of 4')
        else:
            print(f'Your number is {user_number} and this is even number')
    else:
        print(f'Your number is {user_number} and this is odd number')
    if num % check == 0:
        print(f'{num}\n{check}\nCheck divides evenly into num')
    else:
        print(f'{num}\n{check}\nCheck not divides evenly into num')


odd_or_even(user_number=10, num=20, check=5)
