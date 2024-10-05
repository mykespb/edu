#!isr/bin/env python
# Mikhail Kolodin, 2024
# 2024-10-05 2024-10-05 1.0
# определить, одинаковы ли списки с точностью до перестановок

import random

a1 = [random.randint(0, 3) for _ in range(10)]
a2 = [random.randint(0, 3) for _ in range(10)]

def cmp(a1, a2):
    if len(a1) != len(a2): return False
    
    ca1 = a1[:]
    ca2 = a2[:]

    while ca1 and ca2:
        e = ca1.pop()
        if e in ca2:
            ca2.remove(e)
        else:
            return False
    else:
        return True

    return ca1 == ca2

print(f"{a1=}, {a2=} => {cmp(a1, a2)}")

# ~ a1=[0, 5, 1, 4, 1, 2, 0, 4, 5, 4], a2=[0, 4, 3, 0, 3, 2, 3, 3, 1, 5] => False
# ~ a1=[2, 0, 2, 2, 1, 3, 2, 3, 3, 1], a2=[0, 1, 2, 3, 3, 1, 3, 2, 2, 2] => True
