#!/usr/bin/env python

# Mikhail (myke) Kolodin, 2025-2026
# 2025-09-19 202601-30 12.1
# numsys-convert.py

# ~ Перевести число n из одной позиционной системы счисления b1 в другую b2,
# ~ 2 <= b_i <= 36.


def convert(nin: str, b1: int, b2:int) -> str:
    """convert"""

    assert type(nin) == str and len(nin) > 0, "String for number must be non-empty"
    assert type(b1) == int and 2 <= b1 <= 36, "Base b1 must be between 2 and 36 incl."
    assert type(b2) == int and 2 <= b2 <= 36, "Base b2 must be between 2 and 36 incl."

    # pattern for all digits
    digits = "0123456789abcdefghijklmnopqrstuvwxyz"

    try:    
        # read nin
        num = 0
        nin = nin.lower()

# 1st variant, -->

        for c in nin:
            if c not in digits[:b1]:
                raise ValueError
                
            num = num * b1 + digits.find(c)

# 2nd variant,  <--

# 2a
#    for power, dig in enumerate(nin[::-1]):
#        num += int(dig, b1) * b1 ** power

# 2b
#    num = int(nin, b1)

# 3rd variant
        
    # ~ return int(nin, b1)

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
    

def demo():
# ~ normal
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

    # ~ errors
    say_convert("89", 8, 10)
    say_convert("90", 8, 10)


# ~ demo()


if __name__ == '__main__':
    demo()



# ~ Прочее:

# ~ 1. https://www.youtube.com/shorts/Kkv3UIAuPzg
# ~ Простой перевод в любую систему счисления

# ~ 2. https://www.youtube.com/watch?v=juhMGb5KJFU
# ~ Перевод из двоичной в восьмеричную систему счисления

# ~ 3. https://www.youtube.com/watch?v=FQiDzqtjkjU
# ~ Перевод из восьмеричной в двоичную систему счисления

# ~ 4. https://www.youtube.com/watch?v=pdXQ9r1NqBQ
# ~ Перевод из 16 в 8 систему счисления

# ~ abba (16) -> ... (8)
# ~ 1010 1011 1011 1010 (2)
# ~ 1 010 101 110 111 010 (2)
# ~ 1 2 5 6 7 2    (8)
