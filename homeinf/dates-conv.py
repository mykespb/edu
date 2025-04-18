#!/usr/bin/env python
# myke 2022-04-25 2022-04-25 1.4

# ~ конвертор дат 
# ~ есть 2 формата YYYY-MM-DD и DD.MM.YYYY
# ~ получив строку с датой в одном из этих форматов, 
# ~ перевести её в другой из этих- форматов и вернуть как результат

# программа
def conv(di):
    if '-' in di:
        return ".".join(di.split('-')[::-1])
    else:
        return "-".join(di.split('.')[::-1])


# проверка
dates = "20.03.1968 1946-01-21 01.07.1946 29.04.2010" . split()

for adate in dates:
    print(adate, "-->", conv(adate))


# ~ 20.03.1968 --> 1968-03-20
# ~ 1946-01-21 --> 21.01.1946
# ~ 01.07.1946 --> 1946-07-01
# ~ 29.04.2010 --> 2010-04-29
