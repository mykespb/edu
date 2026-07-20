#!/usr/bin/env python

# Mikhail (myke) Kolodin, 2025
# finnish-doubles-simple.py
# 2025-02-12 2025-02-14 2.4

# ~ Города Финляндии с двойными буквами
# ~ -----------------------------------------------

# ~ Дан список городов,
# ~ распечатать имена тех, у которых есть хотя бы одна пара двойных букв
# ~ (подряд идущих одинаковых).
# ~ Посчитать, сколько получилось.

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

def main():
    """run it all"""

    print("\nCities with double characters in names:\n")
    cities = data.strip().split()

    num = 0
    for city in cities:
        for i in range(len(city)-1):
            if city[i] == city[i+1]:
                print(city, end=", ")
                num += 1
                break

    print("\n\nThere are", num, "such cities.\n")


main()

# ---------------------------------------------------
# results

# ~ Cities with double characters in names:

# ~ Akaa, Espoo, Forssa, Haapavesi, Haapajärvi, Hyvinkää, Hämeenlinna, Huittinen, Ikaalinen, Joensuu, Järvenpää, Kaarina, Kankaanpää, Kannus, Karkkila, Kajaani, Keuruu, Kitee, Kokkola, Kristiinankaupunki, Kurikka, Kuusamo, Lappeenranta, Loviisa, Loimaa, Maarianhamina, Mikkeli, Mänttä-Vilppula, Naantali, Orimattila, Pietarsaari, Porvoo, Raahe, Raasepori, Riihimäki, Saarijärvi, Savonlinna, Uusikaarlepyy, Vaasa, Vantaa, Viitasaari, Virrat, 

# ~ There are 42 such cities.

# ---------------------------------------------------
# the end.
