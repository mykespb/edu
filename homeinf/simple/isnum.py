#!/usr/bin/env python
# Miklhail (myke) Kolodin
# simple / isnum.py
# 2026-08-18 2026-08-18 1.1
# ~ Есть текст, в котором перечисляются, среди прочего, некие предметы,
# ~ причём им предшествует количество оных (числом).
# ~ Выписать все предметы, а также подсчитать локальное (для строки) и общее их количества.

text = """
100 кошек, желающих съесть 1 мышку, будут расстроены: 95 хищников даже не догадаются, что происходит.
15 человек на 1 сундук 1 мертвеца, йо-хо-хо, и 1 бутылка рому.
10 негритят отправились обедать.
7 негритят дрова рубили вместе.
"""


def test(s):
    ss = s.strip().split()
    objs = 0
    
    for n in range(len(ss)-1):
        if ss[n].isnumeric():
            objs += int(ss[n])
            print("нашли:", ss[n], ss[n+1])

    print("тут объектов:", objs)

    return objs


def tests(t):
    total = 0
    
    for at in t.strip().splitlines():
        at = at.replace('.', ' ').replace(',', ' ')
        print("\nстрока: ", at)
        total += test(at)

    print("\nвсего объектов:", total)

tests(text)

