#!/usr/bin/env python

# Mikhail (myke) Kolodin, 2025
# finnish-doubles.py
# 2025-02-02 2025-02-02 1.4

# ~ Города Финляндии с двойными буквами
# ~ -----------------------------------------------

# ~ Дан список городов,
# ~ вывести те, укоторых есть 1 только пара двойных букв,
# ~ ровно 2 пары, ровно 3 пары...
# ~ Посчитать, сколько городов получилость в каждой группе.

# ~ Ähtäri Äänekoski
# ~ Akaa Alavus Alajärvi
# ~ Espoo
# ~ Forssa
# ~ Haapavesi Haapajärvi Hamina Hanko Harjavalta Heinola Helsinki Hyvinkää Hämeenlinna Huittinen
# ~ Iisalmi Ikaalinen Imatra
# ~ Joensuu Jyväskylä Jämsä Järvenpää
# ~ Kaarina Kalajoki Kangasala Kankaanpää Kannus Karkkila Kaskinen Kauniainen Kauhava Kauhajoki Kajaani Kemi Kemijärvi Kerava Keuruu Kitee Kiuruvesi Kokemäki Kokkola Kotka Kouvola Kristiinankaupunki Kuopio Kurikka Kuusamo Kuhmo
# ~ Laitila Lappeenranta Lapua Lahti Lieksa Loviisa Loimaa Lohja
# ~ Maarianhamina Mikkeli Mänttä-Vilppula
# ~ Naantali Närpiö Nivala Nokia Nurmes
# ~ Orivesi Orimattila Oulainen Oulu Outokumpu
# ~ Paimio Parainen Parkano Pieksämäki Pietarsaari Porvoo Pori Pudasjärvi Pyhäjärvi
# ~ Raahe Raisio Raasepori Rauma Riihimäki Rovaniemi
# ~ Saarijärvi Savonlinna Salo Sastamala Seinäjoki Somero Suonenjoki
# ~ Tampere Tornio Turku
# ~ Ulvila Uusikaarlepyy Uusikaupunki
# ~ Vaasa Valkeakoski Vantaa Varkaus Viitasaari Virrat
# ~ Ylöjärvi Ylivieska

# ~ https://ru.wikipedia.org/wiki/%D0%93%D0%BE%D1%80%D0%BE%D0%B4%D0%B0_%D0%A4%D0%B8%D0%BD%D0%BB%D1%8F%D0%BD%D0%B4%D0%B8%D0%B8

# ---------------------------------------------------
# data

data = """
Ähtäri Äänekoski
Akaa Alavus Alajärvi
Espoo
Forssa
Haapavesi Haapajärvi Hamina Hanko Harjavalta Heinola Helsinki Hyvinkää Hämeenlinna Huittinen
Iisalmi Ikaalinen Imatra
Joensuu Jyväskylä Jämsä Järvenpää
Kaarina Kalajoki Kangasala Kankaanpää Kannus Karkkila Kaskinen Kauniainen Kauhava Kauhajoki Kajaani Kemi Kemijärvi Kerava Keuruu Kitee Kiuruvesi Kokemäki Kokkola Kotka Kouvola Kristiinankaupunki Kuopio Kurikka Kuusamo Kuhmo
Laitila Lappeenranta Lapua Lahti Lieksa Loviisa Loimaa Lohja
Maarianhamina Mikkeli Mänttä-Vilppula
Naantali Närpiö Nivala Nokia Nurmes
Orivesi Orimattila Oulainen Oulu Outokumpu
Paimio Parainen Parkano Pieksämäki Pietarsaari Porvoo Pori Pudasjärvi Pyhäjärvi
Raahe Raisio Raasepori Rauma Riihimäki Rovaniemi
Saarijärvi Savonlinna Salo Sastamala Seinäjoki Somero Suonenjoki
Tampere Tornio Turku
Ulvila Uusikaarlepyy Uusikaupunki
Vaasa Valkeakoski Vantaa Varkaus Viitasaari Virrat
Ylöjärvi Ylivieska
"""

# ---------------------------------------------------
# imports

from itertools import pairwise

# ---------------------------------------------------
# program

def estim(el):
    """estimate element: give number of same sequential letters
    """

    pairs = 0
    for c1, c2 in pairwise(el):
        pairs += c1 == c2

    return pairs

# ---------------------------------------------------

def main():
    """run it all
    """

    global data

    print()
    data = data.strip().split()
    result = []
    maxlen = 0

    for datel in data:
        result.append((datel, (l := estim(datel))))
        maxlen = max(maxlen, l)

    result = list(filter(lambda x: x[1], result))
    result.sort()

    for alen in range(maxlen, 0, -1):
        many = 0
        print(f"words with {alen} pair(s) of same letters:")
        for word in result:
            if word[1] == alen:
                print(word[0], end=", ")
                many += 1
        print(f"\nFound {many} cities.\n")

# ---------------------------------------------------
# runs

main()

# ---------------------------------------------------
# results

# ~ words with 2 pair(s) of same letters:
# ~ Hämeenlinna, Kankaanpää, Lappeenranta, Mänttä-Vilppula, Uusikaarlepyy, Viitasaari, 
# ~ Found 6 cities.

# ~ words with 1 pair(s) of same letters:
# ~ Akaa, Espoo, Forssa, Haapajärvi, Haapavesi, Huittinen, Hyvinkää, Ikaalinen, Joensuu, Järvenpää, Kaarina, Kajaani, Kannus, Karkkila, Keuruu, Kitee, Kokkola, Kristiinankaupunki, Kurikka, Kuusamo, Loimaa, Loviisa, Maarianhamina, Mikkeli, Naantali, Orimattila, Pietarsaari, Porvoo, Raahe, Raasepori, Riihimäki, Saarijärvi, Savonlinna, Vaasa, Vantaa, Virrat, 
# ~ Found 36 cities.

# ---------------------------------------------------
# the end.
