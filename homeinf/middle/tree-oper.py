#!/usr/bin/env python

# Mikhail (myke) Kolodin, 2025
# 2026-01-06 2026-01-07 1.1
# tree-oper.py

# ~ Операции над бинарными деревьями:
# ~ вывод левый (по возрастанию), правый (по убыванию).

from pprint import pp

# предзаданное дерево

bt = [5,
        [3,
            [1, None, [2, None, None]],
            [4, None, None]],
        [7,
            [6, None, None],
            [8, None,
                [9, None, None]]]]

pp(bt)

# печать по возрастанию

def print_up(tree):

    if tree[1]:
        print_up(tree[1])

    print(tree[0], end=", ")

    if tree[2]:
        print_up(tree[2])
    

print("печать по возрастанию:")
print_up(bt)
print()

# печать по убыванию

def print_down(tree):

    if tree[2]:
        print_down(tree[2])

    print(tree[0], end=", ")

    if tree[1]:
        print_down(tree[1])
    

print("печать по убыванию:")
print_down(bt)
print()
