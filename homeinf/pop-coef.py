#!/usr/bin/env python

# Mikhail (myke) Kolodin, 2026
# pop-coef.py
# 2026-06-24 2026-06-24 1.2

# ~ изучаем население мира, покажи (dict[dict]) такое для каждой страны мира из 200 (всё по-англ.):
# ~ - name; название страны,
# ~ - pop: население (тыс. чел.),
# ~ - add: прирост населения (тыс. чел.) за 5 лет (возможно, отрицательный),
# ~ - coef: коэффициент рождаемости;
# ~ вывод вложенного словаря сделай в 1 строку, ключ внешнего словаря - название страны

# -------------------------- данные -------------------------

data = {
    "India": {"pop": 1476625, "add": 61200, "coef": 2.0},
    "China": {"pop": 1412914, "add": -11800, "coef": 1.2},
    "United States": {"pop": 349035, "add": 9400, "coef": 1.7},
    "Indonesia": {"pop": 287886, "add": 11800, "coef": 2.1},
    "Pakistan": {"pop": 259299, "add": 24200, "coef": 3.3},
    "Nigeria": {"pop": 242431, "add": 26100, "coef": 5.0},
    "Brazil": {"pop": 213562, "add": 4900, "coef": 1.6},
    "Bangladesh": {"pop": 177818, "add": 8100, "coef": 1.9},
    "Russia": {"pop": 143200, "add": -2900, "coef": 1.5},
    "Ethiopia": {"pop": 138879, "add": 17100, "coef": 3.8},
    "Mexico": {"pop": 132997, "add": 5050, "coef": 1.8},
    "Japan": {"pop": 122427, "add": -3400, "coef": 1.3},
    "Egypt": {"pop": 118200, "add": 9100, "coef": 2.7},
    "Philippines": {"pop": 117900, "add": 7500, "coef": 2.4},
    "DR Congo": {"pop": 112100, "add": 15800, "coef": 6.0},
    "Vietnam": {"pop": 101900, "add": 3600, "coef": 1.9},
    "Iran": {"pop": 92300, "add": 2900, "coef": 1.7},
    "Turkey": {"pop": 86300, "add": 2400, "coef": 1.6},
    "Germany": {"pop": 83400, "add": 200, "coef": 1.5},
    "Tanzania": {"pop": 72563, "add": 8900, "coef": 4.6},
    "Thailand": {"pop": 71559, "add": -290, "coef": 1.3},
    "United Kingdom": {"pop": 69931, "add": 1750, "coef": 1.6},
    "France": {"pop": 68900, "add": 850, "coef": 1.7},
    "South Africa": {"pop": 61500, "add": 3100, "coef": 2.3},
    "Italy": {"pop": 58965, "add": -750, "coef": 1.3},
    "Kenya": {"pop": 57100, "add": 5400, "coef": 3.3},
    "Myanmar": {"pop": 55200, "add": 1400, "coef": 2.1},
    "Colombia": {"pop": 53936, "add": 2100, "coef": 1.7},
    "Sudan": {"pop": 53282, "add": 5900, "coef": 4.5},
    "Uganda": {"pop": 52761, "add": 6400, "coef": 4.8},
    "South Korea": {"pop": 51600, "add": -220, "coef": 0.7},
    "Spain": {"pop": 47900, "add": 600, "coef": 1.3},
    "Algeria": {"pop": 46800, "add": 3300, "coef": 2.8},
    "Iraq": {"pop": 46500, "add": 4900, "coef": 3.4},
    "Argentina": {"pop": 46200, "add": 1900, "coef": 1.9},
    "Afghanistan": {"pop": 44300, "add": 5100, "coef": 4.5},
    "Yemen": {"pop": 35300, "add": 3500, "coef": 3.6},
    "Canada": {"pop": 42100, "add": 3600, "coef": 1.4},
    "Poland": {"pop": 40200, "add": -500, "coef": 1.3},
    "Morocco": {"pop": 38400, "add": 1800, "coef": 2.3},
    "Angola": {"pop": 38300, "add": 4900, "coef": 5.2},
    "Ukraine": {"pop": 37200, "add": -4800, "coef": 1.1},
    "Uzbekistan": {"pop": 37100, "add": 3200, "coef": 2.8},
    "Saudi Arabia": {"pop": 37000, "add": 2100, "coef": 2.2},
    "Peru": {"pop": 34900, "add": 1600, "coef": 2.2},
    "Malaysia": {"pop": 34600, "add": 1800, "coef": 1.8},
    "Ghana": {"pop": 34500, "add": 3600, "coef": 3.6},
    "Mozambique": {"pop": 34300, "add": 4300, "coef": 4.7},
    "Nepal": {"pop": 31400, "add": 1400, "coef": 1.9},
    "Madagascar": {"pop": 31200, "add": 3500, "coef": 3.9},
    "Ivory Coast": {"pop": 30100, "add": 3400, "coef": 4.2},
    "Venezuela": {"pop": 29400, "add": 1200, "coef": 2.2},
    "Camero0n": {"pop": 29300, "add": 3300, "coef": 4.4},
    "Niger": {"pop": 28400, "add": 4400, "coef": 6.6},
    "Australia": {"pop": 27200, "add": 1650, "coef": 1.6},
    "North Korea": {"pop": 26300, "add": 210, "coef": 1.8},
    "Mali": {"pop": 25100, "add": 3200, "coef": 5.9},
    "Taiwan": {"pop": 23900, "add": -50, "coef": 0.9},
    "Burkina Faso": {"pop": 23800, "add": 2600, "coef": 5.0},
    "Syria": {"pop": 23500, "add": 3100, "coef": 2.7},
    "Sri Lanka": {"pop": 21900, "add": 150, "coef": 1.9},
    "Malawi": {"pop": 21800, "add": 2400, "coef": 3.9},
    "Zambia": {"pop": 21700, "add": 2600, "coef": 4.2},
    "Kazakhstan": {"pop": 20400, "add": 1400, "coef": 2.9},
    "Chad": {"pop": 19400, "add": 2500, "coef": 5.6},
    "Chile": {"pop": 19700, "add": 300, "coef": 1.5},
    "Romania": {"pop": 19100, "add": -350, "coef": 1.6},
    "Somalia": {"pop": 19200, "add": 2500, "coef": 5.9},
    "Senegal": {"pop": 18500, "add": 2000, "coef": 4.4},
    "Guatemala": {"pop": 18300, "add": 1300, "coef": 2.3},
    "Netherlands": {"pop": 18100, "add": 450, "coef": 1.5},
    "Ecuador": {"pop": 18200, "add": 950, "coef": 2.0},
    "Cambodia": {"pop": 17200, "add": 650, "coef": 2.2},
    "Zimbabwe": {"pop": 17100, "add": 1500, "coef": 3.4},
    "Guinea": {"pop": 14700, "add": 1600, "coef": 4.4},
    "Benin": {"pop": 14200, "add": 1650, "coef": 4.7},
    "Rwanda": {"pop": 14400, "add": 1400, "coef": 3.2},
    "Burundi": {"pop": 13700, "add": 1600, "coef": 5.0},
    "Bolivia": {"pop": 12500, "add": 800, "coef": 2.6},
    "Tunisia": {"pop": 12600, "add": 350, "coef": 1.9},
    "Haiti": {"pop": 11800, "add": 600, "coef": 2.8},
    "Belgium": {"pop": 11800, "add": 200, "coef": 1.5},
    "Jordan": {"pop": 11500, "add": 400, "coef": 2.6},
    "Cuba": {"pop": 11000, "add": -250, "coef": 1.4},
    "South Sudan": {"pop": 11200, "add": 900, "coef": 4.5},
    "Dominican Republic": {"pop": 11500, "add": 550, "coef": 2.2},
    "Czech Republic": {"pop": 10500, "add": 10, "coef": 1.6},
    "Greece": {"pop": 10200, "add": -200, "coef": 1.3},
    "Sweden": {"pop": 10700, "add": 300, "coef": 1.6},
    "Portugal": {"pop": 10200, "add": -80, "coef": 1.4},
    "Azerbaijan": {"pop": 10500, "add": 250, "coef": 1.6},
    "Tajikistan": {"pop": 10500, "add": 950, "coef": 3.1},
    "Honduras": {"pop": 10700, "add": 700, "coef": 2.3},
    "United Arab Emirates": {"pop": 9600, "add": 250, "coef": 1.4},
    "Hungary": {"pop": 9800, "add": -150, "coef": 1.5},
    "Belarus": {"pop": 9400, "add": -180, "coef": 1.4},
    "Israel": {"pop": 9500, "add": 700, "coef": 2.9},
    "Austria": {"pop": 9000, "add": 120, "coef": 1.4},
    "Papua New Guinea": {"pop": 10500, "add": 900, "coef": 3.4},
    "Switzerland": {"pop": 8900, "add": 250, "coef": 1.5},
    "Sierra Leone": {"pop": 8900, "add": 950, "coef": 3.9},
    "Togo": {"pop": 9200, "add": 1000, "coef": 4.1},
    "Hong Kong": {"pop": 7450, "add": -40, "coef": 0.8},
    "Laos": {"pop": 7700, "add": 500, "coef": 2.4},
    "Paraguay": {"pop": 6900, "add": 420, "coef": 2.1},
    "Bulgaria": {"pop": 6600, "add": -250, "coef": 1.6},
    "Libya": {"pop": 6900, "add": 400, "coef": 2.1},
    "Lebanon": {"pop": 5300, "add": -300, "coef": 1.9},
    "Nicaragua": {"pop": 7100, "add": 500, "coef": 2.2},
    "Kyrgyzstan": {"pop": 7100, "add": 620, "coef": 2.7},
    "El Salvador": {"pop": 6400, "add": 80, "coef": 1.8},
    "Turkmenistan": {"pop": 6600, "add": 480, "coef": 2.6},
    "Singapore": {"pop": 6100, "add": 180, "coef": 1.0},
    "Denmark": {"pop": 5950, "add": 120, "coef": 1.7},
    "Finland": {"pop": 5550, "add": 40, "coef": 1.4},
    "Congo": {"pop": 6200, "add": 750, "coef": 4.2},
    "Slovakia": {"pop": 5400, "add": -40, "coef": 1.6},
    "Norway": {"pop": 5550, "add": 180, "coef": 1.5},
    "Oman": {"pop": 4700, "add": 320, "coef": 2.5},
    "State of Palestine": {"pop": 5500, "add": 600, "coef": 3.4},
    "Liberia": {"pop": 5600, "add": 650, "coef": 4.1},
    "Costa Rica": {"pop": 5200, "add": 150, "coef": 1.5},
    "Ireland": {"pop": 5150, "add": 220, "coef": 1.7},
    "Central African Republic": {"pop": 5800, "add": 680, "coef": 4.3},
    "New Zealand": {"pop": 5300, "add": 240, "coef": 1.6},
    "Mauritania": {"pop": 4900, "add": 600, "coef": 4.3},
    "Panama": {"pop": 4500, "add": 320, "coef": 2.2},
    "Kuwait": {"pop": 4350, "add": 200, "coef": 1.9},
    "Croatia": {"pop": 3950, "add": -120, "coef": 1.5},
    "Moldova": {"pop": 3350, "add": -150, "coef": 1.7},
    "Georgia": {"pop": 3700, "add": -60, "coef": 1.8},
    "Eritrea": {"pop": 3800, "add": 420, "coef": 3.7},
    "Uruguay": {"pop": 3400, "add": 10, "coef": 1.5},
    "Bosnia and Herzegovina": {"pop": 3150, "add": -110, "coef": 1.3},
    "Mongolia": {"pop": 3500, "add": 260, "coef": 2.6},
    "Armenia": {"pop": 2950, "add": -30, "coef": 1.6},
    "Jamaica": {"pop": 2800, "add": -20, "coef": 1.3},
    "Qatar": {"pop": 2750, "add": 90, "coef": 1.8},
    "Albania": {"pop": 2800, "add": -40, "coef": 1.4},
    "Lithuania": {"pop": 2700, "add": -50, "coef": 1.6},
    "Namibia": {"pop": 2700, "add": 280, "coef": 3.1},
    "Gambia": {"pop": 2800, "add": 330, "coef": 4.4},
    "Gabon": {"pop": 2500, "add": 240, "coef": 3.5},
    "Botswana": {"pop": 2700, "add": 250, "coef": 2.6},
    "Lesotho": {"pop": 2350, "add": 130, "coef": 2.9},
    "Slovenia": {"pop": 2100, "add": 10, "coef": 1.6},
    "Latvia": {"pop": 1800, "add": -55, "coef": 1.5},
    "North Macedonia": {"pop": 2050, "add": -25, "coef": 1.4},
    "Kosovo": {"pop": 1650, "add": -40, "coef": 1.5},
    "Guinea-Bissau": {"pop": 2200, "add": 240, "coef": 4.2},
    "Equatorial Guinea": {"pop": 1750, "add": 190, "coef": 4.3},
    "Bahrain": {"pop": 1500, "add": 60, "coef": 1.7},
    "Trinidad and Tobago": {"pop": 1500, "add": -5, "coef": 1.6},
    "Estonia": {"pop": 1300, "add": -5, "coef": 1.6},
    "Timor-Leste": {"pop": 1400, "add": 110, "coef": 3.0},
    "Mauritius": {"pop": 1300, "add": 5, "coef": 1.4},
    "Cyprus": {"pop": 1260, "add": 40, "coef": 1.3},
    "Eswatini": {"pop": 1220, "add": 70, "coef": 2.9},
    "Djibouti": {"pop": 1150, "add": 75, "coef": 2.6},
    "Fiji": {"pop": 940, "add": 35, "coef": 2.6},
    "Comoros": {"pop": 870, "add": 70, "coef": 3.9},
    "Guyana": {"pop": 815, "add": 25, "coef": 2.3},
    "Bhutan": {"pop": 790, "add": 30, "coef": 1.4},
    "Solomon Islands": {"pop": 770, "add": 85, "coef": 3.9},
    "Macao": {"pop": 710, "add": 35, "coef": 1.1},
    "Montenegro": {"pop": 620, "add": -5, "coef": 1.7},
    "Luxembourg": {"pop": 660, "add": 45, "coef": 1.4},
    "Suriname": {"pop": 625, "add": 30, "coef": 2.3},
    "Western Sahara": {"pop": 600, "add": 60, "coef": 2.3},
    "Malta": {"pop": 540, "add": 20, "coef": 1.2},
    "Maldives": {"pop": 520, "add": 12, "coef": 1.6},
    "Brunei": {"pop": 455, "add": 20, "coef": 1.7},
    "Belize": {"pop": 410, "add": 35, "coef": 2.0},
    "Bahamas": {"pop": 415, "add": 18, "coef": 1.4},
    "Iceland": {"pop": 395, "add": 25, "coef": 1.7},
    "Guadeloupe": {"pop": 395, "add": -2, "coef": 1.9},
    "Martinique": {"pop": 365, "add": -5, "coef": 1.8},
    "Vanuatu": {"pop": 340, "add": 35, "coef": 3.6},
    "French Guiana": {"pop": 315, "add": 35, "coef": 3.4},
    "Barbados": {"pop": 282, "add": 0, "coef": 1.6},
    "New Caledonia": {"pop": 295, "add": 12, "coef": 1.9},
    "French Polynesia": {"pop": 280, "add": 8, "coef": 1.8},
    "Mayotte": {"pop": 340, "add": 45, "coef": 4.4},
    "Sao Tome and Principe": {"pop": 235, "add": 22, "coef": 3.5},
    "Samoa": {"pop": 228, "add": 15, "coef": 3.7},
    "Saint Lucia": {"pop": 180, "add": 2, "coef": 1.4},
    "Guam": {"pop": 170, "add": 3, "coef": 2.2},
    "Curaçao": {"pop": 160, "add": 2, "coef": 1.7},
    "Kiribati": {"pop": 135, "add": 12, "coef": 3.3},
    "Grenada": {"pop": 126, "add": 3, "coef": 2.1},
    "St. Vincent and the Grenadines": {"pop": 104, "add": -1, "coef": 1.8},
    "Aruba": {"pop": 107, "add": 1, "coef": 1.8},
    "Micronesia": {"pop": 116, "add": 5, "coef": 2.9},
    "Jersey": {"pop": 112, "add": 4, "coef": 1.4},
    "Tonga": {"pop": 108, "add": 4, "coef": 3.3},
    "Seychelles": {"pop": 108, "add": 3, "coef": 2.0},
    "Antigua and Barbuda": {"pop": 94, "add": 3, "coef": 1.6},
    "Isle of Man": {"pop": 85, "add": 1, "coef": 1.5},
    "Andorra": {"pop": 80, "add": 2, "coef": 1.3},
    "Dominica": {"pop": 73, "add": 1, "coef": 1.9},
    "Cayman Islands": {"pop": 70, "add": 4, "coef": 1.3},
    "Bermuda": {"pop": 64, "add": -1, "coef": 1.3},
    "Guernsey": {"pop": 64, "add": 1, "coef": 1.5},
    "Greenland": {"pop": 56, "add": 0, "coef": 1.9},
    "American Samoa": {"pop": 44, "add": -2, "coef": 2.2},
    "Northern Mariana Islands": {"pop": 50, "add": 1, "coef": 1.6},
    "Saint Kitts and Nevis": {"pop": 48, "add": 1, "coef": 1.6},
    "Marshall Islands": {"pop": 42, "add": 2, "coef": 3.1},
    "Sint Maarten": {"pop": 44, "add": 1, "coef": 1.5},
    "Monaco": {"pop": 36, "add": 0, "coef": 1.5},
    "Gibraltar": {"pop": 34, "add": 0, "coef": 1.8},
    "San Marino": {"pop": 34, "add": 0, "coef": 1.3},
    "Liechtenstein": {"pop": 40, "add": 1, "coef": 1.5},
    "British Virgin Islands": {"pop": 32, "add": 1, "coef": 1.4},
    "Palau": {"pop": 18, "add": 0, "coef": 1.7},
    "Cook Islands": {"pop": 17, "add": 0, "coef": 2.1},
    "Anguilla": {"pop": 16, "add": 0, "coef": 1.6},
    "Nauru": {"pop": 13, "add": 0, "coef": 3.3},
    "Tuvalu": {"pop": 12, "add": 0, "coef": 3.1}
    }

