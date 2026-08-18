#!/usr/bin/env python
# Miklhail (myke) Kolodin
# simple / plustr.py
# 2026-08-14 2026-08-18 1.2

# ~ Дан набор различных слов.
# ~ Известно, что некоторые слова могли быть получены слиянием пары других слов из этого же набора.
# ~ Найти все такие тройки слов или сказать, что их нет.

# каждая строка данных - отдельный тест.

data = """
буква ед буквоед еда
килограмм грамм километр кило метр метро метроном килотонна тонна
хорда хор данетка да даром ром хором кино театр лог кинолог кинотеатр
а у ау мусор ауау
"""

from itertools import permutations


def atest(ex):
    """один тест"""

    num = 0
    for a, b, c in permutations(sorted(ex.split()), 3):
        if a + b == c:
            num += 1
            print(f"{num}) {a} + {b} = {c}")
    if num == 0:
        print("увы, нет слов...")


def btest(ex):
    """другой тест"""

    num = 0
    xex = ex.split()
    
    for first in xex:
        for second in xex:
            # ~ if first == second: continue
            for third in xex:
                # ~ if first == third or second == third: continue
                if first + second == third:
                # ~ if (first + second) in xex:
                    num += 1
                    print(f"{num}) {first} + {second} = {third}")

    if num == 0:
        print("увы, нет слов...")


test = btest


def main():
    """все тесты"""

    for num, ex in enumerate(data.strip().splitlines(), start=1):
        print(f"\n{num}. {ex} =>")
        test(ex)


main()

