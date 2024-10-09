#!usr/bin/env python
# Mikhail Kolodin, 2024
# list-info.py
# 2024-10-09 2024-10-09 1.4
# получение информации по спискам и прочие спецштучки

import random

#1. Задача: узнать, верно ли, что в заданном случайном списке целых чисел все числа больше нуля

def p1():
    for _ in range(10):
        a = [random.randint(0, 9) for _ in range(10)]
        print( ["не", ""][all( [ e > 0 for e in a ] )],
            "все элементы списка", a, "положительны")

# ~ p1()

 # ~ все элементы списка [6, 2, 6, 8, 1, 3, 3, 7, 3, 7] положительны
# ~ не все элементы списка [6, 1, 8, 8, 6, 5, 2, 8, 0, 8] положительны
 # ~ все элементы списка [6, 4, 2, 3, 2, 3, 2, 4, 7, 5] положительны
 # ~ все элементы списка [7, 9, 2, 3, 2, 6, 9, 4, 7, 1] положительны
# ~ не все элементы списка [2, 5, 4, 0, 8, 6, 0, 9, 9, 5] положительны
 # ~ все элементы списка [4, 5, 5, 2, 6, 9, 6, 9, 6, 5] положительны
# ~ не все элементы списка [9, 5, 5, 5, 3, 4, 0, 7, 8, 4] положительны
# ~ не все элементы списка [9, 0, 0, 7, 4, 1, 5, 2, 9, 8] положительны
 # ~ все элементы списка [4, 6, 6, 9, 1, 9, 1, 5, 7, 3] положительны
# ~ не все элементы списка [3, 1, 6, 4, 0, 1, 4, 1, 7, 8] положительны

#2. Задача: узнать, верно ли, что в заданном случайном списке целых чисел есть хотя бы одно число, кратное 5

def p2():

    elems = [1, 2, 3, 4, 6, 7, 8, 9, 0]
    for _ in range(10):
        a = [random.choice(elems) for _ in range(10)]
        print( "есть такие элементы," if any([ e % 5 == 0 for e in a ] ) else "нет таких элементов,",
            "чтобы на 5 нацело делились в списке", a)

# ~ p2()

# ~ есть такие элементы, чтобы на 5 нацело делились в списке [2, 3, 0, 2, 6, 1, 6, 4, 8, 3]
# ~ есть такие элементы, чтобы на 5 нацело делились в списке [3, 1, 4, 8, 0, 3, 2, 6, 4, 0]
# ~ нет таких элементов, чтобы на 5 нацело делились в списке [4, 9, 9, 3, 1, 8, 8, 2, 7, 7]
# ~ есть такие элементы, чтобы на 5 нацело делились в списке [9, 7, 2, 9, 6, 2, 0, 7, 2, 0]
# ~ нет таких элементов, чтобы на 5 нацело делились в списке [7, 3, 3, 4, 7, 3, 1, 1, 4, 2]
# ~ нет таких элементов, чтобы на 5 нацело делились в списке [6, 8, 3, 9, 8, 9, 1, 6, 9, 3]
# ~ есть такие элементы, чтобы на 5 нацело делились в списке [8, 7, 6, 0, 6, 1, 2, 0, 4, 9]
# ~ есть такие элементы, чтобы на 5 нацело делились в списке [8, 6, 8, 9, 4, 0, 1, 2, 8, 6]
# ~ есть такие элементы, чтобы на 5 нацело делились в списке [1, 3, 3, 9, 4, 9, 0, 0, 2, 0]
# ~ есть такие элементы, чтобы на 5 нацело делились в списке [3, 3, 2, 0, 4, 0, 3, 7, 9, 3]

# 3. Задача:  есть список натуральных чисел. Получить из него список пар, являющихся частными и остатками от деления элементов 1го списка на 2.

def p3():
    for _ in range(10):
        a = [ random.randint(1, 99) for _ in range(10) ]
        b = [ divmod(e, 2) for e in a ]
        print(f"для списка {a} частные и остатки от деления на 2 таковы: \n{b}")

# ~ p3()    

# 4. задача: найти сумму элементов матрицы (2-мерного списка) натуральных чисел.
# учтите, что sum(m) не определена.

def p4(size = 2):
    a = [[random.randint(1, 9) for j in range(size)] for i in range(size)]
    s = sum( [ sum(row) for row in a] )
    print(f"для матрицы {a} сумма равна {s}")

# ~ p4(2)

# ~ для матрицы [[1, 8, 3, 8], [3, 9, 3, 3], [2, 1, 4, 7], [2, 6, 1, 9]] сумма равна 70
# ~ для матрицы [[1, 3, 5, 8], [9, 3, 6, 2], [5, 1, 8, 7], [7, 6, 5, 9]] сумма равна 85
# ~ для матрицы [[4, 1, 1, 6], [9, 3, 3, 2], [1, 9, 8, 5], [3, 9, 5, 4]] сумма равна 73
# ~ для матрицы [[9, 3, 8, 1], [7, 7, 8, 2], [3, 2, 4, 6], [1, 9, 1, 8]] сумма равна 79
# ~ для матрицы [[4, 2, 1, 5], [6, 9, 1, 3], [7, 6, 8, 8], [9, 5, 3, 7]] сумма равна 84
# ~ для матрицы [[3, 3], [5, 3]] сумма равна 14
# ~ для матрицы [[2, 3], [4, 3]] сумма равна 12


