# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока 
# делая ход друг после друга. Первый ход определяется жеребьёвкой. 
# За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. 
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""

from random import randint

#Человек против человека:
print('Игра 2021 конфета')
candy_all = 2021
candy = 28
count = 0
name1 = input('Как зовут первого игрока? = ')
name2 = input('Как зовут второго игрока? = ')
print('Жеребьевка:')
rnd = randint(1, 2)
if rnd == 1:
    player_1 = name1
    player_2 = name2
else:
    player_1 = name2
    player_2 = name1
print(f'Первым ходит {player_1}!')
while candy_all > 0:
    if count == 0:
        go = int(input(f'{player_1}, Сколько конфет ты возьмешь? = '))
        if go > candy_all or go > candy:
            go = int(input(f'{player_1}, за ход можно взять от 1 до {candy} конфет, попробуй еще раз: = '))
        candy_all = candy_all - go
    if candy_all > 0:
        print(f'Осталось {candy_all} конфет')
        count = 1
    else:
        print('Конфеты закончились')
    if count == 1:
        go = int(input(f'{player_2}, Сколько конфет ты возьмешь? = '))
        if go > candy_all or go > candy:
            go = int(input(f'{player_2}, за ход можно взять от 1 до {candy} конфет, попробуй еще раз: = '))
        candy_all = candy_all - go
    if candy_all > 0:
        print(f'Осталось {candy_all} конфет')
        count = 0
    else:
        print('Конфеты закончились')
if count == 1:
    print(f'{player_2} победил!')
if count == 0:
    print(f'{player_1} победил')

# #Человек против бота:
# candy_all = 50
# candy = 28
# name1 = input('Как тебя зовут? = ')
# name2 = 'Бот'
# players = [name1, name2]
# rnd = randint(-1, 0)
# print(f'Жеребьевка: первым ходит {players[rnd+1]}')
# while candy_all > 0:
#     rnd += 1
#     if players[rnd % 2] == 'Бот':
#         print(f'Ходит {players[rnd%2]}')
#         if candy_all < 29:
#             go = candy_all
#         else:
#             div = candy_all//28
#             go = candy_all - ((div*candy)+1)
#             if go == -1:
#                 go = candy -1
#             if go == 0:
#                 go = candy
#         while go > 28 or go < 1:
#             go = randint(1,28)
#         print(go)
#     else:
#         go = int(input(f'Ходит {players[rnd%2]}, осталось {candy_all} конфет. Сколько конфет ты возьмешь? = '))
#         while go > candy or go > candy_all:
#             go = int(input(f'За один ход можно взять от 1 до {candy} конфет, попробуй еще раз: = '))
#     candy_all = candy_all - go
# print(f'Осталось {candy_all} конфет, победил {players[rnd%2]}!')