#!/usr/bin/env python
# myke 2026-06-22 2026-06-22 1.1
# uk-premier.py

# ~ дай список всех премьер-министров Великобритании, формат: list[dict], поля:
# ~ - имя,
# ~ - полные даты жизни (YYYY-MM-DD),
# ~ - полные даты правления (YYYY-MM-DD),
# ~ - при каком монархе,
# ~ - место рождения,
# ~ - образование и колледж

primes = [
    {
        "name": "Robert Walpole",
        "lifespan": "1676-08-26 - 1745-03-18",
        "term": "1721-04-04 - 1742-02-11",
        "monarch": "George I, George II",
        "birthplace": "Houghton Hall, Norfolk, England",
        "education": "Eton College; King's College, Cambridge"
    },
    {
        "name": "Spencer Compton",
        "lifespan": "1673-03-01 - 1743-07-02",
        "term": "1742-02-16 - 1743-07-02",
        "monarch": "George II",
        "birthplace": "Compton Wynyates, Warwickshire, England",
        "education": "St Paul's School; Trinity College, Oxford"
    },
    {
        "name": "Henry Pelham",
        "lifespan": "1694-09-25 - 1754-03-06",
        "term": "1743-08-27 - 1754-03-06",
        "monarch": "George II",
        "birthplace": "Laughton, Sussex, England",
        "education": "Westminster School; Hart Hall, Oxford"
    },
    {
        "name": "Thomas Pelham-Holles",
        "lifespan": "1693-07-21 - 1768-11-17",
        "term": "1754-03-16 - 1756-11-16, 1757-07-02 - 1762-05-26",
        "monarch": "George II, George III",
        "birthplace": "London, England",
        "education": "Westminster School; Clare Hall, Cambridge"
    },
    {
        "name": "William Cavendish",
        "lifespan": "1720-05-08 - 1764-10-02",
        "term": "1756-11-16 - 1757-06-25",
        "monarch": "George II",
        "birthplace": "London, England",
        "education": "Privately educated"
    },
    {
        "name": "John Stuart",
        "lifespan": "1713-05-25 - 1792-03-10",
        "term": "1762-05-26 - 1763-04-08",
        "monarch": "George III",
        "birthplace": "Edinburgh, Scotland",
        "education": "Eton College; University of Leiden"
    },
    {
        "name": "George Grenville",
        "lifespan": "1712-10-14 - 1770-11-13",
        "term": "1763-04-16 - 1765-07-13",
        "monarch": "George III",
        "birthplace": "London, England",
        "education": "Eton College; Christ Church, Oxford"
    },
    {
        "name": "Charles Watson-Wentworth",
        "lifespan": "1730-05-13 - 1782-07-01",
        "term": "1765-07-13 - 1766-07-30, 1782-03-27 - 1782-07-01",
        "monarch": "George III",
        "birthplace": "Wentworth, Yorkshire, England",
        "education": "Westminster School; St John's College, Cambridge"
    },
    {
        "name": "William Pitt 'The Elder'",
        "lifespan": "1708-11-15 - 1778-05-11",
        "term": "1766-07-30 - 1768-10-14",
        "monarch": "George III",
        "birthplace": "Westminster, London, England",
        "education": "Eton College; Trinity College, Oxford"
    },
    {
        "name": "Augustus FitzRoy",
        "lifespan": "1735-09-28 - 1811-03-14",
        "term": "1768-10-14 - 1770-01-28",
        "monarch": "George III",
        "birthplace": "London, England",
        "education": "Westminster School; Peterhouse, Cambridge"
    },
    {
        "name": "Frederick North",
        "lifespan": "1732-04-13 - 1792-08-05",
        "term": "1770-01-28 - 1782-03-22",
        "monarch": "George III",
        "birthplace": "London, England",
        "education": "Eton College; Christ Church, Oxford"
    },
    {
        "name": "William Petty",
        "lifespan": "1737-05-02 - 1805-05-07",
        "term": "1782-07-04 - 1783-04-02",
        "monarch": "George III",
        "birthplace": "Dublin, Ireland",
        "education": "Westminster School; Christ Church, Oxford"
    },
    {
        "name": "William Cavendish-Bentinck",
        "lifespan": "1738-04-14 - 1809-10-30",
        "term": "1783-04-02 - 1783-12-19, 1807-03-31 - 1809-10-04",
        "monarch": "George III",
        "birthplace": "Nottinghamshire, England",
        "education": "Westminster School; Christ Church, Oxford"
    },
    {
        "name": "William Pitt 'The Younger'",
        "lifespan": "1759-05-28 - 1806-01-23",
        "term": "1783-12-19 - 1801-03-14, 1804-05-10 - 1806-01-23",
        "monarch": "George III",
        "birthplace": "Hayes, Kent, England",
        "education": "Pembroke Hall, Cambridge"
    },
    {
        "name": "Henry Addington",
        "lifespan": "1757-05-30 - 1844-02-15",
        "term": "1801-03-17 - 1804-05-10",
        "monarch": "George III",
        "birthplace": "Holborn, London, England",
        "education": "Winchester College; Brasenose College, Oxford"
    },
    {
        "name": "William Grenville",
        "lifespan": "1759-10-25 - 1834-01-12",
        "term": "1806-02-11 - 1807-03-31",
        "monarch": "George III",
        "birthplace": "Buckinghamshire, England",
        "education": "Eton College; Christ Church, Oxford"
    },
    {
        "name": "Spencer Perceval",
        "lifespan": "1762-11-01 - 1812-05-11",
        "term": "1809-10-04 - 1812-05-11",
        "monarch": "George III",
        "birthplace": "Mayfair, London, England",
        "education": "Harrow School; Trinity College, Cambridge"
    },
    {
        "name": "Robert Jenkinson",
        "lifespan": "1770-06-07 - 1828-12-04",
        "term": "1812-06-08 - 1827-04-09",
        "monarch": "George III, George IV",
        "birthplace": "London, England",
        "education": "Charterhouse School; Christ Church, Oxford"
    },
    {
        "name": "George Canning",
        "lifespan": "1770-04-11 - 1827-08-08",
        "term": "1827-04-12 - 1827-08-08",
        "monarch": "George IV",
        "birthplace": "Marylebone, London, England",
        "education": "Eton College; Christ Church, Oxford"
    },
    {
        "name": "Frederick John Robinson",
        "lifespan": "1782-11-01 - 1859-01-28",
        "term": "1827-08-31 - 1828-01-21",
        "monarch": "George IV",
        "birthplace": "London, England",
        "education": "Harrow School; St John's College, Cambridge"
    },
    {
        "name": "Arthur Wellesley",
        "lifespan": "1769-05-01 - 1852-09-14",
        "term": "1828-01-22 - 1830-11-16, 1834-11-17 - 1834-12-09",
        "monarch": "George IV, William IV",
        "birthplace": "Dublin, Ireland",
        "education": "Eton College; Royal Academy of Equitation, Angers"
    },
    {
        "name": "Charles Grey",
        "lifespan": "1764-03-13 - 1845-07-17",
        "term": "1830-11-22 - 1834-07-16",
        "monarch": "William IV",
        "birthplace": "Fallodon, Northumberland, England",
        "education": "Eton College; Trinity College, Cambridge"
    },
    {
        "name": "William Lamb",
        "lifespan": "1779-03-15 - 1848-11-24",
        "term": "1834-07-16 - 1834-11-14, 1835-04-18 - 1841-08-30",
        "monarch": "William IV, Victoria",
        "birthplace": "London, England",
        "education": "Eton College; Trinity College, Cambridge; University of Glasgow"
    },
    {
        "name": "Robert Peel",
        "lifespan": "1788-02-05 - 1850-07-02",
        "term": "1834-12-10 - 1835-04-08, 1841-08-30 - 1846-06-29",
        "monarch": "William IV, Victoria",
        "birthplace": "Bury, Lancashire, England",
        "education": "Harrow School; Christ Church, Oxford"
    },
    {
        "name": "John Russell",
        "lifespan": "1792-08-18 - 1878-05-28",  
        "term": "1846-06-30 - 1852-02-23, 1865-10-29 - 1866-06-26",
        "monarch": "Victoria",
        "birthplace": "London, England",
        "education": "Westminster School; University of Edinburgh"
    },
    {
        "name": "Edward Smith-Stanley",
        "lifespan": "1799-03-29 - 1869-10-23",  
        "term": "1852-02-23 - 1852-11-17, 1858-02-20 - 1859-06-11, 1866-06-28 - 1868-02-27",
        "monarch": "Victoria",
        "birthplace": "Knowsley Hall, Lancashire, England",
        "education": "Eton College; Christ Church, Oxford"
    },
    {
        "name": "George Hamilton-Gordon",
        "lifespan": "1784-01-28 - 1860-12-14",  
        "term": "1852-12-19 - 1855-01-30",
        "monarch": "Victoria",
        "birthplace": "Edinburgh, Scotland",
        "education": "Harrow School; St John's College, Cambridge"
    },
    {
        "name": "Henry John Temple",
        "lifespan": "1784-10-20 - 1865-10-18",  
        "term": "1855-02-06 - 1858-02-19, 1859-06-12 - 1865-10-18",
        "monarch": "Victoria",
        "birthplace": "Westminster, London, England",
        "education": "Harrow School; University of Edinburgh; St John's College, Cambridge"
    },
    {
        "name": "Benjamin Disraeli",
        "lifespan": "1804-12-21 - 1881-04-19",
        "term": "1868-02-27 - 1868-12-01, 1874-02-20 - 1880-04-21",
        "monarch": "Victoria",
        "birthplace": "Bloomsbury, London, England",
        "education": "Higham Hall School"
    },
    {
        "name": "William Ewart Gladstone",
        "lifespan": "1809-12-29 - 1898-05-19",
        "term": "1868-12-03 - 1874-02-17, 1880-04-23 - 1885-06-09, 1886-02-01 - 1886-07-20, 1892-08-15 - 1894-03-02",
        "monarch": "Victoria",
        "birthplace": "Liverpool, England",
        "education": "Eton College; Christ Church, Oxford"
    },
    {
        "name": "Robert Gascoyne-Cecil",
        "lifespan": "1830-02-03 - 1903-08-22",
        "term": "1885-06-23 - 1886-01-28, 1886-07-25 - 1892-08-11, 1895-06-25 - 1902-07-11",
        "monarch": "Victoria, Edward VII",
        "birthplace": "Hatfield House, Hertfordshire, England",
        "education": "Eton College; Christ Church, Oxford"
    },
    {
        "name": "Archibald Primrose",
        "lifespan": "1847-05-07 - 1929-05-21",
        "term": "1894-03-05 - 1895-06-21",
        "monarch": "Victoria",
        "birthplace": "Mayfair, London, England",
        "education": "Eton College; Christ Church, Oxford"
    },
    {
        "name": "Arthur Balfour",
        "lifespan": "1848-07-25 - 1930-03-19",
        "term": "1902-07-11 - 1905-12-05",
        "monarch": "Edward VII",
        "birthplace": "Whittingehame, East Lothian, Scotland",
        "education": "Eton College; Trinity College, Cambridge"
    },
    {
        "name": "Henry Campbell-Bannerman",
        "lifespan": "1836-09-07 - 1908-04-22",
        "term": "1905-12-05 - 1908-04-03",
        "monarch": "Edward VII",
        "birthplace": "Glasgow, Scotland",
        "education": "High School of Glasgow; University of Glasgow; Trinity College, Cambridge"
    },
    {
        "name": "H. H. Asquith",
        "lifespan": "1852-09-12 - 1928-02-15",
        "term": "1908-04-05 - 1916-12-05",
        "monarch": "Edward VII, George V",
        "birthplace": "Morley, West Yorkshire, England",
        "education": "Huddersfield College; City of London School; Balliol College, Oxford"
    },
    {
        "name": "David Lloyd George",
        "lifespan": "1863-01-17 - 1945-03-26",
        "term": "1916-12-06 - 1922-10-19",
        "monarch": "George V",
        "birthplace": "Chorlton-on-Medlock, Manchester, England",
        "education": "Llanystumdwy National School"
    },
    {
        "name": "Andrew Bonar Law",
        "lifespan": "1858-09-16 - 1923-10-30",
        "term": "1922-10-23 - 1923-05-20",
        "monarch": "George V",
        "birthplace": "Five Elevens, New Brunswick, Canada",
        "education": "High School of Glasgow"
    },
    {
        "name": "Stanley Baldwin",
        "lifespan": "1867-08-03 - 1947-12-14",
        "term": "1923-05-22 - 1924-01-22, 1924-11-04 - 1929-06-04, 1935-06-07 - 1937-05-28",
        "monarch": "George V, Edward VIII, George VI",
        "birthplace": "Bewdley, Worcestershire, England",
        "education": "Harrow School; Trinity College, Cambridge"
    },
    {
        "name": "Ramsay MacDonald",
        "lifespan": "1866-10-12 - 1937-11-09",
        "term": "1924-01-22 - 1924-11-04, 1929-06-05 - 1935-06-07",
        "monarch": "George V",
        "birthplace": "Lossiemouth, Moray, Scotland",
        "education": "Drainie Board School"
    },
    {
        "name": "Neville Chamberlain",
        "lifespan": "1869-03-18 - 1940-11-09",
        "term": "1937-05-28 - 1940-05-10",
        "monarch": "George VI",
        "birthplace": "Edgbaston, Birmingham, England",
        "education": "Rugby School; Mason Science College"
    },
    {
        "name": "Winston Churchill",
        "lifespan": "1874-11-30 - 1965-01-24",
        "term": "1940-05-10 - 1945-07-26, 1951-10-26 - 1955-04-05",
        "monarch": "George VI, Elizabeth II",
        "birthplace": "Blenheim Palace, Oxfordshire, England",
        "education": "Harrow School; Royal Military College, Sandhurst"
    },
    {
        "name": "Clement Attlee",
        "lifespan": "1883-01-03 - 1967-10-08",
        "term": "1945-07-26 - 1951-10-26",
        "monarch": "George VI",
        "birthplace": "Putney, London, England",
        "education": "Haileybury College; University College, Oxford"
    },
    {
        "name": "Anthony Eden",
        "lifespan": "1897-06-12 - 1977-01-14",
        "term": "1955-04-06 - 1957-01-09",
        "monarch": "Elizabeth II",
        "birthplace": "Windlestone Hall, County Durham, England",
        "education": "Eton College; Christ Church, Oxford"
    },
    {
        "name": "Harold Macmillan",
        "lifespan": "1894-02-10 - 1986-12-29",
        "term": "1957-01-10 - 1963-10-18",
        "monarch": "Elizabeth II",
        "birthplace": "Belgravia, London, England",
        "education": "Eton College; Balliol College, Oxford"
    },
    {
        "name": "Alec Douglas-Home",
        "lifespan": "1903-07-02 - 1995-10-09",
        "term": "1963-10-19 - 1964-10-16",
        "monarch": "Elizabeth II",
        "birthplace": "Mayfair, London, England",
        "education": "Eton College; Christ Church, Oxford"
    },
    {
        "name": "Harold Wilson",
        "lifespan": "1916-03-11 - 1995-05-24",
        "term": "1964-10-16 - 1970-06-19, 1974-03-04 - 1976-04-05",
        "monarch": "Elizabeth II",
        "birthplace": "Huddersfield, Yorkshire, England",
        "education": "Royds Hall Grammar School; Jesus College, Oxford"
    },
    {
        "name": "Edward Heath",
        "lifespan": "1916-07-09 - 2005-07-17",
        "term": "1970-06-19 - 1974-03-04",
        "monarch": "Elizabeth II",
        "birthplace": "Broadstairs, Kent, England",
        "education": "Chatham House Grammar School; Balliol College, Oxford"
    },
    {
        "name": "James Callaghan",
        "lifespan": "1912-03-27 - 2005-03-26",
        "term": "1976-04-05 - 1979-05-04",
        "monarch": "Elizabeth II",
        "birthplace": "Portsmouth, Hampshire, England",
        "education": "Portsmouth Northern Grammar School"
    },
    {
        "name": "Margaret Thatcher",
        "lifespan": "1925-10-13 - 2013-04-08",
        "term": "1979-05-04 - 1990-11-28",
        "monarch": "Elizabeth II",
        "birthplace": "Grantham, Lincolnshire, England",
        "education": "Kesteven and Grantham Girls' School; Somerville College, Oxford"
    },
    {
        "name": "John Major",
        "lifespan": "1943-03-29 - Alive",
        "term": "1990-11-28 - 1997-05-02",
        "monarch": "Elizabeth II",
        "birthplace": "Carshalton, Surrey, England",
        "education": "Rutlish School"
    },
    {
        "name": "Tony Blair",
        "lifespan": "1953-05-06 - Alive",
        "term": "1997-05-02 - 2007-06-27",
        "monarch": "Elizabeth II",
        "birthplace": "Edinburgh, Scotland",
        "education": "Fettes College; St John's College, Oxford"
    },
    {
        "name": "Gordon Brown",
        "lifespan": "1951-02-20 - Alive",
        "term": "2007-06-27 - 2010-05-11",
        "monarch": "Elizabeth II",
        "birthplace": "Giffnock, Renfrewshire, Scotland",
        "education": "Kirkcaldy High School; University of Edinburgh"
    },
    {
        "name": "David Cameron",
        "lifespan": "1966-10-09 - Alive",
        "term": "2010-05-11 - 2016-07-13",
        "monarch": "Elizabeth II",
        "birthplace": "Marylebone, London, England",
        "education": "Eton College; Brasenose College, Oxford"
    },
    {
        "name": "Theresa May",
        "lifespan": "1956-10-01 - Alive",
        "term": "2016-07-13 - 2019-07-24",
        "monarch": "Elizabeth II",
        "birthplace": "Eastbourne, Sussex, England",
        "education": "Holton Park Girls' Grammar School; St Hugh's College, Oxford"
    },
    {
        "name": "Boris Johnson",
        "lifespan": "1964-06-19 - Alive",
        "term": "2019-07-24 - 2022-09-06",
        "monarch": "Elizabeth II",
        "birthplace": "New York City, United States",
        "education": "Eton College; Balliol College, Oxford"
    },
    {
        "name": "Liz Truss",
        "lifespan": "1975-07-26 - Alive",
        "term": "2022-09-06 - 2022-10-25",
        "monarch": "Elizabeth II, Charles III",
        "birthplace": "Oxford, Oxfordshire, England",
        "education": "Roundhay School; Merton College, Oxford"
    },
    {
        "name": "Rishi Sunak",
        "lifespan": "1980-05-12 - Alive",
        "term": "2022-10-25 - 2024-07-05",
        "monarch": "Charles III",
        "birthplace": "Southampton, Hampshire, England",
        "education": "Winchester College; Lincoln College, Oxford; Stanford University"
    },
    {
        "name": "Keir Starmer",
        "lifespan": "1962-09-02 - Alive",
        "term": "2024-07-05 - Incumbent",
        "monarch": "Charles III",
        "birthplace": "Southwark, London, England",
        "education": "Reigate Grammar School; University of Leeds; St Edmund Hall, Oxford"
    }
]


