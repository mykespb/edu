#!/usr/bin/env python

# Mikhail (myke) Kolodin, 2025
# 2026-01-29 2026-01-30 4.0
# find-vars-simple.py

# ~ В данном тексте программы найти (напечатать) все питоновские идентификаторы (имена).
# ~ Ключевые (зарезервированные) слова не включать.
# ~ Буквы - только латинские.
# ~ Внутри комментариев тоже смотрим.
# ~ Решаем тупо прямо.

text = """
from pprint import pp

a1 = a2 = a3 = q1234567890_() = f(x) = _a = _1 = 7

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

pp(bt, width=25, indent=4, compact=False)


def fn(t, n):
    # найти число n в бинарном дереве t
    
    if t[0] == n:
        return True
    
    ...
    

# тесты
print(1,   "=>", fn(bt, 1))
print(12,  "=>", fn(bt, 12))
print(100, "=>", fn(bt, 100))
"""

import keyword, string

# ~ print(keyword.kwlist, keyword.softkwlist)
# ~ print("def", keyword.iskeyword("def"))
# ~ print("do", keyword.iskeyword("do"))
# ~ print("match", keyword.issoftkeyword("match"))
# ~ print("_", keyword.issoftkeyword("_"))

kw = keyword.kwlist + keyword.softkwlist
# ~ print(f"{kw=}")

letters = string.ascii_letters + string.digits + '_'
# ~ print(f"{letters=}")


def fv(txt):

    var = ""

    for ch in txt:
        if ch in letters:
            if var:
                var += ch
            else:
                if ch not in string.digits:
                    var = ch
        else:
            if var:
                if var not in kw:
                    print(var, end=", ")
                var = ""

    print()


fv(text)
