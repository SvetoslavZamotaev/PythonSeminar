
find_write = ""


def Search():
    global find_write
    find_write = input('Введите имя искомого человека ')
    with open('database.txt', 'r', encoding='utf-8') as file:
        for i in file:
            if i.find(find_write) != -1:
                print(i)
                break


def WriteIn(timenow):
    global find_write
    find_write = input(
        'Введите имя и телефон через дефис для записи в книгу ')
    with open('database.txt', 'a', encoding='utf-8') as file:
        file.writelines(f'\n{find_write}: {timenow}')
    with open('database.csv', 'a', encoding='utf-8') as file:
        file.writelines(f'\n{find_write}: {timenow}')
