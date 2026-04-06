#!/usr/bin/env python
# Miklhail (myke) Kolodin
# classes / store-data.py
# 2026-04-06 2026-04-06 1.2
# храним и обрабатываем просто данные, разными способами

# ~ нужно работать с данными о человеках: имя name, возраст age, IQ.
# ~ как это представлять и обрабатывать?
# ~ напр., посчитаем средний IQ в группе человеков

# ~ ----------------------------------------------------------------------
# ~ 1. просто кортеж
# ~ ----------------------------------------------------------------------

tpl = (("Jane", 20, 100), ("John", 40, 85), ("Jack", 77, 125))
print(tpl)

avgIQ = sum(x[2] for x in tpl) / len(tpl)
print(f"average IQ is {avgIQ:.2f}")

# ~ выводы:
# ~ 1. нужно помнить порядок элементов
# ~ 2. неизменяемый

# ~ ----------------------------------------------------------------------
# ~ 2. список
# ~ ----------------------------------------------------------------------

lst = [["Jane", 20, 100], ["John", 40, 85], ["Jack", 77, 125]]
print(lst)

avgIQ = sum(x[2] for x in lst) / len(lst)
print(f"average IQ is {avgIQ:.2f}")

# ~ выводы:
# ~ 1. нужно помнить порядок элементов
# ~ 2. изменяемый

# ~ ----------------------------------------------------------------------
# ~ 3. словарь
# ~ ----------------------------------------------------------------------

dct = [
    {"name": "Jane", "age": 20, "IQ": 100},
    {"name": "John", "age": 40, "IQ": 85},
    {"name": "Jack", "age": 77, "IQ": 125},
]
print(dct)

avgIQ = sum(x["IQ"] for x in dct) / len(dct)
print(f"average IQ is {avgIQ:.2f}")

# ~ выводы:
# ~ 1. произвольный порядок элементов
# ~ 2. изменяемый

# ~ ----------------------------------------------------------------------
# ~ 4. именованный кортеж
# ~ ----------------------------------------------------------------------

from collections import namedtuple

Data = namedtuple("Data", ["name", "age", "IQ"])
d1 = Data("Jane", 20, 100)
d2 = Data("John", 40, 85)
d3 = Data("Jack", 77, 125)
print(d1, d2, d3)

avgIQ = (d1.IQ + d2.IQ + d3.IQ) / 3
print(f"average IQ is {avgIQ:.2f}")

dnt = Data("Jane", 20, 100), Data("John", 40, 85), Data("Jack", 77, 125)
print(dnt)

avgIQ = sum(x[2] for x in dnt) / len(dnt)
print(f"average IQ is {avgIQ:.2f}")

# ~ выводы:
# ~ 1. с именами удобно
# ~ 2. быстро, потому что кортежи
# ~ 3. норм, ибо стандартный тип, хотя и редкий
# ~ 4. неизменяемый

# ~ ----------------------------------------------------------------------
# ~ 5. датакласс
# ~ ----------------------------------------------------------------------

from dataclasses import dataclass

# @dataclass(order=True)
@dataclass()
class DC:
    name: str
    age: int
    IQ: int

d1 = DC("Jane", 20, 100)
d2 = DC("John", 40, 85)
d3 = DC("Jack", IQ=125, age=77)
print(d1, d2, d3)

avgIQ = (d1.IQ + d2.IQ + d3.IQ) / 3
print(f"average IQ is {avgIQ:.2f}")

dc = [DC("Jane", 20, 100), DC("John", 40, 85), DC("Jack", 77, 125)]
print(dc)

avgIQ = sum(x.IQ for x in dc) / len(dc)
print(f"average IQ is {avgIQ:.2f}")

# dc.sort(key=lambda x: x.IQ, reverse=True)
# print(dc)

# ~ выводы:
# ~ 1. универсально, расширяемо, верифицируемо (указаны типы)
# ~ 2. норм, ибо стандартный тип, хотя и редкий
# ~ 3. изменяемый

# ~ ----------------------------------------------------------------------

# ~ (('Jane', 20, 100), ('John', 40, 85), ('Jack', 77, 125))
# ~ average IQ is 103.33

# ~ [['Jane', 20, 100], ['John', 40, 85], ['Jack', 77, 125]]
# ~ average IQ is 103.33

# ~ [{'name': 'Jane', 'age': 20, 'IQ': 100}, {'name': 'John', 'age': 40, 'IQ': 85}, {'name': 'Jack', 'age': 77, 'IQ': 125}]
# ~ average IQ is 103.33

# ~ Data(name='Jane', age=20, IQ=100) Data(name='John', age=40, IQ=85) Data(name='Jack', age=77, IQ=125)
# ~ average IQ is 103.33

# ~ (Data(name='Jane', age=20, IQ=100), Data(name='John', age=40, IQ=85), Data(name='Jack', age=77, IQ=125))
# ~ average IQ is 103.33

# ~ DC(name='Jane', age=20, IQ=100) DC(name='John', age=40, IQ=85) DC(name='Jack', age=77, IQ=125)
# ~ average IQ is 103.33

# ~ (DC(name='Jane', age=20, IQ=100), DC(name='John', age=40, IQ=85), DC(name='Jack', age=77, IQ=125))
# ~ average IQ is 103.33

# [DC(name='Jane', age=20, IQ=100), DC(name='John', age=40, IQ=85), DC(name='Jack', age=77, IQ=125)]
# average IQ is 103.33
#
# [DC(name='Jack', age=77, IQ=125), DC(name='Jane', age=20, IQ=100), DC(name='John', age=40, IQ=85)]

# ~ ----------------------------------------------------------------------
