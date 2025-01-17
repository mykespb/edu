#!/usr/bin/env python

# Mikhail (myke) Kolodin, 2025
# 2025-01-17 2025-01-17 1.0
# what-lang.py

# ~ Язык сообщения

# ~ Даны несколько сообщений.
# ~ Каждое написано на русском либо английском языке.
# ~ Определить, какое на каком.
# ~ В сообщении могу быть небольшие вкрапления слов на соседнем или даже вообще других языках.

# -------------------------------------------------
# тексты

tests = """
Язык сообщения. Даны несколько сообщений. Каждое написано на русском либо английском языке. Определить, какое на каком.
1. Не откладывай до завтра, что можешь сделать сегодня. 2. Не заставляй другого делать то, что можешь сделать сам. 3. Гордость обходится дороже, чем всё, что нужно для еды, питья, жилища, одежды. 4. Сколько мы перемучились из-за того, что не случилось, но лишь могло случиться. 5. Если рассердишься, прежде чем что-нибудь сделаешь или скажешь, сосчитай до десяти. Если не поможет, сосчитай до ста, и это не помогло - сосчитай до тысячи.
И ТО, ЧТО МЫ НАЗЫВЕМ СЧАСТЬЕМ,И ТО, ЧТО НАЗЫВАЕМ НЕСЧАСТЬЕМ, ОДИНАКОВО ПОЛЕЗНО НАМ, ЕСЛИ МЫ СМОТРИМ НА ТО И НА ДРУГОЕ, КАК НА ИСПЫТАНИЕ. Л.Н.ТОЛСТОЙ. СВОБОДА НЕ В ТОМ, ЧТОБЫ НЕ СДЕРЖИВАТЬ СЕБЯ, А В ТОМ, ЧТОБЫ ВЛАДЕТЬ СОБОЙ. Ф.М.ДОСТОЕВСКИЙ
Существует десять цифр: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9. Числа состоят из цифр. Число 52 состоит из двух цифр: 5 и 2. Числа с 1 впереди и последующими нулями имеют названия. Всем известны: 10 — десять, 100 — сто, 1000 — тысяча, 1 000 000 — миллион. Так как большие числа с большим числом нулей записывать неудобно, используют сокращения в виде степеней: запись 1011 означает число с 11-ю нулями, запись 1052 означает число с 52-мя нулями и т.д. Приведем названия чисел с десятками и сотнями нулей.
Benjamin Franklin (January 17, 1706 – April 17, 1790) was an American polymath: a writer, scientist, inventor, statesman, diplomat, printer, publisher and political philosopher. Among the most influential intellectuals of his time, Franklin was one of the Founding Fathers of the United States; a drafter and signer of the Declaration of Independence; and the first postmaster general. Franklin became a successful newspaper editor and printer in Philadelphia, the leading city in the colonies, publishing The Pennsylvania Gazette at age 23. He became wealthy publishing this and Poor Richard's Almanack, which he wrote under the pseudonym "Richard Saunders". As a scientist, his studies of electricity made him a major figure in the American Enlightenment and the history of physics. His inventions include the lightning rod, bifocals, glass harmonica and the Franklin stove. This 1778 portrait of Franklin was painted by Joseph Duplessis.
Англи́йский язы́к (самоназвание — English, the English language) — язык англо-фризской подгруппы западной группы германской ветви индоевропейской языковой семьи. Английский язык — важнейший международный язык, что является следствием колониальной политики Британской империи в XIX и первой половине XX века, а также мирового влияния Соединённых Штатов Америки в XX—XXI веках. Является одним из наиболее распространённых языков в мире. Существует значительное разнообразие диалектов и говоров английского языка.
Кокни (Cockney) — термин для ряда исторических диалектов районов и ремесленных цехов Лондона. Скауз (Scouse) — диалект жителей Ливерпуля. Джорди[англ.] — диалект жителей Нортумберленда, в частности, Ньюкасла на Тайне. West Country East England (Восточная Англия) Birmingham (Brummy, Brummie) (Бирмингем) Cheshire (Чешир) Cornwall (Корнуолл) Cumberland (Камберленд) Central Cumberland (Центральный Камберленд) Devonshire (Девоншир) East Devonshire (Восточный Девоншир) Dorset (Дорсет) Durham (Дарэм) Bolton Lancashire (Болтон в Лэнкэшир) North Lancashire Radcliffe Lancashire Northumberland (Нортумберленд) Norfolk (Норфолк) Tyneside Northumberland (Тайнсайд Нортумберленд) Somerset (Сомерсет) Sussex (Сассекс) Westmorland (Уэстморленд) North Wiltshire (Уилтшир) Craven Yorkshire (Йоркшир) North Yorkshire (Северный Йоркшир) Sheffield Yorkshire (Шеффилд) West Yorkshire (Западный Йоркшир)
English is a West Germanic language in the Indo-European language family, whose speakers, called Anglophones, originated in early medieval England on the island of Great Britain.[4][5][6] The namesake of the language is the Angles, one of the ancient Germanic peoples that migrated to Britain. It is the most spoken language in the world, primarily due to the global influences of the former British Empire (succeeded by the Commonwealth of Nations) and the United States.[7] English is the third-most spoken native language, after Mandarin Chinese and Spanish;[8] it is also the most widely learned second language in the world, with more second-language speakers than native speakers.
Браузер — компьютерная программа для просмотра веб-страниц. Существует довольно много браузеров. Одни из самых популярных: Google Chrome, Microsoft Edge, Mozilla Firefox, Safari и Opera.
"""

