from datetime import datetime as dt
from time import time


def ShowMeTime():
    date = dt.now().strftime('%H:%M:%S')
    return date


def ChangesEdit(before, after):
    with open('log.txt', 'a', encoding='utf-8') as file:
        file.writelines(
            f'Отредактирован: {before} стал: {after}  {ShowMeTime()}\n ')


def ChangesDel(person):
    with open('log.txt', 'a', encoding='utf-8') as file:
        file.writelines(f'Удален: {person} {ShowMeTime()}\n ')


def ChangesAdd(person):
    with open('log.txt', 'a', encoding='utf-8') as file:
        file.writelines(f'Добавлен {person} {ShowMeTime()}\n')
