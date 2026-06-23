#!/usr/bin/env python

# Mikhail (myke) Kolodin, 2026
# uk-great-many.py
# 2026-06-23 2026-06-23 2.1
# великие британцы

# ~ дай список 100 самых знаменитых людей Великобритании за последние 300 лет;
# ~ для каждого укажи полное имя, статус (титул, напр., барон, если есть), годы рождения и смерти, одно основное направление деятельности из списка (lit, sci, art, pol, bus, spo, etc), образование (школа или колледж, институт или университет - какие именно);
# ~ вывод в формате list[list] для python,
# ~ причём список верхнего уровня соответствует людям,
# ~ а вложенный список имеет значения, соответственно:
# ~ 0 - name: полное имя,
# ~ 1 - status: статус,
# ~ 2 - birth: год рождения,
# ~ 3 - death: год смерти (или 'alive', если жив),
# ~ 4 - field: деятельность (только одна, главная),
# ~ 5 - edu: образование,
# ~ причём все ключи и значения только по-английски;
# ~ деятельности обозначены, соответственно:
# ~ ключ: lit, sci, art, pol, bus, spo, etc 
# ~ значение: литература, наука, искусство, бизнес, спорт, прочее

# ------------------------ data -------------------------

famous_100 = [
    ["Winston Churchill", "Sir", 1874, 1965, "pol", "Harrow School, Royal Military College, Sandhurst"],
    ["Isaac Newton", "Sir", 1643, 1727, "sci", "The King's School, Grantham, Trinity College, Cambridge"],
    ["Charles Darwin", "None", 1809, 1882, "sci", "Shrewsbury School, University of Edinburgh, Christ's College, Cambridge"],
    ["Queen Victoria", "Her Majesty", 1819, 1901, "pol", "Privately educated"],
    ["Queen Elizabeth II", "Her Majesty", 1926, 2022, "pol", "Privately educated"],
    ["King Charles III", "His Majesty", 1948, "alive", "pol", "Gordonstoun School, Trinity College, Cambridge"],
    ["Margaret Thatcher", "Baroness", 1925, 2013, "pol", "Kesteven and Grantham Girls' School, Somerville College, Oxford"],
    ["Stephen Hawking", "None", 1942, 2018, "sci", "St Albans School, University College, Oxford, Trinity Hall, Cambridge"],
    ["Alan Turing", "None", 1912, 1954, "sci", "Sherborne School, King's College, Cambridge, Princeton University"],
    ["Alexander Fleming", "Sir", 1881, 1955, "sci", "Kilmarnock Academy, St Mary's Hospital Medical School"],
    ["Adam Smith", "None", 1723, 1790, "sci", "Burgh School of Kirkcaldy, University of Glasgow, Balliol College, Oxford"],
    ["John Maynard Keynes", "Baron", 1883, 1946, "sci", "Eton College, King's College, Cambridge"],
    ["Charles Dickens", "None", 1812, 1870, "lit", "Wellington House Academy"],
    ["George Orwell", "None", 1903, 1950, "lit", "Eton College"],
    ["Jane Austen", "None", 1775, 1817, "lit", "Reading Abbey Girls' School"],
    ["J.K. Rowling", "CH", 1965, "alive", "lit", "Wyedean School, University of Exeter"],
    ["John Lennon", "MBE", 1940, 1980, "art", "Quarry Bank High School, Liverpool College of Art"],
    ["Paul McCartney", "Sir", 1942, "alive", "art", "Liverpool Institute High School for Boys"],
    ["David Bowie", "None", 1947, 2016, "art", "Bromley Technical High School"],
    ["Freddie Mercury", "None", 1946, 1991, "art", "St. Peter's School, Panchgani, Ealing Art College"],
    ["Elton John", "Sir", 1947, "alive", "art", "Pinner County Grammar School, Royal Academy of Music"],
    ["Charlie Chaplin", "Sir", 1889, 1977, "art", "Central London District School"],
    ["Alfred Hitchcock", "Sir", 1899, 1980, "art", "Salesian College, St Ignatius' College"],
    ["Diana, Princess of Wales", "Her Royal Highness", 1961, 1997, "etc", "West Heath Earl's Court School, Institut Alpin Videmanette"],
    ["Florence Nightingale", "OM", 1820, 1910, "sci", "Privately educated"],
    ["James Cook", "Captain", 1728, 1779, "etc", "Great Ayton Postgate School"],
    ["Horatio Nelson", "Viscount", 1758, 1805, "pol", "Paston Grammar School, King Edward VI Grammar School"],
    ["Arthur Wellesley", "Duke of Wellington", 1769, 1852, "pol", "Eton College"],
    ["Tony Blair", "Sir", 1953, "alive", "pol", "Fettes College, St John's College, Oxford"],
    ["David Beckham", "OBE", 1975, "alive", "spo", "Chingford Foundation School"],
    ["Lewis Hamilton", "Sir", 1985, "alive", "spo", "The John Henry Newman School"],
    ["Bobby Charlton", "Sir", 1937, 2023, "spo", "Bedlington Grammar School"],
    ["Andy Murray", "Sir", 1987, "alive", "spo", "Dunblane High School"],
    ["Tim Berners-Lee", "Sir", 1955, "alive", "sci", "Emanuel School, Queen's College, Oxford"],
    ["Richard Branson", "Sir", 1950, "alive", "bus", "Scaitcliffe School, Stowe School"],
    ["Alan Sugar", "Baron", 1947, "alive", "bus", "Brooke House Secondary School"],
    ["James Dyson", "Sir", 1947, "alive", "bus", "Gresham's School, Royal College of Art"],
    ["Agatha Christie", "Dame", 1890, 1976, "lit", "Privately educated"],
    ["J.R.R. Tolkien", "CBE", 1892, 1973, "lit", "King Edward's School, Birmingham, Exeter College, Oxford"],
    ["C.S. Lewis", "None", 1898, 1963, "lit", "Malvern College, University College, Oxford"],
    ["Mary Shelley", "None", 1797, 1851, "lit", "Privately educated"],
    ["Lord Byron", "Baron", 1788, 1824, "lit", "Harrow School, Trinity College, Cambridge"],
    ["William Wordsworth", "None", 1770, 1850, "lit", "Hawkshead Grammar School, St John's College, Cambridge"],
    ["Thomas Hardy", "OM", 1840, 1928, "lit", "Mr Last's Academy"],
    ["Virginia Woolf", "None", 1882, 1941, "lit", "King's College London Ladies' Department"],
    ["Arthur Conan Doyle", "Sir", 1859, 1930, "lit", "Stonyhurst College, University of Edinburgh"],
    ["Rudyard Kipling", "None", 1865, 1936, "lit", "United Services College"],
    ["H.G. Wells", "None", 1866, 1946, "lit", "Midhurst Grammar School, Royal College of Science"],
    ["James Watt", "None", 1736, 1819, "sci", "Greenock Grammar School, University of Glasgow"],
    ["Michael Faraday", "None", 1791, 1867, "sci", "Privately educated"],
    ["Joseph Lister", "Baron", 1827, 1912, "sci", "Grove House School, University College London"],
    ["Ernest Rutherford", "Baron", 1871, 1937, "sci", "Nelson College, Canterbury College, Trinity College, Cambridge"],
    ["Alexander Graham Bell", "None", 1847, 1922, "sci", "Royal High School, Edinburgh, University of Edinburgh"],
    ["William Thomson", "Baron Kelvin", 1824, 1907, "sci", "University of Glasgow, Peterhouse, Cambridge"],
    ["Edward Jenner", "None", 1749, 1823, "sci", "Katherine Lady Berkeley's School"],
    ["John Dalton", "None", 1766, 1844, "sci", "Pardshow Hall School"],
    ["Francis Crick", "OM", 1916, 2004, "sci", "Northampton School for Boys, University College London, Caius College, Cambridge"],
    ["Rosalind Franklin", "None", 1920, 1958, "sci", "St Paul's Girls' School, Newnham College, Cambridge"],
    ["Ada Lovelace", "Countess", 1815, 1852, "sci", "Privately educated"],
    ["William Pitt the Younger", "None", 1759, 1806, "pol", "Pembroke College, Cambridge"],
    ["Benjamin Disraeli", "Earl of Beaconsfield", 1804, 1881, "pol", "Higham Hall School"],
    ["William Gladstone", "None", 1809, 1898, "pol", "Eton College, Christ Church, Oxford"],
    ["Robert Peel", "Sir", 1788, 1850, "pol", "Harrow School, Christ Church, Oxford"],
    ["Clement Attlee", "Earl", 1883, 1967, "pol", "Haileybury College, University College, Oxford"],
    ["Harold Wilson", "Baron", 1916, 1995, "pol", "Wirral Grammar School, Jesus College, Oxford"],
    ["Thomas Paine", "None", 1737, 1809, "pol", "Thetford Grammar School"],
    ["Mary Wollstonecraft", "None", 1759, 1797, "lit", "Privately educated"],
    ["Thomas Malthus", "None", 1766, 1834, "sci", "Jesus College, Cambridge"],
    ["David Ricardo", "None", 1772, 1823, "sci", "Privately educated"],
    ["John Stuart Mill", "None", 1806, 1873, "sci", "Privately educated"],
    ["Robert Stephenson", "None", 1803, 1859, "sci", "Bruce Castle School, University of Edinburgh"],
    ["Isambard Kingdom Brunel", "None", 1806, 1859, "sci", "University of Caen, Lycée Henri-IV"],
    ["William Blake", "None", 1757, 1827, "art", "Pars' Drawing School, Royal Academy of Arts"],
    ["J.M.W. Turner", "None", 1775, 1851, "art", "Royal Academy of Arts"],
    ["John Constable", "None", 1776, 1837, "art", "Royal Academy of Arts"],
    ["Laurence Olivier", "Baron", 1907, 1989, "art", "St Edward's School, Oxford, Central School of Speech and Drama"],
    ["Vivien Leigh", "None", 1913, 1967, "art", "Woldingham School, Royal Academy of Dramatic Art"],
    ["Cary Grant", "None", 1904, 1986, "art", "Fairfield Grammar School"],
    ["Sean Connery", "Sir", 1930, 2020, "art", "Tollcross Primary School"],
    ["Michael Caine", "Sir", 1933, "alive", "art", "Hackney Downs School"],
    ["Mick Jagger", "Sir", 1943, "alive", "art", "Dartford Grammar School, London School of Economics"],
    ["Keith Richards", "None", 1943, "alive", "art", "Dartford Technical High School, Sidcup Art College"],
    ["Eric Clapton", "CBE", 1945, "alive", "art", "Kingston College of Art"],
    ["Ozzy Osbourne", "None", 1948, "alive", "art", "Prince Albert School"],
    ["Phil Collins", "LVO", 1951, "alive", "art", "Chiswick County Grammar School for Boys, Barbara Speake Stage School"],
    ["Sting", "CBE", 1951, "alive", "art", "St Cuthbert's Grammar School, Northern Counties College of Education"],
    ["Amy Winehouse", "None", 1983, 2011, "art", "Sylvia Young Theatre School, BRIT School"],
    ["Adele Adkins", "MBE", 1988, "alive", "art", "BRIT School"],
    ["Ed Sheeran", "MBE", 1991, "alive", "art", "Thomas Mills High School, Academy of Contemporary Music"],
    ["David Attenborough", "Sir", 1926, "alive", "sci", "Wyggeston Grammar School for Boys, Clare College, Cambridge"],
    ["George Stephenson", "None", 1781, 1848, "sci", "Privately educated"],
    ["John Logie Baird", "None", 1888, 1946, "sci", "Larchfield Academy, Royal Technical College, University of Glasgow"],
    ["Alexander MacKenzie", "Sir", 1764, 1820, "etc", "Privately educated"],
    ["David Livingstone", "None", 1813, 1873, "etc", "Chiswick Medical College, University of Glasgow"],
    ["Robert Falcon Scott", "Captain", 1868, 1912, "etc", "Stubbington House School"],
    ["Ernest Shackleton", "Sir", 1874, 1922, "etc", "Dulwich College"],
    ["George Mallory", "None", 1886, 1924, "etc", "Winchester College, Magdalene College, Cambridge"],
    ["Roger Bannister", "Sir", 1929, 2018, "spo", "City of Bath Boys' School, Exeter College, Oxford, Merton College, Oxford"],
    ["Ian Fleming", "None", 1908, 1964, "lit", "Eton College, Royal Military College, Sandhurst, University of Munich"],
    ["Roald Dahl", "None", 1916, 1990, "lit", "Repton School"],
    ["George III", "His Majesty", 1738, 1820, "pol", "Privately educated"],
    ["George IV", "His Majesty", 1762, 1830, "pol", "Privately educated"],
    ["William IV", "His Majesty", 1765, 1837, "pol", "Privately educated"],
    ["Edward VII", "His Majesty", 1841, 1910, "pol", "Privately educated, Christ Church, Oxford, Trinity College, Cambridge"],
    ["George V", "His Majesty", 1865, 1936, "pol", "Privately educated"],
    ["Edward VIII", "His Royal Highness", 1894, 1972, "pol", "Magdalen College, Oxford"],
    ["George VI", "His Majesty", 1895, 1952, "pol", "Trinity College, Cambridge"],
    ["Prince Philip", "Prince", 1921, 2021, "pol", "Gordonstoun School"],
    ["Prince William", "Prince", 1982, "alive", "pol", "Eton College, University of St Andrews"],
    ["Prince Harry", "Prince", 1984, "alive", "pol", "Eton College, Royal Military Academy Sandhurst"],
    ["Theresa May", "Baroness", 1956, "alive", "pol", "St Hugh's College, Oxford"],
    ["Boris Johnson", "None", 1964, "alive", "pol", "Eton College, Balliol College, Oxford"],
    ["Rishi Sunak", "None", 1980, "alive", "pol", "Winchester College, Lincoln College, Oxford, Stanford University"],
    ["Keir Starmer", "Sir", 1962, "alive", "pol", "Reigate Grammar School, University of Leeds, St Edmund Hall, Oxford"],
    ["Gordon Brown", "None", 1951, "alive", "pol", "Kirkcaldy High School, University of Edinburgh"],
    ["John Major", "Sir", 1943, "alive", "pol", "Rutlish School"],
    ["James Callaghan", "Baron", 1912, 2005, "pol", "Portsmouth Northern Grammar School"],
    ["Edward Heath", "Sir", 1916, 2005, "pol", "Chatham House Grammar School, Balliol College, Oxford"],
    ["Alec Douglas-Home", "Baron", 1903, 1995, "pol", "Eton College, Christ Church, Oxford"]
    ]

