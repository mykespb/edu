#!/usr/bin/env python
# Mikhail Kolodin, 2023
# 2023-02-09 2023-02-09 1.2
# ya-rev1list.py

# ~ Задача из яндекса
# ~ Перевернуть 1-связный список
# ~ решение классовое

class Node:
    def __init__(self, value=None):
        self.value = value
        self.link = None

    def get(self):
        return self.value

    def put(self, value):
        self.value = value

    def __repr__(self):
        return self.value


class Osl:
    def __init__(self, value=None):
        self.head = None
        if value is not None:
            node = Node(value)
            self.head = node

    def add(self, elem=None):
        ae = Node(elem)
        ae.link = self.head
        self.head = ae

    def __repr__(self):
        node = self.head
        sout = "OSL( "
        while node:
            sout += str(node.value) + ", "
            node = node.link
        if sout.endswith(", "):
            sout = sout[:-2]
        sout += ") "
        return sout

    def reverse(self):
        obr = Osl()
        node = self.head
        while node:
            obr.add(node.value)
            node = node.link
        self.head = obr.head


# ~ сделать случайный список

def make(items = 10):
    """сделать список.
    items: число элементов, значения - подряд, для удобства проверки
    """

    print('making:', end=" ")
    lo = Osl()

    for item in range(items, 0, -1):
        print(item, end=' ')
        lo.add(item)

    print()
    return lo

# ~ протестировать

lo = Osl(1)
print(lo)
lo.add([1])
print(lo)
lx = make()
print(lx)
lx.reverse()
print(lx)

# ~ OSL( 1) 
# ~ OSL( [1], 1) 
# ~ making: 10 9 8 7 6 5 4 3 2 1 
# ~ OSL( 1, 2, 3, 4, 5, 6, 7, 8, 9, 10) 
# ~ OSL( 10, 9, 8, 7, 6, 5, 4, 3, 2, 1) 