# -------------------------------------------------
# импорты и настройки

lataz  = "abcdefghijklmnopqrstuvwxyz"
latAZ  = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
rusaya = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
rusAYA = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"

alfnames = {
    lataz   : 'English',
    latAZ   : 'English',
    rusaya  : 'Russian', 
    rusAYA  : 'Russian'
    }

# -------------------------------------------------
# определители

def dotest(text):
    """один текст на тест!"""

    cnt = {}
    cnt['English'] = 0
    cnt['Russian'] = 0

    for char in text:
        for alf in alfnames:
            if char in alf:
                cnt[alfnames[alf]] += 1

    return "English" if cnt["English"] > cnt["Russian"] else "Russian", cnt

# -------------------------------------------------
# тесты

def testing():
    """тестируем всё!!"""

    for test in tests.strip().splitlines():
        result, because = dotest(test)
        print(f"""
-------------------------------------------------------------------
text:
{test}
-------------------------------------------------------------------
result:
language = {result}
because  : {because}
-------------------------------------------------------------------

""")

testing()

# -------------------------------------------------
# результаты

# ~ -------------------------------------------------------------------
# ~ text:
# ~ Кокни (Cockney) — термин для ряда исторических диалектов районов и ремесленных цехов Лондона. Скауз (Scouse) — диалект жителей Ливерпуля. Джорди[англ.] — диалект жителей Нортумберленда, в частности, Ньюкасла на Тайне. West Country East England (Восточная Англия) Birmingham (Brummy, Brummie) (Бирмингем) Cheshire (Чешир) Cornwall (Корнуолл) Cumberland (Камберленд) Central Cumberland (Центральный Камберленд) Devonshire (Девоншир) East Devonshire (Восточный Девоншир) Dorset (Дорсет) Durham (Дарэм) Bolton Lancashire (Болтон в Лэнкэшир) North Lancashire Radcliffe Lancashire Northumberland (Нортумберленд) Norfolk (Норфолк) Tyneside Northumberland (Тайнсайд Нортумберленд) Somerset (Сомерсет) Sussex (Сассекс) Westmorland (Уэстморленд) North Wiltshire (Уилтшир) Craven Yorkshire (Йоркшир) North Yorkshire (Северный Йоркшир) Sheffield Yorkshire (Шеффилд) West Yorkshire (Западный Йоркшир)
# ~ -------------------------------------------------------------------
# ~ result:
# ~ language = Russian
# ~ because  : {'English': 329, 'Russian': 398}
# ~ -------------------------------------------------------------------

# ~ -------------------------------------------------------------------
# ~ text:
# ~ Браузер — компьютерная программа для просмотра веб-страниц. Существует довольно много браузеров. Одни из самых популярных: Google Chrome, Microsoft Edge, Mozilla Firefox, Safari и Opera.
# ~ -------------------------------------------------------------------
# ~ result:
# ~ language = Russian
# ~ because  : {'English': 50, 'Russian': 104}
# ~ -------------------------------------------------------------------

# -------------------------------------------------
