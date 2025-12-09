#!/usr/bin/env python

# Mikhail (myke) Kolodin, 2025
# 2025-10-22 2025-12-05 2.1
# digit-2025th.py

# ~ 2025ая цифра

# ~ Некто выписывает подряд натуральные числа с 1, без пробелов.
# ~ Какая цифра будет на 2025 месте?
# ~ (подставь номер года...)

def what(number=2025):
    """find the digit"""

    out = ""
    pout = ""
    lout = 0
    commas = 0

    for n in range(1, number+1):
        sn = str(n)
        lsn = len(sn)

        out += sn
        pout += sn + ","
        commas += 1
        lout += lsn

        # ~ if lout == number:
            # ~ return out[-1]
        if lout >= number:
            return out[ - (lout - number) - 1 ], pout[-20 : number + commas - 1]


def main(number=2025):
    """organize it"""
    
    dig, pout = what(number)
    print(f"{number=} => digit: {dig}, final: ...{pout}")
    # ~ print(f"{number=} => digit: {dig} ({out=})")


# see results:
for n in 1, 2, 3, 4, 9, 10, 11, 12, 13, 20, 100, 1000, 2025, 2026:
    main(n)

# ~ def etc(number):
    # ~ alles = ""
    # ~ for n in range(1, number+1):
        # ~ alles += str(n)
    # ~ print(alles[number-1])

# ~ for nn in 1, 2, 5, 10, 20, 1000, 2025:
    # ~ etc(nn)


# ~ number=1 => digit: 1, final: ...1
# ~ number=2 => digit: 2, final: ...1,2
# ~ number=3 => digit: 3, final: ...1,2,3
# ~ number=4 => digit: 4, final: ...1,2,3,4
# ~ number=9 => digit: 9, final: ...1,2,3,4,5,6,7,8,9
# ~ number=10 => digit: 1, final: ...,2,3,4,5,6,7,8,9,1
# ~ number=11 => digit: 0, final: ...,2,3,4,5,6,7,8,9,10
# ~ number=12 => digit: 1, final: ...3,4,5,6,7,8,9,10,1
# ~ number=13 => digit: 1, final: ...3,4,5,6,7,8,9,10,11
# ~ number=20 => digit: 1, final: ...9,10,11,12,13,14,1
# ~ number=100 => digit: 5, final: ...9,50,51,52,53,54,5
# ~ number=1000 => digit: 3, final: ...366,367,368,369,3
# ~ number=2025 => digit: 1, final: ...707,708,709,710,711
# ~ number=2026 => digit: 7, final: ...708,709,710,711,7
