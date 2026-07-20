#!/usr/bin/env python

# Mikhail (myke) Kolodin, 2026
# uk-great.py
# 2026-06-23 2026-06-23 1.0
# великие британцы

# ~ дай список 100 самых знаменитых людей Великобритании за последние 300 лет; для каждого укажи полное имя, статус (титул, напр., барон, если есть), годы рождения и смерти, одно основное направление деятельности из списка (lit, sci, art, pol, bus, spo, etc), образование (школа или колледж, институт или университет - какие именно); вывод в формате list[dict] для python

# ~ lit, sci, art, pol, bus, spo, etc =
# ~ литература, наука, искусство, бизнес, спорт, прочее

famous = [
    {
        "full_name": "Isaac Newton",
        "status": "Knight",
        "years": "1643–1727",
        "field": "sci",
        "education": "The King's School, Grantham; Trinity College, Cambridge"
    },
    {
        "full_name": "Winston Leonard Spencer Churchill",
        "status": "Knight, Prime Minister",
        "years": "1874–1965",
        "field": "pol",
        "education": "Harrow School; Royal Military College, Sandhurst"
    },
    {
        "full_name": "Charles Robert Darwin",
        "status": "None",
        "years": "1809–1882",
        "field": "sci",
        "education": "Shrewsbury School; University of Edinburgh; Christ's College, Cambridge"
    },
    {
        "full_name": "William Shakespeare",
        "status": "None",
        "years": "1564–1616",
        "field": "lit",
        "education": "King Edward VI School, Stratford-upon-Avon"
    },
    {
        "full_name": "Stephen William Hawking",
        "status": "Companion of Honour",
        "years": "1942–2018",
        "field": "sci",
        "education": "St Albans School; University College, Oxford; Trinity Hall, Cambridge"
    },
    {
        "full_name": "Margaret Hilda Thatcher",
        "status": "Baroness, Prime Minister",
        "years": "1925–2013",
        "field": "pol",
        "education": "Kesteven and Grantham Girls' School; Somerville College, Oxford"
    },
    {
        "full_name": "John Winston Ono Lennon",
        "status": "MBE (Returned)",
        "years": "1940–1980",
        "field": "art",
        "education": "Quarry Bank High School; Liverpool College of Art"
    },
    {
        "full_name": "James Cook",
        "status": "Captain",
        "years": "1728–1779",
        "field": "etc",
        "education": "Postgate School"
    },
    {
        "full_name": "Queen Victoria",
        "status": "Queen, Empress",
        "years": "1819–1901",
        "field": "pol",
        "education": "Private Education"
    },
    {
        "full_name": "Queen Elizabeth II",
        "status": "Queen",
        "years": "1926–2022",
        "field": "pol",
        "education": "Private Education"
    },
    {
        "full_name": "Diana Frances Spencer",
        "status": "Princess of Wales",
        "years": "1961–1997",
        "field": "etc",
        "education": "West Heath School; Institut Alpin Videmanette"
    },
    {
        "full_name": "James Clerk Maxwell",
        "status": "None",
        "years": "1831–1879",
        "field": "sci",
        "education": "Edinburgh Academy; University of Edinburgh; Peterhouse & Trinity College, Cambridge"
    },
    {
        "full_name": "Alexander Fleming",
        "status": "Knight",
        "years": "1881–1955",
        "field": "sci",
        "education": "Louden Moor School; Kilmarnock Academy; St Mary's Hospital Medical School"
    },
    {
        "full_name": "Adam Smith",
        "status": "None",
        "years": "1723–1790",
        "field": "sci",
        "education": "Burgh School of Kirkcaldy; University of Glasgow; Balliol College, Oxford"
    },
    {
        "full_name": "Charles John Huffam Dickens",
        "status": "None",
        "years": "1812–1870",
        "field": "lit",
        "education": "Wellington House Academy"
    },
    {
        "full_name": "Jane Austen",
        "status": "None",
        "years": "1775–1817",
        "field": "lit",
        "education": "Reading Abbey Girls' School"
    },
    {
        "full_name": "Alan Mathison Turing",
        "status": "OBE",
        "years": "1912–1954",
        "field": "sci",
        "education": "Sherborne School; King's College, Cambridge; Princeton University"
    },
    {
        "full_name": "Michael Faraday",
        "status": "None",
        "years": "1791–1867",
        "field": "sci",
        "education": "Self-educated"
    },
    {
        "full_name": "Ernest Rutherford",
        "status": "Baron Rutherford of Nelson",
        "years": "1871–1937",
        "field": "sci",
        "education": "Nelson College; Canterbury College; Trinity College, Cambridge"
    },
    {
        "full_name": "James Watt",
        "status": "None",
        "years": "1736–1819",
        "field": "sci",
        "education": "Greenock Grammar School"
    },
    {
        "full_name": "Alexander Graham Bell",
        "status": "None",
        "years": "1847–1922",
        "field": "sci",
        "education": "Royal High School, Edinburgh; University of Edinburgh; University College London"
    },
    {
        "full_name": "George Stephenson",
        "status": "None",
        "years": "1781–1848",
        "field": "sci",
        "education": "Night School"
    },
    {
        "full_name": "Isambard Kingdom Brunel",
        "status": "None",
        "years": "1806–1859",
        "field": "sci",
        "education": "King's College School; Lycée Henri-IV"
    },
    {
        "full_name": "Horatio Nelson",
        "status": "Viscount Nelson, Vice Admiral",
        "years": "1758–1805",
        "field": "pol",
        "education": "King Edward VI Grammar School"
    },
    {
        "full_name": "Arthur Wellesley",
        "status": "Duke of Wellington, Prime Minister",
        "years": "1769–1852",
        "field": "pol",
        "education": "Eton College; Royal Academy of Equitation, Angers"
    },
    {
        "full_name": "Florence Nightingale",
        "status": "Order of Merit",
        "years": "1820–1910",
        "field": "etc",
        "education": "Private Education"
    },
    {
        "full_name": "Emmeline Pankhurst",
        "status": "None",
        "years": "1858–1928",
        "field": "pol",
        "education": "École Normale de Neuilly"
    },
    {
        "full_name": "Thomas Paine",
        "status": "None",
        "years": "1737–1809",
        "field": "pol",
        "education": "Thetford Grammar School"
    },
    {
        "full_name": "David Lloyd George",
        "status": "Earl Lloyd-George, Prime Minister",
        "years": "1863–1945",
        "field": "pol",
        "education": "Llanystumdwy National School"
    },
    {
        "full_name": "William Ewart Gladstone",
        "status": "Prime Minister",
        "years": "1809–1898",
        "field": "pol",
        "education": "Eton College; Christ Church, Oxford"
    },
    {
        "full_name": "Benjamin Disraeli",
        "status": "Earl of Beaconsfield, Prime Minister",
        "years": "1804–1881",
        "field": "pol",
        "education": "Higham Hall School"
    },
    {
        "full_name": "Robert Peel",
        "status": "Baronet, Prime Minister",
        "years": "1788–1850",
        "field": "pol",
        "education": "Harrow School; Christ Church, Oxford"
    },
    {
        "full_name": "William Pitt the Younger",
        "status": "Prime Minister",
        "years": "1759–1806",
        "field": "pol",
        "education": "Pembroke College, Cambridge"
    },
    {
        "full_name": "Robert Walpole",
        "status": "Earl of Orford, Prime Minister",
        "years": "1676–1745",
        "field": "pol",
        "education": "Eton College; King's College, Cambridge"
    },
    {
        "full_name": "Clement Richard Attlee",
        "status": "Earl Attlee, Prime Minister",
        "years": "1883–1967",
        "field": "pol",
        "education": "Haileybury College; University College, Oxford"
    },
    {
        "full_name": "Tony Blair",
        "status": "Knight, Prime Minister",
        "years": "1953–",
        "field": "pol",
        "education": "Fettes College; St John's College, Oxford"
    },
    {
        "full_name": "John Maynard Keynes",
        "status": "Baron Keynes",
        "years": "1883–1946",
        "field": "sci",
        "education": "Eton College; King's College, Cambridge"
    },
    {
        "full_name": "George Orwell (Eric Arthur Blair)",
        "status": "None",
        "years": "1903–1950",
        "field": "lit",
        "education": "Eton College"
    },
    {
        "full_name": "Agatha Christie",
        "status": "Dame",
        "years": "1890–1976",
        "field": "lit",
        "education": "Private Education"
    },
    {
        "full_name": "John Ronald Reuel Tolkien",
        "status": "CBE",
        "years": "1892–1973",
        "field": "lit",
        "education": "King Edward's School, Birmingham; Exeter College, Oxford"
    },
    {
        "full_name": "Clive Staples Lewis",
        "status": "None",
        "years": "1898–1963",
        "field": "lit",
        "education": "Malvern College; University College, Oxford"
    },
    {
        "full_name": "Arthur Ignatius Conan Doyle",
        "status": "Knight",
        "years": "1859–1930",
        "field": "lit",
        "education": "Stonyhurst College; University of Edinburgh"
    },
    {
        "full_name": "Rudyard Kipling",
        "status": "None",
        "years": "1865–1936",
        "field": "lit",
        "education": "United Services College"
    },
    {
        "full_name": "Virginia Woolf",
        "status": "None",
        "years": "1882–1941",
        "field": "lit",
        "education": "King's College London"
    },
    {
        "full_name": "Mary Shelley",
        "status": "None",
        "years": "1797–1851",
        "field": "lit",
        "education": "Private Education"
    },
    {
        "full_name": "Lord Byron (George Gordon Byron)",
        "status": "Baron Byron",
        "years": "1788–1824",
        "field": "lit",
        "education": "Harrow School; Trinity College, Cambridge"
    },
    {
        "full_name": "William Wordsworth",
        "status": "Poet Laureate",
        "years": "1770–1850",
        "field": "lit",
        "education": "Hawkshead Grammar School; St John's College, Cambridge"
    },
    {
    "full_name": "Samuel Taylor Coleridge",
    "status": "None",
    "years": "1772–1834",
    "field": "lit",
    "education": "Christ's Hospital; Jesus College, Cambridge"
    },
    {
    "full_name": "John Keats",
    "status": "None",
    "years": "1795–1821",
    "field": "lit",
    "education": "John Clarke's School; King's College London"
    },
    {
    "full_name": "Percy Bysshe Shelley",
    "status": "None",
    "years": "1792–1822",
    "field": "lit",
    "education": "Eton College; University College, Oxford"
    },
    {
    "full_name": "Thomas Hardy",
    "status": "Order of Merit",
    "years": "1840–1928",
    "field": "lit",
    "education": "King's College London"
    },
    {
    "full_name": "Charlotte Brontë",
    "status": "None",
    "years": "1816–1855",
    "field": "lit",
    "education": "Clergy Daughters' School"
    },
    {
    "full_name": "Emily Brontë",
    "status": "None",
    "years": "1818–1848",
    "field": "lit",
    "education": "Clergy Daughters' School"
    },
    {
    "full_name": "Robert Burns",
    "status": "None",
    "years": "1759–1796",
    "field": "lit",
    "education": "Self-educated"
    },
    {
    "full_name": "Walter Scott",
    "status": "Baronet",
    "years": "1771–1832",
    "field": "lit",
    "education": "Royal High School, Edinburgh; University of Edinburgh"
    },
    {
    "full_name": "Alfred Tennyson",
    "status": "Baron Tennyson",
    "years": "1809–1892",
    "field": "lit",
    "education": "King Edward VI Grammar School; Trinity College, Cambridge"
    },
    {
    "full_name": "William Blake",
    "status": "None",
    "years": "1757–1827",
    "field": "art",
    "education": "Royal Academy of Arts"
    },
    {
    "full_name": "Joseph Mallord William Turner",
    "status": "None",
    "years": "1775–1851",
    "field": "art",
    "education": "Royal Academy of Arts"
    },
    {
    "full_name": "John Constable",
    "status": "None",
    "years": "1776–1837",
    "field": "art",
    "education": "Royal Academy of Arts"
    },
    {
    "full_name": "Charlie Chaplin",
    "status": "Knight",
    "years": "1889–1977",
    "field": "art",
    "education": "Central London District School"
    },
    {
    "full_name": "Alfred Joseph Hitchcock",
    "status": "Knight",
    "years": "1899–1980",
    "field": "art",
    "education": "Salesian College; St Ignatius' College"
    },
    {
    "full_name": "Paul McCartney",
    "status": "Knight",
    "years": "1942–",
    "field": "art",
    "education": "Liverpool Institute High School for Boys"
    },
    {
    "full_name": "George Harrison",
    "status": "MBE",
    "years": "1943–2001",
    "field": "art",
    "education": "Liverpool Institute High School for Boys"
    },
    {
    "full_name": "Ringo Starr (Richard Starkey)",
    "status": "Knight",
    "years": "1940–",
    "field": "art",
    "education": "Dingle Vale Secondary Modern School"
    },
    {
    "full_name": "David Bowie (David Robert Jones)",
    "status": "None (Declined Knighthood)",
    "years": "1947–2016",
    "field": "art",
    "education": "Ravens Wood School"
    },
    {
    "full_name": "Freddie Mercury (Farrokh Bulsara)",
    "status": "None",
    "years": "1946–1991",
    "field": "art",
    "education": "St. Peter's School, Panchgani; Ealing Art College"
    },
    {
    "full_name": "Elton John (Reginald Kenneth Dwight)",
    "status": "Knight",
    "years": "1947–",
    "field": "art",
    "education": "Pinner County Grammar School; Royal Academy of Music"
    },
    {
    "full_name": "Mick Jagger",
    "status": "Knight",
    "years": "1943–",
    "field": "art",
    "education": "Dartford Grammar School; London School of Economics"
    },
    {
    "full_name": "Keith Richards",
    "status": "None",
    "years": "1943–",
    "field": "art",
    "education": "Dartford Technical High School; Sidcup Art College"
    },
    {
    "full_name": "Eric Patrick Clapton",
    "status": "CBE",
    "years": "1945–",
    "field": "art",
    "education": "Kingston College"
    },
    {
    "full_name": "Jimmy Page",
    "status": "OBE",
    "years": "1944–",
    "field": "art",
    "education": "Sutton Art College"
    },
    {
    "full_name": "Robert Anthony Plant",
    "status": "CBE",
    "years": "1948–",
    "field": "art",
    "education": "King Edward VI Five Ways School"
    },
    {
    "full_name": "Ozzy Osbourne (John Michael Osbourne)",
    "status": "None",
    "years": "1948–",
    "field": "art",
    "education": "Prince Albert Road Junior School"
    },
    {
    "full_name": "Roger Waters",
    "status": "None",
    "years": "1943–",
    "field": "art",
    "education": "Cambridgeshire High School for Boys; Regent Street Polytechnic"
    },
    {
    "full_name": "David Gilmour",
    "status": "CBE",
    "years": "1946–",
    "field": "art",
    "education": "Cambridgeshire High School for Boys"
    },
    {
    "full_name": "Laurence Olivier",
    "status": "Baron Olivier",
    "years": "1907–1989",
    "field": "art",
    "education": "St Edward's School, Oxford; Central School of Speech and Drama"
    },
    {
    "full_name": "Michael Caine (Maurice Joseph Micklewhite)",
    "status": "Knight",
    "years": "1933–",
    "field": "art",
    "education": "Hackney Downs School"
    },
    {
    "full_name": "Sean Connery",
    "status": "Knight",
    "years": "1930–2020",
    "field": "art",
    "education": "Tollcross Primary School"
    },
    {
    "full_name": "J. K. Rowling (Joanne Rowling)",
    "status": "Companion of Honour",
    "years": "1965–",
    "field": "lit",
    "education": "Wyedean School; University of Exeter"
    },
    {
    "full_name": "Richard Branson",
    "status": "Knight",
    "years": "1950–",
    "field": "bus",
    "education": "Scaitcliffe School; Stowe School"
    },
    {
    "full_name": "Alan Sugar",
    "status": "Baron Sugar",
    "years": "1947–",
    "field": "bus",
    "education": "Brooke House Secondary School"
    },
    {
    "full_name": "James Dyson",
    "status": "Knight",
    "years": "1947–",
    "field": "bus",
    "education": "Gresham's School; Royal College of Art"
    },
    {
    "full_name": "Thomas Cook",
    "status": "None",
    "years": "1808–1892",
    "field": "bus",
    "education": "Self-educated"
    },
    {
    "full_name": "Bobby Moore",
    "status": "OBE",
    "years": "1941–1993",
    "field": "sport",
    "education": "Westbury Secondary Modern School"
    },
    {
    "full_name": "David Beckham",
    "status": "OBE",
    "years": "1975–",
    "field": "sport",
    "education": "Chingford Foundation School"
    },
    {
    "full_name": "Lewis Carl Davidson Hamilton",
    "status": "Knight",
    "years": "1985–",
    "field": "sport",
    "education": "The John Henry Newman School"
    },
    {
    "full_name": "Andy Murray",
    "status": "Knight",
    "years": "1987–",
    "field": "sport",
    "education": "Dunblane High School"
    },
    {
    "full_name": "Bobby Charlton",
    "status": "Knight",
    "years": "1937–2023",
    "field": "sport",
    "education": "Bedlington Grammar School"
    },
    {
    "full_name": "Steve Redgrave",
    "status": "Knight",
    "years": "1962–",
    "field": "sport",
    "education": "Great Marlow School"
    },
    {
    "full_name": "Chris Hoy",
    "status": "Knight",
    "years": "1976–",
    "field": "sport",
    "education": "George Watson's College; University of St Andrews; University of Edinburgh"
    },
    {
    "full_name": "Mo Farah",
    "status": "Knight",
    "years": "1983–",
    "field": "sport",
    "education": "Feltham Community College; St Mary's University, Twickenham"
    },
    {
    "full_name": "Ian Botham",
    "status": "Baron Botham",
    "years": "1955–",
    "field": "sport",
    "education": "Buckler's Mead Academy"
    },
    {
    "full_name": "Alexander Parkes",
    "status": "None",
    "years": "1813–1890",
    "field": "sci",
    "education": "Apprenticeship system"
    },
    {
    "full_name": "John Logie Baird",
    "status": "None",
    "years": "1888–1946",
    "field": "sci",
    "education": "Larchfield Academy; Royal Technical College; University of Glasgow"
    },
    {
    "full_name": "Tim Berners-Lee",
    "status": "Knight",
    "years": "1955–",
    "field": "sci",
    "education": "Emanuel School; Queen's College, Oxford"
    },
    {
    "full_name": "Francis Harry Compton Crick",
    "status": "Order of Merit",
    "years": "1916–2004",
    "field": "sci",
    "education": "Mill Hill School; University College London; Caius College, Cambridge"
    },
    {
    "full_name": "Rosalind Elsie Franklin",
    "status": "None",
    "years": "1920–1958",
    "field": "sci",
    "education": "St Paul's Girls' School; Newnham College, Cambridge"
    },
    {
    "full_name": "Joseph Lister",
    "status": "Baron Lister",
    "years": "1827–1912",
    "field": "sci",
    "education": "Grove House School; University College London"
    },
    {
    "full_name": "Edward Jenner",
    "status": "None",
    "years": "1749–1823",
    "field": "sci",
    "education": "Katharine Lady Berkeley's School; St George's, University of London"
    },
    {
    "full_name": "David Attenborough",
    "status": "Knight",
    "years": "1926–",
    "field": "etc",
    "education": "Wyggeston Grammar School for Boys; Clare College, Cambridge"
    }
    ]

