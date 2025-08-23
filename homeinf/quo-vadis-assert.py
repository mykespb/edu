#!/usr/bin/env python

# Mikhail (myke) Kolodin, 2025
# 2025-08-23 2025-08-23 2.0
# quo-vadis.py

# ~ Куда придём?
# ~ -----------------------------------------

# ~ В начале робот находится в позиции с координатами (0, 0).
# ~ Есть программа вида
# ~ ```
# ~ UP 100
# ~ RIGHT 200
# ~ DOWN 100
# ~ LEFT 200
# ~ ```
# ~ Нужно определить, в какой точке окажется робот после выполнения всех команд.

# ~ +1 Нужно проверять синтаксис, ругаясь на плохие команды
# ~ (несуществующие команды, неправильные параметры (не целые числа), и т.п.).


way = """
UP 100
RIGHT 200
DOWN 100
LEFT 200

#JUMP 0
#PRINT x, y
"""


def main():

    assert way

    xplus = {'UP': 0, 'DOWN': 0, 'LEFT': -1, 'RIGHT': 1}
    yplus = {'UP': 1, 'DOWN': -1, 'LEFT': 0, 'RIGHT': 0}

    x = y = 0
    print(f"start at {x=}, {y=}")

    for step in way.strip().splitlines():

        if not step or step.startswith('#'):
            continue

        where, long = step.strip().split()[:2]
        assert where in "UP DOWN LEFT RIGHT".split(), 'direction is NOT in "UP DOWN LEFT RIGHT"'

        long = int(long)
        assert long > 0, 'length must be positive'

        x += xplus[where] * long
        y += yplus[where] * long

        print(f"{where=}, {long=} => {x=}, {y=}")

    print(f"end at {x=}, {y=}")

main()
