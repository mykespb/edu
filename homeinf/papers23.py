#!/usr/bin/env python

# Mikhail (myke) Kolodin, 2021
# 2022-01-21 2022-01-21 1.1
# papers23.py

from papers23src import *

def process(text):
    """обработать данный текст"""

    lat = "abcdefghijklmnopqrstuvwxyz"
    rus = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"

    clat = crus = 0   # счётчик

    for c in text:
        if c in rus:
            crus += 1
        elif c in lat:
            clat += 1

    print(f"""
в тексте
русских букв:   {crus},
латинских букв: {clat},
итог:           {'победили русские' if crus > clat else 'победили латинские' if clat > crus else 'победила дружба'}""")

process (text1)
process (text2)


# ~ в тексте
# ~ русских букв:   504,
# ~ латинских букв: 928,
# ~ итог:           победили латинские

# ~ в тексте
# ~ русских букв:   133,
# ~ латинских букв: 16,
# ~ итог:           победили русские
