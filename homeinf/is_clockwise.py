#!/usr/bin/env python
# Mikhail (myke) Kolodin, 2024
# 2025-01-07 2025-01-07 1.0

# ~ Дан квадрат 2х2.
# ~ Верно ли, что в нём числа стоят по возрастанию по часовой стрелке
# ~ (начиная с любой клетки)?

from random import randint as ri

# проверялка

def test(arr: list[list[int]]) -> bool:
    """проверить круговость"""

    print(arr)

    a, b, d, c = [x for xs in arr for x in xs]

    print(a, b, c, d, end=" | ")
    print(b, c, d, a, end=" | ")
    print(c, d, a, b, end=" | ")
    print(d, a, b, c, end=" !\n")

    res = (
        (a <= b <= c <= d) or
        (b <= c <= d <= a) or
        (c <= d <= a <= b) or
        (d <= a <= b <= c) )
    print("результат:", res)
    return res


# тесты

# заведомо истинный тест
a= [[1, 2], [4, 3]]
test(a)

# теперь много случайных тестов

def many_tests(how_many : int =1) -> None:
    """выполнить много тестов"""

    for one in range(how_many):
        print("тест", one)
        arr = [ [ ri(0, 9), ri(0, 9), ri(0, 9), ri(0, 9), ] ]
        test(arr)


many_tests(10)


# результаты всего:

# ~ тест 7
# ~ [[9, 1, 8, 5]]
# ~ 9 1 5 8 | 1 5 8 9 | 5 8 9 1 | 8 9 1 5 !
# ~ результат: True
# ~ тест 8
# ~ [[6, 7, 8, 6]]
# ~ 6 7 6 8 | 7 6 8 6 | 6 8 6 7 | 8 6 7 6 !
# ~ результат: False
