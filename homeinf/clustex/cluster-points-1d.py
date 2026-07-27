#!/usr/bin/env python

# Mikhail (myke) Kolodin, 2026
# clustex / cluster-points-1d.py
# 2026-07-27 2026-07-27 1.0

# ~ Кластеризации

# ~ Есть несколько натуральных точек на числовой прямой.
# ~ Разделить их на кластеры.
# ~ 1 подход: группы = кластеры = числа, идущие строго подряд
# ~ Одинаковые числа тоже попадают в одну группу.

from collections import defaultdict

class BE(Exception): pass


def cluster(data: list[int]) -> list[list[int]]:
    """
    разделить набор данных на кластеры,
    т.е. на группы близких обеъктов
    """

    assert len(data), "Данные должны быть"

    res = [ [e] for e in data]

    need = True
    while need:
        need = False

        try:

            for g1n, g1v in enumerate(res):
                for g2n, g2v in enumerate(res):
                    if g1n == g2n:
                        continue

                    for e1 in g1v:
                        for e2 in g2v:

                            if abs(e1-e2) < 2:
                                need = True
                                do1, do2 = g1n, g2n
                                raise BE

        except BE:

            res[do1] = res[do1] + res[do2]
            # var. 1
            del res[do2]
            # var. 2
            # ~ res[do2] = []

    # var. 1
    res = sorted( [ sorted(d) for d in res ] )
    # var. 1
    # ~ res = sorted( [ sorted(d) for d in res if d] )

    return res


def proc(nabor: list[int]) -> None:
    """
    запустить 1 тест
    """
    
    print("--------------------------------\n")

    print(">>>", nabor)
    res = cluster(nabor)
    print("<<<", end=" ")

    print(res)
    print("")


# ------------------------------------------------------    

proc([1, 11, 1, 2, 5, 6, 10])

proc([1, 2, 100, 11, 12, 101, 13, 102])

proc([1, 8, 12, 11, 2, 3, 5, 6, 7])

proc([1])

proc([1, 1, 1, 1])

