#!/usr/bin/env python

# Mikhail (myke) Kolodin, 2025
# 2025-05-30 2025-07-21 1.0

# ~ numinlists.py

# ~ Есть глубоко вложенный список (кортеж).
# ~ Определить, есть ли в нём заданное число.

# примеры для проверки
lex = (
    (1),
    (1, 2),
    (1, 2, 3),
    (1, (2, 3)),
    (1, (2, (3, (4, 5, 6), 7), 8), 9)
)

def find(lst, num):
    """найти num в lst"""

    for e in lst:
        if e == num:
            return True

        if type(e) == tuple and find(e, num):
            return True

    return False
    

print(find(lex, 1))
print(find(lex, 4))
print(find(lex, 0))
print(find(lex, 100500))
