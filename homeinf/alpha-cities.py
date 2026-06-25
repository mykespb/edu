#!/usr/bin/env python

# Mikhail (myke) Kolodin, 2026
# alpha-cities.py
# 2026-06-25 2026-06-25 1.1

# ~ Дай список альфа-городов мира.
# ~ Переведи этот список в формат list[dict], всё по-английски. 
# ~ Поля: 
# ~ - name: название
# ~ - country: страна
# ~ - continent: континент
# ~ - status: статус (a-, a, a+, a++)
# ~ - population: население (тыс.чел.)
# ~ - dollars: ВВП (млн. USD)
# ~ - geo: геокоординаты ([lat, lon])
# ~ - growth: рост за последние 10 лет в процентах (float)
# ~ - exp: краткое объяснение, почему он альфа

# ~ Here is the list of Alpha-tier global cities, converted into an English list[dict] structure as requested. 
# ~ Note: Population values represent the wider metropolitan or urban agglomeration area in thousands. GDP (dollars) values refer to the Gross Metropolitan Product (GMP) in millions of USD. Growth figures represent estimated real macroeconomic GDP growth trends over the last decade.

alphas = [
    # --- Alpha++ Tier ---
    {
    "name": "London",
    "country": "United Kingdom",
    "continent": "Europe",
    "status": "a++",
    "population": 9748,
    "dollars": 685000,
    "geo": [51.5074, -0.1278],
    "growth": 14.5,
    "exp": "Top global financial hub, unmatched legal, insurance, and cultural integration alongside New York."
    },
    {
    "name": "New York",
    "country": "United States",
    "continent": "North America",
    "status": "a++",
    "population": 19426,
    "dollars": 2300000,
    "geo": [40.7128, -74.0060],
    "growth": 18.2,
    "exp": "The world's absolute leading financial capital, housing Wall Street and dominant corporate headquarters."
    },

    # --- Alpha+ Tier ---
    {
    "name": "Hong Kong",
    "country": "China",
    "continent": "Asia",
    "status": "a+",
    "population": 7490,
    "dollars": 382000,
    "geo": [22.3193, 114.1694],
    "growth": 11.1,
    "exp": "The premier financial gateway connecting mainland China with Western global capital markets."
    },
    {
    "name": "Singapore",
    "country": "Singapore",
    "continent": "Asia",
    "status": "a+",
    "population": 6040,
    "dollars": 466000,
    "geo": [1.3521, 103.8198],
    "growth": 28.4,
    "exp": "The most connected trade, logistics, and financial wealth-management hub in Southeast Asia."
    },
    {
    "name": "Shanghai",
    "country": "China",
    "continent": "Asia",
    "status": "a+",
    "population": 29867,
    "dollars": 690000,
    "geo": [31.2304, 121.4737],
    "growth": 45.8,
    "exp": "The industrial and financial superpower of mainland China, holding a massive shipping network."
    },
    {
    "name": "Beijing",
    "country": "China",
    "continent": "Asia",
    "status": "a+",
    "population": 21890,
    "dollars": 615000,
    "geo": [39.9042, 116.4074],
    "growth": 42.1,
    "exp": "Political and regulatory nerve center of China, hosting massive state-owned global corporations."
    },
    {
    "name": "Paris",
    "country": "France",
    "continent": "Europe",
    "status": "a+",
    "population": 11208,
    "dollars": 765000,
    "geo": [48.8566, 2.3522],
    "growth": 12.3,
    "exp": "The political and corporate anchor of Eurozone economic activity alongside luxury sector dominance."
    },
    {
    "name": "Tokyo",
    "country": "Japan",
    "continent": "Asia",
    "status": "a+",
    "population": 37785,
    "dollars": 1600000,
    "geo": [35.6764, 139.6500],
    "growth": 7.5,
    "exp": "The largest metropolitan economy in Asia, a core node for global banking and tech R&D."
    },
    {
    "name": "Dubai",
    "country": "United Arab Emirates",
    "continent": "Asia",
    "status": "a+",
    "population": 3610,
    "dollars": 115000,
    "geo": [25.2048, 55.2708],
    "growth": 35.6,
    "exp": "The hyper-fast-growing financial, aviation, and logistics bridge linking East and West."
    },

    # --- Alpha Tier ---
    {
    "name": "Los Angeles",
    "country": "United States",
    "continent": "North America",
    "status": "a",
    "population": 12534,
    "dollars": 1120000,
    "geo": [34.0522, -118.2437],
    "growth": 19.5,
    "exp": "Global media capital and major trans-Pacific trade gateway for North America."
    },
    {
    "name": "Toronto",
    "country": "Canada",
    "continent": "North America",
    "status": "a",
    "population": 6431,
    "dollars": 410000,
    "geo": [43.6532, -79.3832],
    "growth": 16.8,
    "exp": "Financial powerhouse of Canada, dominating the nation's banking and mining capital markets."
    },
    {
    "name": "Mumbai",
    "country": "India",
    "continent": "Asia",
    "status": "a",
    "population": 21673,
    "dollars": 2600000,
    "geo": [19.0760, 72.8777],
    "growth": 54.0,
    "exp": "Commercial and financial engine of India, housing the RBI and massive conglomerate HQs."
    },
    {
    "name": "Amsterdam",
    "country": "Netherlands",
    "continent": "Europe",
    "status": "a",
    "population": 1174,
    "dollars": 185000,
    "geo": [52.3676, 4.9041],
    "growth": 18.5,
    "exp": "Major European financial hub and a magnet for international corporate tax structures and tech."
    },
    {
    "name": "Frankfurt",
    "country": "Germany",
    "continent": "Europe",
    "status": "a",
    "population": 796,
    "dollars": 230000,
    "geo": [50.1109, 8.6821],
    "growth": 10.2,
    "exp": "The financial heart of continental Europe, hosting the European Central Bank (ECB)."
    },
    {
    "name": "Chicago",
    "country": "United States",
    "continent": "North America",
    "status": "a",
    "population": 8931,
    "dollars": 740000,
    "geo": [41.8781, -87.6298],
    "growth": 11.4,
    "exp": "Global epicenter for derivatives, futures trading, and industrial corporate management."
    },
    {
    "name": "Sydney",
    "country": "Australia",
    "continent": "Oceania",
    "status": "a",
    "population": 5121,
    "dollars": 345000,
    "geo": [-33.8688, 151.2093],
    "growth": 21.0,
    "exp": "The primary financial gateway linking the Australian continent with Asian markets."
    },
    {
    "name": "San Paulo",
    "country": "Brazil",
    "continent": "South America",
    "status": "a",
    "population": 22626,
    "dollars": 420000,
    "geo": [-23.5505, -46.6333],
    "growth": 8.0,
    "exp": "The undisputed financial capital and largest corporate services market in Latin America."
    },
    {
    "name": "Kuala Lumpur",
    "country": "Malaysia",
    "continent": "Asia",
    "status": "a",
    "population": 8810,
    "dollars": 190000,
    "geo": [3.1390, 101.6869],
    "growth": 34.2,
    "exp": "A leading global hub for Islamic finance and corporate services within SE Asia."
    },
    {
    "name": "Madrid",
    "country": "Spain",
    "continent": "Europe",
    "status": "a",
    "population": 6751,
    "dollars": 250000,
    "geo": [40.4168, -3.7038],
    "growth": 13.1,
    "exp": "The dominant financial node of Spain and the bridge for European-Latin American commerce."
    },
    {
    "name": "Milan",
    "country": "Italy",
    "continent": "Europe",
    "status": "a",
    "population": 3155,
    "dollars": 215000,
    "geo": [45.4642, 9.1900],
    "growth": 9.4,
    "exp": "The industrial, fashion, and banking capital driving Italy's integration with the world."
    },
    {
    "name": "Mexico City",
    "country": "Mexico",
    "continent": "North America",
    "status": "a",
    "population": 22281,
    "dollars": 290000,
    "geo": [19.4326, -99.1332],
    "growth": 20.4,
    "exp": "Massive political-economic hub linking Spanish-speaking markets to North American supply chains."
    },
    {
    "name": "Brussels",
    "country": "Belgium",
    "continent": "Europe",
    "status": "a",
    "population": 2132,
    "dollars": 160000,
    "geo": [50.8503, 4.3517],
    "growth": 10.8,
    "exp": "De facto capital of the EU, drawing unprecedented diplomatic, lobbying, and legal services."
    },
    {
    "name": "Seoul",
    "country": "South Korea",
    "continent": "Asia",
    "status": "a",
    "population": 9982,
    "dollars": 480000,
    "geo": [37.5665, 126.9780],
    "growth": 24.6,
    "exp": "Tech and engineering megacity, managing South Korea's massive global manufacturing networks."
    },
    {
    "name": "Guangzhou",
    "country": "China",
    "continent": "Asia",
    "status": "a",
    "population": 14510,
    "dollars": 410000,
    "geo": [23.1291, 113.2644],
    "growth": 48.0,
    "exp": "The anchor of the Pearl River Delta trade powerhouse and global manufacturing commerce."
    },
    {
    "name": "Shenzhen",
    "country": "China",
    "continent": "Asia",
    "status": "a",
    "population": 13035,
    "dollars": 490000,
    "geo": [22.5431, 114.0579],
    "growth": 65.2,
    "exp": "The 'Silicon Valley of China', leading global hardware innovations and venture tech capital."
    },

    # --- Alpha- Tier ---
    {
    "name": "San Francisco",
    "country": "United States",
    "continent": "North America",
    "status": "a-",
    "population": 3315,
    "dollars": 620000,
    "geo": [37.7749, -122.4194],
    "growth": 28.0,
    "exp": "The epicenter of global venture capital and transformative digital technology industries."
    },
    {
    "name": "Vienna",
    "country": "Austria",
    "continent": "Europe",
    "status": "a-",
    "population": 1975,
    "dollars": 145000,
    "geo": [48.2082, 16.3738],
    "growth": 11.2,
    "exp": "Crucial diplomatic capital and economic bridge between Western and Central-Eastern Europe."
    },
    {
    "name": "Melbourne",
    "country": "Australia",
    "continent": "Oceania",
    "status": "a-",
    "population": 5150,
    "dollars": 295000,
    "geo": [-37.8136, 144.9631],
    "growth": 22.4,
    "exp": "Rapidly growing corporate hub managing massive commodities and financial tech services."
    },
    {
    "name": "Dublin",

    "country": "Ireland",
    "continent": "Europe",
    "status": "a-",
    "population": 1263,
    "dollars": 175000,
    "geo": [53.3498, -6.2603],
    "growth": 62.5,
    "exp": "European headquarters for global tech giants due to highly competitive corporate legal systems."
    },
    {
    "name": "Zurich",
    "country": "Switzerland",
    "continent": "Europe",
    "status": "a-",
    "population": 1430,
    "dollars": 165000,
    "geo": [47.3769, 8.5417],
    "growth": 12.0,
    "exp": "A premier global banking, private wealth management, and gold-trading powerhouse."
    },
    {
    "name": "Bangkok",
    "country": "Thailand",
    "continent": "Asia",
    "status": "a-",
    "population": 11070,
    "dollars": 170000,
    "geo": [13.7563, 100.5018],
    "growth": 25.1,
    "exp": "Major regional hub for tourism, trade, and corporate operations across Indochina."
    },
    {
    "name": "New Delhi",
    "country": "India",
    "continent": "Asia",
    "status": "a-",
    "population": 33800,
    "dollars": 210000,
    "geo": [28.6139, 77.2090],
    "growth": 58.3,
    "exp": "India's massive regulatory and administrative capital driving political-economic networks."
    },
    {
    "name": "Stockholm",
    "country": "Sweden",
    "continent": "Europe",
    "status": "a-",
    "population": 1690,
    "dollars": 110000,
    "geo": [59.3293, 18.0686],
    "growth": 15.6,
    "exp": "The financial and tech-startup capital connecting the entire Scandinavian region."
    },
    {
    "name": "Istanbul",
    "country": "Turkey",
    "continent": "Europe",
    "status": "a-",
    "population": 15900,
    "dollars": 240000,
    "geo": [41.0082, 28.9784],
    "growth": 30.2,
    "exp": "Critical geopolitical and trade bridge linking European, Middle Eastern, and Asian systems."
    },
    {
    "name": "Houston",
    "country": "United States",
    "continent": "North America",
    "status": "a-",
    "population": 7340,
    "dollars": 540000,
    "geo": [29.7604, -95.3698],
    "growth": 15.0,
    "exp": "The energy capital of the world, commanding global oil, gas, and petrochemical logistics."
    },
    {
    "name": "Boston",
    "country": "United States",
    "continent": "North America",
    "status": "a-",
    "population": 4940,
    "dollars": 490000,
    "geo": [42.3601, -71.0589],
    "growth": 22.1,
    "exp": "World leader in biotechnology, advanced higher education, and venture medical capital."
    },
    {
    "name": "Manila",
    "country": "Philippines",
    "continent": "Asia",
    "status": "a-",
    "population": 14940,
    "dollars": 130000,
    "geo": [14.5995, 120.9842],
    "growth": 45.3,
    "exp": "A leading global center for business process outsourcing (BPO) and regional services."
    },
    {
    "name": "Jakarta",
    "country": "Indonesia",
    "continent": "Asia",
    "status": "a-",
    "population": 11240,
    "dollars": 205000,
    "geo": [-6.2088, 106.8456],
    "growth": 42.0,
    "exp": "Economic powerhouse of the massive Indonesian market, drawing massive consumer services."
    },
    {
    "name": "Vancouver",
    "country": "Canada",
    "continent": "North America",
    "status": "a-",
    "population": 2640,
    "dollars": 150000,
    "geo": [49.2827, -123.1207],
    "growth": 24.8,
    "exp": "Canada's Pacific gateway, heavily integrated with Asian trade, real estate, and film industry."
    },
    {
    "name": "Atlanta",
    "country": "United States",
    "continent": "North America",
    "status": "a-",
    "population": 6220,
    "dollars": 440000,
    "geo": [33.7490, -84.3880],
    "growth": 23.5,
    "exp": "Major logistics node housing the world's busiest airport and giant Fortune 500 corporate HQs."
    },
    {
    "name": "Washington",
    "country": "United States",
    "continent": "North America",
    "status": "a-",
    "population": 6350,
    "dollars": 570000,
    "geo": [38.9072, -77.0369],
    "growth": 14.1,
    "exp": "Global center of political power, international development banking, and defense tech procurement."
    },
    {
    "name": "Miami",
    "country": "United States",
    "continent": "North America",
    "status": "a-",
    "population": 6140,
    "dollars": 380000,
    "geo": [25.7617, -80.1918],
    "growth": 26.3,
    "exp": "The financial gateway managing North American business investments across Latin America."
    },
    {
    "name": "Lima",
    "country": "Peru",
    "continent": "South America",
    "status": "a-",
    "population": 11140,
    "dollars": 110000,
    "geo": [-12.0464, -77.0428],
    "growth": 21.4,
    "exp": "The dominant industrial and financial nexus linking the Peruvian market to global mining markets."
    },
    {
    "name": "Johannesburg",
    "country": "South Africa",
    "continent": "Africa",
    "status": "a-",
    "population": 6320,
    "dollars": 95000,
    "geo": [-26.2041, 28.0473],
    "growth": 5.5,
    "exp": "The financial gateway of Sub-Saharan Africa, hosting Africa's largest stock exchange (JSE)."
    },
    {
    "name": "Santiago",
    "country": "Chile",
    "continent": "South America",
    "status": "a-",
    "population": 6850,
    "dollars": 140000,
    "geo": [-33.4489, -70.6693],
    "growth": 14.8,
    "exp": "One of Latin America's most stable corporate service environments and mining hubs."
    },
    {
    "name": "Taipei",
    "country": "Taiwan",
    "continent": "Asia",
    "status": "a-",
    "population": 7050,
    "dollars": 340000,
    "geo": [25.0330, 121.5654],
    "growth": 25.8,
    "exp": "Crucial node managing the world's most critical semiconductor and electronics tech supply chains."
    },
    {
    "name": "Warsaw",
    "country": "Poland",
    "continent": "Europe",
    "status": "a-",
    "population": 1860,
    "dollars": 120000,
    "geo": [52.2297, 21.0122],
    "growth": 35.0,
    "exp": "The primary corporate services and banking capital for the Central European region."
    },
    {
    "name": "Lisbon",
    "country": "Portugal",
    "continent": "Europe",
    "status": "a-",
    "population": 2980,
    "dollars": 85000,
    "geo": [38.7223, -9.1393],
    "growth": 16.2,
    "exp": "Growing tech hub and trade bridge between Western Europe and Portuguese-speaking nations."
    },
    {
    "name": "Cairo",
    "country": "Egypt",
    "continent": "Africa",
    "status": "a-",
    "population": 22600,
    "dollars": 145000,
    "geo": [30.0444, 31.2357],
    "growth": 38.0,
    "exp": "The massive historic, political, and corporate nexus managing the Arab world and North Africa."
    },
    {
    "name": "Luxembourg",
    "country": "Luxembourg",
    "continent": "Europe",
    "status": "a-",
    "population": 650,
    "dollars": 88000,
    "geo": [49.6116, 6.1319],
    "growth": 18.2,
    "exp": "A highly specialized global leader in international mutual funds and institutional banking."
    },
    {
    "name": "Chengdu",
    "country": "China",
    "continent": "Asia",
    "status": "a-",
    "population": 21400,
    "dollars": 320000,
    "geo": [30.5728, 104.0668],
    "growth": 52.6,
    "exp": "The leading economic, logistical, and high-tech powerhouse of Western inland China."
    }
]

# ---------------------------------------------------

from collections import Counter, defaultdict
from pprint import pprint

# ---------------------------------------------------

print("\n#1. сколько всего каких?")

cnt = defaultdict(list)

for city in alphas:
    cnt[city['status']] .append (city)

pprint(cnt)
print()

for k, v in cnt.items():
    print(f"статус {k:5} -- городов: {len(v)}")

# ~ статус a++   -- городов: 2
# ~ статус a+    -- городов: 7
# ~ статус a     -- городов: 16
# ~ статус a-    -- городов: 26

# -------------------------------------------------------

print("\n#2. сколько всего по континентам?")

cont = defaultdict(list)

for city in alphas:
    cont[city['continent']] .append (city)

for k, v in cont.items():
    print(f"для {k:15} -- городов: {len(v):2}")

# ~ #2. сколько всего по континентам?
# ~ для Europe          -- городов: 15
# ~ для North America   -- городов: 12
# ~ для Asia            -- городов: 17
# ~ для Oceania         -- городов:  2
# ~ для South America   -- городов:  3
# ~ для Africa          -- городов:  2

# ---------------------------------------------------
print()
