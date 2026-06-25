#!/usr/bin/env python

# Mikhail (myke) Kolodin, 2026
# usa-elect.py
# 2026-06-25 2026-06-25 2.3

# ~ Изучаем выборы Президентов США. 
# ~ Нужен список (формат: list[dict], всё по-английски) записей с полями:
# ~ - elect: год выборов,
# ~ - duty: дата вступления в должность,
# ~ - fio: ФИО избранного президента,
# ~ - number: его номер,
# ~ - party: его партия,
# ~ - vice: ФИО вице-президента,
# ~ - result: результат (ok: доработал, died: умер в должности)

# ~ Чтобы корректно добавить промежуточных президентов (которые заняли пост не в результате победы на выборах, а в порядке конституционного преемственности после смерти или отставки предшественника), структура данных немного расширена.Для промежуточных президентов в поле elect (год выборов) указано значение 0, так как выборы в этот год не проводились. Список составлен в хронологическом порядке вступления в должность.
# ~ Возраст (age) рассчитан на момент официального вступления президента в должность (даты инаугурации) [STEM].

# ------------------------ data -----------------------------

usa = [
    {
    "elect": 1788,
    "duty": "1789-04-30",
    "fio": "George Washington",
    "number": 1,
    "party": "Independent",
    "vice": "John Adams",
    "age": 57,
    "result": "ok"
    },
    {
    "elect": 1792,
    "duty": "1793-03-04",
    "fio": "George Washington",
    "number": 1,
    "party": "Independent",
    "vice": "John Adams",
    "age": 61,
    "result": "ok"
    },
    {
    "elect": 1796,
    "duty": "1797-03-04",
    "fio": "John Adams",
    "number": 2,
    "party": "Federalist",
    "vice": "Thomas Jefferson",
    "age": 61,
    "result": "ok"
    },
    {
    "elect": 1800,
    "duty": "1801-03-04",
    "fio": "Thomas Jefferson",
    "number": 3,
    "party": "Democratic-Republican",
    "vice": "Aaron Burr",
    "age": 57,
    "result": "ok"
    },
    {
    "elect": 1804,
    "duty": "1805-03-04",
    "fio": "Thomas Jefferson",
    "number": 3,
    "party": "Democratic-Republican",
    "vice": "George Clinton",
    "age": 61,
    "result": "ok"
    },
    {
    "elect": 1808,
    "duty": "1809-03-04",
    "fio": "James Madison",
    "number": 4,
    "party": "Democratic-Republican",
    "vice": "George Clinton",
    "age": 57,
    "result": "ok"
    },
    {
    "elect": 1812,
    "duty": "1813-03-04",
    "fio": "James Madison",
    "number": 4,
    "party": "Democratic-Republican",
    "vice": "Elbridge Gerry",
    "age": 61,
    "result": "ok"
    },
    {
    "elect": 1816,
    "duty": "1817-03-04",
    "fio": "James Monroe",
    "number": 5,
    "party": "Democratic-Republican",
    "vice": "Daniel D. Tompkins",
    "age": 58,
    "result": "ok"
    },
    {
    "elect": 1820,
    "duty": "1821-03-05",
    "fio": "James Monroe",
    "number": 5,
    "party": "Democratic-Republican",
    "vice": "Daniel D. Tompkins",
    "age": 62,
    "result": "ok"
    },
    {
    "elect": 1824,
    "duty": "1825-03-04",
    "fio": "John Quincy Adams",
    "number": 6,
    "party": "Democratic-Republican",
    "vice": "John C. Calhoun",
    "age": 57,
    "result": "ok"
    },
    {
    "elect": 1828,
    "duty": "1829-03-04",
    "fio": "Andrew Jackson",
    "number": 7,
    "party": "Democratic",
    "vice": "John C. Calhoun",
    "age": 61,
    "result": "ok"
    },
    {
    "elect": 1832,
    "duty": "1833-03-04",
    "fio": "Andrew Jackson",
    "number": 7,
    "party": "Democratic",
    "vice": "Martin Van Buren",
    "age": 65,
    "result": "ok"
    },
    {
    "elect": 1836,
    "duty": "1837-03-04",
    "fio": "Martin Van Buren",
    "number": 8,
    "party": "Democratic",
    "vice": "Richard Mentor Johnson",
    "age": 54,
    "result": "ok"
    },
    {
    "elect": 1840,
    "duty": "1841-03-04",
    "fio": "William Henry Harrison",
    "number": 9,
    "party": "Whig",
    "vice": "John Tyler",
    "age": 68,
    "result": "died"
    },
    {
    "elect": 0,
    "duty": "1841-04-04",
    "fio": "John Tyler",
    "number": 10,
    "party": "Whig / Independent",
    "vice": "None",
    "age": 51,
    "result": "ok"
    },
    {
    "elect": 1844,
    "duty": "1845-03-04",
    "fio": "James K. Polk",
    "number": 11,
    "party": "Democratic",
    "vice": "George M. Dallas",
    "age": 49,
    "result": "ok"
    },
    {
    "elect": 1848,
    "duty": "1849-03-05",
    "fio": "Zachary Taylor",
    "number": 12,
    "party": "Whig",
    "vice": "Millard Fillmore",
    "age": 64,
    "result": "died"
    },
    {
    "elect": 0,
    "duty": "1850-07-09",
    "fio": "Millard Fillmore",
    "number": 13,
    "party": "Whig",
    "vice": "None",
    "age": 50,
    "result": "ok"
    },
    {
    "elect": 1852,
    "duty": "1853-03-04",
    "fio": "Franklin Pierce",
    "number": 14,
    "party": "Democratic",
    "vice": "William R. King",
    "age": 48,
    "result": "ok"
    },
    {
    "elect": 1856,
    "duty": "1857-03-04",
    "fio": "James Buchanan",
    "number": 15,
    "party": "Democratic",
    "vice": "John C. Breckinridge",
    "age": 65,
    "result": "ok"
    },
    {
    "elect": 1860,
    "duty": "1861-03-04",
    "fio": "Abraham Lincoln",
    "number": 16,
    "party": "Republican",
    "vice": "Hannibal Hamlin",
    "age": 52,
    "result": "ok"
    },
    {
    "elect": 1864,
    "duty": "1865-03-04",
    "fio": "Abraham Lincoln",
    "number": 16,
    "party": "National Union",
    "vice": "Andrew Johnson",
    "age": 56,
    "result": "died"
    },
    {
    "elect": 0,
    "duty": "1865-04-15",
    "fio": "Andrew Johnson",
    "number": 17,
    "party": "Democratic / National Union",
    "vice": "None",
    "age": 56,
    "result": "ok"
    },
    {
    "elect": 1868,
    "duty": "1869-03-04",
    "fio": "Ulysses S. Grant",
    "number": 18,
    "party": "Republican",
    "vice": "Schuyler Colfax",
    "age": 46,
    "result": "ok"
    },
    {
    "elect": 1872,
    "duty": "1873-03-04",
    "fio": "Ulysses S. Grant",
    "number": 18,
    "party": "Republican",
    "vice": "Henry Wilson",
    "age": 50,
    "result": "ok"
    },
    {
    "elect": 1876,
    "duty": "1877-03-05",
    "fio": "Rutherford B. Hayes",
    "number": 19,
    "party": "Republican",
    "vice": "William A. Wheeler",
    "age": 54,
    "result": "ok"
    },
    {
    "elect": 1880,
    "duty": "1881-03-04",
    "fio": "James A. Garfield",
    "number": 20,
    "party": "Republican",
    "vice": "Chester A. Arthur",
    "age": 49,
    "result": "died"
    },
    {
    "elect": 0,
    "duty": "1881-09-19",
    "fio": "Chester A. Arthur",
    "number": 21,
    "party": "Republican",
    "vice": "None",
    "age": 51,
    "result": "ok"
    },
    {
    "elect": 1884,
    "duty": "1885-03-04",
    "fio": "Grover Cleveland",
    "number": 22,
    "party": "Democratic",
    "vice": "Thomas A. Hendricks",
    "age": 47,
    "result": "ok"
    },
    {
    "elect": 1888,
    "duty": "1889-03-04",
    "fio": "Benjamin Harrison",
    "number": 23,
    "party": "Republican",
    "vice": "Levi P. Morton",
    "age": 55,
    "result": "ok"
    },
    {
    "elect": 1892,
    "duty": "1893-03-04",
    "fio": "Grover Cleveland",
    "number": 24,
    "party": "Democratic",
    "vice": "Adlai Stevenson I",
    "age": 55,
    "result": "ok"
    },
    {
    "elect": 1896,
    "duty": "1897-03-04",
    "fio": "William McKinley",
    "number": 25,
    "party": "Republican",
    "vice": "Garret Hobart",
    "age": 54,
    "result": "ok"
    },
    {
    "elect": 1900,
    "duty": "1901-03-04",
    "fio": "William McKinley",
    "number": 25,
    "party": "Republican",
    "vice": "Theodore Roosevelt",
    "age": 57,
    "result": "died"
    },
    {
    "elect": 0,
    "duty": "1901-09-14",
    "fio": "Theodore Roosevelt",
    "number": 26,
    "party": "Republican",
    "vice": "None",
    "age": 42,
    "result": "ok"
    },
    {
    "elect": 1904,
    "duty": "1905-03-04",
    "fio": "Theodore Roosevelt",
    "number": 26,
    "party": "Republican",
    "vice": "Charles W. Fairbanks",
    "age": 46,
    "result": "ok"
    },
    {
    "elect": 1908,
    "duty": "1909-03-04",
    "fio": "William Howard Taft",
    "number": 27,
    "party": "Republican",
    "vice": "James S. Sherman",
    "age": 51,
    "result": "ok"
    },
    {
    "elect": 1912,
    "duty": "1913-03-04",
    "fio": "Woodrow Wilson",
    "number": 28,
    "party": "Democratic",
    "vice": "Thomas R. Marshall",
    "age": 56,
    "result": "ok"
    },
    {
    "elect": 1916,
    "duty": "1917-03-05",
    "fio": "Woodrow Wilson",
    "number": 28,
    "party": "Democratic",
    "vice": "Thomas R. Marshall",
    "age": 60,
    "result": "ok"
    },
    {
    "elect": 1920,
    "duty": "1921-03-04",
    "fio": "Warren G. Harding",
    "number": 29,
    "party": "Republican",
    "vice": "Calvin Coolidge",
    "age": 55,
    "result": "died"
    },
    {
    "elect": 0,
    "duty": "1923-08-02",
    "fio": "Calvin Coolidge",
    "number": 30,
    "party": "Republican",
    "vice": "None",
    "age": 51,
    "result": "ok"
    },
    {
    "elect": 1924,
    "duty": "1925-03-04",
    "fio": "Calvin Coolidge",
    "number": 30,
    "party": "Republican",
    "vice": "Charles G. Dawes",
    "age": 52,
    "result": "ok"
    },
    {
    "elect": 1928,
    "duty": "1929-03-04",
    "fio": "Herbert Hoover",
    "number": 31,
    "party": "Republican",
    "vice": "Charles Curtis",
    "age": 54,
    "result": "ok"
    },
    {
    "elect": 1932,
    "duty": "1933-03-04",
    "fio": "Franklin D. Roosevelt",
    "number": 32,
    "party": "Democratic",
    "vice": "John Nance Garner",
    "age": 50,
    "result": "ok"
    },
    {

    "elect": 1936,
    "duty": "1937-01-20",
    "fio": "Franklin D. Roosevelt",
    "number": 32,
    "party": "Democratic",
    "vice": "John Nance Garner",
    "age": 54,
    "result": "ok"
    },
    {
    "elect": 1940,
    "duty": "1941-01-20",
    "fio": "Franklin D. Roosevelt",
    "number": 32,
    "party": "Democratic",
    "vice": "Henry A. Wallace",
    "age": 58,
    "result": "ok"
    },
    {
    "elect": 1944,
    "duty": "1945-01-20",
    "fio": "Franklin D. Roosevelt",
    "number": 32,
    "party": "Democratic",
    "vice": "Harry S. Truman",
    "age": 62,
    "result": "died"
    },
    {
    "elect": 0,
    "duty": "1945-04-12",
    "fio": "Harry S. Truman",
    "number": 33,
    "party": "Democratic",
    "vice": "None",
    "age": 60,
    "result": "ok"
    },
    {
    "elect": 1948,
    "duty": "1949-01-20",
    "fio": "Harry S. Truman",
    "number": 33,
    "party": "Democratic",
    "vice": "Alben W. Barkley",
    "age": 64,
    "result": "ok"
    },
    {
    "elect": 1952,
    "duty": "1953-01-20",
    "fio": "Dwight D. Eisenhower",
    "number": 34,
    "party": "Republican",
    "vice": "Richard Nixon",
    "age": 62,
    "result": "ok"
    },
    {
    "elect": 1956,
    "duty": "1957-01-21",
    "fio": "Dwight D. Eisenhower",
    "number": 34,
    "party": "Republican",
    "vice": "Richard Nixon",
    "age": 66,
    "result": "ok"
    },
    {
    "elect": 1960,
    "duty": "1961-01-20",
    "fio": "John F. Kennedy",
    "number": 35,
    "party": "Democratic",
    "vice": "Lyndon B. Johnson",
    "age": 43,
    "result": "died"
    },
    {
    "elect": 0,
    "duty": "1963-11-22",
    "fio": "Lyndon B. Johnson",
    "number": 36,
    "party": "Democratic",
    "vice": "None",
    "age": 55,
    "result": "ok"
    },
    {
    "elect": 1964,
    "duty": "1965-01-20",
    "fio": "Lyndon B. Johnson",
    "number": 36,
    "party": "Democratic",
    "vice": "Hubert Humphrey",
    "age": 56,
    "result": "ok"
    },
    {
    "elect": 1968,
    "duty": "1969-01-20",
    "fio": "Richard Nixon",
    "number": 37,
    "party": "Republican",
    "vice": "Spiro Agnew",
    "age": 56,
    "result": "ok"
    },
    {
    "elect": 1972,
    "duty": "1973-01-20",
    "fio": "Richard Nixon",
    "number": 37,
    "party": "Republican",
    "vice": "Spiro Agnew",
    "age": 60,
    "result": "ok"
    },
    {
    "elect": 0,
    "duty": "1974-08-09",
    "fio": "Gerald Ford",
    "number": 38,
    "party": "Republican",
    "vice": "Nelson Rockefeller",
    "age": 61,
    "result": "ok"
    },
    {
    "elect": 1976,
    "duty": "1977-01-20",
    "fio": "Jimmy Carter",
    "number": 39,
    "party": "Democratic",
    "vice": "Walter Mondale",
    "age": 52,
    "result": "ok"
    },
    {
    "elect": 1980,
    "duty": "1981-01-20",
    "fio": "Ronald Reagan",
    "number": 40,
    "party": "Republican",
    "vice": "George H. W. Bush",
    "age": 69,
    "result": "ok"
    },
    {
    "elect": 1984,
    "duty": "1985-01-20",
    "fio": "Ronald Reagan",
    "number": 40,
    "party": "Republican",
    "vice": "George H. W. Bush",
    "age": 73,
    "result": "ok"
    },
    {
    "elect": 1988,
    "duty": "1989-01-20",
    "fio": "George H. W. Bush",
    "number": 41,
    "party": "Republican",
    "vice": "Dan Quayle",
    "age": 64,
    "result": "ok"
    },
    {
    "elect": 1992,
    "duty": "1993-01-20",
    "fio": "Bill Clinton",
    "number": 42,
    "party": "Democratic",
    "vice": "Al Gore",
    "age": 46,
    "result": "ok"
    },
    {
    "elect": 1996,
    "duty": "1997-01-20",
    "fio": "Bill Clinton",
    "number": 42,
    "party": "Democratic",
    "vice": "Al Gore",
    "age": 50,
    "result": "ok"
    },
    {
    "elect": 2000,
    "duty": "2001-01-20",
    "fio": "George W. Bush",
    "number": 43,
    "party": "Republican",
    "vice": "Dick Cheney",
    "age": 54,
    "result": "ok"
    },
    {
    "elect": 2004,
    "duty": "2005-01-20",
    "fio": "George W. Bush",
    "number": 43,
    "party": "Republican",
    "vice": "Dick Cheney",
    "age": 58,
    "result": "ok"
    },
    {
    "elect": 2008,
    "duty": "2009-01-20",
    "fio": "Barack Obama",
    "number": 44,
    "party": "Democratic",
    "vice": "Joe Biden",
    "age": 47,
    "result": "ok"
    },
    {
    "elect": 2012,
    "duty": "2013-01-20",
    "fio": "Barack Obama",
    "number": 44,
    "party": "Democratic",
    "vice": "Joe Biden",
    "age": 51,
    "result": "ok"
    },
    {
    "elect": 2016,
    "duty": "2017-01-20",
    "fio": "Donald Trump",
    "number": 45,
    "party": "Republican",
    "vice": "Mike Pence",
    "age": 70,
    "result": "ok"
    },
    {
    "elect": 2020,
    "duty": "2021-01-20",
    "fio": "Joe Biden",
    "number": 46,
    "party": "Democratic",
    "vice": "Kamala Harris",
    "age": 78,
    "result": "ok"
    },
    {
    "elect": 2024,
    "duty": "2025-01-20",
    "fio": "Donald Trump",
    "number": 47,
    "party": "Republican",
    "vice": "JD Vance",
    "age": 78,
    "result": "ok"
    }
    ]

