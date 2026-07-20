#!/usr/bin/env python

# Mikhail (myke) Kolodin, 2025
# travel-london.py
# 2025-02-11 2025-02-11 1.0

# ~ Как известно, Большой Лондон - большой.
# ~ И в нём есть много дорог и транспортов.
# ~ И они зачастую принадлежат разным компаниям.
# ~ И их сотрудники часто бастуют.
# ~ И тогда движение по бастующей линии прекращается.
# ~ И связность городской транспортной системы может нарушиться.

# ~ Даны данные о связности в данный момент
# ~ и откуда и куда едет пассажир.
# ~ Вопрос: сможет ли он проехать?
# ~ Даны несколько желаемых поездок, решить задачу для каждой отдельно.

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
Cannon Street, Bayswater
Wimbledon, Kensington
Kensington, Gospel Oak
Gospel Oak, Crouch Hill
"""

travels = """
London City Airport, Heathrow Airport
Highgate, Richmond
"""

from pprint import pp, pprint

def prepare(data):
    """данные о транспорте
    """
    
    info = []

    for line in data.strip().splitlines():
        who = line.strip().split(',')
        who = list(map(str.strip, who))
        info.append(who)

    kune = []
    for line in info:
        kune.append(set(line))

    rept = True
    while rept:
        rept = False
        
        for iset in range(len(kune)-1):
            if not kune[iset]: continue
            
            for jset in range(iset+1,len(kune)):
                if not kune[jset]: continue

                if kune[iset] & kune[jset]:
                    kune[iset] |= kune[jset]
                    kune[jset] = set()
                    rept = True

    out = sorted([ sorted(x, key=str.lower) for x in kune if x ])

    # ~ for ngroup, group in enumerate(out, 1):
        # ~ print("группа", ngroup, ": ", end="")
        # ~ print(*group, sep=", ")
    # ~ print()

    return out

def all_ways(data):
    """данные о поездках
    """
    
    info = []

    for line in data.strip().splitlines():
        who = line.strip().split(',')
        who = list(map(str.strip, who))
        info.append(who)

    return info
    

def main(links, ways):
    """заказ проходимости маршрутов
    """

    print("\nработают линии:")
    linked = prepare(links)
    travs  = all_ways(travels)
    print(linked)
    print("\nнаши поездки:")
    print(travs)

    for start, finish in travs:
        print(f"\nищем путь от {start} до {finish}", end=" => ")
        for link in linked:
            if start in link and finish in link:
                print("успешно")
                break
        else:
            print("неуспешно")

    print()

main(links, travels)

# результат:
# ~ работают линии:
# ~ [['Bank', 'Camden Town', 'Charing Cross', 'Green Park', 'Heathrow Airport', 'High Barnet', 'Highgate', 'Holiborn', 'London Bridge', 'London City Airport', 'Morden', 'Victoria', 'Waterloo', 'Westminster'], ['Bayswater', 'Cannon Street', 'Crouch Hill', 'Gospel Oak', 'Kensington', 'Richmond', 'Wimbledon']]

# ~ наши поездки:
# ~ [['London City Airport', 'Heathrow Airport'], ['Highgate', 'Richmond']]

# ~ ищем путь от London City Airport до Heathrow Airport => успешно

# ~ ищем путь от Highgate до Richmond => неуспешно
