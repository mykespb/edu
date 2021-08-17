#!/usr/bin/env python3.9

# div1016.py
# 2021-08-17 2021-08-17 1.3
# (C) Mikhail (myke) Kolodin

# задание из ЕГЭ:
# найти числа из [1016; 7937],
# которые делятся на 3
# и не делятся на 7, 17, 19, 27.
# найти количество их и макс из них.
# ответ: 2 эти целых числа

# variant 1

print("вариант 1")

def howmany(scope=None, divs=None, nodivs=None):
    """ найти числа """

    if scope  == None: scope  = [1016, 7937+1]
    if divs   == None: divs   = [3]
    if nodivs == None: nodivs = [7, 17, 19, 27]

    # ~ print(f"{scope=}, {divs=}, {nodivs=}")

    res = []

    for n in range(*scope):
        if any([n % x for x in divs]): continue
        if any([n % x == 0 for x in nodivs]): continue
        res.append(n)

    if res:
        return len(res), max(res)
    else:
        return 0, 0

# ~ print(*howmany([1, 15], [3], [5]))
print(*howmany())

# variant 2

print("вариант 2")

nums = [i for i in range(1016, 7937+1) if i%3==0 and i%7 and i%17 and i%19 and i%27]
print(len(nums), max(nums))

# вариант 1
# 1568 7935
# вариант 2
# 1568 7935

