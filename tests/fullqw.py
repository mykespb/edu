#!/python3.10

# Mikhail (myke) Kolodin, 2021
# 2021-12-21 2021-12-21 1.0
# fullqw.py

print("""
задача: 
найти все числа в заданном диапазоне,
являющиеся полными квадратами
""")

import math

a, b = map(int, input("укажите через пробел 2 числа - границы диапазона: ") .split())

for i in range(a, b+1):
	if math.isqrt(i)**2 == i:
		print(i, end=", ")
