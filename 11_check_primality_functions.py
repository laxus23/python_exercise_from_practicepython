def is_prime_number_from_input():
    """
    Ask the user for a number and determine whether the number is prime or not. (For those who have forgotten,
    a prime number is a number that has no divisors.). You can (and should!) use your answer to Exercise 4 to help
    you. Take this opportunity to practice using functions, described below.
    :return:
    """
    while True:
        try:
            users_input = int(input("Please provide a number: "))
            is_prime(number=users_input)
        except:
            print("This isn't a number")
        game = input('Do u wanna play again? Press 1 if yes\n')
        if game != '1':
            return False


def is_prime(number: int):
    """
    Function check, if number is a prime number.
    :param number: random integer
    :return: print prime or not prime number
    """
    prime_list = [x for x in range(2, number) if number % x == 0]
    if number > 1 and len(prime_list) == 0:
        print(f'Number {number} is a prime number')
    else:
        print(f'Number {number} is not a prime number')


is_prime_number_from_input()
