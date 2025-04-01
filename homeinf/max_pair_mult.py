#!/usr/bin/env python
# Mikhail (myke) Kolodin
# max_pair_mult.py
# 2025-04-01 2025-04-01 1.0

# ~ Есть несколько наборов натуральных чисел, записанных построчно.
# ~ Определить пару чисел (внутри одного из наборов), дающих максимальное произведение.
# ~ (Если наборов нет, сообщить. Если максимумов несколько, показать один любой.)

data = """
15 45 22 456 34 77 22 455 666
789 45 239 843
5678 12 34 56 789
998 665 221
"""

# ~ data = ""

def solve():
    """решить всё"""

    groups = data.strip().splitlines()
    print(f"{groups=}")

    assert len(groups), "Должны быть указаны наборы чисел!"

    mval = left = right = 0
    
    for line in groups:
        nums = list(map(int, line.strip().split()))
        # ~ print(f"{nums=}")
    
        for i in range(len(nums)-1):
            prod = nums[i]*nums[i+1]

            if prod > mval:
                mval = prod
                left = nums[i]
                right = nums[i+1]

    print(f"максимальное произведение равно {mval} для чисел {left} и {right}")

solve()
