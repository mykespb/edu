#!/usr/bin/env python

# Mikhail (myke) Kolodin, 2025
# count-plus-minus.py 2025-01-18 2025-01-18 1.3

# ~ Сложение плюсов и минусов
# ~ вида
# ~ +++ ----- ++++ + + ---
# ~ это
# ~ +3 -5 -4 +1 +1 -3
# ~ а могут быть с или без пробелов
# ~ (на самом деле надо просто посчитать плюсы и минусы и вычесть)


# --------------------------
# проверялка

def sum1(par : str) -> int:
    """сумматор 1"""
    
    cnt = 0

    plus = {'+': 1, '-': -1}

    for e in par:
        cnt += plus[e] if e in plus else 0 

    return cnt


def sum2(par : str) -> int:
    """сумматор 2"""

    return sum(
        map(
            lambda x: 1 if x=='+' else -1 if x=='-' else 0, 
            list(par)
        ))


def sum3(par : str) -> int:
    """сумматор 3"""

    return par.count('+') - par.count('-')


# --------------------------
# тесты

def test(t : str) -> None:
    """запуск 1 теста"""

    print(f"строка '{t}' даёт в сумме {sum1(t)} (1 способ) или {sum2(t)} (2 способ) или {sum3(t)} (3 способ)")


test("+-")
test("++-")
test("- +++ --- ++ ------ ++ ++++++++ +")
test("-+-+-+-+")
test("+-+-+-+-+-+")
test("-")
test("+")
test("")

# --------------------------
# результаты

# ~ строка '+-' даёт в сумме 0 (1 способ) или 0 (2 способ) или 0 (3 способ)
# ~ строка '++-' даёт в сумме 1 (1 способ) или 1 (2 способ) или 1 (3 способ)
# ~ строка '- +++ --- ++ ------ ++ ++++++++ +' даёт в сумме 6 (1 способ) или 6 (2 способ) или 6 (3 способ)
# ~ строка '-+-+-+-+' даёт в сумме 0 (1 способ) или 0 (2 способ) или 0 (3 способ)
# ~ строка '+-+-+-+-+-+' даёт в сумме 1 (1 способ) или 1 (2 способ) или 1 (3 способ)
# ~ строка '-' даёт в сумме -1 (1 способ) или -1 (2 способ) или -1 (3 способ)
# ~ строка '+' даёт в сумме 1 (1 способ) или 1 (2 способ) или 1 (3 способ)
# ~ строка '' даёт в сумме 0 (1 способ) или 0 (2 способ) или 0 (3 способ)

# --------------------------
