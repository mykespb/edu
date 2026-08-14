#!/usr/bin/env python
# Miklhail (myke) Kolodin
# simple / plustr.py
# 2026-08-14 2026-08-14 1.0

# ~ Дан набор слов.
# ~ Известно, что некоторые слова могли быть получены слиянием пары других слов из этого же набора.
# ~ Найти все такие тройки слов или сказать, что их нет.

# каждая строка данных - отдельный тест.

data = """
буква ед буквоед еда
килограмм грамм километр кило метр метро метроном
хорда хор данетка да 
"""


from itertools import permutations


def main():
    """все тесты"""

    for num, ex in enumerate(data.strip().splitlines(), start=1):
        print(f"{num}. {ex} =>")
        atest(ex)


def atest(ex):
    """один тест"""

    num = 0
    for a, b, c in permutations(sorted(ex.split()), 3):
        if a + b == c:
            num += 1
            print(f"{num}) {a} + {b} = {c}")
    if num == 0:
        print("увы, нет слов...")

main()