# -----------------------------------------------------------------

# ------------------------ prepare -------------------------

from pprint import pp, pprint

# ----------------------------------------------------------

def part(name):
    print(f"""
----------------------------------------------------------
{name}
----------------------------------------------------------
""")

def cprint(kv, wleft=20):
    for k, v in kv:
        print(f"{k:{wleft}} | {v}")


# -------------------------------------------------
part("1. List of all primes' names.")
# -----------------------------------------------------------------

for n, prm in enumerate(primes, start=1):
    print(f"{n}. {prm['name']}")


# ~ 1. Robert Walpole
# ~ 2. Spencer Compton
# ~ 3. Henry Pelham
# ~ 4. Thomas Pelham-Holles
# ~ 5. William Cavendish
# ~ 6. John Stuart
# ~ 7. George Grenville
# ~ 8. Charles Watson-Wentworth
# ~ 9. William Pitt 'The Elder'
# ~ 10. Augustus FitzRoy
# ~ 11. Frederick North
# ~ 12. William Petty
# ~ 13. William Cavendish-Bentinck
# ~ 14. William Pitt 'The Younger'
# ~ 15. Henry Addington
# ~ 16. William Grenville
# ~ 17. Spencer Perceval
# ~ 18. Robert Jenkinson
# ~ 19. George Canning
# ~ 20. Frederick John Robinson
# ~ 21. Arthur Wellesley
# ~ 22. Charles Grey
# ~ 23. William Lamb
# ~ 24. Robert Peel
# ~ 25. John Russell
# ~ 26. Edward Smith-Stanley
# ~ 27. George Hamilton-Gordon
# ~ 28. Henry John Temple
# ~ 29. Benjamin Disraeli
# ~ 30. William Ewart Gladstone
# ~ 31. Robert Gascoyne-Cecil
# ~ 32. Archibald Primrose
# ~ 33. Arthur Balfour
# ~ 34. Henry Campbell-Bannerman
# ~ 35. H. H. Asquith
# ~ 36. David Lloyd George
# ~ 37. Andrew Bonar Law
# ~ 38. Stanley Baldwin
# ~ 39. Ramsay MacDonald
# ~ 40. Neville Chamberlain
# ~ 41. Winston Churchill
# ~ 42. Clement Attlee
# ~ 43. Anthony Eden
# ~ 44. Harold Macmillan
# ~ 45. Alec Douglas-Home
# ~ 46. Harold Wilson
# ~ 47. Edward Heath
# ~ 48. James Callaghan
# ~ 49. Margaret Thatcher
# ~ 50. John Major
# ~ 51. Tony Blair
# ~ 52. Gordon Brown
# ~ 53. David Cameron
# ~ 54. Theresa May
# ~ 55. Boris Johnson
# ~ 56. Liz Truss
# ~ 57. Rishi Sunak
# ~ 58. Keir Starmer


