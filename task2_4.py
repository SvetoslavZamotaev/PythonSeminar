# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях.
# Позиции хранятся в файле file.txt в одной строке одно число.
# (для продвинутых - с файлом, вариант минимум - ввести позиции в консоли)
#  -2 -1 0 1 2 Позиции: 0,1 -> 2

n = int(input('Введите число не меньше трёх '))

start_list = list(range(-n, n+1))
print(start_list)
indexFromFile = []
with open('fileTask2_4.txt') as f:
    for row in f:
        for letter in row:
            if letter != '\n':
                indexFromFile.append(int(letter))
print(indexFromFile)


mult = 1  # константа для перемножения двух элементов списка индексов
result = []
for i in range(len(indexFromFile)):
    if i % 2 == 0:  # Условие чтоб mult заного стал единицей после перемножения
        mult = 1
    mult = mult * start_list[indexFromFile[i]]
    if i % 2 != 0:  # Условие чтоб мы записали результаты парного перемножения
        result.append(mult)
print(
    f'массив : {start_list}\n индексы:{indexFromFile}\n ответ: {result}')