# ----------------------------------------------------

famous_200 = [
    ["Winston Churchill", "Sir", 1874, 1965, "pol", "Harrow School, Royal Military College, Sandhurst"],
    ["Isaac Newton", "Sir", 1643, 1727, "sci", "The King's School, Grantham, Trinity College, Cambridge"],
    ["Charles Darwin", "None", 1809, 1882, "sci", "Shrewsbury School, University of Edinburgh, Christ's College, Cambridge"],
    ["Queen Victoria", "Her Majesty", 1819, 1901, "pol", "Privately educated"],
    ["Queen Elizabeth II", "Her Majesty", 1926, 2022, "pol", "Privately educated"],
    ["King Charles III", "His Majesty", 1948, "alive", "pol", "Gordonstoun School, Trinity College, Cambridge"],
    ["Margaret Thatcher", "Baroness", 1925, 2013, "pol", "Kesteven and Grantham Girls' School, Somerville College, Oxford"],
    ["Stephen Hawking", "None", 1942, 2018, "sci", "St Albans School, University College, Oxford, Trinity Hall, Cambridge"],
    ["Alan Turing", "None", 1912, 1954, "sci", "Sherborne School, King's College, Cambridge, Princeton University"],
    ["Alexander Fleming", "Sir", 1881, 1955, "sci", "Kilmarnock Academy, St Mary's Hospital Medical School"],
    ["Adam Smith", "None", 1723, 1790, "sci", "Burgh School of Kirkcaldy, University of Glasgow, Balliol College, Oxford"],
    ["John Maynard Keynes", "Baron", 1883, 1946, "sci", "Eton College, King's College, Cambridge"],
    ["Charles Dickens", "None", 1812, 1870, "lit", "Wellington House Academy"],
    ["George Orwell", "None", 1903, 1950, "lit", "Eton College"],
    ["Jane Austen", "None", 1775, 1817, "lit", "Reading Abbey Girls' School"],
    ["J.K. Rowling", "CH", 1965, "alive", "lit", "Wyedean School, University of Exeter"],
    ["John Lennon", "MBE", 1940, 1980, "art", "Quarry Bank High School, Liverpool College of Art"],
    ["Paul McCartney", "Sir", 1942, "alive", "art", "Liverpool Institute High School for Boys"],
    ["David Bowie", "None", 1947, 2016, "art", "Bromley Technical High School"],
    ["Freddie Mercury", "None", 1946, 1991, "art", "St. Peter's School, Panchgani, Ealing Art College"],
    ["Elton John", "Sir", 1947, "alive", "art", "Pinner County Grammar School, Royal Academy of Music"],
    ["Charlie Chaplin", "Sir", 1889, 1977, "art", "Central London District School"],
    ["Alfred Hitchcock", "Sir", 1899, 1980, "art", "Salesian College, St Ignatius' College"],
    ["Diana, Princess of Wales", "Her Royal Highness", 1961, 1997, "etc", "West Heath Earl's Court School, Institut Alpin Videmanette"],
    ["Florence Nightingale", "OM", 1820, 1910, "sci", "Privately educated"],
    ["James Cook", "Captain", 1728, 1779, "etc", "Great Ayton Postgate School"],
    ["Horatio Nelson", "Viscount", 1758, 1805, "pol", "Paston Grammar School, King Edward VI Grammar School"],
    ["Arthur Wellesley", "Duke of Wellington", 1769, 1852, "pol", "Eton College"],
    ["Tony Blair", "Sir", 1953, "alive", "pol", "Fettes College, St John's College, Oxford"],
    ["David Beckham", "OBE", 1975, "alive", "spo", "Chingford Foundation School"],
    ["Lewis Hamilton", "Sir", 1985, "alive", "spo", "The John Henry Newman School"],
    ["Bobby Charlton", "Sir", 1937, 2023, "spo", "Bedlington Grammar School"],
    ["Andy Murray", "Sir", 1987, "alive", "spo", "Dunblane High School"],
    ["Tim Berners-Lee", "Sir", 1955, "alive", "sci", "Emanuel School, Queen's College, Oxford"],
    ["Richard Branson", "Sir", 1950, "alive", "bus", "Scaitcliffe School, Stowe School"],
    ["Alan Sugar", "Baron", 1947, "alive", "bus", "Brooke House Secondary School"],
    ["James Dyson", "Sir", 1947, "alive", "bus", "Gresham's School, Royal College of Art"],
    ["Agatha Christie", "Dame", 1890, 1976, "lit", "Privately educated"],
    ["J.R.R. Tolkien", "CBE", 1892, 1973, "lit", "King Edward's School, Birmingham, Exeter College, Oxford"],
    ["C.S. Lewis", "None", 1898, 1963, "lit", "Malvern College, University College, Oxford"],
    ["Mary Shelley", "None", 1797, 1851, "lit", "Privately educated"],
    ["Lord Byron", "Baron", 1788, 1824, "lit", "Harrow School, Trinity College, Cambridge"],
    ["William Wordsworth", "None", 1770, 1850, "lit", "Hawkshead Grammar School, St John's College, Cambridge"],
    ["Thomas Hardy", "OM", 1840, 1928, "lit", "Mr Last's Academy"],
    ["Virginia Woolf", "None", 1882, 1941, "lit", "King's College London Ladies' Department"],
    ["Arthur Conan Doyle", "Sir", 1859, 1930, "lit", "Stonyhurst College, University of Edinburgh"],
    ["Rudyard Kipling", "None", 1865, 1936, "lit", "United Services College"],
    ["H.G. Wells", "None", 1866, 1946, "lit", "Midhurst Grammar School, Royal College of Science"],
    ["James Watt", "None", 1736, 1819, "sci", "Greenock Grammar School, University of Glasgow"],
    ["Michael Faraday", "None", 1791, 1867, "sci", "Privately educated"],
    ["Joseph Lister", "Baron", 1827, 1912, "sci", "Grove House School, University College London"],
    ["Ernest Rutherford", "Baron", 1871, 1937, "sci", "Nelson College, Canterbury College, Trinity College, Cambridge"],
    ["Alexander Graham Bell", "None", 1847, 1922, "sci", "Royal High School, Edinburgh, University of Edinburgh"],
    ["William Thomson", "Baron Kelvin", 1824, 1907, "sci", "University of Glasgow, Peterhouse, Cambridge"],
    ["Edward Jenner", "None", 1749, 1823, "sci", "Katherine Lady Berkeley's School"],
    ["John Dalton", "None", 1766, 1844, "sci", "Pardshow Hall School"],
    ["Francis Crick", "OM", 1916, 2004, "sci", "Northampton School for Boys, University College London, Caius College, Cambridge"],
    ["Rosalind Franklin", "None", 1920, 1958, "sci", "St Paul's Girls' School, Newnham College, Cambridge"],
    ["Ada Lovelace", "Countess", 1815, 1852, "sci", "Privately educated"],
    ["William Pitt the Younger", "None", 1759, 1806, "pol", "Pembroke College, Cambridge"],
    ["Benjamin Disraeli", "Earl of Beaconsfield", 1804, 1881, "pol", "Higham Hall School"],
    ["William Gladstone", "None", 1809, 1898, "pol", "Eton College, Christ Church, Oxford"],
    ["Robert Peel", "Sir", 1788, 1850, "pol", "Harrow School, Christ Church, Oxford"],
    ["Clement Attlee", "Earl", 1883, 1967, "pol", "Haileybury College, University College, Oxford"],
    ["Harold Wilson", "Baron", 1916, 1995, "pol", "Wirral Grammar School, Jesus College, Oxford"],
    ["Thomas Paine", "None", 1737, 1809, "pol", "Thetford Grammar School"],
    ["Mary Wollstonecraft", "None", 1759, 1797, "lit", "Privately educated"],
    ["Thomas Malthus", "None", 1766, 1834, "sci", "Jesus College, Cambridge"],
    ["David Ricardo", "None", 1772, 1823, "sci", "Privately educated"],
    ["John Stuart Mill", "None", 1806, 1873, "sci", "Privately educated"],
    ["Robert Stephenson", "None", 1803, 1859, "sci", "Bruce Castle School, University of Edinburgh"],
    ["Isambard Kingdom Brunel", "None", 1806, 1859, "sci", "University of Caen, Lycée Henri-IV"],
    ["William Blake", "None", 1757, 1827, "art", "Pars' Drawing School, Royal Academy of Arts"],
    ["J.M.W. Turner", "None", 1775, 1851, "art", "Royal Academy of Arts"],
    ["John Constable", "None", 1776, 1837, "art", "Royal Academy of Arts"],
    ["Laurence Olivier", "Baron", 1907, 1989, "art", "St Edward's School, Oxford, Central School of Speech and Drama"],
    ["Vivien Leigh", "None", 1913, 1967, "art", "Woldingham School, Royal Academy of Dramatic Art"],
    ["Cary Grant", "None", 1904, 1986, "art", "Fairfield Grammar School"],
    ["Sean Connery", "Sir", 1930, 2020, "art", "Tollcross Primary School"],
    ["Michael Caine", "Sir", 1933, "alive", "art", "Hackney Downs School"],
    ["Mick Jagger", "Sir", 1943, "alive", "art", "Dartford Grammar School, London School of Economics"],
    ["Keith Richards", "None", 1943, "alive", "art", "Dartford Technical High School, Sidcup Art College"],
    ["Eric Clapton", "CBE", 1945, "alive", "art", "Kingston College of Art"],
    ["Ozzy Osbourne", "None", 1948, "alive", "art", "Prince Albert School"],
    ["Phil Collins", "LVO", 1951, "alive", "art", "Chiswick County Grammar School for Boys, Barbara Speake Stage School"],
    ["Sting", "CBE", 1951, "alive", "art", "St Cuthbert's Grammar School, Northern Counties College of Education"],
    ["Amy Winehouse", "None", 1983, 2011, "art", "Sylvia Young Theatre School, BRIT School"],
    ["Adele Adkins", "MBE", 1988, "alive", "art", "BRIT School"],
    ["Ed Sheeran", "MBE", 1991, "alive", "art", "Thomas Mills High School, Academy of Contemporary Music"],
    ["David Attenborough", "Sir", 1926, "alive", "sci", "Wyggeston Grammar School for Boys, Clare College, Cambridge"],
    ["George Stephenson", "None", 1781, 1848, "sci", "Privately educated"],
    ["John Logie Baird", "None", 1888, 1946, "sci", "Larchfield Academy, Royal Technical College, University of Glasgow"],
    ["Alexander MacKenzie", "Sir", 1764, 1820, "etc", "Privately educated"],
    ["David Livingstone", "None", 1813, 1873, "etc", "Chiswick Medical College, University of Glasgow"],
    ["Robert Falcon Scott", "Captain", 1868, 1912, "etc", "Stubbington House School"],
    ["Ernest Shackleton", "Sir", 1874, 1922, "etc", "Dulwich College"],
    ["George Mallory", "None", 1886, 1924, "etc", "Winchester College, Magdalene College, Cambridge"],
    ["Roger Bannister", "Sir", 1929, 2018, "spo", "City of Bath Boys' School, Exeter College, Oxford, Merton College, Oxford"],
    ["Ian Fleming", "None", 1908, 1964, "lit", "Eton College, Royal Military College, Sandhurst, University of Munich"],
    ["Roald Dahl", "None", 1916, 1990, "lit", "Repton School"],
    ["George III", "His Majesty", 1738, 1820, "pol", "Privately educated"],
    ["George IV", "His Majesty", 1762, 1830, "pol", "Privately educated"],
    ["William IV", "His Majesty", 1765, 1837, "pol", "Privately educated"],
    ["Edward VII", "His Majesty", 1841, 1910, "pol", "Privately educated, Christ Church, Oxford, Trinity College, Cambridge"],
    ["George V", "His Majesty", 1865, 1936, "pol", "Privately educated"],
    ["Edward VIII", "His Royal Highness", 1894, 1972, "pol", "Magdalen College, Oxford"],
    ["George VI", "His Majesty", 1895, 1952, "pol", "Trinity College, Cambridge"],
    ["Prince Philip", "Prince", 1921, 2021, "pol", "Gordonstoun School"],
    ["Prince William", "Prince", 1982, "alive", "pol", "Eton College, University of St Andrews"],
    ["Prince Harry", "Prince", 1984, "alive", "pol", "Eton College, Royal Military Academy Sandhurst"],
    ["Theresa May", "Baroness", 1956, "alive", "pol", "St Hugh's College, Oxford"],
    ["Boris Johnson", "None", 1964, "alive", "pol", "Eton College, Balliol College, Oxford"],
    ["Rishi Sunak", "None", 1980, "alive", "pol", "Winchester College, Lincoln College, Oxford, Stanford University"],
    ["Keir Starmer", "Sir", 1962, "alive", "pol", "Reigate Grammar School, University of Leeds, St Edmund Hall, Oxford"],
    ["Gordon Brown", "None", 1951, "alive", "pol", "Kirkcaldy High School, University of Edinburgh"],
    ["John Major", "Sir", 1943, "alive", "pol", "Rutlish School"],
    ["James Callaghan", "Baron", 1912, 2005, "pol", "Portsmouth Northern Grammar School"],
    ["Edward Heath", "Sir", 1916, 2005, "pol", "Chatham House Grammar School, Balliol College, Oxford"],
    ["Alec Douglas-Home", "Baron", 1903, 1995, "pol", "Eton College, Christ Church, Oxford"],
    ["Robert Walpole", "Sir", 1676, 1745, "pol", "Eton College, King's College, Cambridge"],
    ["Thomas Gainsborough", "None", 1727, 1788, "art", "Sudbury Grammar School"],
    ["Joshua Reynolds", "Sir", 1723, 1792, "art", "Plympton Grammar School"],
    ["Samuel Johnson", "None", 1709, 1784, "lit", "Lichfield Grammar School, Pembroke College, Oxford"],
    ["Edward Gibbon", "None", 1737, 1794, "lit", "Westminster School, Magdalen College, Oxford"],
    ["Robert Burns", "None", 1759, 1796, "lit", "Privately educated"],
    ["Walter Scott", "Sir", 1771, 1832, "lit", "Royal High School, Edinburgh, University of Edinburgh"],
    ["Percy Bysshe Shelley", "None", 1792, 1822, "lit", "Eton College, University College, Oxford"],
    ["John Keats", "None", 1795, 1821, "lit", "John Clarke's School"],
    ["Charlotte Bronte", "None", 1816, 1855, "lit", "Clergy Daughters' School, Cowan Bridge"],
    ["Emily Bronte", "None", 1818, 1848, "lit", "Clergy Daughters' School, Cowan Bridge"],
    ["George Eliot", "None", 1819, 1880, "lit", "Privately educated"],
    ["Lewis Carroll", "None", 1832, 1898, "lit", "Rugby School, Christ Church, Oxford"],
    ["Robert Louis Stevenson", "None", 1850, 1894, "lit", "Edinburgh Academy, University of Edinburgh"],
    ["Oscar Wilde", "None", 1854, 1900, "lit", "Portora Royal School, Trinity College Dublin, Magdalen College, Oxford"],
    ["George Bernard Shaw", "None", 1856, 1950, "lit", "Privately educated"],
    ["T.S. Eliot", "OM", 1888, 1965, "lit", "Smith Academy, Harvard University, Merton College, Oxford"],
    ["Salman Rushdie", "Sir", 1947, "alive", "lit", "Rugby School, King's College, Cambridge"],
    ["Doris Lessing", "CH", 1919, 2013, "lit", "Privately educated"],
    ["Joseph Priestley", "None", 1733, 1804, "sci", "Daventry Academy"],
    ["Humphry Davy", "Sir", 1778, 1829, "sci", "Truro Grammar School"],
    ["Charles Babbage", "None", 1791, 1871, "sci", "Trinity College, Cambridge, Peterhouse, Cambridge"],
    ["James Clerk Maxwell", "None", 1831, 1879, "sci", "Edinburgh Academy, University of Edinburgh, Trinity College, Cambridge"],
    ["J.J. Thomson", "Sir", 1856, 1940, "sci", "Owens College, Trinity College, Cambridge"],
    ["James Chadwick", "Sir", 1891, 1974, "sci", "University of Manchester, Gonville and Caius College, Cambridge"],
    ["Paul Dirac", "OM", 1902, 1984, "sci", "Merchant Venturers' Technical College, University of Bristol, St John's College, Cambridge"],
    ["John Cockcroft", "Sir", 1897, 1967, "sci", "University of Manchester, St John's College, Cambridge"],
    ["Dorothy Hodgkin", "OM", 1910, 1994, "sci", "Sir John Leman High School, Somerville College, Oxford, Newnham College, Cambridge"],
    ["Peter Higgs", "CH", 1929, 2024, "sci", "Cotham Grammar School, King's College London"],
    ["William Cavendish", "Duke of Devonshire", 1720, 1764, "pol", "Privately educated"],
    ["Charles Watson-Wentworth", "Marquess of Rockingham", 1730, 1782, "pol", "Westminster School"],
    ["Lord North", "Earl of Guilford", 1732, 1792, "pol", "Eton College, Trinity College, Oxford"],
    ["William Wyndham Grenville", "Baron Grenville", 1759, 1834, "pol", "Eton College, Christ Church, Oxford"],
    ["Spencer Perceval", "None", 1762, 1812, "pol", "Harrow School, Trinity College, Cambridge"],
    ["Lord Liverpool", "Earl of Liverpool", 1770, 1828, "pol", "Charterhouse School, Christ Church, Oxford"],
    ["George Canning", "None", 1770, 1827, "pol", "Eton College, Christ Church, Oxford"],
    ["Lord Melbourne", "Viscount", 1779, 1848, "pol", "Eton College, Trinity College, Cambridge"],
    ["Lord Palmerston", "Viscount", 1784, 1865, "pol", "Harrow School, University of Edinburgh, St John's College, Cambridge"],
    ["Lord Salisbury", "Marquess of Salisbury", 1830, 1903, "pol", "Eton College, Christ Church, Oxford"],
    ["Arthur Balfour", "Earl of Balfour", 1848, 1930, "pol", "Eton College, Trinity College, Cambridge"],
    ["H.H. Asquith", "Earl of Oxford and Asquith", 1852, 1928, "pol", "Huddersfield College, Balliol College, Oxford"],
    ["David Lloyd George", "Earl", 1863, 1945, "pol", "Llanystumdwy National School"],
    ["Stanley Baldwin", "Earl Baldwin of Bewdley", 1867, 1947, "pol", "Harrow School, Trinity College, Cambridge"],
    ["Neville Chamberlain", "None", 1869, 1940, "pol", "Rugby School, Mason Science College"],
    ["Anthony Eden", "Earl of Avon", 1897, 1977, "pol", "Eton College, Christ Church, Oxford"],
    ["Josiah Wedgwood", "None", 1730, 1795, "bus", "Privately educated"],
    ["Thomas Cook", "None", 1808, 1892, "bus", "Privately educated"],
    ["William Lever", "Viscount Leverhulme", 1851, 1925, "bus", "Bolton Church Institute"],
    ["Thomas Lipton", "Sir", 1848, 1931, "bus", "Privately educated"],
    ["John Cadbury", "None", 1801, 1889, "bus", "Privately educated"],
    ["Henry Royce", "Sir", 1863, 1933, "bus", "Privately educated"],
    ["Charles Rolls", "None", 1877, 1910, "bus", "Eton College, Trinity College, Cambridge"],
    ["Anita Roddick", "Dame", 1942, 2007, "bus", "Maude Allen Secondary Modern School, Newton Park College"],
    ["James Hunt", "None", 1947, 1993, "spo", "Wellington College"],
    ["Jackie Stewart", "Sir", 1939, "alive", "spo", "Dumbarton Academy"],
    ["Stirling Moss", "Sir", 1929, 2020, "spo", "Shrewsbury House School"],
    ["George Best", "None", 1946, 2005, "spo", "Grosvenor High School"],
    ["Gary Lineker", "OBE", 1960, "alive", "spo", "City of Leicester Boys' Grammar School"],
    ["Wayne Rooney", "None", 1985, "alive", "spo", "De La Salle School"],
    ["Harry Kane", "MBE", 1993, "alive", "spo", "Chingford Foundation School"],
    ["Steve Redgrave", "Sir", 1962, "alive", "spo", "Great Marlow School"],
    ["Chris Hoy", "Sir", 1976, "alive", "spo", "George Watson's College, University of St Andrews, University of Edinburgh"],
    ["Mo Farah", "Sir", 1983, "alive", "spo", "Feltham Community College"],
    ["Bradley Wiggins", "Sir", 1980, "alive", "spo", "St Augustine's Church of England High School"],
    ["Ian Botham", "Baron", 1955, "alive", "spo", "Buckler's Mead Community School"],
    ["Nick Faldo", "Sir", 1957, "alive", "spo", "Welwyn Garden City Grammar School"],
    ["Lennox Lewis", "CBE", 1965, "alive", "spo", "Cameron Heights Collegiate Institute"],
    ["Ronnie O'Sullivan", "OBE", 1975, "alive", "spo", "Privately educated"],
    ["Mary Berry", "Dame", 1935, "alive", "etc", "Bath High School, Bath College of Domestic Science"],
    ["Gordon Ramsay", "OBE", 1966, "alive", "etc", "North Oxfordshire Technical College"],
    ["Jamie Oliver", "MBE", 1975, "alive", "etc", "Newport Free Grammar School, Westminster Kingsway College"],
    ["Benedict Cumberbatch", "CBE", 1976, "alive", "art", "Harrow School, University of Manchester, London Academy of Music and Dramatic Art"],
    ["Daniel Craig", "None", 1968, "alive", "art", "Calday Grange Grammar School, Guildhall School of Music and Drama"],
    ["Judi Dench", "Dame", 1934, "alive", "art", "The Mount School, York, Central School of Speech and Drama"],
    ["Maggie Smith", "Dame", 1934, 2024, "art", "Oxford High School, Oxford Playhouse School"],
    ["Helen Mirren", "Dame", 1945, "alive", "art", "St Bernard's High School for Girls, New College of Speech and Drama"],
    ["Kate Winslet", "CBE", 1975, "alive", "art", "Redroofs Theatre School"],
    ["Idris Elba", "OBE", 1972, "alive", "art", "Kingsland High School, National Youth Music Theatre"],
    ["Tom Hardy", "CBE", 1977, "alive", "art", "Reed's School, Drama Centre London"],
    ["Hugh Grant", "None", 1960, "alive", "art", "Latymer Upper School, New College, Oxford"],
    ["Gary Oldman", "None", 1958, "alive", "art", "West Greenwich Secondary School, Rose Bruford College"],
    ["Rowan Atkinson", "CBE", 1955, "alive", "art", "Durham Choristers School, St Bees School, Newcastle University, The Queen's College, Oxford"]
    ]

