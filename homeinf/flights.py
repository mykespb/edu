#!/usr/bin/env python

# Mikhail (myke) Kolodin, 2026
# 2026-06-19 2026-06-19 1.2
# flights.py

# ~ "проанализируй сегодняшнее состояние перелётов (напр., по flightradar) и сделай список из 100 выбранных наугад рейсов, указав:
# ~ - flight: номер рейса,
# ~ - plane: тип самолёта (напр., Pilatus PC-24),
# ~ - dept: пункт отправления,
# ~ - dest: пункт прибытия,
# ~ - long: время в пути (планируемое),
# ~ - dist: расстояние."

# ~ Анализ текущего состояния воздушного пространства по данным Flightradar24 показывает высокую плотность движения по всему миру. В настоящий момент в небе одновременно находится более 12 000 — 15 000 коммерческих, грузовых и частных рейсов. Наблюдается традиционная утренняя и вечерняя пиковая нагрузка в крупнейших авиахабах Европы, Ближнего Востока и Азии. Большинство рейсов выполняется в штатном режиме, а задержки носят локальный характер и вызваны грозовыми фронтами в отдельных регионах. Ниже сформирован список из 100 случайно выбранных активных рейсов со всеми запрашиваемыми параметрами.

fdata = [
    {"flight": "LH430", "plane": "Boeing 747-8", "dept": "FRA", "dest": "ORD", "long": "08h 50m", "dist": 6970},
    {"flight": "EK201", "plane": "Airbus A380-800", "dept": "DXB", "dest": "JFK", "long": "14h 20m", "dist": 11000},
    {"flight": "S72502", "plane": "Airbus A320neo", "dept": "OVB", "dest": "DME", "long": "04h 20m", "dist": 2810},
    {"flight": "LX15", "plane": "Airbus A330-300", "dept": "JFK", "dest": "ZRH", "long": "07h 55m", "dist": 6320},
    {"flight": "SU1712", "plane": "Boeing 777-300ER", "dept": "SVO", "dest": "VVO", "long": "08h 15m", "dist": 6420},
    {"flight": "AA100", "plane": "Boeing 777-200ER", "dept": "JFK", "dest": "LHR", "long": "07h 05m", "dist": 5540},
    {"flight": "AF276", "plane": "Boeing 777-300ER", "dept": "CDG", "dest": "NRT", "long": "13h 40m", "dist": 9730},
    {"flight": "TK1985", "plane": "Airbus A321neo", "dept": "IST", "dest": "LHR", "long": "04h 10m", "dist": 2510},
    {"flight": "QR701", "plane": "Boeing 777-300ER", "dept": "DOH", "dest": "JFK", "long": "14h 45m", "dist": 11150},
    {"flight": "DP203", "plane": "Boeing 737-800", "dept": "VKO", "dest": "AER", "long": "03h 30m", "dist": 1360},
    {"flight": "SQ22", "plane": "Airbus A350-900ULR", "dept": "SIN", "dest": "EWR", "long": "18h 45m", "dist": 15340},
    {"flight": "BA209", "plane": "Boeing 777-200", "dept": "LHR", "dest": "MIA", "long": "09h 15m", "dist": 7120},
    {"flight": "QF9", "plane": "Boeing 787-9", "dept": "PER", "dest": "LHR", "long": "17h 20m", "dist": 14490},
    {"flight": "AY131", "plane": "Airbus A320", "dept": "HEL", "dest": "FRA", "long": "02h 40m", "dist": 1510},
    {"flight": "FR2372", "plane": "Boeing 737-800", "dept": "STN", "dest": "AGP", "long": "02h 50m", "dist": 1670},
    {"flight": "U6263", "plane": "Airbus A321", "dept": "DME", "dest": "AYT", "long": "04h 45m", "dist": 2160},
    {"flight": "FZ727", "plane": "Boeing 737 MAX 8", "dept": "DXB", "dest": "SVO", "long": "05h 30m", "dist": 3680},
    {"flight": "JL6", "plane": "Boeing 777-300ER", "dept": "HND", "dest": "JFK", "long": "13h 05m", "dist": 10860},
    {"flight": "NH211", "plane": "Boeing 787-9", "dept": "HND", "dest": "LHR", "long": "14h 20m", "dist": 9570},
    {"flight": "CX840", "plane": "Airbus A350-1000", "dept": "HKG", "dest": "JFK", "long": "16h 05m", "dist": 12960},
    {"flight": "MS777", "plane": "Boeing 777-300ER", "dept": "CAI", "dest": "LHR", "long": "05h 10m", "dist": 3510},
    {"flight": "KE81", "plane": "Boeing 747-8", "dept": "ICN", "dest": "JFK", "long": "14h 20m", "dist": 11050},
    {"flight": "DL401", "plane": "Boeing 767-400ER", "dept": "JFK", "dest": "LHR", "long": "07h 15m", "dist": 5540},
    {"flight": "OS65", "plane": "Boeing 767-300ER", "dept": "VIE", "dest": "ORD", "long": "09h 40m", "dist": 7560},
    {"flight": "KL641", "plane": "Boeing 777-200ER", "dept": "AMS", "dest": "JFK", "long": "08h 15m", "dist": 5860},
    {"flight": "EI133", "plane": "Airbus A321LR", "dept": "DUB", "dest": "BOS", "long": "06h 45m", "dist": 4820},
    {"flight": "W61301", "plane": "Airbus A321neo", "dept": "WAW", "dest": "LTN", "long": "02h 35m", "dist": 1450},
    {"flight": "SU2134", "plane": "Sukhoi Superjet 100", "dept": "SVO", "dest": "IST", "long": "04h 50m", "dist": 1750},
    {"flight": "AC856", "plane": "Boeing 787-9", "dept": "YVR", "dest": "LHR", "long": "09h 25m", "dist": 7600},
    {"flight": "NZ1", "plane": "Boeing 787-9", "dept": "JFK", "dest": "AKL", "long": "17h 35m", "dist": 14180},
    {"flight": "LX40", "plane": "Airbus A340-300", "dept": "ZRH", "dest": "LAX", "long": "11h 40m", "dist": 9560},
    {"flight": "ET500", "plane": "Boeing 787-8", "dept": "ADD", "dest": "IAD", "long": "13h 30m", "dist": 11560},
    {"flight": "AI101", "plane": "Boeing 777-300ER", "dept": "DEL", "dest": "JFK", "long": "15h 40m", "dist": 11750},
    {"flight": "EY101", "plane": "Boeing 787-10", "dept": "AUH", "dest": "JFK", "long": "14h 10m", "dist": 11020},
    {"flight": "SV111", "plane": "Boeing 777-300ER", "dept": "JED", "dest": "LHR", "long": "06h 15m", "dist": 4760},
    {"flight": "LO26", "plane": "Boeing 787-8", "dept": "JFK", "dest": "WAW", "long": "08h 10m", "dist": 6850},
    {"flight": "FI615", "plane": "Boeing 737 MAX 8", "dept": "KEF", "dest": "JFK", "long": "05h 45m", "dist": 4160},
    {"flight": "TP201", "plane": "Airbus A321LR", "dept": "LIS", "dest": "EWR", "long": "08h 05m", "dist": 5460},
    {"flight": "BR32", "plane": "Boeing 777-300ER", "dept": "TPE", "dest": "JFK", "long": "14h 55m", "dist": 12550},
    {"flight": "R3487", "plane": "Boeing 737-700", "dept": "VKO", "dest": "YKS", "long": "06h 40m", "dist": 4890},
    {"flight": "LX242", "plane": "Airbus A340-300", "dept": "ZRH", "dest": "BOM", "long": "07h 45m", "dist": 5280},
    {"flight": "BJD24", "plane": "Pilatus PC-24", "dept": "VNY", "dest": "LAS", "long": "00h 45m", "dist": 370},
    {"flight": "N724PC", "plane": "Pilatus PC-24", "dept": "APA", "dest": "ASE", "long": "00h 35m", "dist": 210},
    {"flight": "EZY813", "plane": "Airbus A320", "dept": "LGW", "dest": "NCE", "long": "02h 00m", "dist": 1030},
    {"flight": "VY8023", "plane": "Airbus A320neo", "dept": "CDG", "dest": "BCN", "long": "01h 40m", "dist": 860},
    {"flight": "A46001", "plane": "Sukhoi Superjet 100", "dept": "AER", "dest": "EVN", "long": "01h 20m", "dist": 510},
    {"flight": "TO3120", "plane": "Boeing 737-800", "dept": "ORY", "dest": "RAK", "long": "03h 15m", "dist": 2100},
    {"flight": "HV5133", "plane": "Boeing 737-800", "dept": "AMS", "dest": "AGP", "long": "03h 00m", "dist": 1880},
    {"flight": "PC1251", "plane": "Airbus A321neo", "dept": "SAW", "dest": "AMS", "long": "03h 50m", "dist": 2220},
    {"flight": "JU500", "plane": "Airbus A319", "dept": "BEG", "dest": "CDG", "long": "02h 35m", "dist": 1440},
    {"flight": "RO361", "plane": "Boeing 737-700", "dept": "OTP", "dest": "AMS", "long": "02h 55m", "dist": 1800},
    {"flight": "BT421", "plane": "Airbus A220-300", "dept": "RIX", "dest": "SVO", "long": "01h 40m", "dist": 850},
    {"flight": "OU440", "plane": "Dash 8 Q400", "dept": "ZAG", "dest": "VIE", "long": "00h 50m", "dist": 270},
    {"flight": "FB431", "plane": "Embraer 190", "dept": "SOF", "dest": "CDG", "long": "02h 50m", "dist": 1760},
    {"flight": "KM478", "plane": "Airbus A320neo", "dept": "MLA", "dest": "CDG", "long": "02h 45m", "dist": 1740},
    {"flight": "A3600", "plane": "Airbus A320neo", "dept": "ATH", "dest": "CDG", "long": "03h 25m", "dist": 2100},
    {"flight": "CY101", "plane": "Airbus A220-300", "dept": "LCA", "dest": "ATH", "long": "01h 40m", "dist": 930},
    {"flight": "ME201", "plane": "Airbus A321neo", "dept": "BEY", "dest": "CDG", "long": "04h 40m", "dist": 3190},
    {"flight": "MS799", "plane": "Boeing 737-800", "dept": "CAI", "dest": "CDG", "long": "04h 45m", "dist": 3210},
    {"flight": "AH1000", "plane": "Boeing 737-800", "dept": "ALG", "dest": "CDG", "long": "02h 20m", "dist": 1360},
    {"flight": "AT760", "plane": "Boeing 737 MAX 8", "dept": "CMN", "dest": "CDG", "long": "03h 00m", "dist": 1900},
    {"flight": "TU716", "plane": "Airbus A320", "dept": "TUN", "dest": "CDG", "long": "02h 30m", "dist": 1600},
    {"flight": "LN123", "plane": "CRJ-900", "dept": "TIP", "dest": "IST", "long": "02h 55m", "dist": 1660},
    {"flight": "WY101", "plane": "Boeing 787-9", "dept": "MCT", "dest": "LHR", "long": "07h 45m", "dist": 5830},
    {"flight": "GF3", "plane": "Boeing 787-9", "dept": "BAH", "dest": "LHR", "long": "06h 45m", "dist": 5060},
    {"flight": "KU101", "plane": "Boeing 777-300ER", "dept": "KWI", "dest": "LHR", "long": "06h 30m", "dist": 4650},
    {"flight": "QA1", "plane": "Pilatus PC-24", "dept": "DOH", "dest": "MCT", "long": "01h 25m", "dist": 700},
    {"flight": "EK73", "plane": "Airbus A380-800", "dept": "DXB", "dest": "CDG", "long": "07h 15m", "dist": 5240},
    {"flight": "QR41", "plane": "Boeing 787-9", "dept": "DOH", "dest": "CDG", "long": "07h 00m", "dist": 4970},
    {"flight": "EY31", "plane": "Boeing 787-10", "dept": "AUH", "dest": "CDG", "long": "07h 10m", "dist": 5250},
    {"flight": "SV127", "plane": "Boeing 787-9", "dept": "RUH", "dest": "CDG", "long": "06h 20m", "dist": 4680},
    {"flight": "WY131", "plane": "Airbus A330-300", "dept": "MCT", "dest": "CDG", "long": "07h 35m", "dist": 5570},
    {"flight": "BI1", "plane": "Boeing 787-8", "dept": "BWN", "dest": "LHR", "long": "14h 25m", "dist": 11270},
    {"flight": "SQ308", "plane": "Airbus A380-800", "dept": "SIN", "dest": "LHR", "long": "13h 50m", "dist": 10880},
    {"flight": "MH2", "plane": "Airbus A350-900", "dept": "KUL", "dest": "LHR", "long": "13h 55m", "dist": 10600},
    {"flight": "TG910", "plane": "Boeing 777-300ER", "dept": "BKK", "dest": "LHR", "long": "12h 50m", "dist": 9540},
    {"flight": "VN55", "plane": "Boeing 787-9", "dept": "HAN", "dest": "LHR", "long": "12h 45m", "dist": 9230},
    {"flight": "GA86", "plane": "Boeing 777-300ER", "dept": "CGK", "dest": "AMS", "long": "14h 10m", "dist": 11350},
    {"flight": "CI65", "plane": "Airbus A350-900", "dept": "TPE", "dest": "CDG", "long": "14h 15m", "dist": 9840},
    {"flight": "BR87", "plane": "Boeing 777-300ER", "dept": "TPE", "dest": "CDG", "long": "14h 10m", "dist": 9840},
    {"flight": "CZ347", "plane": "Airbus A350-900", "dept": "CAN", "dest": "CDG", "long": "12h 40m", "dist": 9450},
    {"flight": "MU553", "plane": "Airbus A350-900", "dept": "PVG", "dest": "CDG", "long": "12h 30m", "dist": 9260},
    {"flight": "CA933", "plane": "Boeing 777-300ER", "dept": "PEK", "dest": "CDG", "long": "11h 25m", "dist": 8220},
    {"flight": "HU487", "plane": "Boeing 787-9", "dept": "PEK", "dest": "BRU", "long": "11h 00m", "dist": 7970},
    {"flight": "MF825", "plane": "Boeing 787-9", "dept": "XMN", "dest": "CDG", "long": "13h 05m", "dist": 9710},
    {"flight": "FM851", "plane": "Boeing 787-9", "dept": "PVG", "dest": "LGW", "long": "12h 40m", "dist": 9290},
    {"flight": "HO1607", "plane": "Boeing 787-9", "dept": "PVG", "dest": "HEL", "long": "10h 20m", "dist": 7400},
    {"flight": "3U3837", "plane": "Airbus A350-900", "dept": "TFU", "dest": "FCO", "long": "11h 15m", "dist": 8160},
    {"flight": "8L801", "plane": "Airbus A330-200", "dept": "KMG", "dest": "CDG", "long": "12h 30m", "dist": 8780},
    {"flight": "JD429", "plane": "Airbus A330-300", "dept": "HAK", "dest": "CDG", "long": "13h 15m", "dist": 9410},
    {"flight": "O37135", "plane": "Boeing 757-200F", "dept": "SZX", "dest": "ALA", "long": "06h 10m", "dist": 4120},
    {"flight": "Y87425", "plane": "Boeing 747-400BDSF", "dept": "CGO", "dest": "LGW", "long": "12h 10m", "dist": 8550},
    {"flight": "N124PC", "plane": "Pilatus PC-24", "dept": "BUD", "dest": "GVA", "long": "01h 45m", "dist": 1010},
    {"flight": "SU6023", "plane": "Airbus A319", "dept": "LED", "dest": "SVO", "long": "01h 25m", "dist": 640},
    {"flight": "UT379", "plane": "Boeing 737-500", "dept": "VKO", "dest": "SGC", "long": "03h 15m", "dist": 2140},
    {"flight": "WZ445", "plane": "Sukhoi Superjet 100", "dept": "ZIA", "dest": "EVN", "long": "04h 10m", "dist": 1810},
    {"flight": "N712PC", "plane": "Pilatus PC-24", "dept": "TEB", "dest": "PBI", "long": "02h 30m", "dist": 1640},
    {"flight": "G-OFLT", "plane": "BAe Systems Avro RJ100", "dept": "FAB", "dest": "MAN", "long": "00h 50m", "dist": 260},
    {"flight": "LX2800", "plane": "Airbus A220-100", "dept": "ZRH", "dest": "GVA", "long": "00h 45m", "dist": 230},
    {"flight": "N240PC", "plane": "Pilatus PC-24", "dept": "DEN", "dest": "SLC", "long": "01h 15m", "dist": 620}
    ]

