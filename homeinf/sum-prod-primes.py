#!/usr/bin/env python3
# sum-prod-primes.py
# (C) Mikhail Kolodin, 2025
# 2025-12-19 2025-12-19 1.0

# ~ Найти сумму и произведение простых чисел до 100.

def psp(limit : int = 100) -> None:
    """print sum and product of primes tilll limit"""

    psum = 0
    pprod = 1
    primes = []

    for n in range(2, limit):
        for d in primes:
            if n % d == 0:
                break
        else:
            psum += n
            pprod *= n
            primes.append(n)

    # ~ print(primes)
    return psum, pprod


def main(limit : int = 100) -> None:
    """run it all"""

    print(f"primes till {limit} give: ", end="")
    asum, aprod = psp(limit)
    print(f"sum = {asum:_}, product = {aprod:_}")


main()



# ~ primes till 100 give: [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
# ~ sum = 1060, product = 2305567963945518424753102147331756070

# ~ primes till 100 give: sum = 1_060, product = 2_305_567_963_945_518_424_753_102_147_331_756_070
