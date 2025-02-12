#!/usr/bin/env python
# Mikhail (myke) Kolodin
# 2025-01-16 2025-01-16 1.1
# max-sum-digits.py

# ~ Найти число с макс. суммой цифр (натуральное, из случайно заданного набора)

SIZE  = 10              # количество чисел в тесте
#LIMIT = 1_000_000       # предел для величины числа
LIMIT = 100              # предел для величины числа

from random import randint

# -------------------------------------
# генерация

def make() -> int:
    """сделать число"""

    return [ randint(1, LIMIT) for _ in range(SIZE) ]

# -------------------------------------
# подсчёт

def summa(n : int) -> int:
    """сумма для одного числа"""

    return sum( int(c) for c in str(n) )


def max_sum(lst : list[int]) -> int:
    """найти число с макс суммой"""

    return ( out := max( lst, key = summa ), summa(out))

# -------------------------------------
# тестирование

def test() -> None:
    """протестировать"""

    seq = make()
    res, su = max_sum(seq)

    print(f"для последовательности {seq}\nчисло с макс. суммой цифр это {res} с суммой {su}")

test()

# -------------------------------------
# результаты

# ~ для последовательности [10, 15, 18, 16, 13, 8, 18, 8, 1, 13]
# ~ число с макс. суммой цифр это 18 с суммой 9

# ~ для последовательности [1, 15, 6, 14, 17, 20, 18, 19, 9, 19]
# ~ число с макс. суммой цифр это 19 с суммой 10

# ~ для последовательности [671126, 974240, 813889, 716208, 692931, 98909, 850005, 982868, 988825, 687527]
# ~ число с макс. суммой цифр это 982868 с суммой 41

# ~ для последовательности [466035, 868114, 847890, 542862, 912134, 433930, 857411, 701041, 417970, 139648]
# ~ число с макс. суммой цифр это 847890 с суммой 36

# ~ для последовательности [586054, 152694, 543598, 925388, 907430, 92998, 204366, 886686, 14280, 221031]
# ~ число с макс. суммой цифр это 886686 с суммой 42

# ~ для последовательности [596268, 911852, 418991, 739604, 907574, 408768, 699935, 994132, 603447, 649122]
# ~ число с макс. суммой цифр это 699935 с суммой 41

# ~ для последовательности [501316, 716788, 814942, 708148, 429124, 676050, 530766, 841066, 322193, 69346]
# ~ число с макс. суммой цифр это 716788 с суммой 37

# -------------------------------------
