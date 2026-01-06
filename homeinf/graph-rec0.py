#!/usr/bin/env python

# Mikhail (myke) Kolodin, 2025
# 2025-11-21 2026-01-06 1.2
# graph-rec0.py

# рекурсивный обход графа, бинарное дерево, обход в глубину
# ~ короткий вариант

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

    return bool(g) and (g[0] == n or fn(g[1], n) or fn(g[2], n))


# тесты
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
