#!/usr/bin/env python

# Mikhail (myke) Kolodin, 2026
# 2026-04-28 2026-04-28 1.0
# ortodroma-commi.py

# ~ Найти кратчайший путь между указанными городами,
# ~ по земным координатам и формуле ортодромы.


from pprint import pprint
from math import pi, sin, cos, asin, sqrt
from itertools import permutations

# -------------------------------

def sign(a):
    return -1 if a<0. else 1 if a>0. else 0.
    

def dms2d(d=0., m=0., s=0.):
    return sign(d) * (abs(d) + m/60 + s/3600)


def deg2rad(a):
    return a * pi / 180

# -------------------------------

points = [
    # ~ city, latitude, langitude
    ('spb',   deg2rad(dms2d(59, 57)),      deg2rad(dms2d(30, 15)) ),
    ('msk',   deg2rad(dms2d(55, 45, 2)),   deg2rad(dms2d(37, 37, 3)) ),
    ('nsk',   deg2rad(dms2d(55, 1)),       deg2rad(dms2d(82,55)) ),
    ('che',   deg2rad(dms2d(55, 9)),       deg2rad(dms2d(61, 24)) ),
    ('paris', deg2rad(48.858),             deg2rad(2.294) ),
    ]

dpoints = {}
for c in points:
    dpoints[c[0]] = (c[1], c[2])

pprint(points)
pprint(dpoints)

# -------------------------------

def orto(p1, p2):
    if p1[0] == p2[0]:
        return 0.

    dlat = p2[1] - p1[1]
    dlon = p2[2] - p1[2]
    R = 6371.

    a = sin(dlat / 2)**2 + cos(p1[1]) * cos(p2[1]) * sin(dlon /2)**2
    d = 2 * R * asin(sqrt(a))

    return d

# -------------------------------

print('\nspb - msk:', orto( points[0], points[1] ))

# -------------------------------

print('\nfrom - to   ', end="")
for c1 in points:
    print(f"{c1[0]:>12}", end="")
print()

dists = {}

for c1 in points:
    print(f"{c1[0]:>12}", end="")
    for c2 in points:
        o12 = orto(c1, c2)
        if c1 != c2:
            dists[(c1[0], c2[0])] = o12
            dists[(c2[0], c1[0])] = o12
        print(f"{o12:12.2f}", end="")
    print()
    
pprint(dists)

print()

# -------------------------------

cn = [ x[0] for x in points ]
print("cities:", cn)

print("\nBest way for:", end=" ")
print(*cn, sep=", ")

best_way = ()
best_dist = 1e24

for perm in permutations(cn, len(cn)):
    dist = 0.
    for n in range(len(perm)-1):
        cfrom = perm[n]
        cto   = perm[n+1]
        step  = dists[(cfrom, cto)]
        dist  += step
        if step > best_dist:
            break
    if dist < best_dist:
        best_dist = dist
        best_way = perm

print("%10.2f" % best_dist, ":", end=" ")
print(*best_way, sep=" - ")

print('\n')

# -------------------------------

# ~ [('spb', 1.0463248865706007, 0.5279620987282847),
 # ~ ('msk', 0.9730307542604609, 0.6565492313689668),
 # ~ ('nsk', 0.9602219768055469, 1.447168838111965),
 # ~ ('che', 0.9625490824748727, 1.0716321607245183),
 # ~ ('paris', 0.8527329659393895, 0.04003785304074992)]
# ~ {'che': (0.9625490824748727, 1.0716321607245183),
 # ~ 'msk': (0.9730307542604609, 0.6565492313689668),
 # ~ 'nsk': (0.9602219768055469, 1.447168838111965),
 # ~ 'paris': (0.8527329659393895, 0.04003785304074992),
 # ~ 'spb': (1.0463248865706007, 0.5279620987282847)}

# ~ spb - msk: 638.1009681529763

# ~ from - to            spb         msk         nsk         che       paris
         # ~ spb        0.00      638.10     3108.58     1913.49     2163.86
         # ~ msk      638.10        0.00     2811.26     1493.86     2489.79
         # ~ nsk     3108.58     2811.26        0.00     1364.10     5256.78
         # ~ che     1913.49     1493.86     1364.10        0.00     3980.89
       # ~ paris     2163.86     2489.79     5256.78     3980.89        0.00
# ~ {('che', 'msk'): 1493.8578586299343,
 # ~ ('che', 'nsk'): 1364.1041222243614,
 # ~ ('che', 'paris'): 3980.8883434255167,
 # ~ ('che', 'spb'): 1913.4850198855281,
 # ~ ('msk', 'che'): 1493.8578586299343,
 # ~ ('msk', 'nsk'): 2811.2593617010393,
 # ~ ('msk', 'paris'): 2489.7858747725645,
 # ~ ('msk', 'spb'): 638.1009681529763,
 # ~ ('nsk', 'che'): 1364.1041222243614,
 # ~ ('nsk', 'msk'): 2811.2593617010393,
 # ~ ('nsk', 'paris'): 5256.7817810834995,
 # ~ ('nsk', 'spb'): 3108.581786230263,
 # ~ ('paris', 'che'): 3980.8883434255167,
 # ~ ('paris', 'msk'): 2489.7858747725645,
 # ~ ('paris', 'nsk'): 5256.7817810834995,
 # ~ ('paris', 'spb'): 2163.8581750914564,
 # ~ ('spb', 'che'): 1913.4850198855281,
 # ~ ('spb', 'msk'): 638.1009681529763,
 # ~ ('spb', 'nsk'): 3108.581786230263,
 # ~ ('spb', 'paris'): 2163.8581750914564}

# ~ cities: ['spb', 'msk', 'nsk', 'che', 'paris']

# ~ Best way for: spb, msk, nsk, che, paris
   # ~ 5659.92 : nsk - che - msk - spb - paris
