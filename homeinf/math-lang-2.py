#!/usr/bin/env python
# Mikhail (myke) Kolodin
# 2025-02-20 2025-04-16 2.2
# math-lang-2.py

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

# ~ Распечатать значения всех переменных после выполнения программы.

# ----------------- data

prog1 = """
A=1
B = A
B =23
C= A
D=C
FAN =    56
ANSWER  =   42
NOOB =   FAN
VAR = B
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
        
        if right in dex:
            dex[left] = dex[right]
        else:
            dex[left] = int(right)

    print("\nрезультат:")

    width = max( [ len(x) for x in dex] )

    for k in sorted(dex):
        print(f"{k:{width}} : {dex[k]}")


calc(prog1)


# ~ #  1: A=1
# ~ #  2: B = A
# ~ #  3: B =23
# ~ #  4: C= A
# ~ #  5: D=C
# ~ #  6: FAN =    56
# ~ #  7: ANSWER  =   42
# ~ #  8: NOOB =   FAN
# ~ #  9: VAR = B

# ~ результат:
# ~ A : 1
# ~ ANSWER : 42
# ~ B : 23
# ~ C : 1
# ~ D : 1
# ~ FAN : 56
# ~ NOOB : 56
# ~ VAR : 23
# ~ A      : 1
# ~ ANSWER : 42
# ~ B      : 23
# ~ C      : 1
# ~ D      : 1
# ~ FAN    : 56
# ~ NOOB   : 56
# ~ VAR    : 23
