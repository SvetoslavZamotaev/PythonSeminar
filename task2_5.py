# Реализуйте алгоритм перемешивания списка.
import random
list = list(range(17))
mash_up_list = []
i = 0
while i < len(list):
    mash_up_list.append(list[random.randint(0, 16)])
    i = i + 1
print(f'перемешаный изначальный массив {mash_up_list}')
