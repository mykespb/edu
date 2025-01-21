#!/usr/bin/env python

# Mikhail (myke) Kolodin, 2021
# 2021-12-03 2025-01-21 1.1
# iters1.py
# ~ игры с итераторами

import itertools, random

subj = "русский литература физкультура математика география "\
    "история английский технология".split()

for num in itertools.count():
    rm = random.randint (2, 5)
    rs = random.choice (subj)
    re = random.randint (1, 100)
    print (num, "предмет", rs, "оценка", rm)
    if re % 10 == 0:
        break
