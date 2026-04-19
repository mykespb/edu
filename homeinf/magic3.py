#!/usr/bin/env python

# Mikhail (myke) Kolodin, 2025
# 2026-0-419 2026-04-19 1.0
# magic3.py

# ~ построить магический квадрат со стороной 3.
# ~ 0 1 2
# ~ 3 4 5
# ~ 6 7 8


from itertools import permutations


def solve():
    sols = 0
    for b in permutations( (1, 2, 3, 4, 5, 6, 7, 8, 9), r=9):
        if ( b[0] + b[1] + b[2] ==
             b[3] + b[4] + b[5] ==
             b[6] + b[7] + b[8] ==
             b[0] + b[3] + b[6] ==
             b[1] + b[4] + b[7] ==
             b[2] + b[5] + b[8] ==
             b[0] + b[4] + b[8] ==
             b[2] + b[4] + b[6] ):
                 sols += 1
                 printout(sols, b)
             

def printout(sols, b):
    print(f"""solution {sols}
{b[0]} {b[1]} {b[2]}
{b[3]} {b[4]} {b[5]}
{b[6]} {b[7]} {b[8]}
""")


solve()


# ~ solution 1
# ~ 2 7 6
# ~ 9 5 1
# ~ 4 3 8

# ~ solution 2
# ~ 2 9 4
# ~ 7 5 3
# ~ 6 1 8

# ~ solution 3
# ~ 4 3 8
# ~ 9 5 1
# ~ 2 7 6

# ~ solution 4
# ~ 4 9 2
# ~ 3 5 7
# ~ 8 1 6

# ~ solution 5
# ~ 6 1 8
# ~ 7 5 3
# ~ 2 9 4

# ~ solution 6
# ~ 6 7 2
# ~ 1 5 9
# ~ 8 3 4

# ~ solution 7
# ~ 8 1 6
# ~ 3 5 7
# ~ 4 9 2

# ~ solution 8
# ~ 8 3 4
# ~ 1 5 9
# ~ 6 7 2

# ~ See: https://docs.python.org/3/library/itertools.html
