#!/usr/bin/env python

# Mikhail (myke) Kolodin, 2026
# 2026-05-05 2026-05-05 1.0
# det.py

# ~ Нахождение определителя матрицы 1x1, 2х2 или 3х3.
# ~ https://ru.wikipedia.org/wiki/%D0%9E%D0%BF%D1%80%D0%B5%D0%B4%D0%B5%D0%BB%D0%B8%D1%82%D0%B5%D0%BB%D1%8C


def det1(m):
    """det matrix x1"""

    return m[0][0]


def det2(m):
    """det matrix x2"""

    return m[0][0] * m[1][1] - m[0][1] * m [1][0]


def det3(m):
    """det matrix x3"""

    return (m[0][0] * m[1][1] * m[2][2]
        - m[0][0] * m[1][2] * m[2][1]
        - m[0][1] * m[1][0] * m[2][2]
        + m[0][1] * m[1][2] * m[2][0]
        + m[0][2] * m[1][0] * m[2][1]
        - m[0][2] * m[1][1] * m[2][0]
        )


print ("matrix 1x1")

m1 = [[1],[1]]
dm1 = det1(m1)
print(m1)
print(dm1)

print ("matrix 2x2")

m2 = ((1, 2), (2, 1))
dm2 = det2(m2)
print(m2)
print(dm2)

print ("matrix 3x3")

m3 = ((1, 2, 3), (2, 3, 4), (3, 4, 5))
dm3 = det3(m3)
print(m3)
print(dm3)

m3 = ((1, 2, 3), (1.1, 1.2, 1.5), (2.2, 2.3, 2.5))
dm3 = det3(m3)
print(m3)
print(dm3)


# ~ matrix 1x1
# ~ [[1], [1]]
# ~ 1
# ~ matrix 2x2
# ~ ((1, 2), (2, 1))
# ~ -3
# ~ matrix 3x3
# ~ ((1, 2, 3), (2, 3, 4), (3, 4, 5))
# ~ 0
# ~ ((1, 2, 3), (1.1, 1.2, 1.5), (2.2, 2.3, 2.5))
# ~ 0.32000000000000206