# ------------------------ prepare -------------------------

# ~ from collections import Counter
from pprint import pprint

def part(name):
    print(f"""
----------------------------------------------------------
{name}
----------------------------------------------------------
""")

# ~ pprint(fdata)

# --------------------------------------------------------
part("1. выбрать все типы самолётов")
# --------------------------------------------------------

planes = sorted({ f['plane'] for f in fdata })
print("\nВсе самолёты: ")
print(*planes, sep=", ")

comps = sorted({ a.split()[0].split('-')[0] for a in planes })
print("\nВсе производители самолётов:")
print(*comps, sep=", ")

# ~ CRJ (Canadair Regional Jet) — это семейство популярных региональных узкофюзеляжных реактивных самолетов, изначально разработанных канадской компанией Bombardier. В 2020 году программа перешла под управление японской корпорации Mitsubishi, которая осуществляет поддержку этих лайнеров.
# ~ Основные модификацииCRJ-100 и CRJ-200: Самые массовые 50-местные самолеты. Отличаются друг от друга только типом двигателей. Их коммерческое производство уже остановлено, однако они до сих пор активно летают на коротких маршрутах во многих региональных авиакомпаниях.CRJ-700, CRJ-900 и CRJ-1000: Удлиненные версии вместимостью от 70 до 100 пассажиров.
# ~ Производятся и используются для обслуживания более загруженных направлений.Летные характеристикиДальность полета: от 2800 км (у моделей 100/200) до 3700 км (CRJ-700/900).Крейсерская скорость: около 850 км/ч.Надежность: самолеты считаются одними из самых безопасных и экономичных в своем классе, идеально подходя для перелетов между небольшими городами.
# ~ https://ru.wikipedia.org/wiki/Bombardier_CRJ

