#!/usr/bin/env python

# Mikhail (myke) Kolodin, 2026
# clustex / cluster-colors.py
# 2026-07-27 2026-07-27 1.0

# ~ Кластеризации

# ~ Есть несколько объектов с наборами заранее заданных параметров или вычисляемых по ним данных.
# ~ Нужно разделить объкты на группы по наибольшему сходству.
# ~ Количество групп (кластеров) заранее не известно.
# ~ Явно заданы цвета (белый, зелёный,...).


from collections import defaultdict


def cluster(data: str) -> list[str]:
    """
    разделить набор данных на кластеры,
    т.е. на группы близких обеъктов
    """

    dd = defaultdict(list)

    data = data.strip().split(",")
    data = map(str.strip, data)

    for para in data:
        which, what = para.split()
        dd[which].append(what)

    return dd
    

def proc(what: str) -> None:
    print("\n--------------------------------\n")

    print(">>>", what)
    res = cluster(what)
    print("<<<")

    for k in res.keys():
        print(k, ":\n    ", end="")
        print(*res[k], sep=", ")

    print("\n--------------------------------\n")
    

proc("""горячий снег, жаркий лёд, весёлая тоска, горькая радость,
весёлая песня, горячий лист, рабочий посёлок,
рабочий человек, весёлая покойницкая, жаркий ответ
""")

proc("""
white snow, white color, green leaf, blue sea, green apple,
green grass, white paper
""")
