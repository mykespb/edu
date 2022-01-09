#!/usr/bin/env python

# sumkubdig.py
# (C) Mikhail (myke) Kolodin, 2021
# 2022-01-10 2022-01-10 1.3

# ~ Найдите 3-значные числа, равные сумме кубов своих цифр.

kolvo = 0

for d1 in range(1, 10):
    for d2 in range(10):
        for d3 in range(10):
            if d1**3 + d2**3 + d3**3 == d1*100 + d2*10 + d3:
                kolvo += 1
                print("нумер", kolvo, ", число", d1, d2, d3)
print("\nвсего:", kolvo)

# ~ нумер 1 , число 1 5 3
# ~ нумер 2 , число 3 7 0
# ~ нумер 3 , число 3 7 1
# ~ нумер 4 , число 4 0 7

# ~ всего: 4
