#!/usr/bin/env python3
# sum-prod-primes-gen.py
# (C) Mikhail Kolodin, 2025
# 2025-12-19 2025-12-25 2.1

# Найти сумму и произведение простых чисел до 100.
# Используем генератор.

def give_primes(limit : int = 100) -> int:
    """generate primes"""
    
    primes = []
    for n in range(2, limit+1):
        for test in primes:
            if n % test == 0:
                break
        else:
            primes.append(n)
            yield n
            

def psp(limit : int = 100) -> tuple:
    """print sum and product of primes till limit"""

    psum = 0
    pprod = 1

    for n in give_primes(100):
        # print(n, end=", ")
        psum  += n
        pprod *= n

    # print()
    return psum, pprod


def main(limit : int = 100) -> None:
    """run it all"""

    print(f"primes till {limit} give: ", end="")
    asum, aprod = psp(limit)
    print(f"sum = {asum:_}, product = {aprod:_}")


main()

# results

# ~ primes till 100 give: [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
# ~ sum = 1060, product = 2305567963945518424753102147331756070

# ~ primes till 100 give: sum = 1_060, product = 2_305_567_963_945_518_424_753_102_147_331_756_070
