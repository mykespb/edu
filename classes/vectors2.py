#!/usr/bin/env python
# Miklhail (myke) Kolodin
# classes / vectors2.py
# 2026-04-16 2026-04-17 2.1
# работа с векторами

import math

class Vector2:
    def __init__(self, x1=0., y1=0., x2=None, y2=None):
        if y2 is not None:
            self.x = x2 - x1
            self.y = y2 - y1
        else:
            self.x = x1
            self.y = y1

    @property
    def length(self):
        return math.sqrt( self.x**2 + self.y**2 )

    @property
    def norma(self):
        return self.x, self.y

    # сравнения
    def __eq__(self, other):
        return self.norma == other.norma

    # сложение - вычитание и т.п.
    def __add__(self, other):
        return Vector2(0, 0, self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector2(0, 0, self.x - other.x, self.y - other.y)

    # печать
    def __str__(self):
        return f"Vector({self.x}, {self.y})"
        
    def __repr__(self):
        return f"<Vector({self.x}, {self.y})>"
        
v = Vector2()

print(v)
print(str(v))
print(repr(v))

v1 = Vector2(0, 0, 1, 1)
print(v1)
print(str(v1))
print(repr(v1))

v2 = Vector2(1, 1, 2, 2)
print(v2)
print(str(v2))
print(repr(v2))

v3 = Vector2(0, 0, 2, 2)
print(v3)
print(str(v3))
print(repr(v3))

v4 = Vector2(1, 1, 0, 0)
print(v4)
print(str(v4))
print(repr(v4))

print(f"длина вектора v1 равна {v1.length}")
print(f"длина вектора v2 равна {v2.length}")
print(f"длина вектора v3 равна {v3.length}")
print(f"длина вектора v4 равна {v4.length}")

print("вектора v1, v2 равны?", v1 == v2)
print("вектора v1, v3 равны?", v1 == v3)
print("вектора v2, v3 равны?", v2 == v3)
print("вектора v1, v4 равны?", v1 == v4)

va = v1 + v2
print(va)

vb = v1 + v4
print(vb)

v10 = Vector2(5, 5)
v11 = Vector2(10, 10)
v12 = Vector2(-5, -5)

print(f"{v10=}")
print(f"{v11=}")
print(f"{v12=}")

v1011 = v10 + v11
v1012 = v10 + v12
v1112 = v11 + v12

print(f"{v1011=}")
print(f"{v1012=}")
print(f"{v1112=}")


# ~ https://rszalski.github.io/magicmethods/
# ~ https://www.geeksforgeeks.org/python/dunder-magic-methods-python/

# ~ Vector(0.0, 0.0)
# ~ Vector(0.0, 0.0)
# ~ <Vector(0.0, 0.0, 0.0, 0.0)>
# ~ Vector(1, 1)
# ~ Vector(1, 1)
# ~ <Vector(0, 0, 1, 1)>
# ~ Vector(1, 1)
# ~ Vector(1, 1)
# ~ <Vector(1, 1, 2, 2)>
# ~ Vector(2, 2)
# ~ Vector(2, 2)
# ~ <Vector(0, 0, 2, 2)>
# ~ Vector(-1, -1)
# ~ Vector(-1, -1)
# ~ <Vector(1, 1, 0, 0)>
# ~ длина вектора v1 равна 1.4142135623730951
# ~ длина вектора v2 равна 1.4142135623730951
# ~ длина вектора v3 равна 2.8284271247461903
# ~ длина вектора v4 равна 1.4142135623730951
# ~ вектора v1, v2 равны? True
# ~ вектора v1, v3 равны? False
# ~ вектора v2, v3 равны? False
# ~ вектора v1, v4 равны? False
