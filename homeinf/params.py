#!/usr/bin/env python
# M.Kolodin
# params.py 2024-12-09 2024-12-09 1.0
# работа с параметрами функций

# Часть 1. Вход

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

fun(1, name='Sherlock', surname='Holmes', 22, 300, 400, 500)
# ~ File "/home/myke/pro/edu/homeinf/params.py", line 46
# ~ fun(1, name='Sherlock', surname='Holmes', 22, 300, 400, 500)
# ~ SyntaxError: positional argument follows keyword argument

# Часть 2. Выход TBD
