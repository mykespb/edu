#!/usr/bin/env python
# Mikhail (myke) Kolodin, 2024
# 2025-01-11 2025-01-13 1.1
# subsquares.py

# ~ Субквадратная матрица 

# ~ Дана матрица целых чисел.
# ~ Она "субквадратная", если сумма чисел в любом подквадрате 2х2 положительна.
# ~ Проверить!


from random import random

# ------------------------------------
# создать матрицу

def create(size = 10):
    """создать матрицу,
    вернуть её же
    """

    return [ [ (random()-0.2)*10 for j in range(size) ] for i in range(size) ]


# ------------------------------------
# напечатать матрицу

def show(mat):
    """печатаем как таблицу, аккуратно, с автоокруглением
    """

    size = len(mat)

    for i in range(size):
        for j in range(size):
            print( "%10.5f" % mat[i][j] , end=" ")
        print()


# ------------------------------------
# проверить матрицу

def test(mat):
    """тестируем матрицу на субквадратность
    """

    size = len(mat)

    for i in range(size-1):
        for j in range(size-1):
            if (minus := mat[i][j] + mat[i][j+1] + mat[i+1][j] + mat[i+1][j+1]) <= 0:
                return False, minus

    return True
    

# ------------------------------------
# всё протестировать

def main():
    """всё запускаем и смотрим
    """

    mat = create()
    show(mat)

    match test(mat):
        case True:
            print("OK, матрица субквадратная")
        case False, minus:
            print(f"Не OK, матрица не субквадратная, с  минусом {minus}")
        

main()

# ------------------------------------

  # ~ -0.15688    2.60381    1.28110    1.41667    5.84171    7.40464    0.00473    0.22143    6.22292    1.51781 
   # ~ 4.34736    8.41700    6.96539   -0.49626    7.60241    5.53895    2.21591    4.42068    6.20573    6.73707 
   # ~ 3.03709    7.06135    4.41601   -0.19222    5.66123    6.69866    2.35914    8.03180    3.82571    5.48760 
   # ~ 2.11197    2.31817    2.02717    0.67241    5.16874    6.10714    4.35998    0.08018    8.40245    7.28230 
   # ~ 7.39258    3.71092    2.00426    0.71388   -1.07921    3.41524    8.61469    7.89505    5.45292   -0.60652 
   # ~ 0.25153    4.84509    4.71057   -0.47767    6.12075    1.69884    6.84240    8.04990    0.34039    5.23968 
   # ~ 2.49915    6.27721    1.85010   -0.28275   -1.12619    6.22660    0.60528    8.52123    7.17338    0.94377 
   # ~ 0.77040    7.53907   -0.18022    2.64296    0.15632    4.24378    4.09044   -0.18050   -0.83928    4.39959 
  # ~ -0.82450   -0.91790    7.19948    1.04065    8.25866   -1.04317    6.26223    7.25067    6.05686    7.67101 
   # ~ 5.69365    6.83873   -0.83955    5.35300    5.52236    6.79950    4.43996    0.47355    7.08569    3.37890 
# ~ OK, матрица субквадратная

   # ~ 4.52475    7.81864    5.36325    0.25302    0.60016    3.06756    3.11852    5.40160    1.26256    5.48254 
   # ~ 7.67224    5.89572    0.93859    2.02941    7.71886    8.41567    0.29373    3.45676   -0.79036    3.55769 
  # ~ -0.83108    8.21030    8.44868    0.68995   -0.26491    0.55819    4.87069    1.82532    8.69461    7.66925 
   # ~ 2.10857    3.09084    6.73637    2.40681   -0.74872   -0.83876    7.91576    8.57291    3.09557    7.13444 
  # ~ -0.14339    1.36693    7.97306    1.29756    4.69166    6.72106    0.51621    7.55265    7.76011    6.18444 
   # ~ 2.14014    6.71161    7.98817    7.82719    0.27163    4.84884    0.93219    7.46144    6.52281    1.59522 
   # ~ 8.45391    7.60828    6.40042    1.20292   -0.08360    4.88943    6.48584    1.31587    2.64786    2.67030 
   # ~ 1.05618   -0.06775    2.23389    2.24234    3.82384    8.09425    6.60720    6.15906   -1.05248    3.84292 
   # ~ 5.98113    1.59575    8.04066    3.20067   -0.53041    0.53333   -0.35673    6.70646    7.82968    2.19804 
   # ~ 4.69861   -0.33800    1.87498    0.12836    2.46319   -1.12007    6.23473    4.45199   -0.35497    0.55658 
# ~ Не OK, матрица не субквадратная, с  минусом -1.2941957426850226

