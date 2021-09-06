#!/usr/bin/env python3
# (C) Mikhail Kolodin, 2021
# prints numbers of 3 given digits

# ~ digs = "5 6 7".split()
digs = "0 1 2".split()

diff = False
# ~ diff = True

n = 0

for i in digs:
    s1 = i
    for j in digs:
        if diff and i == j: continue
        s2 = s1 + j
        for k in digs:
            if diff and (i == k or j == k): continue
            s3 = s2 + k
            n += 1
            print("%5d:" % n, s3)
