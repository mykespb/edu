#!/usr/bin/env python

# t-ipo-1.py
# (C) Mikhail (myke) Kolodin, 2021
# 2022-01-07 2022-01-07 1.0

# edu: работа с функциями
# test input - process - output scheme
# отработка схемы "ввод - обработка - вывод"
# работает

global data, lodata


def fin():
    """ ввести данные
    """
    global data
    data = input("введите текст:")
    return True


def fproc():
    """ обработать данные
    """
    global lodata
    lodata = len(data)
    return True
   

def fout():
    """ вывести данные
    """
    print(f"длина текста равна {lodata}")
    return True


def main():
    """ диспетчер
    """
    if fin() and fproc() and fout():
        print("всё готово")

main()


# ~ введите текст:53453453453
# ~ длина текста равна 11
# ~ всё готово

# ~ что плохо?
# ~ необоснованное использование глобальных данных.
# ~ но так тоже можно.
