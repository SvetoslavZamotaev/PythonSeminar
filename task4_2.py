# 2'. Задайте натуральное число N. Напишите программу, которая
# составит список простых множителей числа N.
# * 6 -> [1, 2, 3]
# * 144 -> [2, 3]
import sympy
n = int(input('Введите число '))
print(f'Это список простых множителей этого числа {sympy.primefactors(n)}')
