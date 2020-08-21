def rock_paper_scissors_game():
    """
    Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), compare them, print out a
    message of congratulations to the winner, and ask if the players want to start a new game)

    Remember the rules:

    Rock beats scissors
    Scissors beats paper
    Paper beats rock
    """
    while True:
        global players_choice_list
        players_choice_list = []
        players_choice(player='Player 1')
        players_choice(player='Player 2')
        compare_choices()
        retry = input('Do u wanna play again? Choose 1 if yes\n')
        if retry == '1':
            continue
        else:
            print('Thank you for game!')
            return False


def print_chooses(player_choice: str, player: str):
    """
    Print players choices.
    :param player_choice: players choices
    :param player: player which choose action
    :return: print players choices
    """
    if player_choice == '1':
        print(f'{player} choose rock')
    elif player_choice == '2':
        print(f'{player} choose scissors')
    elif player_choice == '3':
        print(f'{player} choose paper')


def players_choice(player: str):
    """
    Function which ask user about action to do.
    :param player: player which choose action
    :return: player_choice
    """
    while True:
        player_choice = input(f"{player}. Choose one: \n1 - rock \n2 - scissors \n3 - paper\n")
        choice_list = ['1', '2', '3']
        if player_choice in choice_list:
            print_chooses(player_choice=player_choice, player=player)
            players_choice_list.append(player_choice)
            break
        else:
            print("You choose wrong value. Type 1, 2 or 3")
            continue


def compare_choices():
    """
    Compare choices and print the winner.
    :return: print winner
    """
    choices = {
        '11': 'Draw!',
        '12': 'Player 1 win!',
        '13': 'Player 2 win!',
        '21': 'Player 2 win!',
        '22': 'Draw!',
        '23': 'Player 1 win!',
        '31': 'Player 1 win!',
        '32': 'Player 2 win!',
        '33': 'Draw!'
    }
    choices_str = ''
    choices_str += players_choice_list[0]
    choices_str += players_choice_list[1]
    print(choices[choices_str])


rock_paper_scissors_game()
