# Напишите программу, которая принимает на вход координаты точки (X и Y),
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится
# эта точка (или на какой оси она находится).

# Пример:

# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

x = int(input('Введите координату x '))
y = int(input('Введите координату y '))
if x > 0 and y > 0:
    print("Это первая четверть, диапазон x(1;+infinity) , y(1;+infinity)")
elif x < 0 and y < 0:
    print("Это третья четверть, диапазон x(-1;-infinity) , y(-1;-infinity)")
elif x > 0 and y < 0:
    print("Это четвертая четверть, диапазон x(1;+infinity) , y(-1;-infinity)")
elif x < 0 and y > 0:
    print("Это вторая четверть, диапазон x(-1;-infinity) , y(1;+infinity)")
elif x == 0 or y == 0:
    print('Ни одна из координат не должна быть "0"')
