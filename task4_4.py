# 4'. Задана натуральная степень k. Сформировать случайным
# образом список коэффициентов (значения от 0 до 100) многочлена и записать
#  в файл многочлен степени k.

# Пример:

# k=2 => 2*x*2 + 4*x + 5 = 0 или x2 + 5 = 0 или 10*x*2 = 0
# k=3 => 2*x*3 + 4*x*2 + 4*x + 5 = 0 5'.
import random
randListK = []
for i in range(100):
    str(randListK.append(random.randint(2, 101)))
print(randListK)
for i in randListK:
    with open('func4_4.txt', 'a') as file:
        file.writelines(f'X^{str(i)} + 5 = 0 \n')
