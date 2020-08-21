import datetime


def when_user_reach_100_years(name: str, age: int, how_many_copies: int):
    """
    Create a program that asks the user to enter their name and their age. Print out a message addressed to them that
    tells them the year that they will turn 100 years old.

    Extras:
    1. Add on to the previous program by asking the user for another number and printing out that many copies of the
    previous message. (Hint: order of operations exists in Python)
    2. Print out that many copies of the previous message on
    separate lines. (Hint: the string "\n is the same as pressing the ENTER button)
    """
    # name = input("Please provide your name: ")
    # age = int(input("Please provide your age: "))
    # how_many_copies = int(input("How many copies of message you need: "))
    current_time = (datetime.datetime.now())
    if age < 100:
        future_age = (100 - age) + current_time.year
    elif age == 100:
        future_age = current_time.year
    else:
        future_age = current_time.year - (age - 100)
    while how_many_copies > 0:
        print(f'\nHello, {name}. You will turn 100 of years on {future_age}')
        how_many_copies -= 1


when_user_reach_100_years(name="Adam", age=120, how_many_copies=3)
