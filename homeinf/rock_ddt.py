#!/usr/bin/env python
# myke 2022-05-07 2022-05-07 1.0
# rock_ddt.py

# ~ Есть некоторые сведения о русском роке.
# ~ Найти разную полезную информацию.

# ~ Дискография группы "ДДТ"

from rock_ddt_data import *
from pprint import pp

# 1.
print("\nПросто распечатаем всё поальбомно\n")
pp(ddt)

# ~ Просто распечатаем всё поальбомно

# ~ [{'Альбом': 'Я получил эту роль',
  # ~ 'Релиз': '1989',
  # ~ 'Лейбл': 'Мелодия, DDT, Квадро-Диск, KDK, Grand, Астра',
  # ~ 'Формат': 'LP (1989/1990/1991), CS (1994/1999/2001), CD (1994/1999/2001)'},
 # ~ {'Альбом': 'Оттепель',
  # ~ 'Релиз': 'ноябрь 1991',
  # ~ 'Лейбл': 'SNC, Квадро-Диск, СНС, Grand',
  # ~ 'Формат': 'LP (1991), CS (1993/2001), CD (1993/1999/2001)'},
  и т.д.


# 2.
print("\nВ какие годы были выпуски альбомов\n")
for record in ddt:
    print(record["Релиз"])

# ~ В какие годы были выпуски альбомов

# ~ 1989
# ~ ноябрь 1991
# ~ ноябрь 1992
# ~ 1995
# ~ 1995
# ~ 23 ноября 1996
# ~ 25 марта 1999
# ~ февраль 2000
# ~ 26 ноября 2002, 27 мая 2003
# ~ 23 апреля 2005
# ~ 19 апреля 2007
# ~ 25 октября 2011
# ~ 16 мая 2014
# ~ 9 июня 2018
# ~ 28 октября 2021


# 3.
print("\nКакие альбомы были выпущены на LP (на пластинках)?\n")
for record in ddt:
    if "LP" in record["Формат"]:
        print(record["Альбом"])

# ~ Какие альбомы были выпущены на LP (на пластинках)?

# ~ Я получил эту роль
# ~ Оттепель
# ~ Актриса Весна
# ~ Это всё...
# ~ Мир номер ноль
# ~ Иначе
# ~ Прозрачный
# ~ Галя ходи
# ~ Творчество в пустоте