# ------------------------ prepare -------------------------

from pprint import pp, pprint
from collections import defaultdict
from enum import IntEnum

class Item(IntEnum):
    NAME  = 0
    STATUS = 1
    BIRTH = 2
    DEATH = 3
    FIELD = 4
    EDU   = 5

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
for prm in famous_200:
    edu = prm[Item.EDU]
    if 'Oxford' in edu: oxford += 1
    if 'Cambridge' in edu: cambridge += 1
    if 'Oxford' not in edu and 'Cambridge' not in edu: others += 1
    if 'Eton' in edu: eton += 1

print(f"Colleges: {oxford=}, {cambridge=}, {others=}, {eton=}\n")

fromto = { (edu.value, field.value): 0 for edu in Edu for field in Field }

# ~ print(fromto)

fields = "etc,lit,sci,art,pol,bus,spo".split(',')

# ~ print(fields)

for person in famous_200:
    status = person[Item.STATUS]
    field = person[Item.FIELD]
    educ = person[Item.EDU]

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

print("            etc      oxford    cambridge")
for lnum, lname in enumerate(fields):
    print(f"{lname:5}", end="")
    for cnum in range(3):
        print(f"{fromto[(cnum, lnum)]:10}", end="")
    print()
# ~ print()

print("""
ключ     : lit,        sci,   art,       pol,      bus,    spo,   etc 
значение : литература, наука, искусство, политика, бизнес, спорт, прочее
""")

# ~ Colleges: oxford=12, cambridge=18, others=71, eton=6

            # ~ etc      oxford    cambridge
# ~ etc           8         1         1
# ~ lit          23         8         3
# ~ sci          18         2        18
# ~ art          33         4         0
# ~ pol          21        20        10
# ~ bus          10         0         1
# ~ spo          19         1         0

# ~ ключ     : lit,        sci,   art,       pol,      bus,    spo,   etc 
# ~ значение : литература, наука, искусство, политика, бизнес, спорт, прочее


# -----------------------------------------------------------------
part("The End.")
# -----------------------------------------------------------------


