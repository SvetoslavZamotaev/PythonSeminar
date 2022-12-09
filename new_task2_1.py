# Напишите программу, которая принимает на вход
# вещественное число и показывает сумму его цифр.

# Пример:

# - 6782 -> 23
# - 0,56 -> 11
string_num_arr = input('Введите число :')
res = sum([int(i) for i in string_num_arr if i.isnumeric()])
print(res)
