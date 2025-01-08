#!/usr/bin/env python
# Mikhail (myke) Kolodin, 2024
# 2025-01-05 2025-01-08 3.2

# ~ Сделать список из нескольких (настраивается) чисел, случайно, каждое от 1 до 100 (вкл.).
# ~ Подсчитать, каких получилось чисел больше, чётных или нечётных.

LIMIT = 100
SIZE  = 10

from random import randint
from time import asctime, time

print(f"Начинаем в {time()} = {asctime()}")

def make():
    """make list"""

    out = [ randint(1, LIMIT) for _ in range(SIZE-5, SIZE+5) ]
    print("list = ", out)

    return out


def comparethem1(numbers):
    """evens or odds?"""

    len_list = len(numbers)

    num_odds = num_evens = 0

    for i in range(len_list):
        if numbers[i] % 2 == 1:
            num_odds += 1
        else:
            num_evens += 1

    if num_odds > num_evens:
        print("Больше нечётных, чем чётных")
    elif num_odds < num_evens:
        print("Больше чётных, чем нечётных.")
    else:
        print("Нечётных и чётных поровну.")


def comparethem2(numbers):
    """evens or odds?"""

    num_odds = num_evens = 0

    for e in numbers:
        if e % 2 == 1:
            num_odds += 1
        else:
            num_evens += 1

    if num_odds > num_evens:
        print("Больше нечётных, чем чётных")
    elif num_odds < num_evens:
        print("Больше чётных, чем нечётных.")
    else:
        print("Нечётных и чётных поровну.")


def comparethem3(numbers):
    """evens or odds?"""

    num_odds  = len( list( filter( lambda x: x % 2 == 1, numbers)))
    num_evens = len( list( filter( lambda x: x % 2 == 0, numbers)))

    if num_odds > num_evens:
        print("Больше нечётных, чем чётных")
    elif num_odds < num_evens:
        print("Больше чётных, чем нечётных.")
    else:
        print("Нечётных и чётных поровну.")


def comparethem4(numbers):
    """evens or odds?"""

    len_list = len(numbers)
    len_half = len_list // 2 + 1

    num_odds = num_evens = 0

    for e in numbers:
        if e % 2 == 1:
            num_odds += 1
            if num_odds >= len_half:
                break
        else:
            num_evens += 1
            if num_evens >= len_half:
                break

    if num_odds > num_evens:
        print("Больше нечётных, чем чётных")
    elif num_odds < num_evens:
        print("Больше чётных, чем нечётных.")
    else:
        print("Нечётных и чётных поровну.")


def comparethem5(numbers):
    """evens or odds?"""

    num = 0

    for e in numbers:
        num += 1 if e % 2 == 1 else -1 if e % 2 == 0 else 0

    if num > 0:
        print("Больше нечётных, чем чётных")
    elif num < 0:
        print("Больше чётных, чем нечётных.")
    else:
        print("Нечётных и чётных поровну.")


def comparethem6(numbers):
    """evens or odds?"""

    len_list = len(numbers)
    len_half = len_list // 2 + 1

    num = 0

    for e in numbers:
        num += 1 if e % 2 == 1 else -1 if e % 2 == 0 else 0
        if num >= len_half:
            break

    if num > 0:
        print("Больше нечётных, чем чётных")
    elif num < 0:
        print("Больше чётных, чем нечётных.")
    else:
        print("Нечётных и чётных поровну.")


def comparethem7(numbers):
    """evens or odds?"""

    num_odds  = len( list( filter( lambda x: x % 2 == 1, numbers)))
    num_evens = len(numbers) - num_odds

    if num_odds > num_evens:
        print("Больше нечётных, чем чётных")
    elif num_odds < num_evens:
        print("Больше чётных, чем нечётных.")
    else:
        print("Нечётных и чётных поровну.")


compare = comparethem7

def main1(times=1):
    """starter"""

    lst = make()
    compare(lst)


def main2(times=1):
    """starter with timer"""

    total1 = total2 = total3 = total4 = total5 = total6 = total7 = 0
    
    for rept in range(times):
        lst = make()
        
        start = time()
        comparethem1(lst)
        end = time()
        total1 += end - start

        start = time()
        comparethem2(lst)
        end = time()
        total2 += end - start

        start = time()
        comparethem3(lst)
        end = time()
        total3 += end - start

        start = time()
        comparethem4(lst)
        end = time()
        total4 += end - start

        start = time()
        comparethem5(lst)
        end = time()
        total5 += end - start

        start = time()
        comparethem6(lst)
        end = time()
        total6 += end - start

        start = time()
        comparethem7(lst)
        end = time()
        total7 += end - start

    print(f"Потребовалось в среднем секунд:...")
    print(f"для 1 версии: {total1 / times}")
    print(f"для 2 версии: {total2 / times}")
    print(f"для 3 версии: {total3 / times}")
    print(f"для 4 версии: {total4 / times}")
    print(f"для 5 версии: {total5 / times}")
    print(f"для 6 версии: {total6 / times}")
    print(f"для 7 версии: {total7 / times}")

main = main2

main(1)


# ~ list =  [1, 1, 1, 2, 1, 2, 2, 1, 2, 1, 2, 2, 1, 2, 2, 1, 2]
# ~ Больше чётных, чем нечётных.
# ~ Больше чётных, чем нечётных.
# ~ Больше чётных, чем нечётных.
# ~ Больше чётных, чем нечётных.
# ~ Больше чётных, чем нечётных.
# ~ Больше чётных, чем нечётных.
# ~ Больше чётных, чем нечётных.
# ~ Потребовалось в среднем секунд:...
# ~ для 1 версии: 2.2411346435546875e-05
# ~ для 2 версии: 4.76837158203125e-06
# ~ для 3 версии: 6.67572021484375e-06
# ~ для 4 версии: 3.5762786865234375e-06
# ~ для 5 версии: 3.0994415283203125e-06
# ~ для 6 версии: 3.814697265625e-06
# ~ для 7 версии: 3.5762786865234375e-06