# ~ Dash — это семейство канадских двухмоторных турбовинтовых пассажирских самолетов для региональных авиалиний. Изначально проект разрабатывался компанией de Havilland Canada, затем перешел к Bombardier, а сейчас правами владеет De Havilland Canada.
# ~ https://ru.wikipedia.org/wiki/Bombardier_Q_Series

# --------------------------------------------------------
part("2. выбрать все аэродромы")
# --------------------------------------------------------

adept = { f['dept'] for f in fdata}
adest = { f['dest'] for f in fdata}
ad = sorted(adept | adest)
print(ad)

# ~ "По прилагаемому списку кодов аэродромов дай таблицу:
# ~ - код аэродрома,
# ~ - название аэродрома,
# ~ - страна аэродрома,
# ~ - географические координаты аэродрома:
# ~ ['ADD', 'AER', 'AGP', 'AKL', 'ALA', 'ALG', 'AMS', 'APA', 'ASE', 'ATH', 'AUH', 'AYT', 'BAH', 'BCN', 'BEG', 'BEY', 'BKK', 'BOM', 'BOS', 'BRU', 'BUD', 'BWN', 'CAI', 'CAN', 'CDG', 'CGK', 'CGO', 'CMN', 'DEL', 'DEN', 'DME', 'DOH', 'DUB', 'DXB', 'EVN', 'EWR', 'FAB', 'FCO', 'FRA', 'GVA', 'HAK', 'HAN', 'HEL', 'HKG', 'HND', 'IAD', 'ICN', 'IST', 'JED', 'JFK', 'KEF', 'KMG', 'KUL', 'KWI', 'LAS', 'LAX', 'LCA', 'LED', 'LGW', 'LHR', 'LIS', 'LTN', 'MAN', 'MCT', 'MIA', 'MLA', 'NCE', 'NRT', 'ORD', 'ORY', 'OTP', 'OVB', 'PBI', 'PEK', 'PER', 'PVG', 'RAK', 'RIX', 'RUH', 'SAW', 'SGC', 'SIN', 'SLC', 'SOF', 'STN', 'SVO', 'SZX', 'TEB', 'TFU', 'TIP', 'TPE', 'TUN', 'VIE', 'VKO', 'VNY', 'VVO', 'WAW', 'XMN', 'YKS', 'YVR', 'ZAG', 'ZIA', 'ZRH']"

