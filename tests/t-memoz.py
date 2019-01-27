#! /usr/bin/env python3
# python3, fibos, with timeit
# myke 2019-01-26 1.3

import timeit

def fibclassic (n):
    """ classic version of fibonacci """

    return 1 if n < 3 else fibclassic (n-2) + fibclassic (n-1)


def fibdynamic (n):
    """ dynamic version of fibonacci """

    res = {}

    def fib (n):
        nonlocal res
        if n < 3:
            return 1
        if n in res:
            return res [n]
        sum = fib (n-2) + fib (n-1)
        res [n] = sum
        return sum

    return fib (n)


def fibnormal (n):
    """ fibonacci as it should be"""

    if n < 3:
        return 1
    f1 = f2 = 1
    for i in range (n-1):
        f3 = f1 + f2
        f1, f2 = f2, f3

    return f3


def alltests():
    """ perform it all """
    MAX = 41

    print ("classics:\n")
    for n in range (1, MAX):
        print ("number=", n, end=", time=")
        print (timeit.timeit("fibclassic (%d)" % (n,), number=1, globals=globals()))

    print ("\ndynamic:\n")
    for n in range (1, MAX):
        print ("number=", n, end=", time=")
        print (timeit.timeit("fibdynamic (%d)" % (n,), number=1, globals=globals()))

    print ("\nnormal:\n")
    for n in range (1, MAX):
        print ("number=", n, end=", time=")
        print (timeit.timeit("fibnormal (%d)" % (n,), number=1, globals=globals()))


alltests()


# -------------------------- results --------------------------

# ~ classics:

# ~ number= 1, time=1.034990418702364e-06
# ~ number= 2, time=7.019843906164169e-07
# ~ number= 3, time=1.2899981811642647e-06
# ~ number= 4, time=1.567008439451456e-06
# ~ number= 5, time=1.9849976524710655e-06
# ~ number= 6, time=2.6659981813281775e-06
# ~ number= 7, time=3.5910052247345448e-06
# ~ number= 8, time=4.889006959274411e-06
# ~ number= 9, time=7.526017725467682e-06
# ~ number= 10, time=1.1476018698886037e-05
# ~ number= 11, time=2.6518013328313828e-05
# ~ number= 12, time=2.8813985409215093e-05
# ~ number= 13, time=4.558401997201145e-05
# ~ number= 14, time=7.27360020391643e-05
# ~ number= 15, time=0.000116731011075899
# ~ number= 16, time=0.00018816499505192041
# ~ number= 17, time=0.0003031770174857229
# ~ number= 18, time=0.0005407760036177933
# ~ number= 19, time=0.0008094219956547022
# ~ number= 20, time=0.001280739001231268
# ~ number= 21, time=0.002295913000125438
# ~ number= 22, time=0.004461036995053291
# ~ number= 23, time=0.007025163999060169
# ~ number= 24, time=0.008781154989264905
# ~ number= 25, time=0.013856413017492741
# ~ number= 26, time=0.023656976991333067
# ~ number= 27, time=0.04232543500256725
# ~ number= 28, time=0.06111709700780921
# ~ number= 29, time=0.09513099698233418
# ~ number= 30, time=0.15315496400580741
# ~ number= 31, time=0.2465798019838985
# ~ number= 32, time=0.3952583830105141
# ~ number= 33, time=0.6446352399943862
# ~ number= 34, time=1.0405004739877768
# ~ number= 35, time=1.687662000011187
# ~ number= 36, time=2.7748038659919985
# ~ number= 37, time=4.445053566014394
# ~ number= 38, time=7.191507424984593
# ~ number= 39, time=11.613657659996534
# ~ number= 40, time=18.7474125350127

# ~ dynamic:

