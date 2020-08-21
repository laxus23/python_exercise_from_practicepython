import random

def guess_a_number():
    """
    Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number, then tell them
    whether they guessed too low, too high, or exactly right. (Hint: remember to use the user input lessons from the
    very first exercise)

    Extras:

    Keep the game going until the user types “exit”
    Keep track of how many guesses the user has taken, and when the game ends, print this out.
    :return:
    """

    game = '1'
    number_of_guesses = 0
    random_number = random.randint(0, 9)
    while game == '1':
        user_guess = int(input("Guess a generate number: "))
        if random_number == user_guess:
            number_of_guesses += 1
            print(f'Excellent! You guess {user_guess} and the generate number is {random_number}! You needed '
                  f'{number_of_guesses} attempts to type correctly!')
        elif random_number > user_guess:
            number_of_guesses += 1
            print(f'Your number is {user_guess} and it is too low')
        else:
            number_of_guesses += 1
            print(f'Your number is {user_guess} and it is too high')
        game = input('Do u wanna play again? Choose 1 if yes\n')


guess_a_number()
