#!/usr/bin/env python

# Mikhail (myke) Kolodin, 2025
# 2025-10-17 2025-10-17 1.0
# opposites.py

# ~ Даны два списка целых чисел.
# ~ Найти пары чисел (одно из 1го списка, 2ое из 2го) таких, что они равны по модулю,
# ~ но противоположны по знаку.
# ~ (Если несколько одинаковых - трактовать как угодно).


from random import randint, shuffle, choice

LIST_SIZE = 10
SIZE_PM = 5
MAX_INT = 1000


def make():
    """make 2 lists"""

    l1 = [ randint(-MAX_INT, MAX_INT) for _ in range(randint(LIST_SIZE-SIZE_PM, LIST_SIZE+SIZE_PM)) ] 
    l2 = [ randint(-MAX_INT, MAX_INT) for _ in range(randint(LIST_SIZE-SIZE_PM, LIST_SIZE+SIZE_PM)) ] 
    for _ in range(randint(1, SIZE_PM)):
        l1.append(- choice(l2) )
        l2.append(- choice(l1) )
    l1 = list(set(l1))
    l2 = list(set(l2))
    shuffle(l1)
    shuffle(l2)

    return l1, l2


def solve(l1, l2):
    """solve 1 task"""

    res = []
    for v1 in l1:
        for v2 in l2:
            if v1 == -v2:
                res.append((v1, v2))

    return res
    

def main():
    """dispatcher"""

    l1, l2 = make()
    res = solve(l1, l2)
    res.sort()
    print(f"{l1=}\n{l2=}\n{res=}, ")


main()