# ~ Ниже представлены координаты всех 102 аэродромов, пересчитанные в десятичный формат (до сотых долей градуса). В соответствии с вашим правилом, северная широта и восточная долгота имеют знак плюс, а южная широта и западная долгота — знак минус.

airports_dict = {
    "ADD": {"name": "Боле (Bole)", "country": "Эфиопия", "lat": 8.9778, "lon": 38.7994},
    "AER": {"name": "Сочи (Адлер)", "country": "Россия", "lat": 43.4500, "lon": 39.9567},
    "AGP": {"name": "Малага — Коста-дель-Соль", "country": "Испания", "lat": 36.6750, "lon": -4.4992},
    "AKL": {"name": "Окленд", "country": "Новая Зеландия", "lat": -37.0081, "lon": 174.7917},
    "ALA": {"name": "Алматы", "country": "Казахстан", "lat": 43.3519, "lon": 77.0406},
    "ALG": {"name": "Хуари Бумедьен", "country": "Алжир", "lat": 36.6908, "lon": 3.2153},
    "AMS": {"name": "Схипхол (Schiphol)", "country": "Нидерланды", "lat": 52.3081, "lon": 4.7642},
    "APA": {"name": "Сентенниал (Денвер)", "country": "США", "lat": 39.5700, "lon": -104.8492},
    "ASE": {"name": "Аспен — Питкин Каунти", "country": "США", "lat": 39.2231, "lon": -106.8689},
    "ATH": {"name": "Элефтериос Венизелос", "country": "Греция", "lat": 37.9364, "lon": 23.9444},
    "AUH": {"name": "Заед (Абу-Даби)", "country": "ОАЭ", "lat": 24.4281, "lon": 54.6511},
    "AYT": {"name": "Анталья", "country": "Турция", "lat": 36.9003, "lon": 30.7928},
    "BAH": {"name": "Бахрейн", "country": "Бахрейн", "lat": 26.2708, "lon": 50.6336},
    "BCN": {"name": "Эль-Прат (Барселона)", "country": "Испания", "lat": 41.2969, "lon": 2.0783},
    "BEG": {"name": "Никола Тесла (Белград)", "country": "Сербия", "lat": 44.8194, "lon": 20.3069},
    "BEY": {"name": "Рафик Харири (Бейрут)", "country": "Ливан", "lat": 33.8211, "lon": 35.4883},
    "BKK": {"name": "Суvarnabhumi (Бангкок)", "country": "Таиланд", "lat": 13.6856, "lon": 100.7503},
    "BOM": {"name": "Чхатрапати Шиваджи (Мумбаи)", "country": "Индия", "lat": 19.0886, "lon": 72.8681},
    "BOS": {"name": "Логан (Бостон)", "country": "США", "lat": 42.3642, "lon": -71.0053},
    "BRU": {"name": "Брюссель (Завентем)", "country": "Бельгия", "lat": 50.9014, "lon": 4.4844},
    "BUD": {"name": "Ференц Лист (Будапешт)", "country": "Венгрия", "lat": 47.4394, "lon": 19.2619},
    "BWN": {"name": "Бруней (Бандар-Сери-Бегаван)", "country": "Бруней", "lat": 4.9442, "lon": 114.9283},
    "CAI": {"name": "Каир", "country": "Египет", "lat": 30.1219, "lon": 31.4056},
    "CAN": {"name": "Байюнь (Гуанчжоу)", "country": "Китай", "lat": 23.3925, "lon": 113.2989},
    "CDG": {"name": "Шарль-де-Голль (Париж)", "country": "Франция", "lat": 49.0097, "lon": 2.5478},
    "CGK": {"name": "Сукарно-Хатта (Джакарта)", "country": "Индонезия", "lat": -6.1256, "lon": 106.6558},
    "CGO": {"name": "Синьчжэн (Чжэнчжоу)", "country": "Китай", "lat": 34.5197, "lon": 113.8408},
    "CMN": {"name": "Мухаммед V (Касабланка)", "country": "Марокко", "lat": 33.3672, "lon": -7.5897},
    "DEL": {"name": "Индиры Ганди (Дели)", "country": "Индия", "lat": 28.5664, "lon": 77.1031},
    "DEN": {"name": "Денвер", "country": "США", "lat": 39.8617, "lon": -104.6731},
    "DME": {"name": "Домодедово (Москва)", "country": "Россия", "lat": 55.4086, "lon": 37.9064},
    "DOH": {"name": "Хамад (Доха)", "country": "Катар", "lat": 25.2731, "lon": 51.6081},
    "DUB": {"name": "Дублин", "country": "Ирландия", "lat": 53.4214, "lon": -6.2700},
    "DXB": {"name": "Дубай", "country": "ОАЭ", "lat": 25.2528, "lon": 55.3644},
    "EVN": {"name": "Звартноц (Ереван)", "country": "Армения", "lat": 40.1472, "lon": 44.3958},
    "EWR": {"name": "Либерти (Ньюарк)", "country": "США", "lat": 40.6925, "lon": -74.1686},
    "FAB": {"name": "Фарнборо", "country": "Великобритания", "lat": 51.2753, "lon": -0.7775},
    "FCO": {"name": "Фьюмичино (Рим)", "country": "Италия", "lat": 41.8003, "lon": 12.2389},
    "FRA": {"name": "Франкфурт-на-Майне", "country": "Германия", "lat": 50.0333, "lon": 8.5706},
    "GVA": {"name": "Женева (Куантран)", "country": "Швейцария", "lat": 46.2383, "lon": 6.1094},
    "HAK": {"name": "Мэйлань (Хайкоу)", "country": "Китай", "lat": 20.0294, "lon": 110.4592},
    "HAN": {"name": "Нойбай (Ханой)", "country": "Вьетнам", "lat": 21.2211, "lon": 105.8072},
    "HEL": {"name": "Хельсинки-Вантаа", "country": "Финляндия", "lat": 60.3172, "lon": 24.9633},
    "HKG": {"name": "Чеклапкок (Гонконг)", "country": "Гонконг (КНР)", "lat": 22.3089, "lon": 113.9144},
    "HND": {"name": "Ханеда (Токио)", "country": "Япония", "lat": 35.5533, "lon": 139.7811},
    "IAD": {"name": "Даллес (Вашингтон)", "country": "США", "lat": 38.9444, "lon": -77.4558},
    "ICN": {"name": "Инчхон (Сеул)", "country": "Южная Корея", "lat": 37.4625, "lon": 126.4392},
    "IST": {"name": "Стамбул (Новый)", "country": "Турция", "lat": 41.2608, "lon": 28.7425},
    "JED": {"name": "Король Абдул-Азиз (Джидда)", "country": "Саудовская Аравия", "lat": 21.6794, "lon": 39.1567},
    "JFK": {"name": "им. Джона Кеннеди (Нью-Йорк)", "country": "США", "lat": 40.6397, "lon": -73.7789},
    "KEF": {"name": "Кеблавик (Рейкьявик)", "country": "Исландия", "lat": 63.9850, "lon": -22.6056},
    "KMG": {"name": "Чаншуй (Куньмин)", "country": "Китай", "lat": 25.1017, "lon": 102.9258},
    "KUL": {"name": "Куала-Лумпур", "country": "Малайзия", "lat": 2.7456, "lon": 101.7100},
    "KWI": {"name": "Кувейт", "country": "Кувейт", "lat": 29.2267, "lon": 47.9800},
    "LAS": {"name": "Гарри Рид (Лас-Вегас)", "country": "США", "lat": 36.0800, "lon": -115.1522},
    "LAX": {"name": "Лос-Анджелес", "country": "США", "lat": 33.9425, "lon": -118.4081},
    "LCA": {"name": "Ларнака", "country": "Кипр", "lat": 34.8789, "lon": 33.6303},
    "LED": {"name": "Пулково (Санкт-Петербург)", "country": "Россия", "lat": 59.8003, "lon": 30.2625},
    "LGW": {"name": "Гатвик (Лондон)", "country": "Великобритания", "lat": 51.1481, "lon": -0.1903},
    "LHR": {"name": "Хитроу (Лондон)", "country": "Великобритания", "lat": 51.4775, "lon": -0.4614},
    "LIS": {"name": "Умберту Делгаду (Лиссабон)", "country": "Португалия", "lat": 38.7783, "lon": -9.1342},
    "LTN": {"name": "Лутон (Лондон)", "country": "Великобритания", "lat": 51.8747, "lon": -0.3683},
    "MAN": {"name": "Манчестер", "country": "Великобритания", "lat": 53.3536, "lon": -2.2750},
    "MCT": {"name": "Маскат", "country": "Оман", "lat": 23.5933, "lon": 58.2844},
    "MIA": {"name": "Майами", "country": "США", "lat": 25.7933, "lon": -80.2906},
    "MLA": {"name": "Мальта", "country": "Мальта", "lat": 35.8575, "lon": 14.4775},
    "NCE": {"name": "Лазурный Берег (Ницца)", "country": "Франция", "lat": 43.6653, "lon": 7.2150},
    "NRT": {"name": "Нарита (Токио)", "country": "Япония", "lat": 35.7653, "lon": 140.3864},
    "ORD": {"name": "О’Хара (Чикаго)", "country": "США", "lat": 41.9786, "lon": -87.9047},
    "ORY": {"name": "Орли (Париж)", "country": "Франция", "lat": 48.7233, "lon": 2.3794},
    "OTP": {"name": "Анри Коанда (Бухарест)", "country": "Румыния", "lat": 44.5711, "lon": 26.0850},
    "OVB": {"name": "Толмачёво (Новосибирск)", "country": "Россия", "lat": 55.0128, "lon": 82.6506},
    "PBI": {"name": "Палм-Бич", "country": "США", "lat": 26.6847, "lon": -80.0947},
    "PEK": {"name": "Шоуду (Пекин Столичный)", "country": "Китай", "lat": 40.0800, "lon": 116.5844},
    "PER": {"name": "Перт", "country": "Австралия", "lat": -31.9403, "lon": 115.9669},
    "PVG": {"name": "Пудун (Шанхай)", "country": "Китай", "lat": 31.1433, "lon": 121.8053},
    "RAK": {"name": "Менара (Марракеш)", "country": "Марокко", "lat": 31.6069, "lon": -8.0364},
    "RIX": {"name": "Рига", "country": "Латвия", "lat": 56.9236, "lon": 23.9711},
    "RUH": {"name": "Король Халид (Эр-Рияд)", "country": "Саудовская Аравия", "lat": 24.9578, "lon": 46.6989},
    "SAW": {"name": "Сабиха Гёкчен (Стамбул)", "country": "Турция", "lat": 40.8983, "lon": 29.4283},
    "SGC": {"name": "Сургут", "country": "Россия", "lat": 61.3431, "lon": 73.4019},
    "SIN": {"name": "Чанги (Сингапур)", "country": "Сингапур", "lat": 1.3503, "lon": 103.9944},
    "SLC": {"name": "Солт-Лейк-Сити", "country": "США", "lat": 40.7883, "lon": -111.9778},
    "SOF": {"name": "София", "country": "Болгария", "lat": 42.6950, "lon": 23.4061},
    "STN": {"name": "Станстед (Лондон)", "country": "Великобритания", "lat": 51.8850, "lon": 0.4450},
    "SVO": {"name": "Шереметьево (Москва)", "country": "Россия", "lat": 55.9728, "lon": 37.4147},
    "SZX": {"name": "Баоань (Шэньчжэнь)", "country": "Китай", "lat": 22.6442, "lon": 113.8108},
    "TEB": {"name": "Тетерборо (Нью-Джерси)", "country": "США", "lat": 40.8500, "lon": -74.0617},
    "TFU": {"name": "Тяньфу (Чэнду)", "country": "Китай", "lat": 30.3208, "lon": 104.4458},
    "TIP": {"name": "Триполи (Международный)", "country": "Ливия", "lat": 32.6694, "lon": 13.1592},
    "TPE": {"name": "Таоюань (Тайбэй)", "country": "Тайвань", "lat": 25.0764, "lon": 121.2239},
    "TUN": {"name": "Тунис-Карфаген", "country": "Тунис", "lat": 36.8511, "lon": 10.2272},
    "VIE": {"name": "Швехат (Вена)", "country": "Австрия", "lat": 48.1103, "lon": 16.5700},
    "VKO": {"name": "Внуково (Москва)", "country": "Россия", "lat": 55.5961, "lon": 37.2678},
    "VNY": {"name": "Ван-Найс (Лос-Анджелес)", "country": "США", "lat": 34.2097, "lon": -118.4900},
    "VVO": {"name": "Кневичи (Владивосток)", "country": "Россия", "lat": 43.3992, "lon": 132.1483},
    "WAW": {"name": "им. Фредерика Шопена (Варшава)", "country": "Польша", "lat": 52.1658, "lon": 21.0064},
    "XMN": {"name": "Гаоци (Сямынь)", "country": "Китай", "lat": 24.5442, "lon": 118.1286},
    "YKS": {"name": "Якутск", "country": "Россия", "lat": 62.0933, "lon": 129.7714},
    "YVR": {"name": "Ванкувер", "country": "Канада", "lat": 49.1942, "lon": -123.1844},
    "ZAG": {"name": "Франьо Туджман (Загреб)", "country": "Хорватия", "lat": 45.7431, "lon": 16.0689},
    "ZIA": {"name": "Жуковский (Москва)", "country": "Россия", "lat": 55.5533, "lon": 38.1517},
    "ZRH": {"name": "Клотен (Цюрих)", "country": "Швейцария", "lat": 47.4647, "lon": 8.5492}
}

# ~ Ниже представлена готовая функция на Python для расчета ортодромического расстояния (кратчайшего расстояния между двумя точками на поверхности Земли) по формуле гаверсинусов (Haversine formula).Функция автоматически извлекает координаты аэропортов из созданного ранее словаря airports_dict по их IATA-кодам.

import math

def calculate_distance(origin_code, dest_code, airports_data):
    """
    Рассчитывает кратчайшее расстояние в километрах между двумя аэропортами.
    
    :param origin_code: IATA-код аэропорта отправления (например, 'SVO')
    :param dest_code: IATA-код аэропорта прибытия (например, 'JFK')
    :param airports_data: Словарь с данными аэропортов (airports_dict)
    :return: Расстояние в километрах (округленное до целого) или None, если код не найден
    """
    # Проверяем наличие кодов в базе данных
    if origin_code not in airports_data or dest_code not in airports_data:
        print(f"Ошибка: Один из кодов ({origin_code} или {dest_code}) не найден в базе.")
        return None
        
    # Извлекаем широту и долготу, переводим их в радианы
    lat1 = math.radians(airports_data[origin_code]["lat"])
    lon1 = math.radians(airports_data[origin_code]["lon"])
    lat2 = math.radians(airports_data[dest_code]["lat"])
    lon2 = math.radians(airports_data[dest_code]["lon"])
    
    # Разница координат
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    
    # Формула гаверсинусов
    a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    
    # Средний радиус Земли в километрах
    EARTH_RADIUS = 6371.0
    
    distance = EARTH_RADIUS * c
    return round(distance)

# --- ПРИМЕР ИСПОЛЬЗОВАНИЯ ---
# Предположим, переменная airports_dict из прошлого шага уже объявлена:

distance = calculate_distance("SVO", "JFK", airports_dict)
print(f"Расстояние между SVO и JFK: {distance} км")

# --------------------------------------------------------
part("3. найти самый длинный и самый короткий по расстоянию рейс")
# --------------------------------------------------------

short = min( [(f['dist'], f) for f in fdata] )
long  = max( [(f['dist'], f) for f in fdata] )

print(f"""
найдено:
самый короткий рейс: {short[0]:5} км, из {short[1]['dept']} в {short[1]['dest']}
самый длинный рейс:  {long[0]:5} км, из {long[1]['dept']} в {long[1]['dest']}
""")

# --------------------------------------------------------
part("4. найти самый длинный и самый короткий по времени рейс")
# --------------------------------------------------------

def minutes(s : str) -> int:
    h, m = s.split()
    h = h[:-1]
    m = m[:-1]
    if h[0] == '0':
        h = h[1]
    if m[0] == '0':
        m = m[1]
    h = int(h)
    m = int(m)
    return h*60 + m

short = min( [(minutes(f['long']), f) for f in fdata] )
long  = max( [(minutes(f['long']), f) for f in fdata] )

