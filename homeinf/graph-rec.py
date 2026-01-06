#!/usr/bin/env python

# Mikhail (myke) Kolodin, 2025
# 2025-11-21 2025-11-11 1.0
# graph-rec.py

# рекурсивный обход графа, бинарное дерево, обход в глубину

from pprint import pp

bt = [1,
        [2,
            [3, 0, 0],
            [4,
                [41, 0, 0],
                0]
        ],
        [11,
            [12, 0, 0],
            [13, 0,
                [133, 0, 0]
            ]
        ]
    ]

pp(bt)

# найти заданное число в дереве

def fn(g, n):
    """найти число n в графе g"""

    # ~ assert type(g) == list and len(g) == 3
    # ~ assert type(n) == int

    if g[0] == n:
        return True

    if g[1] and fn(g[1], n):
        return True

    if g[2] and fn(g[2], n):
        return True

    return False


# ~ STAR = "***"
STAR = "*"
print( STAR, 1,   fn(bt, 1) )
print( STAR, 2,   fn(bt, 2) )
print( STAR, 41,  fn(bt, 41) )
print( STAR, 111, fn(bt, 111) )
print( STAR, 133, fn(bt, 133) )
print( STAR, 134, fn(bt, 134) )


# ~ [1, [2, [3, 0, 0], [4, [41, 0, 0], 0]], [11, [12, 0, 0], [13, 0, [133, 0, 0]]]]
# ~ 1 True
# ~ 2 True
# ~ 111 False
# ~ 133 True
