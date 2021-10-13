#!python3.10

# (C) Mikhail Kolodin, 2021
# 2021-10-14 2021-10-14 1.1
# Задача из яндекса -
# Дан набор чисел, в котором все числа встречаются дважды,
# и только одно число - один раз. Найти его.

# это набор тестов
tests = [
 (1, 1, 2, 88, 0, -5, 2, 0, -5),
 (6, -2, -6, 6, -2, 7, -6),
 (11, 22, 33, 0, 11, 44, 33, 44, 0)
 ]

from collections import Counter

def tester():
    """ organizer """
    for test in tests:
        finder(test)

# это решения

def finder1(test):
    """ finder itself v.1 """
    cnt = Counter(test)
    for k, v in cnt.items():
        if v == 1:
            print("single is", k)
            return
    print(singles)

def finder2(test):
    """ finder itself v.2 """
    cnt = Counter(test)
    singles = [k for k, v in cnt.items() if v==1][0]
    print("single is", singles)


# запускаем тесты, всё ок
#finder = finder2
finder = finder2

tester()

# ------------------
# results:
