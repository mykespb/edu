#!/usr/bin/env python
# Mikhail (myke) Kolodin
# 2025-02-20 2025-04-16 4.2
# math-lang-4.py

# ~ Язык математики

# ~ Есть простой язык программирования с командами вида
# ~ A = 1
# ~ или
# ~ B = A
# ~ устанавливающими зависимости между переменными и значениями,
# ~ возможно, с переприсваиваниями.

# ~ Дана программа из таких команд.
# ~ Команды исполняются сверху вниз, 
# ~ устанавливая зависимости между переменными.

# ~ Учесть, что значения переменных - целые числа.
# ~ Разрешить в правой части выражения с вычислением суммы или разности целых чисел.
# ~ Разрешить смешанные выражения: переменные и числа.

# ~ Распечатать значения всех переменных после выполнения программы.

# ----------------- data

prog1 = """
A=1
B = A
Z=B
B =23
C= A + 5 + 11
D=C+C
E = 1+2   +3  +4
FAN =    56+A
ANSWER  =   42
nova = ANSWER - 24
NOOB = 5 + 15 + 20 + 10
VAR = B+NOOB
Y=-3
Z=Y-5-1
"""

# ----------------- calc

def calc(prog):
    """посчитать всё и распечатать словарь значений"""

    dex = {}

    for iexpr, expr in enumerate(prog.strip().splitlines(), 1):
        print(f"#{iexpr:3}: {expr}")

        assert '=' in expr
        
        expr = expr.replace(' ', '')

        left, right = expr.split('=')

        assert left
        assert right

        right = right.replace('+', ' +').replace('-', ' -')

        rpart = right.split()

        # ~ print('\n', rpart)

        rsigned = list(
            map(
                lambda x:
                    ('+', x[1:]) if x.startswith('+')
                    else ('-', x[1:]) if x.startswith('-')
                    else ('+', x)
            ,rpart)
            )
        
        # ~ print(rsigned)

        rsub = list(
            map(
                lambda x:
                    (1 if x[0] == '+' else -1) * 
                    (dex[x[1]] if x[1] in dex
                    else int(x[1])
                    )
            , rsigned)
            )

        # ~ print(rsub)

        right = sum(rsub)
        
        dex[left] = right

        # ~ print(f"{dex=}")

    print("\nрезультат:")

    width = max( [ len(x) for x in dex] )

    for k in sorted(dex):
        print(f"{k:{width}} : {dex[k]}")


calc(prog1)


# ~ результат:
# ~ A      : 1
# ~ ANSWER : 42
# ~ B      : 23
# ~ C      : 17
# ~ D      : 34
# ~ E      : 10
# ~ FAN    : 57
# ~ NOOB   : 50
# ~ VAR    : 73
# ~ Y      : -3
# ~ Z      : -9
# ~ nova   : 18

