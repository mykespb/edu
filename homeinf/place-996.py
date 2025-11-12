#!/usr/bin/env python

# Mikhail (myke) Kolodin, 2025
# 2025-11-13 2025-11-13 0.1
# place-996.py

# ~ Место числа 996

# ~ Все натуральные числа от 1 до 1000 выписали в следующем порядке:
# ~ сначала были выписаны в порядке возрастания числа, сумма цифр которых равна 1,
# ~ затем (также в порядке возрастания) — числа, сумма цифр которых равна 2,
# ~ потом числа, сумма цифр которых равна 3 и т. д.
# ~ На каком месте окажется число 996?

NUMBER = 996

from collections import defaultdict

nums = defaultdict(list)

def summa(i):
    """подсчитать сумму цифр цисла"""
    return sum( map(int, str(i)  ))
    

for i in range(1, 1001):
    nums[summa(i)].append(i)
# ~ print(nums)

places = 0

for k in sorted(nums.keys()):
    # ~ print(k, end=", ")
    # ~ print()
    if NUMBER in nums[k]:
        ind = nums[k].index(NUMBER)
        print(f"число {NUMBER} находится на {places + ind + 1} месте")
        break
    else:
        places += len(nums[k])
        

# ~ число 996 находится на 990 месте -- правильно

