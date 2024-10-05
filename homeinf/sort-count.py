#!usr/bin/env python
# Mikhail Kolodin, 2024
# 2024-10-05 2024-10-05 1.0
# list sorter by counting values

import random
from collections import Counter

MAX = 4
arr = [random.randint(0, MAX) for _ in range(10)]
print("old:", arr)

# 1. 
# ~ cnt = [0 for _ in range(MAX+1)]

# ~ for e in arr:
    # ~ cnt[e] += 1

# ~ print("cnt:", cnt)

# ~ out = []
# ~ for i, e in enumerate(cnt):
    # ~ for j in range(e):
        # ~ out.append(i)

# ~ print("out:", out)

# 2.

# ~ arr = [random.randint(0, MAX) for _ in range(10)]
# ~ print("old:", arr)

# ~ cnt = [arr.count(i) for i in range(MAX+1)]
# ~ print("cnt:", cnt)

# ~ out = []
# ~ for i, e in enumerate(cnt):
    # ~ for j in range(e):
        # ~ out.append(i)
# ~ print("out:", out)

# 3. class Counter

# ~ cnt = Counter(arr)
# ~ print("cnt:", cnt)

# ~ srt = [(k, cnt[k]) for k in sorted(cnt) ]
# ~ print("crt:", srt)

# ~ out = []
# ~ for k, v in srt:
    # ~ for i in range(v):
        # ~ out.append(k)
# ~ print("out:", out)

# 4. class Counter

cnt = Counter(arr)
print("cnt:", cnt)

out = [ i for i in sorted(cnt) for e in range(cnt[i]) ]
print("out:", out)
      
        
