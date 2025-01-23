#!/usr/bin/env python

# Mikhail (myke) Kolodin, 2025
# 2025-01-23 2025-01-23 2.1
# ~ long-signs.py

# --------------------------------
# problem

# ~ Длинные серии знаков
# ~ --------------------------------

# ~ Даны последовательности (в 1+ строках) вида
# ~ (знаки разделены пробелами))

# ~ ===
# ~ +++++++ ---------------    ***** ** ----- ++
# ~ ???????????          !!!!!
# ~ ===

# ~ Найти самую длинную из них, указав длину и из каких знаков состоит.

# --------------------------------
# initial data

data = """
+++++++ ---------------    ***** ** ----- ++
???????????          !!!!!
"""

# --------------------------------
# solve

# method 1 - simple

def solve1():
    """method 1"""
    
    result = sorted(data.strip().split(), key=len, reverse=True)
    # ~ print(result)
    return len(result[0]), result[0][0]


# method 2 - finite automata

def solve2():
    """method 2"""

    state = False
    cnt = bestcnt = 0
    bestchar = waschar = ""

    for char in data:

        if char not in " \t\n":

            if state:
                cnt += 1

            else:
                waschar = char
                cnt = 1

            state = True

        else:

            if state:

                if cnt > bestcnt:
                    bestcnt = cnt
                    bestchar = waschar

            state = False

    if state:

        if cnt > bestcnt:
            bestcnt = cnt
            bestchar = waschar

    return bestcnt, bestchar


# method 3 - finite automata

def solve2():
    """method 2"""



# --------------------------------
# start

def main():
    """запуск"""

    length, char = solve1()
    print(f"самая длинная последовательность состоит из знаков '{char}' и имеет длину {length} символов")

    length, char = solve2()
    print(f"самая длинная последовательность состоит из знаков '{char}' и имеет длину {length} символов")


main()

# --------------------------------
# results

# ~ ['---------------', '???????????', '+++++++', '*****', '-----', '!!!!!', '**', '++']
# ~ самая длинная последовательность состоит из знаков '-' и имеет длину 15 символов

# --------------------------------
