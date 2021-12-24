#!/usr/bin/env python3.10
# Mikhail (myke) Kolodin, 2021
# 2021-11-13 2021-11-13 0.3
# o-ecodev.py

# изучение изменения экологической ситуации в моногороде.
# есть моногород (город с 1 заводом = градообразующим предприятием).
# завод дымит прямо пропорционально своей работе.
# если дыма в городе 0.75+, то из него уезжает 10% людей.
# если дыма в городе 0.25-, то в него призжает 10% людей.
# если людей менее нормы, то завод сокращается пропорционально нехватке людей.
# завод не работает более чем на 100% мощности.
# население не превышает 100% от нормы (ибо жить негде: всё жильё служебное).
# экоситуация обратна задымлённости.
# проанализировать развитие города в течение LET (напр., 15) лет.

a_popul = 1.    # population
a_smoke = 1.    # smoke from chimneys
a_eco   = 1.    # ecosituation

YEARS   = 15      # years for simulation
EPS     = 1e-3    # precision

# ~ DEBUG   = 0       # we need no details
DEBUG   = 1       # we need details

b_popul, b_smoke, b_eco = a_popul, a_smoke, a_eco

for year in range(YEARS):

    if a_smoke >= 0.75:
        b_popul *= 0.90
        if DEBUG:
            print ("popul down")
    elif a_smoke <= 0.25:
        b_popul *= 1.10
        if DEBUG:
            print ("popul up")

    if a_popul < 1.:
        b_smoke *= a_popul
        if DEBUG:
            print ("correct smoke to popul")

    b_smoke = min(1., b_smoke)

    b_popul = min(1., b_popul)

    b_eco = 1. if (b_smoke < EPS) else abs(1. - b_smoke)

    print ("экоситуация = %5.2g, \tдыма %5.2g, \tнаселение %5.2g" %
        (b_eco, b_popul, b_smoke))

    a_popul, a_smoke, a_eco = b_popul, b_smoke, b_eco
