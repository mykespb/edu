#/usr/bin/env python

# Mikhail Kolodin, filterintlist.py, 2023-08-28, 2023-08-23, 1.1

# Filter array with integers, deleting repeating values,
# but preserving order of elements.

loi =  [1, 3, 6, 3, 0, 11, 0, 4]
lois = [1, 3, 6, 0, 11, 4]

def uniques(arr: list[int]) -> list[int]:
    """make new list"""

    res = {}

    for e in arr:
        if e not in res:
            res[e] = 1

    return list(res)

print(loi, "=>", sol := uniques(loi), "=>", sol == lois)

# ~ [1, 3, 6, 3, 0, 11, 0, 4] => [1, 3, 6, 0, 11, 4] => True
