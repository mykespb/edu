#!/usr/bin/env python

# Mikhail (myke) Kolodin, 2021
# 2021-11-26 2022-04-22 0.1
# himnabory.py

nabor1 = "H2SO4 H2O марганцовка NaCl HCl NH3 NaOH CuOH спирт"
nabor2 = "нашатырь H2O спирт фенолфталеин Cu Fe Zn KBrO3 NaOH"

# решение 1

n1 = set(nabor1.split())
n2 = set(nabor2.split())

print (f"{n1=}\n{n2=}")
