#!/usr/bin/env python

# Mikhail (myke) Kolodin, 2025
# check-parens.py 2025-01-16 2025-01-21 1.1

# ~ Проверка правильности вложенности скобок.

# --------------------------
# проверялка 1

def good_parens_1(par : str) -> bool:
    """сама проверка"""
    
    cnt = 0

    for e in par:
        if e == '(':
            cnt += 1
        else:
            cnt -= 1
            if cnt < 0:
                return False

    if cnt == 0:
        return True
    else:
        return False
    
# --------------------------
# проверялка 2

def good_parens_2(par : str) -> bool:
    """сама проверка"""
    
    cnt = 0

    for e in par:
        cnt += 1 if e == '(' else -1
        if cnt < 0:
            return False

    return cnt == 0
    
# --------------------------
# проверялка 3

def good_parens_3(par : str) -> bool:
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

good_parens = good_parens_1

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
