#!/usr/bin/env python

# Mikhail (myke) Kolodin, 2025
# 2025-10-22 2025-10-22 1.0
# digit-2025th.py

# ~ 2025ая цифра

# ~ Некто выписывает подряд натуральные числа с 1, без пробелов.
# ~ Какая цифра будет на 2025 месте?
# ~ (подставь номер года...)

def what(number=2025):
    """find the digit"""

    out = ""
    lout = 0

    for n in range(1, number+1):
        sn = str(n)
        lsn = len(sn)

        out += sn
        lout += lsn

        # ~ if lout == number:
            # ~ return out[-1]
        if lout >= number:
            return out[ - (lout - number) -1 ], out[-10:number]


def main(number=2025):
    dig, out = what(number)
    print(f"{number=} => digit: {dig}, final: ...{out}")
    # ~ print(f"{number=} => digit: {dig} ({out=})")


for n in 1, 2, 3, 4, 9, 10, 11, 12, 13, 20, 100, 1000, 2025:
    main(n)