# -------------------------- подготовка -------------------------

from collections import Counter, defaultdict
from pprint import pprint

# -------------------------- расчёт -------------------------

# ---------- тест 1 ----------

print('\n1. табличка по номерам, именам, годам, партиям\n')

for pres in usa:
    print(f"{pres['number']:2}. {pres['fio']:30} @ {pres['elect']:4} - {pres['party']:20}")

# ~ 1. табличка по номерам, именам, годам, партиям

 # ~ 1. George Washington              @ 1788 - Independent         
 # ~ 1. George Washington              @ 1792 - Independent         
 # ~ 2. John Adams                     @ 1796 - Federalist          
 # ~ 3. Thomas Jefferson               @ 1800 - Democratic-Republican
 # ~ 3. Thomas Jefferson               @ 1804 - Democratic-Republican
 # ~ 4. James Madison                  @ 1808 - Democratic-Republican
 # ~ 4. James Madison                  @ 1812 - Democratic-Republican
 # ~ 5. James Monroe                   @ 1816 - Democratic-Republican
 # ~ 5. James Monroe                   @ 1820 - Democratic-Republican
 # ~ 6. John Quincy Adams              @ 1824 - Democratic-Republican
 # ~ 7. Andrew Jackson                 @ 1828 - Democratic          
 # ~ 7. Andrew Jackson                 @ 1832 - Democratic          
 # ~ 8. Martin Van Buren               @ 1836 - Democratic          
 # ~ 9. William Henry Harrison         @ 1840 - Whig                
