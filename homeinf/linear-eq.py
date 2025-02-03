#!/usr/bin/env python

# Mikhail (myke) Kolodin, 2025
# linear-eq.py
# 2025-02-03 2025-02-03 1.0

# ~ Решение линейных уравнений.
# ~ a, b -> x / {}

# -------------------------------------------
# решалка

def linear(a :float, b :float) -> float:
    """решатель"""

    assert a != 0, "Linear equation: coefficient a must be non-zero!"

    return -b / a

# -------------------------------------------
# тестилка

def tester(a :float, b :float) -> None:
    """тестилка"""

    print(f"{a}x + {b} = 0 => x = {linear(a, b)}\n")
    
# -------------------------------------------
# тесты

tester(1., 0.)
tester(1., 2.)
tester(2., 1.)
tester(-1., -2.)

#tester(0., 0.)
#tester(0., -1.)

# -------------------------------------------
# результаты

# ~ 1.0x + 0.0 = 0 => x = -0.0

# ~ 1.0x + 0.0 = 0 => x = -0.0

# ~ 1.0x + 2.0 = 0 => x = -2.0

# ~ 2.0x + 1.0 = 0 => x = -0.5

# ~ -1.0x + -2.0 = 0 => x = -2.0


# ~ Traceback (most recent call last):
  # ~ File "/home/myke/pro/edu/homeinf/linear-eq.py", line 32, in <module>
    # ~ tester(0., 0.)
    # ~ ~~~~~~^^^^^^^^
  # ~ File "/home/myke/pro/edu/homeinf/linear-eq.py", line 26, in tester
    # ~ print(f"{a}x + {b} = 0 => x = {linear(a, b)}")
                                   # ~ ~~~~~~^^^^^^
  # ~ File "/home/myke/pro/edu/homeinf/linear-eq.py", line 16, in linear
    # ~ assert a != 0, "Linear equation: coefficient a must be non-zero!"
           # ~ ^^^^^^
# ~ AssertionError: Linear equation: coefficient a must be non-zero!

# ~ Traceback (most recent call last):
  # ~ File "/home/myke/pro/edu/homeinf/linear-eq.py", line 33, in <module>
    # ~ tester(0., -1.)
    # ~ ~~~~~~^^^^^^^^^
  # ~ File "/home/myke/pro/edu/homeinf/linear-eq.py", line 26, in tester
    # ~ print(f"{a}x + {b} = 0 => x = {linear(a, b)}\n")
                                   # ~ ~~~~~~^^^^^^
  # ~ File "/home/myke/pro/edu/homeinf/linear-eq.py", line 16, in linear
    # ~ assert a != 0, "Linear equation: coefficient a must be non-zero!"
           # ~ ^^^^^^
# ~ AssertionError: Linear equation: coefficient a must be non-zero!

# -------------------------------------------