# ~ number= 1, time=2.7460046112537384e-06
# ~ number= 2, time=4.294997779652476e-06
# ~ number= 3, time=2.8240028768777847e-06
# ~ number= 4, time=2.7859932743012905e-06
# ~ number= 5, time=3.234017640352249e-06
# ~ number= 6, time=3.5609991755336523e-06
# ~ number= 7, time=3.9130100049078465e-06
# ~ number= 8, time=4.3009931687265635e-06
# ~ number= 9, time=4.7470093704760075e-06
# ~ number= 10, time=5.225010681897402e-06
# ~ number= 11, time=5.270994734019041e-06
# ~ number= 12, time=5.762005457654595e-06
# ~ number= 13, time=6.6490028984844685e-06
# ~ number= 14, time=6.729009328410029e-06
# ~ number= 15, time=6.921996828168631e-06
# ~ number= 16, time=7.127993740141392e-06
# ~ number= 17, time=7.161987014114857e-06
# ~ number= 18, time=7.659022230654955e-06
# ~ number= 19, time=8.149974746629596e-06
# ~ number= 20, time=8.301984053105116e-06
# ~ number= 21, time=8.580012945458293e-06
# ~ number= 22, time=9.048002539202571e-06
# ~ number= 23, time=9.381008567288518e-06
# ~ number= 24, time=1.0046991519629955e-05
# ~ number= 25, time=1.0321004083380103e-05
# ~ number= 26, time=1.0611023753881454e-05
# ~ number= 27, time=1.1216994607821107e-05
# ~ number= 28, time=1.1440017260611057e-05
# ~ number= 29, time=1.1724012438207865e-05
# ~ number= 30, time=1.2028991477563977e-05
# ~ number= 31, time=1.2470991350710392e-05
# ~ number= 32, time=1.2823002180084586e-05
# ~ number= 33, time=1.3097014743834734e-05
# ~ number= 34, time=1.3532000593841076e-05
# ~ number= 35, time=1.3702985597774386e-05
# ~ number= 36, time=1.4035991625860333e-05
# ~ number= 37, time=1.4319986803457141e-05
# ~ number= 38, time=1.4817022019997239e-05
# ~ number= 39, time=1.5317986253648996e-05
# ~ number= 40, time=1.5501980669796467e-05

# ~ normal:

# ~ number= 1, time=7.420021574944258e-07
# ~ number= 2, time=5.729962140321732e-07
# ~ number= 3, time=1.9730068743228912e-06
# ~ number= 4, time=1.8200080376118422e-06
# ~ number= 5, time=1.7929996829479933e-06
# ~ number= 6, time=1.8519931472837925e-06
# ~ number= 7, time=1.7609854694455862e-06
# ~ number= 8, time=1.7790007404983044e-06
# ~ number= 9, time=1.8110149540007114e-06
# ~ number= 10, time=1.8580176401883364e-06
# ~ number= 11, time=1.962005626410246e-06
# ~ number= 12, time=1.8959981389343739e-06
# ~ number= 13, time=2.0920124370604753e-06
# ~ number= 14, time=2.1110172383487225e-06
# ~ number= 15, time=2.3260072339326143e-06
# ~ number= 16, time=2.2640160750597715e-06
# ~ number= 17, time=2.2930034901946783e-06
# ~ number= 18, time=2.263986971229315e-06
# ~ number= 19, time=2.354994649067521e-06
# ~ number= 20, time=2.4310138542205095e-06
# ~ number= 21, time=2.4730106815695763e-06
# ~ number= 22, time=2.548011252656579e-06
# ~ number= 23, time=2.450979081913829e-06
# ~ number= 24, time=2.5700137484818697e-06
# ~ number= 25, time=2.5570043362677097e-06
# ~ number= 26, time=2.649001544341445e-06
# ~ number= 27, time=2.6609923224896193e-06
# ~ number= 28, time=2.7929781936109066e-06
# ~ number= 29, time=2.8070062398910522e-06
# ~ number= 30, time=2.9200164135545492e-06
# ~ number= 31, time=2.8989743441343307e-06
# ~ number= 32, time=2.8939975891262293e-06
# ~ number= 33, time=2.9619841370731592e-06
# ~ number= 34, time=3.043009201064706e-06
# ~ number= 35, time=2.9939983505755663e-06
# ~ number= 36, time=3.1149829737842083e-06
# ~ number= 37, time=3.1479867175221443e-06
# ~ number= 38, time=3.188004484400153e-06
# ~ number= 39, time=3.276014467701316e-06
# ~ number= 40, time=3.3060205169022083e-06

