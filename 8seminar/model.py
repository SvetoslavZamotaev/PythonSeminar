
found = False


def Search(find_write):
    global found
    with open('database.txt', 'r', encoding='utf-8') as file:
        for i in file:
            if i.find(find_write) != -1:
                found = True
                return i


def WriteIn(find_write):
    with open('database.txt', 'r+', encoding='utf-8') as file:
        dataList = file.readlines()
    number_last_line = int(dataList[-1][0])+1
    with open('database.txt', 'a', encoding='utf-8') as file:
        file.writelines(f'\n{number_last_line} {find_write}')
    with open('database.csv', 'a', encoding='utf-8') as file:
        file.writelines(f'\n{number_last_line} {find_write}')


def Edit(find_write, edit):
    i = 0
    global found
    with open('database.txt', 'r+', encoding='utf-8') as file:
        dataList = file.readlines()
    for k in dataList:
        if k.find(find_write) != -1:
            dataList[i] = ''
            dataList[i] = f'{i+1} {edit} \n'
            found = True
        i = i + 1
    with open('database.txt', 'w', encoding='utf-8') as file1:
        file1.writelines(dataList)


def showAll():
    with open('database.txt', 'r', encoding='utf-8') as file:
        return file.read()


def Delete(find_write):
    i = 0
    global found
    with open('database.txt', 'r+', encoding='utf-8') as file:
        dataList = file.readlines()
    for k in dataList:
        if k.find(find_write) != -1:
            dataList[i] = ''
            found = True
        i = i + 1
    with open('database.txt', 'w', encoding='utf-8') as file1:
        file1.writelines(dataList)
