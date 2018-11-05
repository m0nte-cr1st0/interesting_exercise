# В этой игре игроки сидят перед кучей из 100 камней. Каждый из них, по очереди, выбирает из кучи от 1 до 5 камней (при условии, что в куче осталось не меньше 5 камней). Игрок, последним вытянувший камень, выигрывает.

def game_stones(stones, count_of_players):
    players = tuple('Player {}'.format(i+1) for i in range(count_of_players))
    index = 0
    current_player = players[index]
    
    for iter_player in players[:len(players)-1]:
        print(iter_player, end=', ')
    print(players[len(players)-1] + '.')
    print()

    while stones > 1:
        numbers = input()
        if numbers.isdigit():
            if 1 <= int(numbers) <= 5:
                if int(numbers) <= stones:
                    stones -= int(numbers)
                else:
                    print("Enter valid value.")
                    continue
            else:
                print("Enter valid value.")
                continue
        else:
            print("Enter valid value.")
            continue

        print('{} took {} stones. There are {} stones left.'.format(current_player, int(numbers), stones))

        index += 1
        index %= len(players)
        if stones > 0:
            current_player = players[index]

    print()
    print('Win is {}!'.format(current_player))

stones = int(input('Enter the number of stones: '))
count_of_players = int(input('Enter the number of players: '))
print('List of players: ', end='')

game_stones(stones, count_of_players)