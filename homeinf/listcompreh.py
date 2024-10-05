#!isr/bin/env python
# Mikhail Kolodin, 2024
# 2024-10-05 2024-10-05 1.0
# list comprehension examples

import random
from pprint import pp

# 1. square matrix with numbers' products

# ~ prod = [ [i*j for i in range(5)] for j in range(5)]
# ~ pp(prod)

# 2. strings product

# ~ prod = [ [i+str(j) for i in 'abcd'] for j in range(5)]
# ~ pp(prod)

# 3. characters' codes

# ~ import string

# ~ codes = [c + '=' + str(ord(c)) + ", " for c in string.ascii_uppercase]
# ~ print(codes)

# 4. div by 7

# ~ div7 = [i for i in range(1, 100) if i % 7 == 0]
# ~ print(div7)

# 5. div by 7, squared

div7 = [i*i for i in range(1, 100) if i % 7 == 0]
print(div7)
