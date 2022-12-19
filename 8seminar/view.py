
mode = "nothing"
edit = "nothing"
find_write = "nothing"


def CheckForFound(bool):
    if bool:
        print('\n Нашелся!')
    else:
        print('В базе не найден')


def askForMode():
    global mode
    print('============MENU==============================')
    print('=Введите команду add - добавить пользователя =')
    print('=find - найти пользователя                   =')
    print('=edit - редактировать пользователя (заменить)=')
    print('=delete - удалить полностью из базы          =')
    print('==============================================')
    mode = input(': ')


def AskSearch():
    global find_write
    find_write = input('Введите данные искомого человека  ')


def AskWriteIn():
    global find_write
    find_write = input(
        'Введите имя телефон через дефис для записи в книгу ')


def AskEdit():
    global edit
    edit = input('на какой контакт вы хотите заменить ? ')


def AskDelete():
    global find_write
    find_write = input('Какой контакт вы хотите удалить?')
