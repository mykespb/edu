#!/usr/bin/env python

# Mikhail (myke) Kolodin, 2022
# 2022-03-13 2024-10-30 2.3
# piplold-same.py

# ~ Дан текст,
# ~ в котором построчно написаны
# ~ год рождения человека,
# ~ год его смерти,
# ~ ФИО человека;
# ~ всё это - через пробелы.
# ~ Распечатать список вида
# ~ возраст - человек,
# ~ причём возраст - это продолжительность жизни,
# ~ и упорядочить строки надо по возрастанию возраста.
# ~ Найти год(ы), в котором жили макс. число упомянутых людей, и кто именно тогда жил.

homoj = """
1682 1725 Пётр I Алексеевич
1766 1826 Николай Карамзин
1799 1837 Александр Пушкин
1814 1841 Михаил Лермонтов
1694 1778 Вольтер
1769 1844 Иван Крылов
1745 1792 Денис Фонвизин
1622 1673 Мольер
1809 1852 Николай Гоголь
1784 1845 Иван Тургенев
1812 1895 Жорж Дантес
1893 1930 Владимир Маяковский
1880 1960 Борис Пастернак
1889 1966 Анна Ахматова
1931 1988 Андрей Ершов
1886 1921 Николай Гумилёв
1912 1992 Лев Гумилёв
1891 1938 Осип Мандельштам
1886 1934 Сергей Киров (Костриков)
1878 1953 Иосиф Сталин (Джугашвили)
1933 2010 Андрей Вознесенский
1865 1936 Редьярд Киплинг
1911 1973 Алексей Ляпунов
1903 1987 Андрей Колмогоров
1915 1983 Игорь Полетаев
1906 1999 Дмитрий Лихачёв
1673 1729 Александр Меншиков
1919 2017 Даниил Гранин
1867 1951 Карл Густав Эмиль Маннергейм
1900 1981 Николай Тимофеев-Ресовский
0 33 Иисус Христос
1892 1973 Джон Рональд Руэл Толкин
"""

from pprint import pp

pipl = []
for homo in homoj.strip().split("\n"):
    if not homo: continue
    born, died, name = homo.split(maxsplit=2)
    pipl.append((int(born), int(died), name))

pipl.sort()

pp(pipl)

ymin, ymax = pipl[0][0], pipl[-1][1]

yd = [ [ y, 
    ( rec := [ p for p in pipl
        if p[0] <= y <= p[1]
    ] ),
    len(rec) ]
    for y in range(ymin, ymax+1) ] 

yd.sort(key=lambda x: x[2])

yd_max = yd[-1][2]
print("макс. число живших одновременно:", yd_max)

yd_best = filter(lambda x: x[2] == yd_max, yd)
pp(list(yd_best))

# ~ макс. число живших одновременно: 17

