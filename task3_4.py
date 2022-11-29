# 4'. Напишите программу, которая будет преобразовывать десятичное число
# в двоичное.

# *Пример:*

# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10


num = int(input('Введите число '))
result = []
mod = 0
while True:
    if num == 0 or num == 1:
        result.append(num)
        break
    else:
        mod = num % 2
        result.append(mod)
        num = num // 2
result.reverse()
print(result)
