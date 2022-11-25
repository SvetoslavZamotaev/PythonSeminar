# Напишите программу, которая принимает на вход число N и выдает
# набор произведений чисел от 1 до N.

# Пример:

# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)
factorial = []
num = int(input('Введите число '))
multiplier = 1
for i in range(1, num+1):
    multiplier = multiplier * i
    factorial.append(multiplier)
print(factorial)
