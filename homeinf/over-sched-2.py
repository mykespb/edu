#!/usr/bin/env python

# Mikhail (myke) Kolodin, 2025
# 2025-01-09 2025-0-1-09 1.0
# over-sched-2.py

# ~ https://www.culture.ru/poems/105/boltunya
# ~ Драмкружок, кружок по фото,
# ~ Хоркружок — мне петь охота,
# ~ За кружок по рисованью
# ~ Тоже все голосовали.
# ~ (С) Агния Барто 1934 г.

# ~ Очень занятый мальчик составил расписание занятий на день,
# ~ и теперь переживает, нет ли там накладок.
# ~ Помогите ему.

# ~ Предыдущее решение неполное.
# ~ Оно проверяет ненакладность только соседних строк,
# ~ а накладки могут быть и в более отдалённых строках.
# ~ надо всех сравнивать со всеми.

sched1 = """
0900 0945 математика
1000 1045 русский язык
1200 1205 обед
0845 0900 завтрак
1315 1330 английский язык
1420 1440 информатика
1900 2000 кино
0800 0815 зарядка
1435 1455 физкультура
0900 1600 пение
1205 1225 рисование
1550 1635 музыка
1630 1700 математика
1325 1345 чтение
"""

sched2 = """
0900 0945 математика
1000 1045 русский язык
1200 1205 обед
0845 0900 завтрак
1315 1330 английский язык
1420 1440 информатика
1205 1225 рисование
1550 1635 музыка
1655 1700 математика
1800 1855 ужин
1900 2000 кино
0800 0815 зарядка
"""


def test(what: str) -> bool:
    """
    проверить расписание
    """

    print("\n--------------------- расписание ---------------------\n")

    sch = []

    for txt in what.strip().splitlines():
        tfrom, tto, desc = txt.strip().split(maxsplit=2)
        sch.append( (tfrom, tto, desc) )

    sch.sort()

    tprint(sch)

    print("\nпроверяем...")
    errors = 0
    for line1 in sch:
        tfrom1, tto1, desc1 = line1

        for line2 in sch:
            tfrom2, tto2, desc2 = line2

            if line1 == line2:
                continue    # с собой не сравниваем
        
            if tfrom1 < tfrom2 < tto1:
                print(f"увы! занятие '{desc2}' (с {tfrom2} до {tto2}) пересекается с занятием '{desc1}' (с {tfrom1} до {tto1})")
                errors += 1

    if errors:
        print(f"\nитого:\n{errors} - столько было ошибок в расписании")
    else:
        print(f"\nитого:\nв расписании нет ошибок")

    print("\n--------------------- конец расписания ---------------------\n")


def tprint(what : list) -> None:
    """
    красиво напечатать расписание
    """

    for line in what:
        tfrom, tto, desc = line
        print(f"{tfrom} {tto} - {desc}")

test(sched1)
test(sched2)

# ~ --------------------- расписание ---------------------

# ~ 0800 0815 - зарядка
# ~ 0845 0900 - завтрак
# ~ 0900 0945 - математика
# ~ 1000 1045 - русский язык
# ~ 1200 1205 - обед
# ~ 1205 1225 - рисование
# ~ 1315 1330 - английский язык
# ~ 1325 1345 - чтение
# ~ 1420 1440 - информатика
# ~ 1435 1455 - физкультура
# ~ 1550 1635 - музыка
# ~ 1630 1700 - математика
# ~ 1900 2000 - кино

# ~ проверяем...
# ~ увы! занятие 'чтение' начинается в 1325, что раньше, чем окончание предыдущего занятия 'английский язык' в 1330
# ~ увы! занятие 'физкультура' начинается в 1435, что раньше, чем окончание предыдущего занятия 'информатика' в 1440
# ~ увы! занятие 'математика' начинается в 1630, что раньше, чем окончание предыдущего занятия 'музыка' в 1635

# ~ итого:
# ~ 3 - столько было ошибок в расписании

# ~ --------------------- конец расписания ---------------------


# ~ --------------------- расписание ---------------------

# ~ 0800 0815 - зарядка
# ~ 0845 0900 - завтрак
# ~ 0900 0945 - математика
# ~ 1000 1045 - русский язык
# ~ 1200 1205 - обед
# ~ 1205 1225 - рисование
# ~ 1315 1330 - английский язык
# ~ 1420 1440 - информатика
# ~ 1550 1635 - музыка
# ~ 1655 1700 - математика
# ~ 1800 1855 - ужин
# ~ 1900 2000 - кино

# ~ проверяем...

# ~ итого:
# ~ в расписании нет ошибок

# ~ --------------------- конец расписания ---------------------