print(f"""
найдено:
самый короткий рейс: {short[0]:5} минут, из {short[1]['dept']} в {short[1]['dest']}
самый длинный рейс:  {long[0]:5} минут, из {long[1]['dept']} в {long[1]['dest']}
""")

# --------------------------------------------------------
part("конец")
# --------------------------------------------------------

# ~ ----------------------------------------------------------
# ~ 1. выбрать все типы самолётов
# ~ ----------------------------------------------------------


# ~ Все самолёты: 
# ~ Airbus A220-100, Airbus A220-300, Airbus A319, Airbus A320, Airbus A320neo, Airbus A321, Airbus A321LR, Airbus A321neo, Airbus A330-200, Airbus A330-300, Airbus A340-300, Airbus A350-1000, Airbus A350-900, Airbus A350-900ULR, Airbus A380-800, BAe Systems Avro RJ100, Boeing 737 MAX 8, Boeing 737-500, Boeing 737-700, Boeing 737-800, Boeing 747-400BDSF, Boeing 747-8, Boeing 757-200F, Boeing 767-300ER, Boeing 767-400ER, Boeing 777-200, Boeing 777-200ER, Boeing 777-300ER, Boeing 787-10, Boeing 787-8, Boeing 787-9, CRJ-900, Dash 8 Q400, Embraer 190, Pilatus PC-24, Sukhoi Superjet 100

