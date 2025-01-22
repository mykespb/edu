#!/usr/bin/env python

# Mikhail (myke) Kolodin, 2025
# 2025-01-17 2025-01-22 1.2
# friday13.py

# ~ Пятница 13ое

# ~ Считается, что этот день несчастный.
# ~ Верите вы в это или нет, но знать об опасности надо :)
# ~ Определить. есть ли в нынешнем году пятница 13, в какие месяцы,
# ~ и сколько дней осталось до ближайшей пятницы 13го. когда бы она ни случилась.

# ---------------------------------------------
# импорты и установки

from datetime import date

# ---------------------------------------------
# программа

wdays = 'пн вт ср чт пт сб вс'.split()

def beware():
    """дать предупреждение про все пт13
    """

    past()
    future()


def past():
    """проработать прошедшую часть года
    """

    global today, proleptic

    today = date.today()
    wd = today.weekday()
    proleptic = today.toordinal()
    
    print(f"{today=}, {wd=}, {wdays[wd]=}, {proleptic=}")

    for amonth in range(1, today.month + 2):
        if amonth == today.month and 13 > today.day:
            break
        d13 = date(today.year, amonth, 13)
        wd13 = d13.weekday()
        if wd13 == 4:
            print(f"{d13} было пятницей")

def future():
    """проработать будущее
    """

    # ищем в этом году

    found = False
    
    for amonth in range(today.month, 13):
        if amonth == today.month and 13 < today.day:
            continue
            
        d13 = date(today.year, amonth, 13)
        wd13 = d13.weekday()
        
        if wd13 == 4:
            print(f"{d13} будет пятницей")
            prolfut = d13.toordinal()
            print(f"до неё осталось дней: {prolfut - proleptic}")
            found = True

    # если не нашли, то ищем во всех последующих годах до 9999 искл.

    if not found:
        for ayear in range(today.year + 1, 9999):
            for amonth in range(1, 13):

                d13 = date(ayear, amonth, 13)
                wd13 = d13.weekday()
                
                if wd13 == 4:
                    print(f"{d13} будет пятницей")
                    prolfut = d13.toordinal()
                    print(f"до неё осталось дней: {prolfut - proleptic}")
                    found = True
                    break
            if found:
                break
            

# ---------------------------------------------
# тестирование

beware()

# ---------------------------------------------
# результаты

# ~ today=datetime.date(2025, 1, 17), wd=4, wdays[wd]='пт', proleptic=739268
# ~ 2025-06-13 будет пятницей
# ~ до него осталось дней: 147
# ~ 2026-02-13 будет пятницей
# ~ до него осталось дней: 392

# ---------------------------------------------
