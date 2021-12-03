#!/usr/bin/env python3.10

# Mikhail (myke) Kolodin, 2021
# 2021-12-03 2021-12-03 1.0
# iters1.py
# ~ игры с итераторами

import itertools, random

subj = "русский литература физкультура математика география"\
    "история английский технология".split()

for num in itertools.count():
    ri = random.randint (2, 5)
    rs = random.choice (subj)
    print (num, "-->", ri, rs)
    if ri % 5 == 0:
        break
