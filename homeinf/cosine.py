#!/usr/bin/env python

# Mikhail (myke) Kolodin, 2026
# 2026-04-23 2026-04-24 1.2
# cosine.py

# ~ Найти число, равное своему косинусу.
# ~ https://en.wikipedia.org/wiki/Dottie_number
# ~ https://www.youtube.com/watch?v=wilJNoc7Ubs
# ~ https://mathworld.wolfram.com/DottieNumber.html

# ~ In mathematics, the Dottie number or the cosine constant is a constant
# ~ that is the unique real root of the equation cos(x)=x, where the argument of cos is in radians.
# ~ The decimal expansion of the Dottie number is given by:
# ~ D = 0.739085133215160641655312087673... (sequence A003957 in the OEIS).

# ~ https://ru.wikipedia.org/wiki/%D0%A7%D0%B8%D1%81%D0%BB%D0%BE_%D0%94%D0%BE%D1%82%D1%82%D0%B8
# ~ Число́ До́тти — постоянная, определяемая как вещественное решение уравнения cos(x)=x,
# ~ где аргумент cos измеряется в радианах. В десятичном представлении число Дотти примерно равно 
# ~ 0,739085133215...


from math import cos

EPS     = 1e-8
nDottie = 0.739085133215160641655312087673

print(f"\n  {nDottie=}")


def calc():

    old = 0.5
    while abs((new := cos(old)) - old) > EPS:
        old = new
    return new
    
cosx = calc()

print(f"     {cosx=}\n{cos(cosx)=}")


  # ~ nDottie=0.7390851332151607
     # ~ cosx=0.7390851372357778
# ~ cos(cosx)=0.7390851305068246
