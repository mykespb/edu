#!/usr/bin/env python
# myke 2026-06-08 2026-06-08 1.0
# london-boros.py

# ~ Есть данные о Лондонских районах вплоть до почтового индекса.
# ~ По каждому есть средневзвешенная общая оценка overall_rating.
# ~ Выполняем интересное по этим данным.

boros = [
  {
    "number": 1,
    "name": "City of London",
    "postcodes": [
      "EC1",
      "EC2",
      "EC3",
      "EC4",
      "WC2"
    ],
    "population": 9000,
    "quality_of_life": 9,
    "crime_rate": 6,
    "average_house_purchase_price_gbp": 950000,
    "annual_rent_3bed_flat_gbp": 54000,
    "greenery_parks": 5,
    "culture": 10,
    "education": 7,
    "education_summary": "Отличные частные школы, но мало государственных из-за низкого числа постоянных жителей.",
    "overall_rating": 8.0
  },
  {
    "number": 2,
    "name": "Barking and Dagenham",
    "postcodes": [
      "IG11",
      "RM8",
      "RM9",
      "RM10"
    ],
    "population": 219000,
    "quality_of_life": 5,
    "crime_rate": 7,
    "average_house_purchase_price_gbp": 340000,
    "annual_rent_3bed_flat_gbp": 24000,
    "greenery_parks": 6,
    "culture": 4,
    "education": 6,
    "education_summary": "Доступные государственные школы, уровень академических успехов средний.",
    "overall_rating": 5.3
  },
  {
    "number": 3,
    "name": "Barnet",
    "postcodes": [
      "NW4",
      "NW7",
      "NW11",
      "N2",
      "N3",
      "N12",
      "N20",
      "HA8"
    ],
    "population": 389000,
    "quality_of_life": 8,
    "crime_rate": 4,
    "average_house_purchase_price_gbp": 600000,
    "annual_rent_3bed_flat_gbp": 31000,
    "greenery_parks": 8,
    "culture": 6,
    "education": 9,
    "education_summary": "Один из лучших районов по числу высокорейтинговых (Outstanding) государственных и грамматических школ.",
    "overall_rating": 7.4
  },
  {
    "number": 4,
    "name": "Bexley",
    "postcodes": [
      "DA5",
      "DA6",
      "DA7",
      "DA8",
      "DA14",
      "DA15",
      "DA16"
    ],
    "population": 247000,
    "quality_of_life": 7,
    "crime_rate": 3,
    "average_house_purchase_price_gbp": 400000,
    "annual_rent_3bed_flat_gbp": 25000,
    "greenery_parks": 8,
    "culture": 4,
    "education": 8,
    "education_summary": "Популярный семейный район с хорошей селективной системой грамматических школ.",
    "overall_rating": 6.6
  },
  {
    "number": 5,
    "name": "Brent",
    "postcodes": [
      "HA0",
      "HA9",
      "NW2",
      "NW6",
      "NW10"
    ],
    "population": 341000,
    "quality_of_life": 6,
    "crime_rate": 7,
    "average_house_purchase_price_gbp": 530000,
    "annual_rent_3bed_flat_gbp": 29000,
    "greenery_parks": 6,
    "culture": 7,
    "education": 7,
    "education_summary": "Высокое культурное разнообразие, школы имеют стабильные средние и хорошие показатели.",
    "overall_rating": 6.3
  },
  {
    "number": 6,
    "name": "Bromley",
    "postcodes": [
      "BR1",
      "BR2",
      "BR3",
      "BR4",
      "BR5",
      "BR6",
      "BR7"
    ],
    "population": 331000,
    "quality_of_life": 8,
    "crime_rate": 3,
    "average_house_purchase_price_gbp": 520000,
    "annual_rent_3bed_flat_gbp": 27000,
    "greenery_parks": 9,
    "culture": 5,
    "education": 8,
    "education_summary": "Самый зеленый район Лондона с отличной репутацией начальных и средних школ.",
    "overall_rating": 7.3
  },
  {
    "number": 7,
    "name": "Camden",
    "postcodes": [
      "NW1",
      "NW3",
      "NW5",
      "NW8",
      "WC1",
      "N6"
    ],
    "population": 211000,
    "quality_of_life": 9,
    "crime_rate": 8,
    "average_house_purchase_price_gbp": 870000,
    "annual_rent_3bed_flat_gbp": 48000,
    "greenery_parks": 8,
    "culture": 10,
    "education": 9,
    "education_summary": "Включает престижные университеты (UCL) и школы топ-уровня, но цены очень высокие.",
    "overall_rating": 8.7
  },
  {
    "number": 8,
    "name": "Croydon",
    "postcodes": [
      "CR0",
      "CR2",
      "CR7",
      "CR8",
      "SE25"
    ],
    "population": 391000,
    "quality_of_life": 6,
    "crime_rate": 7,
    "average_house_purchase_price_gbp": 410000,
    "annual_rent_3bed_flat_gbp": 25000,
    "greenery_parks": 7,
    "culture": 6,
    "education": 7,
    "education_summary": "Крупный транспортный узел с большим выбором колледжей дальнего образования и средних школ.",
    "overall_rating": 6.1
  },
  {
    "number": 9,
    "name": "Ealing",
    "postcodes": [
      "W5",
      "W13",
      "W7",
      "UB1",
      "UB2",
      "NW10"
    ],
    "population": 368000,
    "quality_of_life": 8,
    "crime_rate": 5,
    "average_house_purchase_price_gbp": 540000,
    "annual_rent_3bed_flat_gbp": 30000,
    "greenery_parks": 8,
    "culture": 7,
    "education": 8,
    "education_summary": "Известен как 'королева пригородов' за обилие зелени и качественные семейные школы.",
    "overall_rating": 7.5
  },
  {
    "number": 10,
    "name": "Enfield",
    "postcodes": [
      "EN1",
      "EN2",
      "EN3",
      "N9",
      "N13",
      "N14",
      "N21"
    ],
    "population": 330000,
    "quality_of_life": 6,
    "crime_rate": 6,
    "average_house_purchase_price_gbp": 440000,
    "annual_rent_3bed_flat_gbp": 25000,
    "greenery_parks": 8,
    "culture": 5,
    "education": 7,
    "education_summary": "Хорошие зеленые зоны на севере, школы демонстрируют стабильные средние показатели.",
    "overall_rating": 6.4
  },
  {
    "number": 11,
    "name": "Greenwich",
    "postcodes": [
      "SE10",
      "SE3",
      "SE7",
      "SE18",
      "SE28"
    ],
    "population": 290000,
    "quality_of_life": 8,
    "crime_rate": 6,
    "average_house_purchase_price_gbp": 480000,
    "annual_rent_3bed_flat_gbp": 29000,
    "greenery_parks": 8,
    "culture": 9,
    "education": 7,
    "education_summary": "Дом для Университета Гринвича; школы сильно различаются в зависимости от микрорайона.",
    "overall_rating": 7.7
  },
  {
    "number": 12,
    "name": "Hackney",
    "postcodes": [
      "E5",
      "E8",
      "E9",
      "N16",
      "N1"
    ],
    "population": 260000,
    "quality_of_life": 8,
    "crime_rate": 7,
    "average_house_purchase_price_gbp": 620000,
    "annual_rent_3bed_flat_gbp": 36000,
    "greenery_parks": 7,
    "culture": 9,
    "education": 8,
    "education_summary": "Джентрифицированный хипстерский район; за последние годы качество школ сильно выросло.",
    "overall_rating": 7.7
  },
  {
    "number": 13,
    "name": "Hammersmith and Fulham",
    "postcodes": [
      "W6",
      "W14",
      "SW6"
    ],
    "population": 183000,
    "quality_of_life": 9,
    "crime_rate": 6,
    "average_house_purchase_price_gbp": 850000,
    "annual_rent_3bed_flat_gbp": 44000,
    "greenery_parks": 7,
    "culture": 8,
    "education": 9,
    "education_summary": "Выдающиеся государственные и частные школы, высокий уровень жизни у реки.",
    "overall_rating": 8.3
  },
  {
    "number": 14,
    "name": "Haringey",
    "postcodes": [
      "N4",
      "N8",
      "N10",
      "N15",
      "N17",
      "N22"
    ],
    "population": 264000,
    "quality_of_life": 7,
    "crime_rate": 7,
    "average_house_purchase_price_gbp": 570000,
    "annual_rent_3bed_flat_gbp": 30000,
    "greenery_parks": 7,
    "culture": 7,
    "education": 7,
    "education_summary": "Контрастный район (богатый запад вроде Highgate и более бедные восточные окраины).",
    "overall_rating": 6.8
  },
  {
    "number": 15,
    "name": "Harrow",
    "postcodes": [
      "HA1",
      "HA2",
      "HA3",
      "HA5",
      "HA7"
    ],
    "population": 261000,
    "quality_of_life": 8,
    "crime_rate": 4,
    "average_house_purchase_price_gbp": 510000,
    "annual_rent_3bed_flat_gbp": 27000,
    "greenery_parks": 7,
    "culture": 5,
    "education": 9,
    "education_summary": "Родина знаменитой школы Harrow School. Государственный сектор также очень силен.",
    "overall_rating": 7.3
  },
  {
    "number": 16,
    "name": "Havering",
    "postcodes": [
      "RM1",
      "RM2",
      "RM3",
      "RM7",
      "RM11",
      "RM12",
      "RM14"
    ],
    "population": 262000,
    "quality_of_life": 7,
    "crime_rate": 4,
    "average_house_purchase_price_gbp": 420000,
    "annual_rent_3bed_flat_gbp": 23000,
    "greenery_parks": 8,
    "culture": 4,
    "education": 7,
    "education_summary": "Окраина Лондона с пригородной атмосферой и неплохими базовыми школами.",
    "overall_rating": 6.3
  },
  {
    "number": 17,
    "name": "Hillingdon",
    "postcodes": [
      "UB3",
      "UB7",
      "UB8",
      "UB10",
      "HA4",
      "HA6"
    ],
    "population": 306000,
    "quality_of_life": 7,
    "crime_rate": 5,
    "average_house_purchase_price_gbp": 460000,
    "annual_rent_3bed_flat_gbp": 26000,
    "greenery_parks": 8,
    "culture": 5,
    "education": 7,
    "education_summary": "Включает аэропорт Хитроу и Университет Брунеля. Хороший баланс цены и инфраструктуры.",
    "overall_rating": 6.7
  },
  {
    "number": 18,
    "name": "Hounslow",
    "postcodes": [
      "TW3",
      "TW4",
      "TW5",
      "TW7",
      "W4"
    ],
    "population": 288000,
    "quality_of_life": 7,
    "crime_rate": 6,
    "average_house_purchase_price_gbp": 490000,
    "annual_rent_3bed_flat_gbp": 28000,
    "greenery_parks": 7,
    "culture": 6,
    "education": 7,
    "education_summary": "Район сильно отличается от элитного Chiswick на востоке до индустриального запада.",
    "overall_rating": 6.8
  },
  {
    "number": 19,
    "name": "Islington",
    "postcodes": [
      "N1",
      "N5",
      "N7",
      "N19",
      "EC1"
    ],
    "population": 220000,
    "quality_of_life": 9,
    "crime_rate": 7,
    "average_house_purchase_price_gbp": 720000,
    "annual_rent_3bed_flat_gbp": 40000,
    "greenery_parks": 6,
    "culture": 9,
    "education": 8,
    "education_summary": "Центральный жилой район с высокой плотностью застройки и отличными школами.",
    "overall_rating": 8.0
  },
  {
    "number": 20,
    "name": "Kensington and Chelsea",
    "postcodes": [
      "SW3",
      "SW5",
      "SW7",
      "SW10",
      "W8",
      "W10",
      "W11"
    ],
    "population": 144000,
    "quality_of_life": 10,
    "crime_rate": 6,
    "average_house_purchase_price_gbp": 1300000,
    "annual_rent_3bed_flat_gbp": 65000,
    "greenery_parks": 8,
    "culture": 10,
    "education": 10,
    "education_summary": "Самый дорогой район страны. Элитные частные школы и лучшие музеи мира.",
    "overall_rating": 9.2
  },
  {
    "number": 21,
    "name": "Kingston upon Thames",
    "postcodes": [
      "KT1",
      "KT2",
      "KT3",
      "KT6"
    ],
    "population": 168000,
    "quality_of_life": 9,
    "crime_rate": 3,
    "average_house_purchase_price_gbp": 570000,
    "annual_rent_3bed_flat_gbp": 29000,
    "greenery_parks": 8,
    "culture": 7,
    "education": 9,
    "education_summary": "Один из лучших районов для воспитания детей; безопасный, с топовыми школами.",
    "overall_rating": 8.2
  },
  {
    "number": 22,
    "name": "Lambeth",
    "postcodes": [
      "SE1",
      "SE11",
      "SW2",
      "SW4",
      "SW8",
      "SW9",
      "SW16"
    ],
    "population": 318000,
    "quality_of_life": 8,
    "crime_rate": 7,
    "average_house_purchase_price_gbp": 540000,
    "annual_rent_3bed_flat_gbp": 34000,
    "greenery_parks": 7,
    "culture": 9,
    "education": 7,
    "education_summary": "Включает культурный центр South Bank. Школы в основном хорошие, но есть перенаселенность.",
    "overall_rating": 7.5
  },
  {
    "number": 23,
    "name": "Lewisham",
    "postcodes": [
      "SE4",
      "SE6",
      "SE13",
      "SE14",
      "SE23"
    ],
    "population": 301000,
    "quality_of_life": 7,
    "crime_rate": 6,
    "average_house_purchase_price_gbp": 450000,
    "annual_rent_3bed_flat_gbp": 26000,
    "greenery_parks": 7,
    "culture": 7,
    "education": 7,
    "education_summary": "Популярен среди студентов (Goldsmiths University) и молодых семей.",
    "overall_rating": 6.9
  },
  {
    "number": 24,
    "name": "Merton",
    "postcodes": [
      "SW19",
      "SW20",
      "CR4"
    ],
    "population": 215000,
    "quality_of_life": 8,
    "crime_rate": 4,
    "average_house_purchase_price_gbp": 570000,
    "annual_rent_3bed_flat_gbp": 31000,
    "greenery_parks": 8,
    "culture": 7,
    "education": 8,
    "education_summary": "Включает Уимблдон. Прекрасные зеленые зоны и очень престижные школы.",
    "overall_rating": 7.8
  },
  {
    "number": 25,
    "name": "Newham",
    "postcodes": [
      "E6",
      "E7",
      "E12",
      "E13",
      "E15",
      "E16"
    ],
    "population": 351000,
    "quality_of_life": 5,
    "crime_rate": 8,
    "average_house_purchase_price_gbp": 410000,
    "annual_rent_3bed_flat_gbp": 26000,
    "greenery_parks": 6,
    "culture": 6,
    "education": 7,
    "education_summary": "Район Олимпийского парка. Инфраструктура улучшается, но уровень преступности высок.",
    "overall_rating": 5.8
  },
  {
    "number": 26,
    "name": "Redbridge",
    "postcodes": [
      "IG1",
      "IG2",
      "IG3",
      "IG8",
      "E18"
    ],
    "population": 310000,
    "quality_of_life": 7,
    "crime_rate": 5,
    "average_house_purchase_price_gbp": 480000,
    "annual_rent_3bed_flat_gbp": 26000,
    "greenery_parks": 7,
    "culture": 5,
    "education": 9,
    "education_summary": "Привлекает семьи ради сильных государственных и грамматических школ (напр., Ilford County).",
    "overall_rating": 7.0
  },
  {
    "number": 27,
    "name": "Richmond upon Thames",
    "postcodes": [
      "TW9",
      "TW10",
      "TW11",
      "TW12",
      "SW13",
      "SW14"
    ],
    "population": 195000,
    "quality_of_life": 10,
    "crime_rate": 2,
    "average_house_purchase_price_gbp": 760000,
    "annual_rent_3bed_flat_gbp": 38000,
    "greenery_parks": 10,
    "culture": 8,
    "education": 10,
    "education_summary": "Самый безопасный и один из самых зеленых районов Лондона с выдающимся образованием.",
    "overall_rating": 9.1
  },
  {
    "number": 28,
    "name": "Southwark",
    "postcodes": [
      "SE1",
      "SE5",
      "SE15",
      "SE16",
      "SE21",
      "SE22"
    ],
    "population": 307000,
    "quality_of_life": 8,
    "crime_rate": 7,
    "average_house_purchase_price_gbp": 560000,
    "annual_rent_3bed_flat_gbp": 35000,
    "greenery_parks": 7,
    "culture": 9,
    "education": 8,
    "education_summary": "Отличные школы в районе Dulwich. Огромное количество галерей (Tate Modern) и театров.",
    "overall_rating": 7.8
  },
  {
    "number": 29,
    "name": "Sutton",
    "postcodes": [
      "SM1",
      "SM2",
      "SM3",
      "SM4",
      "SM5",
      "SM6"
    ],
    "population": 207000,
    "quality_of_life": 8,
    "crime_rate": 3,
    "average_house_purchase_price_gbp": 430000,
    "annual_rent_3bed_flat_gbp": 24000,
    "greenery_parks": 8,
    "culture": 4,
    "education": 9,
    "education_summary": "Стабильно входит в топ-3 по качеству школьного образования в Лондоне.",
    "overall_rating": 7.1
  },
  {
    "number": 30,
    "name": "Tower Hamlets",
    "postcodes": [
      "E1",
      "E2",
      "E3",
      "E14"
    ],
    "population": 325000,
    "quality_of_life": 6,
    "crime_rate": 8,
    "average_house_purchase_price_gbp": 490000,
    "annual_rent_3bed_flat_gbp": 33000,
    "greenery_parks": 6,
    "culture": 8,
    "education": 7,
    "education_summary": "Район контрастов (Канари-Уорф и Тауэр). Школы развиваются быстро, но переполнены.",
    "overall_rating": 6.3
  },
  {
    "number": 31,
    "name": "Waltham Forest",
    "postcodes": [
      "E4",
      "E10",
      "E11",
      "E17"
    ],
    "population": 278000,
    "quality_of_life": 7,
    "crime_rate": 6,
    "average_house_purchase_price_gbp": 490000,
    "annual_rent_3bed_flat_gbp": 27000,
    "greenery_parks": 8,
    "culture": 7,
    "education": 7,
    "education_summary": "Близость к лесу Epping Forest делает его привлекательным для семей среднего класса.",
    "overall_rating": 7.0
  },
  {
    "number": 32,
    "name": "Wandsworth",
    "postcodes": [
      "SW11",
      "SW12",
      "SW15",
      "SW17",
      "SW18"
    ],
    "population": 327000,
    "quality_of_life": 9,
    "crime_rate": 4,
    "average_house_purchase_price_gbp": 740000,
    "annual_rent_3bed_flat_gbp": 38000,
    "greenery_parks": 8,
    "culture": 7,
    "education": 9,
    "education_summary": "Очень популярный, безопасный и семейный район к югу от реки с прекрасными школами.",
    "overall_rating": 8.3
  },
  {
    "number": 33,
    "name": "Westminster",
    "postcodes": [
      "W1",
      "W2",
      "SW1",
      "NW8",
      "WC2"
    ],
    "population": 204000,
    "quality_of_life": 9,
    "crime_rate": 8,
    "average_house_purchase_price_gbp": 1050000,
    "annual_rent_3bed_flat_gbp": 58000,
    "greenery_parks": 9,
    "culture": 10,
    "education": 9,
    "education_summary": "Сердце Лондона. Королевские парки, главные достопримечательности и престижные академии.",
    "overall_rating": 8.9
  }
]

# ------------------------------------------------
# Найдём лучшие почтовые индексы.
# ------------------------------------------------

def best_postals():
    print("best_postals")
    
    boros.sort(key = lambda x: x["overall_rating"], reverse=True)

    best = []
    for bn in range(3):
        best.extend(q := boros[bn]['postcodes'])
        # ~ print(q)
    best.sort()

    print(best)


best_postals()

# ------------------------------------------------

# ~ https://ru.wikipedia.org/wiki/%D0%91%D0%BE%D1%80%D0%BE_%D0%9B%D0%BE%D0%BD%D0%B4%D0%BE%D0%BD%D0%B0
# ~ https://en.wikipedia.org/wiki/List_of_London_boroughs

# ------------------------------------------------