# ~ [[1919,
  # ~ [(1865, 1936, 'Редьярд Киплинг'),
   # ~ (1867, 1951, 'Карл Густав Эмиль Маннергейм'),
   # ~ (1878, 1953, 'Иосиф Сталин (Джугашвили)'),
   # ~ (1880, 1960, 'Борис Пастернак'),
   # ~ (1886, 1921, 'Николай Гумилёв'),
   # ~ (1886, 1934, 'Сергей Киров (Костриков)'),
   # ~ (1889, 1966, 'Анна Ахматова'),
   # ~ (1891, 1938, 'Осип Мандельштам'),
   # ~ (1892, 1973, 'Джон Рональд Руэл Толкин'),
   # ~ (1893, 1930, 'Владимир Маяковский'),
   # ~ (1900, 1981, 'Николай Тимофеев-Ресовский'),
   # ~ (1903, 1987, 'Андрей Колмогоров'),
   # ~ (1906, 1999, 'Дмитрий Лихачёв'),
   # ~ (1911, 1973, 'Алексей Ляпунов'),
   # ~ (1912, 1992, 'Лев Гумилёв'),
   # ~ (1915, 1983, 'Игорь Полетаев'),
   # ~ (1919, 2017, 'Даниил Гранин')],
  # ~ 17],
 # ~ [1920,
  # ~ [(1865, 1936, 'Редьярд Киплинг'),
   # ~ (1867, 1951, 'Карл Густав Эмиль Маннергейм'),
   # ~ (1878, 1953, 'Иосиф Сталин (Джугашвили)'),
   # ~ (1880, 1960, 'Борис Пастернак'),
   # ~ (1886, 1921, 'Николай Гумилёв'),
   # ~ (1886, 1934, 'Сергей Киров (Костриков)'),
   # ~ (1889, 1966, 'Анна Ахматова'),
   # ~ (1891, 1938, 'Осип Мандельштам'),
   # ~ (1892, 1973, 'Джон Рональд Руэл Толкин'),
   # ~ (1893, 1930, 'Владимир Маяковский'),
   # ~ (1900, 1981, 'Николай Тимофеев-Ресовский'),
   # ~ (1903, 1987, 'Андрей Колмогоров'),
   # ~ (1906, 1999, 'Дмитрий Лихачёв'),
   # ~ (1911, 1973, 'Алексей Ляпунов'),
   # ~ (1912, 1992, 'Лев Гумилёв'),
   # ~ (1915, 1983, 'Игорь Полетаев'),
   # ~ (1919, 2017, 'Даниил Гранин')],
  # ~ 17],
 # ~ [1921,
  # ~ [(1865, 1936, 'Редьярд Киплинг'),
   # ~ (1867, 1951, 'Карл Густав Эмиль Маннергейм'),
   # ~ (1878, 1953, 'Иосиф Сталин (Джугашвили)'),
   # ~ (1880, 1960, 'Борис Пастернак'),
   # ~ (1886, 1921, 'Николай Гумилёв'),
   # ~ (1886, 1934, 'Сергей Киров (Костриков)'),
   # ~ (1889, 1966, 'Анна Ахматова'),
   # ~ (1891, 1938, 'Осип Мандельштам'),
   # ~ (1892, 1973, 'Джон Рональд Руэл Толкин'),
   # ~ (1893, 1930, 'Владимир Маяковский'),
   # ~ (1900, 1981, 'Николай Тимофеев-Ресовский'),
   # ~ (1903, 1987, 'Андрей Колмогоров'),
   # ~ (1906, 1999, 'Дмитрий Лихачёв'),
   # ~ (1911, 1973, 'Алексей Ляпунов'),
   # ~ (1912, 1992, 'Лев Гумилёв'),
   # ~ (1915, 1983, 'Игорь Полетаев'),
   # ~ (1919, 2017, 'Даниил Гранин')],
  # ~ 17],
 # ~ [1933,
  # ~ [(1865, 1936, 'Редьярд Киплинг'),
   # ~ (1867, 1951, 'Карл Густав Эмиль Маннергейм'),
   # ~ (1878, 1953, 'Иосиф Сталин (Джугашвили)'),
   # ~ (1880, 1960, 'Борис Пастернак'),
   # ~ (1886, 1934, 'Сергей Киров (Костриков)'),
   # ~ (1889, 1966, 'Анна Ахматова'),
   # ~ (1891, 1938, 'Осип Мандельштам'),
   # ~ (1892, 1973, 'Джон Рональд Руэл Толкин'),
   # ~ (1900, 1981, 'Николай Тимофеев-Ресовский'),
   # ~ (1903, 1987, 'Андрей Колмогоров'),
   # ~ (1906, 1999, 'Дмитрий Лихачёв'),
   # ~ (1911, 1973, 'Алексей Ляпунов'),
   # ~ (1912, 1992, 'Лев Гумилёв'),
   # ~ (1915, 1983, 'Игорь Полетаев'),
   # ~ (1919, 2017, 'Даниил Гранин'),
   # ~ (1931, 1988, 'Андрей Ершов'),
   # ~ (1933, 2010, 'Андрей Вознесенский')],
  # ~ 17],
 # ~ [1934,
  # ~ [(1865, 1936, 'Редьярд Киплинг'),
   # ~ (1867, 1951, 'Карл Густав Эмиль Маннергейм'),
   # ~ (1878, 1953, 'Иосиф Сталин (Джугашвили)'),
   # ~ (1880, 1960, 'Борис Пастернак'),
   # ~ (1886, 1934, 'Сергей Киров (Костриков)'),
   # ~ (1889, 1966, 'Анна Ахматова'),
   # ~ (1891, 1938, 'Осип Мандельштам'),
   # ~ (1892, 1973, 'Джон Рональд Руэл Толкин'),
   # ~ (1900, 1981, 'Николай Тимофеев-Ресовский'),
   # ~ (1903, 1987, 'Андрей Колмогоров'),
   # ~ (1906, 1999, 'Дмитрий Лихачёв'),
   # ~ (1911, 1973, 'Алексей Ляпунов'),
   # ~ (1912, 1992, 'Лев Гумилёв'),
   # ~ (1915, 1983, 'Игорь Полетаев'),
   # ~ (1919, 2017, 'Даниил Гранин'),
   # ~ (1931, 1988, 'Андрей Ершов'),
   # ~ (1933, 2010, 'Андрей Вознесенский')],
  # ~ 17]]
