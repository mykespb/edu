#!/usr/bin/env python
# myke 2022-04-25 2022-04-25 1.0

# ~ конвертер дат 
# ~ есть 2 формата YYYY-MM-DD и DD.MM.YYYY
# ~ получив строку с датой в одном из этих форматов, 
# ~ перевести её в другой из этих- форматов и вернуть как результат

def conv(di):
    if '-' in di:
        return ".".join(di.split('-')[::-1])
    else:
        return "-".join(di.split('.')[::-1])

dates = "20.03.1968 1946-01-21 01.07.1946 29.04.2010" . split()

for adate in dates:
    print(adate, "-->", conv(adate))
