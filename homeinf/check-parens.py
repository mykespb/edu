#!/usr/bin/env python

# Mikhail (myke) Kolodin, 2025
# check-parens.py 2025-01-16 2025-01-16 1.0

# ~ Проверка правильности вложенности скобок.

# --------------------------
# проверялка

def good_parens(par : str) -> bool:
    """сама проверка"""
    
    cnt = 0

    plus = {'(': 1, ')': -1}

    for e in par:
        cnt += plus[e]
        if cnt < 0:
            return False

    return cnt == 0

# --------------------------
# тесты

def test(t : str) -> None:
    """запуск 1 теста"""

    print(f"строка {t} записана",
        "правильно" if good_parens(t)
        else "неправильно"
        )

test("()")
test(")(")
test("(()")
test("())")
test("()()")
test("(()()(()))")

# --------------------------
# результаты

# ~ строка () записана правильно
# ~ строка )( записана неправильно
# ~ строка (() записана неправильно
# ~ строка ()) записана неправильно
# ~ строка ()() записана правильно
# ~ строка (()()(())) записана правильно

# --------------------------
