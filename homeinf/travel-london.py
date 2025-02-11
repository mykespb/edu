#!/usr/bin/env python

# Mikhail (myke) Kolodin, 2025
# travel-london.py
# 2025-02-11 2025-02-11 0.1

# ~ Как известно, Большой Лондон - большой.
# ~ И в нём есть много дорог и транспортов.
# ~ И они зачастую принадлежат разным компаниям.
# ~ И их сотрудники часто бастуют.
# ~ И тогда движение по бастующей линии прекращается
# ~ и связность городской транспортной ситсемы может нарушиться.

# ~ Даны данные о связности в данный момент
# ~ и откуда и куда едет пассажир.
# ~ Вопрос: сможет ли он проехать?
# ~ И как именно?

links = """
High Barnet, Highgate
Highgate, Camden Town
Camden Town, Charing Cross
Camden Town, London Bridge
London Bridge, Morden
Waterloo, Charing Cross
Waterloo, Westminster
Westminster, Victoria
Waterloo, Green Park
Green Park, Heathrow Airport
London City Airport, Bank
Bank, Holiborn
Holiborn, Heathrow Airport
Richmond, Wimbledon
Wimbledon, Cannon Street
"""

ways = (
"London City Airport, Heathrow Airport",
"Highgate, Richmond"
)
