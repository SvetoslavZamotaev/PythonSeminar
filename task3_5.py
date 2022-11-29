# 5'. Задайте число. Составьте список чисел Фибоначчи, в том числе
# для отрицательных индексов.(Дополнительно)

# *Пример:*

# - для k = 8 список будет выглядеть так:
# [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] [Негафибоначчи]

n = int(input('введите колличество чисел из посл. Фибоначчи:')) + 1
i = 0
list = []
while i < n:
    if i == 0 or i == 1:
        list.append(i)
        i += 1
    else:
        list.append(list[i-2]+list[i-1])
        i += 1

negList = []
for i in range(len(list)):
    if i == 0:
        continue
    elif i % 2 == 0:
        negList.append(list[i]*(-1))
    else:
        negList.append(list[i])
negList.reverse()
negList.extend(list)
print(negList)
