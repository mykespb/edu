#!/usr/bin/env python3
# Mikhail Kolodin
# печать числа по цифрам
# 2021-09-22 1.0

cif = {
    0: "нуль",
    1: "один",
    2: "два",
    3: "три",
    4: "четыре",
    5: "пять",
    6: "шесть",
    7: "семь",
    8: "восемь",
    9: "девять"
    }

def podig(n):
    """ главный расчёт """
    if n == 0:
        return "ноль"

    s = ""
    while n:
        d = n % 10
        n //= 10
        s = cif[d] + " " + s
    return s

def test(n):
    """ тестер """
    print(n, "->", podig(n))

# запуски
print(podig(123))

test(123)
test(12)
test(1)
test(0)

# ===