# ~ 10. John Tyler                     @    0 - Whig / Independent  
# ~ 11. James K. Polk                  @ 1844 - Democratic          
# ~ 12. Zachary Taylor                 @ 1848 - Whig                
# ~ 13. Millard Fillmore               @    0 - Whig                
# ~ 14. Franklin Pierce                @ 1852 - Democratic          
# ~ 15. James Buchanan                 @ 1856 - Democratic          
# ~ 16. Abraham Lincoln                @ 1860 - Republican          
# ~ 16. Abraham Lincoln                @ 1864 - National Union      
# ~ 17. Andrew Johnson                 @    0 - Democratic / National Union
# ~ 18. Ulysses S. Grant               @ 1868 - Republican          
# ~ 18. Ulysses S. Grant               @ 1872 - Republican          
# ~ 19. Rutherford B. Hayes            @ 1876 - Republican          
# ~ 20. James A. Garfield              @ 1880 - Republican          
# ~ 21. Chester A. Arthur              @    0 - Republican          
# ~ 22. Grover Cleveland               @ 1884 - Democratic          
# ~ 23. Benjamin Harrison              @ 1888 - Republican          
# ~ 24. Grover Cleveland               @ 1892 - Democratic          
# ~ 25. William McKinley               @ 1896 - Republican          
# ~ 25. William McKinley               @ 1900 - Republican          
# ~ 26. Theodore Roosevelt             @    0 - Republican          
# ~ 26. Theodore Roosevelt             @ 1904 - Republican          
# ~ 27. William Howard Taft            @ 1908 - Republican          
# ~ 28. Woodrow Wilson                 @ 1912 - Democratic          
# ~ 28. Woodrow Wilson                 @ 1916 - Democratic          
# ~ 29. Warren G. Harding              @ 1920 - Republican          
# ~ 30. Calvin Coolidge                @    0 - Republican          
# ~ 30. Calvin Coolidge                @ 1924 - Republican          
# ~ 31. Herbert Hoover                 @ 1928 - Republican          
# ~ 32. Franklin D. Roosevelt          @ 1932 - Democratic          
# ~ 32. Franklin D. Roosevelt          @ 1936 - Democratic          
# ~ 32. Franklin D. Roosevelt          @ 1940 - Democratic          
# ~ 32. Franklin D. Roosevelt          @ 1944 - Democratic          
# ~ 33. Harry S. Truman                @    0 - Democratic          
# ~ 33. Harry S. Truman                @ 1948 - Democratic          
# ~ 34. Dwight D. Eisenhower           @ 1952 - Republican          
# ~ 34. Dwight D. Eisenhower           @ 1956 - Republican          
# ~ 35. John F. Kennedy                @ 1960 - Democratic          
# ~ 36. Lyndon B. Johnson              @    0 - Democratic          
# ~ 36. Lyndon B. Johnson              @ 1964 - Democratic          
# ~ 37. Richard Nixon                  @ 1968 - Republican          
# ~ 37. Richard Nixon                  @ 1972 - Republican          
# ~ 38. Gerald Ford                    @    0 - Republican          
# ~ 39. Jimmy Carter                   @ 1976 - Democratic          
# ~ 40. Ronald Reagan                  @ 1980 - Republican          
# ~ 40. Ronald Reagan                  @ 1984 - Republican          
# ~ 41. George H. W. Bush              @ 1988 - Republican          
# ~ 42. Bill Clinton                   @ 1992 - Democratic          
# ~ 42. Bill Clinton                   @ 1996 - Democratic          
# ~ 43. George W. Bush                 @ 2000 - Republican          
# ~ 43. George W. Bush                 @ 2004 - Republican          
# ~ 44. Barack Obama                   @ 2008 - Democratic          
# ~ 44. Barack Obama                   @ 2012 - Democratic          
# ~ 45. Donald Trump                   @ 2016 - Republican          
# ~ 46. Joe Biden                      @ 2020 - Democratic          
# ~ 47. Donald Trump                   @ 2024 - Republican

# ---------- тест 2 ----------

print('\n2. сколько выжило и померло\n')

fate = Counter( [ pres['result'] for pres in usa] )

pprint(fate)

# ~ 2. сколько выжило и померло

# ~ Counter({'ok': 61, 'died': 8})

# ---------- тест 3 ----------

print('\n3. изучаем возраст при вступлении\n')

ages = Counter( [ pres['age'] for pres in usa] )

print("возрасты:", ages)

print(f"""
статистика:
минимальный:   { min(ages) }
максимальный:  { max(ages) }
средний:       { sum(ages) / len(ages) }
""")

# ~ 3. изучаем возраст при вступлении

# ~ возрасты: Counter({61: 6, 54: 6, 57: 5, 51: 5, 56: 5, 50: 4, 55: 4, 58: 3, 62: 3, 64: 3, 52: 3, 46: 3, 60: 3, 65: 2, 49: 2, 47: 2, 78: 2, 68: 1, 48: 1, 42: 1, 66: 1, 43: 1, 69: 1, 73: 1, 70: 1})

# ~ статистика:
# ~ минимальный:   42
# ~ максимальный:  78
# ~ средний:       57.76

# ------------------------ конец -----------------------------
print()
