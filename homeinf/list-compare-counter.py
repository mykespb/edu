#!/usr/bin/env python
# Mikhail Kolodin, 2024
# 2024-10-05 2024-10-05 1.0
# определить, одинаковы ли списки с точностью до перестановок

import random
from collections import Counter

a1 = [random.randint(0, 3) for _ in range(10)]
a2 = [random.randint(0, 3) for _ in range(10)]
a3 = a1[:]
random.shuffle(a3)

def cmp(a1, a2):
    if len(a1) != len(a2): return False
    
    cnt1 = Counter(a1)
    cnt2 = Counter(a2)

    return cnt1 == cnt2


print(f"{a1=}, {a2=} => {cmp(a1, a2)}")
print(f"{a1=}, {a3=} => {cmp(a1, a3)}")

# ~ a1=[0, 5, 1, 4, 1, 2, 0, 4, 5, 4], a2=[0, 4, 3, 0, 3, 2, 3, 3, 1, 5] => False
# ~ a1=[2, 0, 2, 2, 1, 3, 2, 3, 3, 1], a2=[0, 1, 2, 3, 3, 1, 3, 2, 2, 2] => True
# ~ a1=[2, 1, 3, 1, 2, 1, 1, 0, 2, 1], a2=[1, 3, 1, 2, 0, 1, 0, 0, 0, 2] => False
# ~ a1=[2, 1, 3, 1, 2, 1, 1, 0, 2, 1], a3=[1, 3, 2, 0, 2, 2, 1, 1, 1, 1] => True
