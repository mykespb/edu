#!/usr/bin/env python
# Miklhail (myke) Kolodin
# classes / prio-queue-own.py
# 2026-04-15 2026-04-15 3.3
# Очередь с приоритетами
# ~ Приоритет берётся
# ~ а) если явно указан,
# ~ б) из свойств добавляемого объекта,
# ~ в) если и такового нет, то 0.

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

    def push(self, elem, prio = None):
        if prio is not None:
            _prio = prio
        elif 'prio' in dir(elem):
            _prio = elem.prio
        else:
            _prio = 0
        self.data[_prio].append(elem)
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
# ~ print("q len => ", q.cnt)
# ~ print("general len =>", len(q))

# ~ ===================================================

class Common:
    def __str__(self):
        if 'prio' in dir(self):
            return f"{self.name} ({self.prio})"
        else:
            return f"{self.name}"

class Car(Common):
    def __init__(self, name="Car", prio=0):
        self.name = name
        self.prio = prio

class Animal(Common):
    def __init__(self, name="Animal", prio=0):
        self.name = name
        self.prio = prio

class Other(Common):
    def __init__(self, name="Other"):
        self.name = name
    
# ~ ===================================================

print("\n---------- The cars are: ----------\n")

ambulance = Car("Ambulance", 9)
fire_command = Car("Fire Command", 7)
boss_tachka = Car("Super Boss", 5)
my_car = Car("My Small Car", 3)
lorry = Car("Lorry", 1)

print(ambulance)
print(fire_command)
print(boss_tachka)
print(my_car)
print(lorry)

q.push(ambulance)
print(q)
q.push(lorry)
print(q)
q.push(boss_tachka)
print(q)
q.push(my_car)
print(q)
q.push(fire_command)
print(q)
q.push(lorry)
print(q)
q.push(lorry)
print(q)
q.push(lorry, 6)
print(q)
print(repr(q))

print("\n----------Let them drive: ----------\n")
while q:
    print(q.pop())

# ~ ===================================================

print("\n---------- The others are: ----------\n")

other1 = Other()
other2 = Other()
print(other1)
print(other2)

# ~ ===================================================

print("\n---------- The animals are: ----------\n")

grizzley = Animal("Grizzley", 4)
brown_bear = Animal("Brown Bear", 4)
wolf = Animal("Grey Wolf", 3)
pesec = Animal("Arctic Fox", 3)
fox = Animal("Fox", 2)
hare_white = Animal("Hare of White", 1)
hare_grey = Animal("Hare of Grey", 1)

q.push(grizzley)
print(q)
q.push(brown_bear)
print(q)
q.push(brown_bear)
print(q)
q.push(wolf)
print(q)
q.push(fox)
print(q)
q.push(hare_grey)
print(q)
q.push(hare_white)
print(q)
q.push(pesec)
print(q)

# add others :)
q.push(other1)
print(q)
q.push(other2)
print(q)

print("\n---------- Let them run: ----------\n")
while q:
    print(q.pop())

# ~ ===================================================

print("\n---------- The End. ----------\n")
