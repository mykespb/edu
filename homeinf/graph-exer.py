#!/usr/bin/env python

# Mikhail (myke) Kolodin, 2025
# 2025-11-21 2025-11-11 1.0
# graph-exer.py

# неориентированный граф

g = ((1, 2), (1, 3), (1, 9), (2, 5), (5, 6), (4, 1), (2, 1), (2, 1), (1, 1))

# с какими узлами связан узел 1? node, link, graph

nodewith1 = []
for link in g:
    for inlink in link:
        if inlink == link[0] == 1:
            nodewith1.append(link[1])
        elif inlink == link[1] == 1:
            nodewith1.append(link[0])
print(f"Вот с чем связана единица - {nodewith1}")

ones = []

for left, right in g:
    if left == 1:
        ones.append(right)
    elif right == 1:
        ones.append(left)
        
ones = sorted(set(ones))
print(ones)

# сколько всего узлов в сети?

# 1) list

nodes = []

for left, right in g:
    if left not in nodes:
        nodes.append(left)
    if right not in nodes:
        nodes.append(right)
        
print("всего узлов:", len(nodes), ", это", sorted(nodes))

# 2) set

nodes = set()
for left, right in g:
    nodes.add(left)
    nodes.add(right)

print("всего узлов:", len(nodes), ", это", sorted(nodes))

# у какого узла больше всего соседей? (если таких несколько, указать все)

# 1) dict

cnt = {}
maxvalue = 0

for e in g:
    for v in e:
    
        if v not in cnt:
            cnt[v] = 1
        else:
            cnt[v] += 1

        maxvalue = max(cnt[v], maxvalue)

#print("счётчики соседей:")
#print(cnt)

print("максимум соседей:")
for k, v in cnt.items():
    if v == maxvalue:
        print(f"у узла {k} есть {v} соседей")

# 2) defaultdict

from collections import defaultdict

cnt = defaultdict(int)
maxvalue = 0

for e in g:
    for v in e:
        cnt[v] += 1
        maxvalue = max(cnt[v], maxvalue)

#print("счётчики соседей:")
#print(cnt)

print("максимум соседей:")
for k, v in cnt.items():
    if v == maxvalue:
        print(f"у узла {k} есть {v} соседей")
