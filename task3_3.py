# 3'. Задайте список из вещественных чисел. Напишите программу, которая найдёт
# разницу между максимальным и минимальным значением дробной части элементов.

# *Пример:*

# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19
import math
floats = []
calc = 0
list = [1.1, 1.2, 3.1, 5, 10.01]
for i in list:
    calc = round(i - math.trunc(i), 2)
    if calc == 0:
        continue
    floats.append(calc)
print(floats)
floats.sort()
print(f'разница между максимальным и минимальным равна {floats[-1]-floats[0]}')