# ~ Все производители самолётов:
# ~ Airbus, BAe, Boeing, CRJ, Dash, Embraer, Pilatus, Sukhoi

# ~ ----------------------------------------------------------
# ~ 2. выбрать все аэродромы
# ~ ----------------------------------------------------------

# ~ ['ADD', 'AER', 'AGP', 'AKL', 'ALA', 'ALG', 'AMS', 'APA', 'ASE', 'ATH', 'AUH', 'AYT', 'BAH', 'BCN', 'BEG', 'BEY', 'BKK', 'BOM', 'BOS', 'BRU', 'BUD', 'BWN', 'CAI', 'CAN', 'CDG', 'CGK', 'CGO', 'CMN', 'DEL', 'DEN', 'DME', 'DOH', 'DUB', 'DXB', 'EVN', 'EWR', 'FAB', 'FCO', 'FRA', 'GVA', 'HAK', 'HAN', 'HEL', 'HKG', 'HND', 'IAD', 'ICN', 'IST', 'JED', 'JFK', 'KEF', 'KMG', 'KUL', 'KWI', 'LAS', 'LAX', 'LCA', 'LED', 'LGW', 'LHR', 'LIS', 'LTN', 'MAN', 'MCT', 'MIA', 'MLA', 'NCE', 'NRT', 'ORD', 'ORY', 'OTP', 'OVB', 'PBI', 'PEK', 'PER', 'PVG', 'RAK', 'RIX', 'RUH', 'SAW', 'SGC', 'SIN', 'SLC', 'SOF', 'STN', 'SVO', 'SZX', 'TEB', 'TFU', 'TIP', 'TPE', 'TUN', 'VIE', 'VKO', 'VNY', 'VVO', 'WAW', 'XMN', 'YKS', 'YVR', 'ZAG', 'ZIA', 'ZRH']
# ~ Расстояние между SVO и JFK: 7481 км

# ~ ----------------------------------------------------------
# ~ 3. найти самый длинный и самый короткий по расстоянию рейс
# ~ ----------------------------------------------------------


# ~ найдено:
# ~ самый короткий рейс:   210 км, из APA в ASE
# ~ самый длинный рейс:  15340 км, из SIN в EWR


# ~ ----------------------------------------------------------
# ~ 4. найти самый длинный и самый короткий по времени рейс
# ~ ----------------------------------------------------------


# ~ найдено:
# ~ самый короткий рейс:    35 минут, из APA в ASE
# ~ самый длинный рейс:   1125 минут, из SIN в EWR


# ~ ----------------------------------------------------------
# ~ конец
# ~ ----------------------------------------------------------
