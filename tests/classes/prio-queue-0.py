#!/usr/bin/env python
# Miklhail (myke) Kolodin
# classes / prio-queue-0.py
# 2026-04-15 2026-04-15 2.2
# Очередь с приоритетами
# По умолчанию приоритет равен 0.

# ~ ===================================================
# ~ Rules:

# ~ q = PQ()

# ~ q.push(what, prio)
# ~ e = q.pop()
# ~ print(e)

# ~ ===================================================

from collections import defaultdict

class PQ:
    def __init__(self):
        self.data = defaultdict(list)
        self.cnt = 0

    def push(self, elem, prio=0):
        self.data[prio].append(elem)
        self.cnt += 1

    def pop(self):
        if self.cnt:
            mp = max(self.data)
            out = self.data[mp].pop(0)
            self.cnt -= 1
            if not self.data[mp]:
                del self.data[mp]
            return out
        raise IndexError

    def __len__(self):
        return self.cnt

    def __str__(self):
        out = f"<PrioQueue (len={self.cnt}): "
        keys = sorted(self.data.keys(), reverse=True)
        for key in keys:
            out += f"({key}: "
            for val in self.data[key]:
                out += f"{val}, "
            out += "), "
        out += "> "
        return out

    def __repr__(self):
        return f"<PQ({self.cnt}): {self.data}>"

# ~ ===================================================

q = PQ()
print(q)
print("q len => ", q.cnt)
print("general len =>", len(q))

q.push('summer', 1)
print(q)

q.push('season')
print(q)

q.push('spring', 1)
print(q)

e = q.pop()
print("out =>", e)
print(q)

q.push('autumn', 2)
print(q)

q.push('winter', 3)
print(q)

e = q.pop()
print("out =>", e)
print(q)
print("q len => ", q.cnt)
print("general len =>", len(q))

q.push("noon", 5)
print(q)
print(repr(q))

q.push("midnight", 5)
print(q)
print(repr(q))

e = q.pop()
print("out =>", e)
print(q)
print("q len => ", q.cnt)
print("general len =>", len(q))

e = q.pop()
print("out =>", e)
print(q)

e = q.pop()
print("out =>", e)
print(q)

e = q.pop()
print("out =>", e)
print(q)

e = q.pop()
print("out =>", e)
print(q)

# ~ e = q.pop()
# ~ print("out =>", e)
# ~ print(q)

# ~ ===================================================
