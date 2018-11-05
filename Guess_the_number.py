# Угадай число. 2 игры.
#### -*- coding: utf-8 -*-
import random
import math


# Вспомагательная функция запускает новую игру
def new_game():
    range100()
    range1000()

# Объявление генератора чисел
def range100():
    # Генерирует число в диапазне [0,100) и начинает новую игру
    global secret_number
    global max_n
    secret_number = random.randrange(0, 100)
    max_n = 99
    
    print('New game. Range is [0,{})'.format(100))
    print('Number of remaining guesses is {}'.format(math.ceil(math.log(100)/math.log(2))))
    input_guess()
    print()

def range1000():
    # Генерирует число в диапазне [0,1000) и начинает новую игру     
    global secret_number
    global max_n
    secret_number = random.randrange(0, 1000)
    max_n = 999
    
    print('New game. Range is [0,{})'.format(1000))
    print('Number of remaining guesses is {}'.format(math.ceil(math.log(1000)/math.log(2))))
    input_guess()
    
def input_guess():
    # Основная программа
    k = 0
    
    while k <= math.ceil(math.log(max_n)/math.log(2)):
        answer = int(input())
        print("Guess was {}".format(answer))
        if secret_number > answer:
            print('Higher')
        elif secret_number < answer:
            print('Lower')
        else:
            print('Correct')
            break
        k += 1
        
    else:
        print('You lose!')
                
# Вызов новой игры
new_game()