# -------------------------- подготовка -------------------------

from pprint import pprint

# -------------------------- расчёт -------------------------

# ---------- тест 1 ----------

print('\n1. сколько стран?')

print(f"всего стран: {len(data)}")

# ---------- тест 2 ----------

print('\n2. опиши Россию')

land = data['Russia']

# ~ pprint(land)

print(f"""
страна:       Россия
население:    {land['pop']} тыс.чел.
прирост:      {land['add']} тыс.чел.
коэффициент:  {land['coef']} 
""")

# ---------- тест 3 ----------

print('\n3. крайние по приросту')

plus = [ (v['coef'], k) for k, v in data.items()]
plus.sort()

print(f"""
самые неразмножающиеся: {plus[:3]}
самые размножающиеся:   {plus[-3:][::-1]}
""")

# -------------------------- результаты -------------------------

# ~ 1. сколько стран?
# ~ всего стран: 219

# ~ 2. опиши Россию

# ~ страна:       Россия
# ~ население:    143200 тыс.чел.
# ~ прирост:      -2900 тыс.чел.
# ~ коэффициент:  1.5

# ~ 3. крайние по приросту

# ~ самые неразмножающиеся: [(0.7, 'South Korea'), (0.8, 'Hong Kong'), (0.9, 'Taiwan')]
# ~ самые размножающиеся:   [(6.6, 'Niger'), (6.0, 'DR Congo'), (5.9, 'Somalia')]

# -------------------------- обсуждение -------------------------

# ~ `coef` ниже уровня воспроизводства (меньше 2.1).

# -------------------------- конец -------------------------
print()
