#!/usr/bin/env python

# myke's test for happy numbers
# 2024-08-12

from itertools import product

count = 0
for a, b, c, d in product( range(10), range(10), range(10), range(10)):
    count += (a+b == c+d)

print(f"happies: {count=}")

# myke@mykex:~/tmp$ python ./happy4.py 
# happies: count=670
