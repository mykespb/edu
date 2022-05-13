#!/usr/bin/env python
# myke 2022-05-14 2022-05-14 1.0
# hist-hor.py

# ~ Есть набор данных.
# ~ Построить гистограмму, т.е. график, показывающий приближённое соотношение
# ~ данных в наборе.
# ~ График расположить горизонтально, в формате:
# ~ число : ХХХХХХХ

from random import randint


# сколько чисел в наборе
SIZE = 20


def gen_data():
    """создать набор данных.
    пусть будет SIZE(20) чисел,
    каждое от 0 до 100.
    """

    return [randint(0, 100) for _ in range(SIZE)]


def work(times = 1):
    """организация вычислений
    """

    for atime in range(times):
        print("=" * 50, "\n", " набор номер          ", atime+1, "\n", "=" * 50, "\n")
        data = gen_data()
        process(data)


def process(data):
    """обработка данных
    """

    for elem in data:
        print(f"{elem:2}", ":", elem*"X")

    print()
    

work()


# ~ пример работы

# ~ ================================================== 
  # ~ набор номер           1 
 # ~ ================================================== 

# ~ 11 : XXXXXXXXXXX
# ~ 17 : XXXXXXXXXXXXXXXXX
# ~ 74 : XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
# ~ 31 : XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
# ~ 15 : XXXXXXXXXXXXXXX
# ~ 65 : XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
 # ~ 5 : XXXXX
# ~ 75 : XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
# ~ 35 : XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
# ~ 19 : XXXXXXXXXXXXXXXXXXX
# ~ 76 : XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
# ~ 23 : XXXXXXXXXXXXXXXXXXXXXXX
# ~ 47 : XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
# ~ 77 : XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
# ~ 27 : XXXXXXXXXXXXXXXXXXXXXXXXXXX
 # ~ 2 : XX
# ~ 91 : XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
 # ~ 5 : XXXXX
# ~ 29 : XXXXXXXXXXXXXXXXXXXXXXXXXXXXX
# ~ 74 : XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

