#!/usr/bin/env python

# Mikhail (myke) Kolodin, 2025
# 2026-01-06 2026-02-02 2.2
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

    if not tree:
        return

    if tree[1] is not None:
        print_up(tree[1])

    print(tree[0], end=", ")

    if tree[2] is not None:
        print_up(tree[2])
    

# печать по убыванию

def print_down(tree):

    if tree is None:
        return

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

def plus(t, e):
    """add new element e to tree t, or skip"""

    if type(t) != list or type(e) != int:
        raise ValueError

    if t == []:
        t.extend([e, None, None])
        return

    if t[0] == e:
        return

    if t[0] > e:
        if t[1] is None:
            t[1] = [e, None, None]
        else:
            plus(t[1], e)

    else:
        if t[2] is None:
            t[2] = [e, None, None]
        else:
            plus(t[2], e)

# 1st try

# ~ plus = ext
d = []
plus(d, 3)
plus(d, 1)
plus(d, 5)

pp(d)

# 2nd try

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
