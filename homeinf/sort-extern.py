#!/usr/bin/env python

# sort-extern.py
# external sorting
# Mikhail (myke) Kolodin, 2024
# 2024-10-02 2024-10-02 1.1

import random

a1 = [random.randint(-99, 99) for _ in range(10))
a2 = [random.randint(-99, 99) for _ in range(10))
a1.sort()
a2.sort()
#...

# а теперь
a3 = a1 + a2
# но так, чтобы a3 тоже был отсортирован

