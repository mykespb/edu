#!/usr/bin/env python
# Mikhail Kolodin, 2024
# 2024-10-05 2024-10-05 1.1
# многомерные списки и т.п.

import random
import string
from pprint import pp

chars = string.ascii_letters
pp(f"{chars=}")
print()

md = [ random.choice(chars) for i in range(5) ]
pp(md)
print()

md = [ [random.choice(chars) for i in range(5) ] for j in range(4) ]
pp(md)
print()

md = [ [ [random.choice(chars) for i in range(5) ] for j in range(4) ] for k in range(3) ]
pp(md)
print()

# ~ "chars='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'\n\n"

# ~ ['p', 'R', 'p', 'B', 'i']

# ~ [['s', 'r', 'g', 'A', 'F'],
 # ~ ['y', 'r', 'V', 'F', 'I'],
 # ~ ['l', 'c', 'm', 'i', 'L'],
 # ~ ['M', 'Y', 'Q', 't', 'V']]

# ~ [[['g', 'm', 'P', 'j', 'y'],
  # ~ ['P', 'M', 'R', 'R', 'E'],
  # ~ ['F', 'B', 'J', 'B', 'x'],
  # ~ ['O', 'h', 'G', 'm', 'U']],
 # ~ [['X', 'w', 'L', 'v', 'b'],
  # ~ ['g', 'G', 'y', 'U', 'I'],
  # ~ ['u', 'k', 'X', 'h', 'B'],
  # ~ ['U', 'Y', 'Y', 'h', 'I']],
 # ~ [['f', 'y', 'U', 'D', 'X'],
  # ~ ['x', 'B', 'd', 'q', 'p'],
  # ~ ['X', 'b', 'M', 'V', 'K'],
  # ~ ['V', 'O', 'C', 'G', 'E']]]
