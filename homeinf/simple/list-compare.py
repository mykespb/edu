#!usr/bin/env python
# Mikhail Kolodin, 2024
# 2024-10-05 2024-10-05 1.0
# сравнение списков

import random

# ~ a1 = [random.randint(0, 5) for _ in range(10)]
# ~ a2 = [random.randint(0, 5) for _ in range(10)]
# ~ print(f"{a1=} equals {a2=}: {a1==a2}")

# ~ a1=[1, 5, 5, 3, 5, 0, 2, 1, 0, 2] equals a2=[3, 4, 0, 1, 4, 3, 1, 1, 3, 5]: False

a1 = [random.randint(0, 4) for _ in range(10)]
a2 = [random.randint(0, 4) for _ in range(10)]

# ~ print(f"{a1=} equals {a1=}: {sorted(a1)==sorted(a1)}")
# ~ print(f"{a1=} equals {a2=}: {sorted(a1)==sorted(a2)}")

# ~ a1=[1, 5, 3, 5, 2, 1, 3, 5, 4, 0] equals a1=[1, 5, 3, 5, 2, 1, 3, 5, 4, 0]: True
# ~ a1=[1, 5, 3, 5, 2, 1, 3, 5, 4, 0] equals a2=[4, 4, 2, 3, 5, 2, 5, 4, 5, 5]: False

# ~ print(f"{a1=} equals {a1=}: {set(a1)==set(a1)}")
# ~ print(f"{a1=} equals {a2=}: {set(a1)==set(a2)}")

from collections import Counter

cnt1 = Counter(a1)
cnt2 = Counter(a2)

for1 = sorted([e for e in cnt1.keys()])
for2 = sorted([e for e in cnt2.keys()])

print(f"{a1=} and {a2=} состоят из",
    "одинаковых" if
        for1 == for2
    else "разных",
    "элементов"
)

print(f"{a1=} and {a1=} состоят из",
    "одинаковых" if
        for1 == for1
    else "разных",
    "элементов"
)

# ~ a1=[3, 4, 4, 0, 3, 2, 1, 0, 3, 1] and a2=[0, 0, 1, 1, 2, 3, 0, 0, 2, 0] состоят из разных элементов
# ~ a1=[3, 4, 4, 0, 3, 2, 1, 0, 3, 1] and a1=[3, 4, 4, 0, 3, 2, 1, 0, 3, 1] состоят из одинаковых элементов

# ~ print(f"{a1=} equals {a1=}: {set(a1)==set(a1)}")
# ~ print(f"{a1=} equals {a2=}: {set(a1)==set(a2)}")

# ~ a1=[3, 2, 1, 4, 1, 5, 5, 5, 5, 5] equals a1=[3, 2, 1, 4, 1, 5, 5, 5, 5, 5]: True
# ~ a1=[3, 2, 1, 4, 1, 5, 5, 5, 5, 5] equals a2=[2, 2, 2, 1, 2, 3, 3, 2, 2, 4]: False
