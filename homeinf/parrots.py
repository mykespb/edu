#!/usr/bin/env python
# myke 2022-05-16 2022-05-20 1.3
# parrots_data.py 

# ~ взяв речи попугаев из разных книг,
# ~ определить, у какого из них богаче словарный запас (тезаурус)

# ~ данные - в файле parrots_data.py, переменная parrots (словарь)

from parrots_data import *
from pprint import pp

alfa = "абавгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЙЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
chars = alfa + " "

def pre(text):
    """подготовка 1 текста к работе"""
    out = ""
    for c in text:
        if c in chars:
            out += c
    return out
    
def preall():
    """подготовка всех текстов"""
    for k, v in parrots.items():
        parrots[k] = pre(v)
        
def calc(text):
    """вычисление тезауруса 1 попугая"""
    return sorted(set(text.split()))
    
def calcall():
    """вычисление всех тезаурусов"""
    global teza, tezalen
    
    # собрать наборы употребляемых слов
    teza = {}
    for k, v in parrots.items():
        teza[k] = calc(v)
    
    # отсортировать по значениям словарь в обратном порядке
    tezalen = { k: len(teza[k]) for k in teza.keys()}
    tezalen = sorted(tezalen.items(), key = lambda x: x[1], reverse=True)
        
preall()
calcall()
# ~ print(teza)
print("\nразмеры тезаурусов:")
pp(tezalen)

# ~ размеры тезаурусов:
# ~ [(108, 'alisa'), (59, 'gumilev'), (57, 'foton'), (12, 'taiti'), (1, 'silver')]
