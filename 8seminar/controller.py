import view as v
import model as m
import logger as log


def Start():
    v.askForMode()
    if v.mode == 'add':
        v.AskWriteIn()
        log.ChangesAdd(v.find_write)
        m.WriteIn(v.find_write)
    elif v.mode == 'find':
        v.AskSearch()
        print(m.Search(v.find_write))
        v.CheckForFound(m.found)
    elif v.mode == 'delete':
        v.AskDelete()
        log.ChangesDel(v.find_write)
        m.Delete(v.find_write)
        v.CheckForFound(m.found)
    elif v.mode == 'edit':
        v.AskSearch()
        v.AskEdit()
        log.ChangesEdit(v.find_write, v.edit)
        m.Edit(v.find_write, v.edit)
        v.CheckForFound(m.found)
    elif v.mode == 'showall':
        print(m.showAll())
    else:
        print('Вы ввели не корректную команду.Запустите программму снова')


Start()
