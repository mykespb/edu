#!/usr/bin/env python
# Mikhail (myke) Kolodin, 2024
# 2025-01-08 2025-01-08 1.0
# pulis-usa.py

# ~ Есть класс с оценками по амер. система (от A до F).
# ~ Определить рейтинг учеников (от лучшего к худшему).

marks = """
John A A C D E C D F A A
Jim E E E C B
Jane C C D B B B 
Joseff A A B C C D A
Jill C D C D C D D 
Johan C C C D C C C D C C C D
Janna E E E E 
"""

order = "ABCDEF"

def avg(arr):
    """average"""

    return sum(arr) / len(arr) if  arr else 0
    

def proc():
    """process marks"""

    rates = []

    for line in marks.strip().split("\n"):
        name, *notes = line.strip().split()

        notes = list( map( order.index, notes ) )
        rates.append( (name, avg(notes)) )

    rates.sort(key = lambda x: x[1])

    # ~ print(*rates, sep="\n")

    for pupil in rates:
        print(pupil[0], ":", round(pupil[1], 2))


proc()

# ~ Joseff : 1.14
# ~ Jane : 1.67
# ~ John : 1.9
# ~ Johan : 2.25
# ~ Jill : 2.57
# ~ Jim : 3.0
# ~ Janna : 4.0
