#!/usr/bin/env python
# M.Kolodin
# params.py 2024-12-09 2024-12-09 1.1
# работа с параметрами функций, как входными. так и выходными

# ------------------------------------------------
# Часть 1. Вход
# ------------------------------------------------

def fun(p1, p2=42, *arg, **kvarg):
    """функция с разными параметрами"""
    # посмотрим, кто мы
    print(f"{fun.__name__}, {fun.__doc__}")

    # посмотрим, что нам пришло
    print(f"{p1=}, {p2=}, {arg=}, {kvarg=}, ")

# ~ fun()   # --> error!
# ~ Traceback (most recent call last):
  # ~ File "/home/myke/pro/edu/homeinf/params.py", line 13, in <module>
    # ~ fun1()   # --> error!
    # ~ ~~~~^^
# ~ TypeError: fun1() missing 1 required positional argument: 'p1'

fun(1)

# ~ fun, функция с разными параметрами
# ~ p1=1, p2=42, arg=(), kvarg={},

fun(1, 22)

# ~ fun, функция с разными параметрами
# ~ p1=1, p2=22, arg=(), kvarg={}, 

fun(1, 22, 300)

# ~ fun, функция с разными параметрами
# ~ p1=1, p2=22, arg=(300,), kvarg={}, 

fun(1, 22, 300, 400, 500)

# ~ fun, функция с разными параметрами
# ~ p1=1, p2=22, arg=(300, 400, 500), kvarg={}, 

fun(1, name='Sherlock', surname='Holmes')

# ~ fun, функция с разными параметрами
# ~ p1=1, p2=42, arg=(), kvarg={'name': 'Sherlock', 'surname': 'Holmes'}, 

fun(1, 22, 300, 400, 500, name='Sherlock', surname='Holmes')

# ~ fun, функция с разными параметрами
# ~ p1=1, p2=22, arg=(300, 400, 500), kvarg={'name': 'Sherlock', 'surname': 'Holmes'},

# ~ fun(1, name='Sherlock', surname='Holmes', 22, 300, 400, 500)
# ~ File "/home/myke/pro/edu/homeinf/params.py", line 46
# ~ fun(1, name='Sherlock', surname='Holmes', 22, 300, 400, 500)
# ~ SyntaxError: positional argument follows keyword argument

# ------------------------------------------------
# Часть 2. Выход TBD
# ------------------------------------------------

def out0():
    return

def out1():
    return 1

def out2():
    return [1, 2, 3]

def out3():
    return [1, 2, 3, 'hello', 'mister']

def out4():
    return 1, 2, 3, 'hello', 'mister', [100, 200, 300], {1, 2, 3}

def out5a():
    return 1, 2, 3

def out5b():
    return (1, 2, 3)

def out6():
    return "сидя на красивом холме".split()

# ------------------------------------------------
# что на выходе?
# ------------------------------------------------

print(f"{out0()=}")
print(f"{out1()=}")
print(f"{out2()=}")
print(f"{out3()=}")
print(f"{out4()=}")
print(f"{out5a()=}")
print(f"{out5b()=}")
print(f"{out6()=}")

# ~ out0()=None
# ~ out1()=1
# ~ out2()=[1, 2, 3]
# ~ out3()=[1, 2, 3, 'hello', 'mister']
# ~ out4()=(1, 2, 3, 'hello', 'mister', [100, 200, 300], {1, 2, 3})
# ~ out5a()=(1, 2, 3)
# ~ out5b()=(1, 2, 3)
# ~ out6()=['сидя', 'на', 'красивом', 'холме']

# ------------------------------------------------
# как обработать
# ------------------------------------------------

# 1. присваивание

lst = out2()
print(f"{lst=}")

# ~ lst=[1, 2, 3]

one, two, three = out2()
print(f"{one=}, {two=}, {three=}")

# ~ one=1, two=2, three=3

# 2. сразу в работу, напр, в цикл

for e in out6():
    print(f"{e=}, {len(e)=}")

# ~ e='сидя', len(e)=4
# ~ e='на', len(e)=2
# ~ e='красивом', len(e)=8
# ~ e='холме', len(e)=5

# ------------------------------------------------
# пока всё...
# ------------------------------------------------