# -------------------------------------------------
part("2. List of primes' colleges.")
# -----------------------------------------------------------------

from collections import Counter

cnt = Counter()

for prm in primes:
    edus = prm['education'].split(';')
    edus = map(lambda x: x.strip(), edus)
    cnt.update(edus)

cntmc = cnt.most_common() 
cprint(cntmc, 40)

oxford = cambridge = others = 0
for prm in primes:
    edu = prm['education']
    if 'Oxford' in edu: oxford += 1
    elif 'Cambridge' in edu: cambridge += 1
    else: others += 1

print(f"\nColleges: {oxford=}, {cambridge=}, {others=}")


# ~ Eton College                             | 20
# ~ Christ Church, Oxford                    | 14
# ~ Westminster School                       | 7
# ~ Harrow School                            | 7
# ~ Trinity College, Cambridge               | 6
# ~ St John's College, Cambridge             | 4
# ~ Balliol College, Oxford                  | 4
# ~ University of Edinburgh                  | 3
# ~ Trinity College, Oxford                  | 2
# ~ Winchester College                       | 2
# ~ Brasenose College, Oxford                | 2
# ~ University of Glasgow                    | 2
# ~ High School of Glasgow                   | 2
# ~ King's College, Cambridge                | 1
# ~ St Paul's School                         | 1
# ~ Hart Hall, Oxford                        | 1
# ~ Clare Hall, Cambridge                    | 1
# ~ Privately educated                       | 1
# ~ University of Leiden                     | 1
# ~ Peterhouse, Cambridge                    | 1
# ~ Pembroke Hall, Cambridge                 | 1
# ~ Charterhouse School                      | 1
# ~ Royal Academy of Equitation, Angers      | 1
# ~ Higham Hall School                       | 1
# ~ Huddersfield College                     | 1
# ~ City of London School                    | 1
# ~ Llanystumdwy National School             | 1
# ~ Drainie Board School                     | 1
# ~ Rugby School                             | 1
# ~ Mason Science College                    | 1
# ~ Royal Military College, Sandhurst        | 1
# ~ Haileybury College                       | 1
# ~ University College, Oxford               | 1
# ~ Royds Hall Grammar School                | 1
# ~ Jesus College, Oxford                    | 1
# ~ Chatham House Grammar School             | 1
# ~ Portsmouth Northern Grammar School       | 1
# ~ Kesteven and Grantham Girls' School      | 1
# ~ Somerville College, Oxford               | 1
# ~ Rutlish School                           | 1
# ~ Fettes College                           | 1
# ~ St John's College, Oxford                | 1
# ~ Kirkcaldy High School                    | 1
# ~ Holton Park Girls' Grammar School        | 1
# ~ St Hugh's College, Oxford                | 1
# ~ Roundhay School                          | 1
# ~ Merton College, Oxford                   | 1
# ~ Lincoln College, Oxford                  | 1
# ~ Stanford University                      | 1
# ~ Reigate Grammar School                   | 1
# ~ University of Leeds                      | 1
# ~ St Edmund Hall, Oxford                   | 1

# ~ Colleges: oxford=31, cambridge=14, others=13

# -------------------------------------------------
part("3. List of primes - recidivists.")
# -----------------------------------------------------------------

recids = [ prm['name'] for prm in primes if ',' in prm['term']]

print(f"recidivists: {len(recids)}\n")
print(*recids, sep="\n")

#recidivists: 17

# Thomas Pelham-Holles
# Charles Watson-Wentworth
# William Cavendish-Bentinck
# William Pitt 'The Younger'
# Arthur Wellesley
# William Lamb
# Robert Peel
# John Russell
# Edward Smith-Stanley
# Henry John Temple
# Benjamin Disraeli
# William Ewart Gladstone
# Robert Gascoyne-Cecil
# Stanley Baldwin
# Ramsay MacDonald
# Winston Churchill
# Harold Wilson

# -----------------------------------------------------------------
part("The End.")
# -----------------------------------------------------------------
