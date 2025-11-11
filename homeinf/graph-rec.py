#!/usr/bin/env python

# Mikhail (myke) Kolodin, 2025
# 2025-11-21 2025-11-11 1.0
# graph-rec.py

# рекурсивный обход графа, бинарное дерево

from pprint import pp

sg = [1,
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

pp(sg)

# найти заданное числов в дереве

def fn(g, n):
    """найти число n в графе g"""

    assert type(g) == list and len(g) == 3
    assert type(n) == int

    if g[0] == n:
        return True

    if g[1] and fn(g[1], n):
        return True

    if g[2] and fn(g[2], n):
        return True

    return False


print( 1,   fn(sg, 1) )
print( 2,   fn(sg, 2) )
print( 111, fn(sg, 111) )


# ~ [1, [2, [3, 0, 0], [4, [41, 0, 0], 0]], [11, [12, 0, 0], [13, 0, [133, 0, 0]]]]
# ~ 1 True
# ~ 2 True
# ~ 111 False
