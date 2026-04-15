#!/usr/bin/env python

# plus.py
# проверки арифметики - простое сложение
# Mikhail (myke) Kolodin, 2026
# 2026-04-15 2026-04-15 1.1

# ------------------------------------------------
# ~ из "диджитализируй" 2026-04-15

a = 0.1
b = 0.2
c = 0.3

print(a+b+c)
print(c+b+a)

# ~ assert a+b+c == c+b+a, "oops!"

eps = 1e-6

assert (a+b+c - (c+b+a)) <= eps, "oops!"

# ~ 0.6000000000000001
# ~ 0.6
# ~ Traceback (most recent call last):
  # ~ File "/home/myke/pro/edu/tests/matemagic/plus.py", line 17, in <module>
    # ~ assert a+b+c == c+b+a, "oops!"
           # ~ ^^^^^^^^^^^^^^
# ~ AssertionError: oops!

# ------------------------------------------------
