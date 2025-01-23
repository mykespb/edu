#!/usr/bin/env python

# Mikhail (myke) Kolodin, 2025
# 2025-01-23 2025-01-23 3.0
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
    print(result)
    return len(result[0]), result[0][0]

# --------------------------------

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

# --------------------------------

# method 3 - finite automata

def solve3():
    """method 3"""

    # ~ states : out in end 
    # ~ inchar : space char

    state = 'out'

    cnt = bestcnt = 0
    bestchar = waschar = ""

    def start_word():
        nonlocal cnt, bestcnt, char, bestchar, waschar
        waschar = char
        cnt = 1

    def cont_word():
        nonlocal cnt, bestcnt, char, bestchar, waschar
        cnt += 1

    def end_word():
        nonlocal cnt, bestcnt, char, bestchar, waschar
        if cnt > bestcnt:
            bestcnt = cnt
            bestchar = waschar
            
    def no_action():
        pass

    tabacts = {
        ('out', 'space')  : no_action,
        ('out', 'char')   : start_word,
        ('in',  'space')  : end_word,
        ('in',  'char')   : cont_word,
        ('end', 'space')  : no_action,
        ('end', 'char')   : no_action,
    }

    tabstates = {
        ('out', 'space')  : 'out',
        ('out', 'char')   : 'in',
        ('in',  'space')  : 'out',
        ('in',  'char')   : 'in',
    }

    for char in data:

        chartype = 'char' if char not in " \t\n" else 'space'

        tabacts [state, chartype] ()
        state = tabstates [state, chartype]

        # ~ if state == 'end': break

    tabacts [state, chartype] ()

    return bestcnt, bestchar


# --------------------------------
# start

def main():
    """запуск"""

    length, char = solve1()
    print(f"самая длинная последовательность состоит из знаков '{char}' и имеет длину {length} символов")

    length, char = solve2()
    print(f"самая длинная последовательность состоит из знаков '{char}' и имеет длину {length} символов")

    length, char = solve3()
    print(f"самая длинная последовательность состоит из знаков '{char}' и имеет длину {length} символов")


main()

# --------------------------------
# results

# ~ ['---------------', '???????????', '+++++++', '*****', '-----', '!!!!!', '**', '++']
# ~ самая длинная последовательность состоит из знаков '-' и имеет длину 15 символов
# ~ самая длинная последовательность состоит из знаков '-' и имеет длину 15 символов
# ~ самая длинная последовательность состоит из знаков '-' и имеет длину 15 символов

# --------------------------------
