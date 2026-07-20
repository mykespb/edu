#!/usr/bin/env python
# myke 2022-05-14 2024-10-30 2.2
# hist-hor.py

# ~ Есть набор данных.
# ~ Построить гистограмму, т.е. график, показывающий приближённое соотношение
# ~ данных в наборе.
# ~ График расположить горизонтально, в формате:
# ~ число : ХХХХХХХ
# ~ Вар. 1. Число крестов = отображаемому числу.
# ~ Вар. 2. Число крестов = отображаемому числу в отношении к максимуму (нормирование).

from random import randint

# сколько чисел в наборе
SIZE = 20

def gen_data():
    """создать набор данных.
    пусть будет SIZE(20) чисел,
    каждое от 0 до 100.
    """

    return [randint(0, 100) for _ in range(SIZE)]


def process1(data):
    """обработка данных
    """

    for elem in data:
        print(f"{elem:2}", ":", elem * "X")

    print()
    

def process2(data):
    """обработка данных, нормированно до SIZE = 50 позиций
    """

    WIDTH = 50
    mv  = max(data)

    for elem in data:
        print(f"{elem:2}", ":", (elem * WIDTH // mv) * "X")

    print()
    

def work(times = 1, process = process1):
    """организация вычислений
    """

    for atime in range(times):
        print("=" * 50, "\n", " набор номер          ", atime+1, "\n", "=" * 50, "\n")
        data = gen_data()
        process(data)


work(times = 1, process = process2)


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

# ~ ================================================== 
  # ~ набор номер           1 
 # ~ ================================================== 

 # ~ 9 : XXXX
# ~ 94 : XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
# ~ 36 : XXXXXXXXXXXXXXXXXXX
# ~ 14 : XXXXXXX
# ~ 78 : XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
# ~ 90 : XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
# ~ 88 : XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
# ~ 81 : XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
# ~ 44 : XXXXXXXXXXXXXXXXXXXXXXX
# ~ 46 : XXXXXXXXXXXXXXXXXXXXXXXX
# ~ 19 : XXXXXXXXXX
# ~ 10 : XXXXX
# ~ 87 : XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
# ~ 67 : XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
# ~ 17 : XXXXXXXXX
# ~ 91 : XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
# ~ 23 : XXXXXXXXXXXX
# ~ 45 : XXXXXXXXXXXXXXXXXXXXXXX
# ~ 29 : XXXXXXXXXXXXXXX
 # ~ 5 : XX

