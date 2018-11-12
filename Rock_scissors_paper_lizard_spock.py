#Реализация игры с компьютером "Камень, ножницы, бумага, ящерица, спок"
# -*- coding: utf-8 -*-
import random


def name_to_number(name):
    if name == 'rock':
        number = 0        
    elif name == 'Spock':
        number = 1
    elif name == 'paper':
        number = 2
    elif name == 'lizard':
        number = 3
    elif name == 'scissors':
        number = 4
    else:
        print('Error.')
    return number

def number_to_name(number):
    if number == 0:
        name = 'rock'
    elif number == 1:
        name = 'Spock'
    elif number == 2:
        name = 'paper'
    elif number == 3:
        name = 'lizard'
    elif number == 4:
        name = 'scissors'
    else:
        print('Error')
    return name

def rpsls(player_choice): 
    print()
    print('Player chooses ' + player_choice)
    player_number = name_to_number(player_choice)
    comp_number = random.randrange(0, 5)
    comp_choice = number_to_name(comp_number)
    print('Computer chooses ' + comp_choice)

    res = comp_number % 5 - player_number % 5

    if res == -4 or res == -3 or res == 1 or res == 2:
        print('Computer wins!')
    elif res == 0:
        print('Draw')
    else:
        print('Player wins!')

rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")
