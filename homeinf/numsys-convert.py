#!/usr/bin/env python

# Mikhail (myke) Kolodin, 2025
# 2025-09-19 2025-09-25 1.2
# numsys-convert.py

# ~ Перевести число n из одной позиционной системы счисления b1 в другую b2,
# ~ 2 <= b_i <= 36.

def convert(nin: str, b1: int, b2:int) -> str:
    """convert"""

    assert type(nin) == str and len(nin) > 0
    assert type(b1) == int and 2 <= b1 <= 36
    assert type(b2) == int and 2 <= b2 <= 36

    # pattern for all digits
    digits = "0123456789abcdefghijklmnopqrstuvwxyz"

    # read nin
    num = 0
    nin = nin.lower()

    try:
    
        for c in nin:
            if c not in digits[:b1]:
                raise ValueError
                
            num = num * b1 + digits.index(c)

        # write nout
        nout = ""

        while num:
            dig = num % b2
            num //= b2
            nout = digits[dig] + nout 

        return nout or "0"

    except ValueError as e:
        print("Error: bad base", e, end=":: ")
        return None
        

def say_convert(nin: str, b1: int, b2:int) -> str:
    """demo convertion"""

    print(f"convertion: {nin}({b1}) -> {convert(nin, b1, b2)}({b2})")
    

say_convert("0", 10, 10)
say_convert("0", 2, 10)
say_convert("0", 10, 16)

say_convert("1", 2, 10)
say_convert("10", 2, 10)
say_convert("11", 2, 10)

say_convert("1", 10, 2)
say_convert("10", 10, 2)
say_convert("11", 10, 2)

say_convert("1", 8, 2)
say_convert("10", 8, 2)
say_convert("11", 8, 2)

say_convert("1", 8, 10)
say_convert("10", 8, 10)
say_convert("11", 8, 10)

say_convert("10", 16, 2)
say_convert("10", 16, 8)
say_convert("10", 16, 10)

say_convert("hello", 36, 10)
say_convert("world", 36, 10)

say_convert("29234652", 10, 36)
say_convert("54903217", 10, 36)

say_convert("89", 8, 10)
say_convert("90", 8, 10)
