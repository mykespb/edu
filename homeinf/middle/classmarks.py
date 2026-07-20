#!/usr/bin/env python

# Mikhail (myke) Kolodin, 2021
# 2022-01-21 2022-04-11 1.0
# classmarks.py

# ~ Есть данные об отметках учеников класса.
# ~ Разделить оных на неуспевающих, середнячков и отличников.

from classmarks_data import *

# ~ print(data)

# уровни качества
GOOD = 4.0
MIDL = 3.0

def getdata():
    """только получаем данные"""

    am = {}

    for line in data.strip().split("\n"):
        name, mark = line.strip().split()
        if name in am:
            am[name] += [int(mark)]
        else:
            am[name] = [int(mark)]

    return am
    

marks = getdata()

# ~ print(marks)

def avg(a):
    """calculate average in list"""

    if len(a) == 0:
        return 0

    return sum(a) / len(a)
    

def calc(marks):
    """calulate averages"""

    avgs = {}

    for person, ms in marks.items():
        avgs[person] = avg(ms)

    return avgs

calced = calc(marks)

# ~ print(calced)

print("Классные успехи\n")

goods = [x for x in calced.keys() if calced[x] >= GOOD]
print("отличники:", ", ".join(goods))
midls = [x for x in calced.keys() if GOOD > calced[x] >= MIDL ]
print("\nхорошисты:", ", ".join(midls))
bads = [x for x in calced.keys() if calced[x] < MIDL]
print("\nпрочие:", ", ".join(bads))


# ~ Классные успехи

# ~ отличники: Иванов, Иванова, Петров, Сидоров, Куликов, Дятлов

# ~ хорошисты: Берёзкина, Феофанкин, Прозова, Стихов, Местный, Дальний, Итокский, Месиво

# ~ прочие: Думка, Спорый, Шанец
