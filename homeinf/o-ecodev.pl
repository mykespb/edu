# Mikhail (myke) Kolodin, 2021
# 2021-11-13 2021-11-13 0.1
# o-ecodev.py

# изучение изменения экологической ситуации в моногороде.
# есть моногород (город с 1 заводом = градообразующим предприятием).
# завод дымит прямо пропорционально своей работе.
# если дыма в городе 0.75+, то из него уезжает 10% людей.
# если дыма в городе 0.25-, то в него призжает 10% людей.
# если людей менее 0.5 от нормы, то завод сокращается на 50% в год.
# проанализировать развитие города в течение 20 лет.

a_popul = 100.    # population
a_enter = 100.    # enterprise
a_smoke = 0.      # smoke from chimneys
a_eco   = 100.    # ecosituation

YEARS   = 20      # years fro simulation

for year in range(YEARS):

    b_popul, b_enter, b_smoke, b_eco = a_popul, a_enter, a_smoke, a_eco

    if a_smoke >= 0.75:


