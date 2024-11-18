#!/usr/bin/env python
# Mikhail (myke) Kolodin, 2021
# 2021-12-18 2021-12-18 1.0
# mk-turtle-01.py

import random, turtle

LIMIT = 30

dirs = [90*n for n in range(4)]
#dirs = [30*n for n in range(12)]
#dirs = [45*n for n in range(8)]
colors = "green yellow navy silver gray red white blue cyan black".split()

t = turtle.Turtle()
t.width(5)

for step in range(LIMIT):
	if random.choice((True, False)):
		dir = random.choice(dirs)
		t.right(dir)
	far = random.randint(10, 50)
	col = random.choice(colors)
	t.color(col)
	t.fd(far)
	
input()
