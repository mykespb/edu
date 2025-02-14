#!/usr/bin/env python
# Mikhail (myke) Kolodin
# 2025-02-14 2025-02-14 1.0
# chebd-color.py

# ~ Определить цвет данной клетки на шахматной доске.

from random import choice

letters = "ABCDEFGH"
digits  = "12345678"


def test() -> str:
    """выбрать клетку"""

    return choice(letters) + choice(digits)


def find_color(point: str) -> str:
    """определить цвет"""

    return ["black", "white"] [ ( letters.index(point[0]) + digits.index(point[1]) ) % 2 ]
    

def run_tests(num: int = 1) -> None:
    """запуск всех тестов"""

    for irun in range(1, num+1):
        point = test()
        color = find_color(point)
        print(f"test {irun:2}: {point=} {color=}")


run_tests(10)


# ~ test  1: point='D3' color='white'
# ~ test  2: point='D7' color='white'
# ~ test  3: point='E2' color='white'
# ~ test  4: point='C6' color='white'
# ~ test  5: point='A1' color='black'
# ~ test  6: point='C8' color='white'
# ~ test  7: point='H2' color='black'
# ~ test  8: point='F8' color='black'
# ~ test  9: point='D2' color='black'
# ~ test 10: point='A4' color='white'
