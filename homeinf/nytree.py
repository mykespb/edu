#!/usr/bin/env python

# Mikhail (myke) Kolodin, 2021
# 2021-11-15 2021-11-21 1.0
# nytree.py
# ~ рисование новогодней ёлочки

size = 5     # размер ёлочки = число веток

for branch in range(size):
    print (" " * (size-branch-1), "*" * (branch*2+1), sep="")

print(" " * (size-1), "*", sep="")
