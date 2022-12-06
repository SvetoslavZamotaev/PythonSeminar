# 2. Создайте программу для игры в ""Крестики-нолики"".
# (в консоли происходит выбор позиции)
arr = [['.', '.', '.'], ['.', '.', '.'], ['.', '.', '.']]


def PrintMatr(list):
    for i in range(0, len(list)):
        for j in range(0, len(list[i])):
            print(list[i][j], end=' ')
        print()


def PutX(arr):
    while True:
        i, j = list(map(int, input('Введите координаты для Х ').split()))
        if arr[i][j] != 'O' and arr[i][j] != 'X':
            arr[i][j] = 'X'
            break
        else:
            print('Место занято!')


def PutO(arr):
    while True:
        i, j = list(map(int, input('Введите координаты для O ').split()))
        if arr[i][j] != 'O' and arr[i][j] != 'X':
            arr[i][j] = 'O'
            break
        else:
            print('Место занято!')


def CheckForWin(arr, symbol_X_or_O):
    if arr[0][0] == symbol_X_or_O and arr[0][1] == symbol_X_or_O and arr[0][2] == symbol_X_or_O:
        return True
    elif arr[1][0] == symbol_X_or_O and arr[1][1] == symbol_X_or_O and arr[1][2] == symbol_X_or_O:
        return True
    elif arr[2][0] == symbol_X_or_O and arr[2][1] == symbol_X_or_O and arr[2][2] == symbol_X_or_O:
        return True
    elif arr[0][0] == symbol_X_or_O and arr[1][0] == symbol_X_or_O and arr[2][0] == symbol_X_or_O:
        return True
    elif arr[0][1] == symbol_X_or_O and arr[1][1] == symbol_X_or_O and arr[2][1] == symbol_X_or_O:
        return True
    elif arr[0][2] == symbol_X_or_O and arr[1][2] == symbol_X_or_O and arr[2][2] == symbol_X_or_O:
        return True
    elif arr[0][0] == symbol_X_or_O and arr[1][1] == symbol_X_or_O and arr[2][2] == symbol_X_or_O:
        return True
    elif arr[2][0] == symbol_X_or_O and arr[1][1] == symbol_X_or_O and arr[0][2] == symbol_X_or_O:
        return True


print('start!')

while True:
    PutX(arr)
    PrintMatr(arr)
    if CheckForWin(arr, 'X'):
        print('Выйграл Х!')
        break
    PutO(arr)
    PrintMatr(arr)
    if CheckForWin(arr, 'O'):
        print('Выйграл O!')
        break
