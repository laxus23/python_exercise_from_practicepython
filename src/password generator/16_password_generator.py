import random


def password_generator(user_choice: int):
    """
    Write a password generator in Python. Be creative with how you generate passwords - strong passwords have a mix
    of lowercase letters, uppercase letters, numbers, and symbols. The passwords should be random, generating a new
    password every time the user asks for a new password. Include your run-time code in a main method.

    Extra:

    Ask the user how strong they want their password to be. For weak passwords, pick a word or two from a list.
    :return:
    """
    weak_pass_list = ['cat', 'dog']
    # user_choice = int(input("Do u need:\n1 - weak password\n2 - strong password\n"))
    user_choices = []
    x = 0
    while x < 100:
        if user_choice == 1:
            weak_pass = random.choice(weak_pass_list) + random.choice(weak_pass_list)
            if weak_pass not in user_choices:
                print(weak_pass)
                print(True)
                user_choices.append(weak_pass)
        x += 1
    # elif user_choice == 2:
    

password_generator(user_choice=1)
