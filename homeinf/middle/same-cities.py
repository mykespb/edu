#!/usr/bin/env python
# Mikhail (myke) Kolodin, 2024
# 2025-01-08 2025-01-08 1.0

# ~ Найти города, которые есть в более чем одной стране
# ~ (напечатать города и их страны, группами).

cities = """
Russia Moscow St.Petersburg Paris Rim Varna Irkutsk Saratov
USA Moscow St.Petersburg Washington Vancouver New-York
Canada Dover London Woodstock Boston Vancouver Toronto
UK Dover London Woodstock Boston Odessa Hull
Ukraine Odessa Kiiv Mariupol Lugansk Herson Dnepr
France Paris Bresta Lyon Dijon
Italy Rim Bari Napoli
Bulgaria Varna Plovdiv
Turkey Ankara
Czechia Praha Ostrava Brno
"""


from collections import defaultdict
from pprint import pprint

def commons():
    """find & print"""

    coms = defaultdict(list)

    for line in cities.strip().split("\n"):
        country, *towns = line.split()
        for town in towns:
            coms[town].append(country)

    # ~ pprint(coms)

    towns = sorted(coms.keys())

    # ~ print("\n-------------\nитого:\n")

    for tone in towns:
        # ~ print(tone)
        if len(coms[tone]) > 1:
            print(f"city: {tone}, countries: ", end="")
            for ctry in coms[tone]:
                print(ctry, end=", ")
            print()


commons()


# ~ city: Boston, countries: Canada, UK, 
# ~ city: Dover, countries: Canada, UK, 
# ~ city: London, countries: Canada, UK, 
# ~ city: Moscow, countries: Russia, USA, 
# ~ city: Odessa, countries: UK, Ukraine, 
# ~ city: Paris, countries: Russia, France, 
# ~ city: Rim, countries: Russia, Italy, 
# ~ city: St.Petersburg, countries: Russia, USA, 
# ~ city: Vancouver, countries: USA, Canada, 
# ~ city: Varna, countries: Russia, Bulgaria, 
# ~ city: Woodstock, countries: Canada, UK, 



# Потом: Найти страны, названия которых совпадают или близки к названию их столиц.
