#!/usr/bin/env python

# Mikhail Kolodin
# allsubs2.py 2023-04-17 2023-04-17 0.1
# compare substrings of 2 strings

from itertools import combinations as comb

def subs(s):
    """process 1 string"""

    los = len(s)
    if los < 1:
        return 0, []
    elif los == 1:
        return 1, [s]
    
    als = {}

    for nod in range(los, 0, -1):
        for res in comb(s, nod):
            if nod in als:
                als[nod] += [''.join(res)]
            else:
                als[nod] = [''.join(res)]

    return als


def have_common(a1, a2):
    """2 arrays have common elements"""

    for e1 in a1:
        if e1 in a2:
            return True
    return False


def comp(s1, s2):
    """compare 2 strings"""

    c1 = subs(s1)
    c2 = subs(s2)

    minlen = min(max(c1.keys(), max(c2.keys())))

    if minlen < 1:
        return 0, []

    for alen in range(minlen, 0, -1):
        if (good := have_common(c1[alen], c2[alen])):
            return alen, good
        
    return 0, []


print(comp('abcde', 'ace'))
print(comp('abc', 'def'))
      