# ------------------------ prepare -------------------------

from pprint import pp, pprint
from collections import defaultdict
from enum import IntEnum

class Field(IntEnum):
    ETC = 0
    LIT = 1
    SCI = 2
    ART = 3
    POL = 4
    BUS = 5
    SPO = 6

class Edu(IntEnum):
    ETC = 0
    OXF = 1
    CAM = 2

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


# ----------------------------------------------------------
part("1. сколько из школ и вузов?")
# ----------------------------------------------------------

oxford = cambridge = others = eton = 0
for prm in famous:
    edu = prm['education']
    if 'Oxford' in edu: oxford += 1
    if 'Cambridge' in edu: cambridge += 1
    if 'Oxford' not in edu and 'Cambridge' not in edu: others += 1
    if 'Eton' in edu: eton += 1

print(f"Colleges: {oxford=}, {cambridge=}, {others=}, {eton=}\n")

fromto = { (edu.value, field.value): 0 for edu in Edu for field in Field }

# ~ print(fromto)

fields = "etc,lit,sci,art,pol,bus,spo".split(',')

# ~ print(fields)

for person in famous:
    status = person['status']
    field = person['field']
    educ = person['education']

    edu = 0
    if 'Oxford' in educ:    edu = 1
    if 'Cambridge' in educ: edu = 2
    if 'Oxford' not in educ and 'Cambridge' not in educ: edu = 0

    nfield = 0
    if 'lit' in field: nfield = 1
    if 'sci' in field: nfield = 2
    if 'art' in field: nfield = 3
    if 'pol' in field: nfield = 4
    if 'bus' in field: nfield = 5
    if 'spo' in field: nfield = 6

    fromto[(edu,nfield)] += 1

# ~ pprint(fromto)

print("             etc       oxford    cambridge")
for lnum, lname in enumerate(fields):
    print(f"{lname:5}", end="")
    for cnum in range(3):
        print(f"{fromto[(cnum, lnum)]:10}", end="")
    print()
print()


# ~ Colleges: oxford=12, cambridge=18, others=71, eton=6

             # ~ etc       oxford    cambridge
# ~ etc           3         0         1
# ~ lit          16         3         4
# ~ sci          10         2         9
# ~ art          20         1         2
# ~ pol           9         5         2
# ~ bus           4         0         0
# ~ spo           9         0         0


# -----------------------------------------------------------------
part("The End.")
# -----------------------------------------------------------------


