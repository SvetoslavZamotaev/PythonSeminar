def ShowMeAll():
    with open('database.txt', 'r', encoding='utf-8') as file:
        return file.read()


mode = ""


def askFor():
    global mode
    mode = input(
        'Команда "add" - добавить пользователя, "find" - найти пользователя , команда "showme" показать всю книгу ')
    if mode == 'find':
        mode = 'find'
    elif mode == 'add':
        mode = 'add'
    elif mode == 'showme':
        print('Список всех контактов')
