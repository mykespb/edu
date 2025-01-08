#!/usr/bin/env python
# Mikhail (myke) Kolodin, 2024
# 2025-01-08 2025-01-08 1.1
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

# ~ order = " ABCDEF"    # если А=1
order = "ABCDEF"    # если A=0

def avg(arr):
    """average"""

    return sum(arr) / len(arr) if arr else 0
    

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
        print(f"{pupil[0]:20} : {round(pupil[1], 2):5.2}")


proc()


# ~ Joseff               :   2.1
# ~ Jane                 :   2.7
# ~ John                 :   2.9
# ~ Johan                :   3.2
# ~ Jill                 :   3.6
# ~ Jim                  :   4.0
# ~ Janna                :   5.0

# ~ Joseff               :   1.1
# ~ Jane                 :   1.7
# ~ John                 :   1.9
# ~ Johan                :   2.2
# ~ Jill                 :   2.6
# ~ Jim                  :   3.0
# ~ Janna                :   4.0
