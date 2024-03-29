#!/usr/bin/env python

# t-ipo-0.py
# (C) Mikhail (myke) Kolodin, 2021
# 2022-01-07 2022-01-07 3.0

# edu: работа с функциями
# test input - process - output scheme
# отработка схемы "ввод - обработка - вывод"
# работает

data, lodata = "", 0


def fin():
    """ ввести данные
    """
    global data
    data = input("введите непустой текст без точек: ")
    return "." not in data


def fproc():
    """ обработать данные
    """
    global lodata
    lodata = len(data)
    return lodata
   

def fout():
    """ вывести данные
    """
    print(f"длина текста равна {lodata}")
    return True


def main():
    """ диспетчер
    """
    print("начинаем работу")
    fin()
    fproc()
    fout()
    print("закончили работу")


main()


# ~ начинаем работу
# ~ введите непустой текст без точек: 5 3485 345 345
# ~ длина текста равна 14
# ~ закончили работу

# ~ что хорошо?
# ~ работает, понятно, чёткая последовательность
# ~ что плохо?
# ~ необоснованное использование глобальных данных.
# ~ нет обработки ошибок
# ~ даже после неправильного ввода работа продолжается (неправильно)
