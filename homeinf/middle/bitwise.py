#!/usr/bin/env python

# Mikhail (myke) Kolodin, 2025
# 2025-01-30 2025-01-30 1.0
# bitwise.py

# ~ (По)битовые операции -- понятия и упражнения

# ~ & | ^ ! << >>

# ~ https://wiki.python.org/moin/BitwiseOperators
# ~ https://www.geeksforgeeks.org/python-bitwise-operators/
# ~ https://stackoverflow.com/questions/1746613/bitwise-operation-and-usage
# ~ https://www.geeksforgeeks.org/bitwise-algorithm-in-python/
# ~ https://note.nkmk.me/en/python-bit-operation/

# ~ x << y
# ~ Returns x with the bits shifted to the left by y places (and new bits on the right-hand-side are zeros). This is the same as multiplying x by 2**y.
# ~ x >> y
# ~ Returns x with the bits shifted to the right by y places. This is the same as floor division of x by 2**y.
# ~ x & y
# ~ Does a "bitwise and". Each bit of the output is 1 if the corresponding bit of x AND of y is 1, otherwise it's 0.
# ~ x | y
# ~ Does a "bitwise or". Each bit of the output is 0 if the corresponding bit of x AND of y is 0, otherwise it's 1.
# ~ ~ x
# ~ Returns the complement of x - the number you get by switching each 1 for a 0 and each 0 for a 1. This is the same as -x - 1.
# ~ x ^ y
# ~ Does a "bitwise exclusive or". Each bit of the output is the same as the corresponding bit in x if that bit in y is 0, and it's the complement of the bit in x if that bit in y is 1.

# ~ -----------------------------------------------

x = 0b111
y = 0b100

print(f"{x:03b} & {y:03b} = {x&y:b}")
# ~ 7 & 4 = 4

# ~ -----------------------------------------------

x = 0b111
y = 0b100

print(f"{x:03b} | {y:03b} = {x|y:03b}")
# ~ 7 | 4 = 7

# ~ -----------------------------------------------

x = 0b111
y = 0b100

print(f"{x:03b} ^ {y:03b} = {x^y:03b}")
# ~ 7 ^ 4 = 3

# ~ -----------------------------------------------

x = 0b111

print(f"~{x:03b} = {~x:03b}")
# ~ ~7 = -8

# ~ -----------------------------------------------

x = 0b010

print(f"{x:03b} >> 1 = {x>>1:03b}")
# ~ 2 >> 1 = 1

# ~ -----------------------------------------------

x = 0b010

print(f"{x:03b} << 1 = {x<<1:03b}")
# ~ 2 << 1 = 4

# ~ -----------------------------------------------
