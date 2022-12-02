# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.
# В file1.txt:
# 2*x**2 + 4*x + 5
# В file2.txt:
# 4*x**2 + 1*x + 4
# Результирующий файл:
# 6*x**2 + 5*x + 9
import sympy


first = ''
second = ''


with open('task4_5.txt') as file1:
    first = (file1.read().split('\n'))
with open('task4_5_2.txt') as file2:
    second = (file2.read().split('\n'))
row = ''
with open('task4_5_result.txt', 'a+') as res:
    for i in range(len(first)):
        row = str(sympy.simplify(f'{first[i]} + {second[i]}'))
        res.writelines(f'{row} \n')
