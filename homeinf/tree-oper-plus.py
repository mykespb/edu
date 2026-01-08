#!/usr/bin/env python

# Mikhail (myke) Kolodin, 2025
# 2026-01-06 2026-01-08 2.0
# tree-oper-plus.py

# ~ Операции над бинарными деревьями:
# ~ вывод левый (по возрастанию), правый (по убыванию).
# ~ добавление (условное).

from pprint import pp

# -----------------------------------------------
# предзаданное дерево
# -----------------------------------------------

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

# ~ [5,
 # ~ [3, [1, None, [2, None, None]], [4, None, None]],
 # ~ [7, [6, None, None], [8, None, [9, None, None]]]]
# ~ печать по возрастанию:
# ~ 1, 2, 3, 4, 5, 6, 7, 8, 9, 
# ~ печать по убыванию:
# ~ 9, 8, 7, 6, 5, 4, 3, 2, 1, 
# ~ [3, [1, None, None], [5, None, None]]

# -----------------------------------------------
# построение дерева по последовательности
# -----------------------------------------------

def ext(t, e):
    """add element e to tree t"""

    if type(t) != list:
        raise ValueError

    if t == []:
        t.extend([e, None, None])
        return

    if t[0] == e:
        return

    if t[0] > e:
        if t[1] == None:
            t[1] = [e, None, None]
        else:
            ext(t[1], e)

    else:
        if t[2] == None:
            t[2] = [e, None, None]
        else:
            ext(t[2], e)


d = []
plus(d, 3)
plus(d, 1)
plus(d, 5)

pp(d)
    

seq = 5, 3, 7, 1, 8, 2, 4, 9, 6
print("sequence=", seq)

st = []
for e in seq:
    plus(st, e)

pp(st)

print("печать по возрастанию:")
print_up(st)
print()

print("печать по убыванию:")
print_down(st)
print()


# ~ sequence= (5, 3, 7, 1, 8, 2, 4, 9, 6)
# ~ [5,
 # ~ [3, [1, None, [2, None, None]], [4, None, None]],
 # ~ [7, [6, None, None], [8, None, [9, None, None]]]]
# ~ печать по возрастанию:
# ~ 1, 2, 3, 4, 5, 6, 7, 8, 9, 
# ~ печать по убыванию:
# ~ 9, 8, 7, 6, 5, 4, 3, 2, 1, 

# -----------------------------------------------
