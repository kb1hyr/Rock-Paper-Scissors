# Write your code here
import random


def center_list(game_pieces, choice):
    the_size = len(game_pieces)
    the_place = game_pieces.index(choice)
    middle_index = int((the_size - 1) / 2)

    temp_list = game_pieces

    while the_place != middle_index:
        temp_list = rotate_right(temp_list, 1)
        the_place = temp_list.index(choice)
    return temp_list


def rotate_right(lists, num):
    output_list = []
    for item in range(len(lists) - num, len(lists)):
        output_list.append(lists[item])
    for item in range(0, len(lists) - num):
        output_list.append(lists[item])
    return output_list


def rpc_winner(computer, user, game_pieces):
    middle = int((len(game_pieces) - 1) / 2)
    centered_pieces = center_list(game_pieces, user)
    computer_place = centered_pieces.index(computer)
    ##  debug
    # print(f"comp: {computer}, user: {user}")
    # print("Game: ", game_pieces)
    # print("centered: ", centered_pieces)
    # print(f"middle: {middle}  comp: {computer_place}")
    ##  debug
    if computer_place == middle:
        return 'draw'
    elif computer_place > middle:
        return 'computer'
    else:
        return 'user'


def computer_choice(game_pieces):
    an_int = random.randint(0, len(game_pieces) - 1)
    return game_pieces[an_int]


def get_choice(game_pieces):
    valid_choices = []
    valid_choices.append('!exit')
    valid_choices.append('!rating')
    valid_choices.extend(game_pieces)
    the_choice = ''
    #  debug
    # print(valid_choices)
    #  debug
    while the_choice not in valid_choices:
        the_choice = input()
        if the_choice not in valid_choices:
            print('Invalid input')
    return the_choice


def get_name():
    print('Enter your name: ', end='')
    name = input()
    print(f'Hello, {name}')
    return name


def get_score(name):
    score = 0
    rating_file = open('rating.txt', mode='r')
    for line in rating_file:
        (line_name, line_score) = line.split(' ')
        if line_name == name:
            score = int(line_score)
    rating_file.close()
    return score


def get_game_pieces():
    a = list()
    b = input()
    if len(b) < 3:
        a.append('rock')
        a.append('paper')
        a.append('scissors')
        return a
    print("Okay, let's start")

    return b.split(',')


# main program
user_name = get_name()
user_score = get_score(user_name)
pieces = get_game_pieces()

user_choice = ''
while user_choice != '!exit':
    user_choice = get_choice(pieces)
    if user_choice == '!exit':
        break
    if user_choice == '!rating':
        print(f"Your rating: {user_score}")
        continue
    puter_choice = computer_choice(pieces)
    the_winner = rpc_winner(puter_choice, user_choice, pieces)

    if the_winner == 'computer':
        print(f"Sorry, but the computer chose {puter_choice}")
    elif the_winner == 'draw':
        print(f"There is a draw ({user_choice})")
        user_score += 50
    else:
        print(f'Well done. The computer chose {puter_choice} and failed')
        user_score += 100

print('Bye!')
