#!/usr/bin/env python

# Mikhail Kolodin
# allsubs.py 2023-04-17 2023-04-17 1.0
# make all substrings of the given string

from itertools import combinations as comb

def subs(s: str) -> list[str] :
    """make all"""

    los = len(s)
    if los < 1:
        return 0, []
    elif los == 1:
        return 1, [s]
    
    als = {}

    for nod in range(los, 0, -1):
        for res in comb(s, nod):
            # print(f"{nod=}, {res=}")
            if nod in als:
                als[nod] += [''.join(res)]
            else:
                als[nod] = [''.join(res)]

    return s, als


print(subs(''))
print(subs('a'))
print(subs('ab'))
print(subs('abc'))
print(subs('abcd'))
