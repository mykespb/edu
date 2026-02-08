#!/usr/bin/env python

# Mikhail (myke) Kolodin, 2025
# 2025-11-21 2026-02-04 2.2
# graph-que.py

# обход графа, бинарное дерево, обход в ширину

from pprint import pp

DEBUG = 0
# ~ DEBUG = 1

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

# найти заданное число в дереве

def fn(g, n):
    """найти число n в графе g"""

    if (DEBUG):
        itern = 0
        print(f"\n{n=}, {g=}")
        
    if g[0] == n:
        return True

    que = g[1:]
    
    while que:
        if (DEBUG):
            itern += 1
            print(f"iteration {itern}: \n{que=}")

        nn = que.pop(0)
        if (DEBUG):
            print(f"{nn=}")
            print(f"{que=}")

        # ~ if type(nn) == list:
        if nn:
            if nn[0] == n:
                return True
            que.extend(nn[1:])

    return False


STAR = "*"
# ~ STAR = ""
print( STAR, 1,   fn(sg, 1) )
print( STAR, 2,   fn(sg, 2) )
print( STAR, 41,  fn(sg, 41) )
print( STAR, 111, fn(sg, 111) )
print( STAR, 133, fn(sg, 133) )
print( STAR, 134, fn(sg, 134) )


# ~ [1, [2, [3, 0, 0], [4, [41, 0, 0], 0]], [11, [12, 0, 0], [13, 0, [133, 0, 0]]]]
# ~ *** 1 True
# ~ *** 2 True
# ~ *** 41 True
# ~ *** 111 False
# ~ *** 133 True
# ~ *** 134 False
