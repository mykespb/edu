#!/usr/bin/env python
# Mikhail (myke) Kolodin
# 2025-02-20 2025-04-16 1.10
# math-lang.py

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

# ~ Распечатать значения всех переменных после выполнения программы.

# ----------------- data

prog1 = """
A=1
B = A
B =23
C= 1
D=B
FAN =    56
ANSWER  =   42
NOOB =   FAN
VAR = B
"""

prog2 = """
A=1
Q =R
B = A
B =23
C= 1
D=B
FAN =    56
ANSWER  =   42
NOOB =   FAN
VAR = B
P=Q
Z=P
The Best Variable = 0
"""

# ~ prog = prog1

# ----------------- calc

def calc(prog):
    """посчитать всё и распечатать словарь значений"""

    dex = {}

    for iexpr, expr in enumerate(prog.strip().splitlines(), 1):
        print(f"#{iexpr:3}: {expr}")

        # ~ assert '=' in expr
        
        expr = expr.replace(' ', '')

        left, right = expr.split('=')

        # ~ assert left
        # ~ assert right
        
        if right in dex:
            dex[left] = dex[right]
        else:
            dex[left] = right

    print("\nрезультат:")

    for k in sorted(dex):
        print(f"{k} : {dex[k]}")
        
    # ~ width = max( [ len(x) for x in dex] )

    # ~ for k in sorted(dex):
        # ~ print(f"{k:{width}} : {dex[k]}")



calc(prog1)
# ~ calc(prog2)


# ----------------- result

# ~ #  1: A=1
# ~ #  2: B = A
# ~ #  3: B =23
# ~ #  4: C= 1
# ~ #  5: D=B
# ~ #  6: FAN =    56
# ~ #  7: ANSWER  =   42
# ~ #  8: NOOB =   FAN
# ~ #  9: VAR = B

# ~ результат:
# ~ A      : 1
# ~ ANSWER : 42
# ~ B      : 23
# ~ C      : 1
# ~ D      : 23
# ~ FAN    : 56
# ~ NOOB   : 56
# ~ VAR    : 23

#  1: A=1
#  2: Q =R
#  3: B = A
#  4: B =23
#  5: C= 1
#  6: D=B
#  7: FAN =    56
#  8: ANSWER  =   42
#  9: NOOB =   FAN
# 10: VAR = B
# 11: P=Q
# 12: Z=P
# 13: The Best Variable = 0

# ~ результат:
# ~ A               : 1
# ~ ANSWER          : 42
# ~ B               : 23
# ~ C               : 1
# ~ D               : 23
# ~ FAN             : 56
# ~ NOOB            : 56
# ~ P               : R
# ~ Q               : R
# ~ TheBestVariable : 0
# ~ VAR             : 23
# ~ Z               : R

# ----------------- the end.
