# На выбор:
# 1. Создайте программу для игры с конфетами человек против человека.
# *' Условие задачи: На столе лежит 117 конфета. Играют два игрока
# делая ход друг после друга. Первый ход определяется жеребьёвкой.
# За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента
# достаются сделавшему последний ход.
# a) Добавьте игру против бота
import random

tableWithCandys = 117


def BotTakeCandy(candysOnTable):
    candysOnTable = random.randint(1, 29)
    return candysOnTable


print('Сыграйте с ботом в игру конфетки,за раз нельзя брать больше 28 конфет!')
print('кинем монетку , если 1 то игрок если 0 то ход бота')
coin = random.randint(0, 1)
print(f'монетка выпала на {coin}')
player = False
human = 0
bot = 0
if coin == 1:
    player = True
while tableWithCandys > 0:
    if player:
        grab = int(input('Возьмите меньше 28 конфет: '))
        tableWithCandys = tableWithCandys - grab
        print(f'осталось конфет  {tableWithCandys}')
        if tableWithCandys <= 0:
            human = 1
            break
        print('ход бота')
        tableWithCandys = tableWithCandys - BotTakeCandy(tableWithCandys)
        print(f'осталось конфет  {tableWithCandys}')
        if tableWithCandys <= 0:
            bot = 1
    else:
        print('ход бота')
        tableWithCandys = tableWithCandys - BotTakeCandy(tableWithCandys)
        print(f'осталось конфет  {tableWithCandys}')
        if tableWithCandys <= 0:
            bot = 1
            break
        grab = int(input('Возьмите меньше 28 конфет: '))
        tableWithCandys = tableWithCandys - grab
        print(f'осталось конфет  {tableWithCandys}')
        if tableWithCandys <= 0:
            human = 1
if human == 1:
    print('Игрок победил и забрал все конфеты!')
elif bot == 1:
    print('Бот победил и забрал все конфеты')
