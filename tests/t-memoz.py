#! /usr/bin/env python3
# python3, quicksort
# myke 2019-01-26 1.1

import timeit

def fibclassic (n):
    """ classic version of fibonacci """
    return n if n < 3 else fibclassic (n-2) + fibclassic (n-1)

def fibdynamic (n):
    """ dynamic version of fibonacci """

    res = {}

    def fib (n):
        nonlocal res
        if n < 3:
            return n
        if n in res:
            return res [n]
        sum = fib (n-2) + fib (n-1)
        res [n] = sum
        return sum

    return fib (n)

def test (n):
    """ test both algos for number n"""
    print ("\nnumber", n, end="")
    f = fibclassic (n)
    print (", classic", f, end="")
    f = fibdynamic (n)
    print (", dynamic", f, end="")

def alltests():
    MAX = 40
    print ("classics:")
    for n in range(MAX):
        print ("number=", n, end=", time=")
        print (timeit.timeit("fibclassic (%d)" % (n,), number=1, globals=globals()))
    print ("dynamic:")
    for n in range(MAX):
        print ("number=", n, end=", time=")
        print (timeit.timeit("fibdynamic (%d)" % (n,), number=1, globals=globals()))

alltests()

# ~ classics:
# ~ number= 0, time=1.4039978850632906e-06
# ~ number= 1, time=7.599883247166872e-07
# ~ number= 2, time=6.410118658095598e-07
# ~ number= 3, time=1.3430253602564335e-06
# ~ number= 4, time=1.487991539761424e-06
# ~ number= 5, time=2.075015800073743e-06
# ~ number= 6, time=2.7819769456982613e-06
# ~ number= 7, time=3.5240082070231438e-06
# ~ number= 8, time=5.073990905657411e-06
# ~ number= 9, time=7.49199534766376e-06
# ~ number= 10, time=1.1625990737229586e-05
# ~ number= 11, time=2.612799289636314e-05
# ~ number= 12, time=2.7600006433203816e-05
# ~ number= 13, time=4.545898991636932e-05
# ~ number= 14, time=7.245500455610454e-05
# ~ number= 15, time=0.0001165269932243973
# ~ number= 16, time=0.00018778600497171283
# ~ number= 17, time=0.00030267800320871174
# ~ number= 18, time=0.0004882840148638934
# ~ number= 19, time=0.0007880170014686882
# ~ number= 20, time=0.0014111459895502776
# ~ number= 21, time=0.0022988319979049265
# ~ number= 22, time=0.0034061729966197163
# ~ number= 23, time=0.0055809640034567565
# ~ number= 24, time=0.00889747601468116
# ~ number= 25, time=0.014196265023201704
# ~ number= 26, time=0.02277593599865213
# ~ number= 27, time=0.037370188016211614
# ~ number= 28, time=0.05908930901205167
# ~ number= 29, time=0.0974465150211472
# ~ number= 30, time=0.15109198598656803
# ~ number= 31, time=0.24432017200160772
# ~ number= 32, time=0.3986199719947763
# ~ number= 33, time=0.6563923089997843
# ~ number= 34, time=1.0405087569961324
# ~ number= 35, time=1.675190031004604
# ~ number= 36, time=2.7158791669935454
# ~ number= 37, time=4.414878101990325
# ~ number= 38, time=7.149948215985205
# ~ number= 39, time=11.520781046012416
# ~ dynamic:
# ~ number= 0, time=2.5240005925297737e-06
# ~ number= 1, time=1.3129902072250843e-06
# ~ number= 2, time=1.146021531894803e-06
# ~ number= 3, time=1.0858988389372826e-05
# ~ number= 4, time=2.782006049528718e-06
# ~ number= 5, time=3.1389936339110136e-06
# ~ number= 6, time=3.4660042729228735e-06
# ~ number= 7, time=3.7260178942233324e-06
# ~ number= 8, time=4.347995854914188e-06
# ~ number= 9, time=4.640023689717054e-06
# ~ number= 10, time=5.164009053260088e-06
# ~ number= 11, time=5.084002623334527e-06
# ~ number= 12, time=5.756999598816037e-06
# ~ number= 13, time=6.500020390376449e-06
# ~ number= 14, time=6.820017006248236e-06
# ~ number= 15, time=6.836024112999439e-06
# ~ number= 16, time=7.07802246324718e-06
# ~ number= 17, time=7.265975000336766e-06
# ~ number= 18, time=7.664988515898585e-06
# ~ number= 19, time=7.953989552333951e-06
# ~ number= 20, time=8.394999895244837e-06
# ~ number= 21, time=8.548988262191415e-06
# ~ number= 22, time=9.179988410323858e-06
# ~ number= 23, time=9.376992238685489e-06
# ~ number= 24, time=1.0045012459158897e-05
# ~ number= 25, time=1.0177987860515714e-05
# ~ number= 26, time=1.0736985132098198e-05
# ~ number= 27, time=1.1109019396826625e-05
# ~ number= 28, time=1.141798566095531e-05
# ~ number= 29, time=1.1704018106684089e-05
# ~ number= 30, time=1.201301347464323e-05
# ~ number= 31, time=1.2419011909514666e-05
# ~ number= 32, time=1.2980017345398664e-05
# ~ number= 33, time=1.3282988220453262e-05
# ~ number= 34, time=1.3405020581558347e-05
# ~ number= 35, time=1.3682001736015081e-05
# ~ number= 36, time=1.3957993360236287e-05
# ~ number= 37, time=1.4451012248173356e-05
# ~ number= 38, time=1.4911987818777561e-05
# ~ number= 39, time=1.5024997992441058e-05

