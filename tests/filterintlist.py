#/usr/bin/env python

# Mikhail Kolodin, filterintlist.py, 2023-08-28, 2023-08-29, 2.0

# Filter array with integers, deleting repeating values,
# but preserving order of elements.

loi =  [1, 3, 6, 3, 0, 11, 0, 4]
lois = [1, 3, 6, 0, 11, 4]


def uniques(arr: list[int]) -> list[int]:
    """make new list, modern python version"""

    res = {}

    for e in arr:
        if e not in res:
            res[e] = 1

    return list(res)


def uniques1(arr: list[int]) -> list[int]:
    """make new list, old python version, without builtin ordering"""

    res = {}
    newpos = 0

    for e in arr:
        if e not in res:
            res[e] = newpos
            newpos += 1

    res = {v: k for k, v in res.items()}
    res = [res[k] for k in range(newpos)]

    return res


print(loi, "=>", 
    sol := uniques(loi), "=>", sol == lois, 
    ", ", sold := uniques1(loi), "=>", sold == lois)

# [1, 3, 6, 3, 0, 11, 0, 4] => [1, 3, 6, 0, 11, 4] => True ,  [1, 3, 6, 0, 11, 4] => True
