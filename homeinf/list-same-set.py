#!/usr/bin/env python
# Mikhail Kolodin, 2024
# 2024-10-05 2024-10-05 1.1
# определить, состоят ли списки из одних и тех же наборов значений

import random

a1 = [random.randint(0, 2) for _ in range(10)]
a2 = [random.randint(0, 2) for _ in range(10)]

def setlist(a):
    b = []
    for e in a:
        if e not in b:
            b.append(e)

    return sorted(b)
    

def cmpset(a1, a2):
    return setlist(a1) == setlist(a2)


print(f"{a1=}, {a2=} => {cmpset(a1, a2)}")

# ~ a1=[0, 0, 0, 2, 1, 1, 0, 0, 0, 2], a2=[1, 0, 1, 2, 0, 2, 1, 3, 1, 2] => False
# ~ a1=[0, 0, 1, 0, 2, 0, 0, 1, 2, 0], a2=[0, 1, 1, 2, 1, 0, 0, 1, 2, 0] => True
# ~ a1=[1, 1, 1, 1, 2, 1, 2, 0, 1, 2], a2=[1, 1, 0, 1, 0, 0, 1, 1, 2, 1] => True
