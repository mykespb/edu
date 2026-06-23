#!/usr/bin/env python

# Mikhail (myke) Kolodin, 2026
# xml-rss-read.py
# 2026-06-23 2026-06-23 1.0
# Чтение ленты RSS
# Пример: https://lenta.ru/rss

import xml.etree.ElementTree as ET

rss = """<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom">
  <channel>
    <language>ru</language>
    <title>Lenta.ru : Новости</title>
    <description>Новости, статьи, фотографии, видео. Семь дней в неделю, 24 часа в сутки.</description>
    <link>https://lenta.ru</link>
    <image>
      <url>https://lenta.ru/images/small_logo.png</url>
      <title>Lenta.ru</title>
      <link>https://lenta.ru</link>
      <width>134</width>
      <height>22</height>
    </image>
    <atom:link rel="self" type="application/rss+xml" href="http://lenta.ru/rss"/>
<item>
  <guid>https://lenta.ru/news/2026/06/23/u-zhilogo-doma-v-turtsii-upal-neopoznannyy-bespilotnik/</guid>
  <author>Марина Совина</author>
  <title>У жилого дома в Турции упал неопознанный беспилотник</title>
  <link>https://lenta.ru/news/2026/06/23/u-zhilogo-doma-v-turtsii-upal-neopoznannyy-bespilotnik/</link>
  <description>
    <![CDATA[]]>
  </description>
  <pubDate>Tue, 23 Jun 2026 22:10:00 +0300</pubDate>
  <enclosure url="https://icdn.lenta.ru/assets/webpack/images/lenta_og.8735b949.png" type="image/png" length="14407"/>
  <category>Мир</category>
</item>
<item>
  <guid>https://lenta.ru/news/2026/06/23/cbornaya-portugalii-razgromila-uzbekistan-v-matche-chm-2026/</guid>
  <author>Владислав Уткин</author>
  <title>Cборная Португалии разгромила Узбекистан в матче ЧМ-2026</title>
  <link>https://lenta.ru/news/2026/06/23/cbornaya-portugalii-razgromila-uzbekistan-v-matche-chm-2026/</link>
  <description>
    <![CDATA[]]>
  </description>
  <pubDate>Tue, 23 Jun 2026 22:07:48 +0300</pubDate>
  <enclosure url="https://icdn.lenta.ru/images/2026/06/23/22/20260623220647179/pic_d90452088a620f4677f462e0a11c29f7.jpg" type="image/jpeg" length="26289"/>
  <category>Спорт</category>
</item>
<item>
  <guid>https://lenta.ru/news/2026/06/23/ronaldu-ustanovil-rekord-chempionatov-mira/</guid>
  <author>Владислав Уткин</author>
  <title>Роналду установил рекорд чемпионатов мира</title>
  <link>https://lenta.ru/news/2026/06/23/ronaldu-ustanovil-rekord-chempionatov-mira/</link>
  <description>
    <![CDATA[]]>
  </description>
  <pubDate>Tue, 23 Jun 2026 20:22:00 +0300</pubDate>
  <enclosure url="https://icdn.lenta.ru/images/2026/06/23/20/20260623201035333/pic_ec78856b75501eb326ece48591e7ea43.jpg" type="image/jpeg" length="21914"/>
  <category>Спорт</category>
</item>
<item>
  <guid>https://lenta.ru/news/2026/06/23/v-moskve-shkolnitsa-sdala-ege-na-maksimalnoe-kolichestvo-ballov/</guid>
  <author>Никита Абрамов</author>
  <title>В Москве школьница сдала ЕГЭ на максимальное количество баллов</title>
  <link>https://lenta.ru/news/2026/06/23/v-moskve-shkolnitsa-sdala-ege-na-maksimalnoe-kolichestvo-ballov/</link>
  <description>
    <![CDATA[]]>
  </description>
  <pubDate>Tue, 23 Jun 2026 20:20:00 +0300</pubDate>
  <enclosure url="https://icdn.lenta.ru/images/2026/06/23/20/20260623201742947/pic_8a7013774d79b548f31f17ee7e39511f.jpg" type="image/jpeg" length="23788"/>
  <category>Россия</category>
</item>
<item>
<guid>https://lenta.ru/news/2026/06/23/rossiyanam-pokazali-realnye-emotsionalnye-kacheli-iz-zhizni-tigrov/</guid>
  <author>Варвара Кошечкина</author>
  <title>Россиянам показали реальные «эмоциональные качели» из жизни тигров</title>
  <link>https://lenta.ru/news/2026/06/23/rossiyanam-pokazali-realnye-emotsionalnye-kacheli-iz-zhizni-tigrov/</link>
  <description>
    <![CDATA[]]>
  </description>
  <pubDate>Tue, 23 Jun 2026 20:15:00 +0300</pubDate>
  <enclosure url="https://icdn.lenta.ru/images/2026/06/23/20/20260623200016117/pic_f19c2ce24cbdc43b7ae68caafba751c2.jpg" type="image/jpeg" length="28092"/>
  <category>Моя страна</category>
</item>
<item>
  <guid>https://lenta.ru/news/2026/06/23/teleskop-roman-pribyl-vo-floridu-dlya-zapuska/</guid>
  <author>Иван Потапов</author>
  <title>Телескоп Roman прибыл во Флориду для запуска</title>
  <link>https://lenta.ru/news/2026/06/23/teleskop-roman-pribyl-vo-floridu-dlya-zapuska/</link>
  <description>
    <![CDATA[]]>
  </description>
  <pubDate>Tue, 23 Jun 2026 19:54:00 +0300</pubDate>
  <enclosure url="https://icdn.lenta.ru/images/2026/06/23/15/20260623152033517/pic_6ee6379ceb27baad2d2c9057a7634af4.jpg" type="image/jpeg" length="44610"/>
  <category>Наука и техника</category>
</item>
<item>
<guid>https://lenta.ru/news/2026/06/23/nazvan-srok-perehoda-na-novuyu-model-vysshego-obrazovaniya-v-rossii/</guid>
  <author>Елена Торубарова</author>
  <title>Назван срок перехода на новую модель высшего образования в России</title>
<link>https://lenta.ru/news/2026/06/23/nazvan-srok-perehoda-na-novuyu-model-vysshego-obrazovaniya-v-rossii/</link>
  <description>
  </description>
  <pubDate>Tue, 23 Jun 2026 19:51:00 +0300</pubDate>
  <enclosure url="https://icdn.lenta.ru/images/2026/06/23/19/20260623195511966/pic_26d5e29b62f1766085e8372d83a69351.jpg" type="image/jpeg" length="30579"/>
  <category>Россия</category>
</item>
<item>
<guid>https://lenta.ru/news/2026/06/23/biznes-dzhet-za-sotni-millionov-rubley-povredili-v-aeroportu-moskvy/</guid>
  <author>Алина Черненко</author>
  <title>Бизнес-джет за сотни миллионов рублей повредили в аэропорту Москвы</title>
<link>https://lenta.ru/news/2026/06/23/biznes-dzhet-za-sotni-millionov-rubley-povredili-v-aeroportu-moskvy/</link>
  <description>
    <![CDATA[]]>
  </description>
  <pubDate>Tue, 23 Jun 2026 16:28:41 +0300</pubDate>
  <enclosure url="https://icdn.lenta.ru/assets/webpack/images/lenta_og.8735b949.png" type="image/png" length="14407"/>
  <category>Путешествия</category>
</item>
</channel>
</rss>
"""

# 1. get it all

root = ET.fromstring(rss)
# ~ root = tree.getroot()

# 2. print it

print(root.tag)
print(root.attrib)

# 3. get children

# ~ for child in root:
    # ~ print(child.tag, child.attrib)

# 4. go to items

channel = root.find('channel')

# ~ for child in channel:
    # ~ print(child, child.tag, child.attrib)

# 5. iterate

for num, item in enumerate(channel.findall('item'), start=1):
    print("новость", num, ":", item.attrib)
    print("автор:", item.find('author').text)
    print("заголовок:", item.find('title').text)
    
# --------------- конец --------------------
