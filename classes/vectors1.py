#!/usr/bin/env python
# Miklhail (myke) Kolodin
# classes / vectors1.py
# 2026-04-16 2026-04-18 1.2
# работа с векторами

import math

class Vector1:

    EPS = 1e-6
    
    def __init__(self, x1=0., y1=0., x2=0., y2=0.):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2

    @property
    def length(self):
        return math.sqrt( (self.x1 - self.x2)**2 + (self.y1 - self.y2)**2 )

    @property
    def norma(self):
        return self.x2 - self.x1, self.y2 - self.y1

    def __eq__(self, v):
        return self.norma == other.norma

        # ~ norm1, norm2 = self.norma, v.norma
        # ~ dx = abs(norm1[0] - norm2[0])
        # ~ dy = abs(norm1[1] - norm2[1])
        # ~ return dx <= Vector1.EPS and dy <= Vector1.EPS

    def __str__(self):
        x, y = self.norma
        return f"Vector({x}, {y})"
        
    def __repr__(self):
        return f"<Vector({self.x1}, {self.y1}, {self.x2}, {self.y2})>"
        
v = Vector1()

print(v)
print(str(v))
print(repr(v))

v1 = Vector1(0, 0, 1, 1)
print(v1)
print(str(v1))
print(repr(v1))

v2 = Vector1(1, 1, 2, 2)
print(v2)
print(str(v2))
print(repr(v2))

v3 = Vector1(0, 0, 2, 2)
print(v3)
print(str(v3))
print(repr(v3))

v4 = Vector1(1, 1, 0, 0)
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
