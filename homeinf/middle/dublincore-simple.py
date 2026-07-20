#!/usr/bin/env python
# myke 2026-06-25 2026-06-26 1.0
# dublincore-simple.py

# ------------------------ постановка -----------------------------

# ~ Дано описание книги в формате Dublin Core.
# ~ Перевести его между версиями text, xml и jsonld.

# ~ Нужна функция вида dc(info: str, sfrom: str, sto: sto) -> str
# ~ где
# ~ info:  исходный текст в одном из форматов
# ~ sfrom: указание на исходный формат (строка 'text', 'xml', 'jsonld')
# ~ sto:   указание на результирующий формат (строка 'text', 'xml', 'jsonld')
# ~ на выходе - текст описания в результирующем формате.

# ~ Упрощения для простой версии:
# ~ 1. все данные для каждого параметра находятся на одной строке,
# ~ нет переводов строк внутри текстов.

# ------------------------ данные -----------------------------

text = """
* dc:title - Архитектура современных веб-приложений
* dc:creator - Иванов, П. С.
* dc:creator - Петров, А. В.
* dc:subject - Веб-разработка, Архитектура ПО, Python, JavaScript
* dc:description - Учебное пособие по проектированию высоконагруженных веб-систем для студентов вузов.
* dc:publisher - ТехноМедиа
* dc:date - 2024
* dc:type - Text
* dc:format - application/pdf
* dc:identifier - ISBN 978-5-1234-5678-9
* dc:language - rus
* dc:relation - Второе издание, переработанное и дополненное.
* dc:rights - Copyright 2024, Издательство ТехноМедиа. Все права защищены.
"""

xml = """
<metadata xmlns:dc="http://purl.org">
    <dc:title>Архитектура современных веб-приложений</dc:title>
    <dc:creator>Иванов, П. С.</dc:creator>
    <dc:creator>Petrov, A. V.</dc:creator>
    <dc:subject>Веб-разработка, Архитектура ПО, Python, JavaScript</dc:subject>
    <dc:description>Учебное пособие по проектированию высоконагруженных веб-систем для студентов вузов.</dc:description>
    <dc:publisher>ТехноМедиа</dc:publisher>
    <dc:date>2024</dc:date>
    <dc:type>Text</dc:type>
    <dc:format>application/pdf</dc:format>
    <dc:identifier>urn:isbn:978-5-1234-5678-9</dc:identifier>
    <dc:language>rus</dc:language>
    <dc:relation>Второе издание, переработанное и дополненное.</dc:relation>
    <dc:rights>Copyright 2024, Издательство ТехноМедиа.</dc:rights>
</metadata>
"""

jsonld = """
{
  "@context": {
    "dc": "http://purl.org"
  },
  "@type": "dc:Text",
  "dc:title": "Архитектура современных веб-приложений",
  "dc:creator": ["Иванов, П. С.", "Петров, А. В."],
  "dc:subject": "Веб-разработка, Архитектура ПО, Python, JavaScript",
  "dc:description": "Учебное пособие по проектированию высоконагруженных веб-систем для студентов вузов.",
  "dc:publisher": "ТехноМедиа",
  "dc:date": "2024",
  "dc:format": "application/pdf",
  "dc:identifier": "ISBN 978-5-1234-5678-9",
  "dc:language": "rus",
  "dc:relation": "Второе издание, переработанное и дополненное.",
  "dc:rights": "Copyright 2024, Издательство ТехноМедиа."
}
"""

# ------------------------------------------------
# ------------------------ подготовка -----------------------------

import json
from pprint import pp, pprint
import re

# ------------------------------------------------
# ------------------------ обработка -----------------------------

def get_dc_text(info):
    out = {}
    dcCreators = []

    for line in info.strip().split('\n'):
        left, right = line.split(' - ')
        left = left.split()[-1]
        if left == 'dc:creator':
            dcCreators.append(right)
        else:
            out[left] = right
    out['dc:creator'] = dcCreators

    return out

# ------------------------------------------------
    
def get_dc_xml(info):
    out = {}
    dcCreators = []

    for line in info.strip().split('\n'):
        if "<metadata " in line or "</metadata>" in line:
            continue

        pat = r"\s*<dc:(\w+)>(.+)</dc:\w+>"
        fs  = re.search(pat, line)
        if fs:
            left = "dc:" + fs.group(1)
            right = fs.group(2)
            
        if left == 'dc:creator':
            dcCreators.append(right)
        else:
            out[left] = right
    out['dc:creator'] = dcCreators

    return out

# ------------------------------------------------
    
def get_dc_jsonld(info):

    out = {}
    info = json.loads(info)
    
    for k, v in info.items():
        if k == "@context" or k == "@type":
            continue

        out[k] = v

    return out
    
# ------------------------------------------------

def put_dc_text(info):

    out = ""

    for k, v in info.items():
        if k == "dc:creator":
            for a in v:
                out += f"* dc:creator - {a}\n"
        else:
            out += f"* {k} - {v}\n"

    return out

# ------------------------------------------------
    
def put_dc_xml(info):
    
    out = '<metadata xmlns:dc="http://purl.org">\n'

    for k, v in info.items():
        if k == "dc:creator":
            for a in v:
                out += f"<dc:creator>{a}</dc:creator>\n"
        else:
            out += f"<{k}>{v}</k>\n"

    out += '</metadata>\n'

    return out


# ------------------------------------------------
    
def put_dc_jsonld(info):

    out = info.copy()
    out['@context'] = {'dc': 'http://purl.org'}
    out["@type"]    = "dc:Text"

    return out
    

# ------------------------------------------------
# ------------------------------------------------

def dc_read(info: str, sfrom: str) -> dict:
    """
    читатель
    """

    sfrom = sfrom.lower()

    assert sfrom in "text xml jsonld".split(), f"Недопустимый входной формат: '{sfrom}'"

    res = {
        'text':     get_dc_text(info),
        'xml':      get_dc_xml(info),
        'jsonld':   get_dc_jsonld(info),
        }[sfrom]

    return res


# ------------------------------------------------

def dc_write(info: dict, sto: str) -> str:
    """
    писатель
    """

    sto   = sto.lower()

    assert sto in "text xml jsonld".split(), f"Недопустимый выходной формат: '{sto}'"

    res = {
        'text':     put_dc_text(info),
        'xml':      put_dc_xml(info),
        'jsonld':   put_dc_jsonld(info),
        }[sto]

    return res

# ------------------------------------------------

def dc(info: str, sfrom: str, sto: sto) -> str:
    """
    преобразователь
    """

    sfrom = sfrom.lower()
    sto   = sto.lower()

    assert sfrom in "text xml jsonld".split(), f"Недопустимый входной формат: '{sfrom}'"
    assert sto in "text xml jsonld".split(), f"Недопустимый выходной формат: '{sto}'"

    data = dc_read(info, sfrom)
    out  = dc_write(data, sto)
    return out

    
# ------------------------------------------------
# ------------------------ тесты -----------------------------

# tests ok:

# test convertion to dict:

print("\n\n*** text -> dict ***")
ddc = get_dc_text(text)
pprint(ddc)

print("\n\n*** xml -> dict ***")
ddc = get_dc_xml(xml)
pprint(ddc)

print("\n\n*** jsonld -> dict ***")
ddc = get_dc_jsonld(jsonld)
pprint(ddc)

# test convertion from dict:

print("\n\n*** dict -> text ***")
otext = put_dc_text(ddc)
print(otext)

print("\n\n*** dict -> xml ***")
oxml = put_dc_xml(ddc)
print(oxml)

print("\n\n*** dict -> jsonld ***")
ojson = put_dc_jsonld(ddc)
pprint(ojson)

# tests combinations:

print("\n\n*** text -> text ***")
ddc = get_dc_text(text)
otext = put_dc_text(ddc)
pprint(otext)

# tests asserts:

# TBD: ...

# ------------------------------------------------
# ------------------------ доки -----------------------------

# ~ Стандарт Dublin Core (Дублинское ядро) используется для описания цифровых ресурсов (веб-страниц, электронных книг, изображений) в формате метаданных. Он состоит из 15 базовых элементов.
# ~ Ниже приведен пример описания той же самой книги по программированию в трех наиболее популярных форматах представления метаданных: в виде простого текстового списка, XML и JSON-LD.
# ~ ## 1. Простой текстовый вид (Ключ - Значение)

# ~ * dc:title - Архитектура современных веб-приложений
# ~ * dc:creator - Иванов, П. С.
# ~ * dc:creator - Петров, А. В.
# ~ * dc:subject - Веб-разработка, Архитектура ПО, Python, JavaScript
# ~ * dc:description - Учебное пособие по проектированию высоконагруженных веб-систем для студентов вузов.
# ~ * dc:publisher - ТехноМедиа
# ~ * dc:date - 2024
# ~ * dc:type - Text
# ~ * dc:format - application/pdf
# ~ * dc:identifier - ISBN 978-5-1234-5678-9
# ~ * dc:language - rus
# ~ * dc:relation - Второе издание, переработанное и дополненное.
# ~ * dc:rights - Copyright 2024, Издательство ТехноМедиа. Все права защищены.

# ~ ------------------------------
# ~ ## 2. Формат XML
# ~ Этот формат часто применяется в электронных библиотеках и репозиториях для автоматического обмена данными (например, через протокол OAI-PMH).

# ~ <metadata xmlns:dc="http://purl.org">
    # ~ <dc:title>Архитектура современных веб-приложений</dc:title>
    # ~ <dc:creator>Иванов, П. С.</dc:creator>
    # ~ <dc:creator>Petrov, A. V.</dc:creator>
    # ~ <dc:subject>Веб-разработка, Архитектура ПО, Python, JavaScript</dc:subject>
    # ~ <dc:description>Учебное пособие по проектированию высоконагруженных веб-систем для студентов вузов.</dc:description>
    # ~ <dc:publisher>ТехноМедиа</dc:publisher>
    # ~ <dc:date>2024</dc:date>
    # ~ <dc:type>Text</dc:type>
    # ~ <dc:format>application/pdf</dc:format>
    # ~ <dc:identifier>urn:isbn:978-5-1234-5678-9</dc:identifier>
    # ~ <dc:language>rus</dc:language>
    # ~ <dc:relation>Второе издание, переработанное и дополненное.</dc:relation>
    # ~ <dc:rights>Copyright 2024, Издательство ТехноМедиа.</dc:rights>
# ~ </metadata>

# ~ ------------------------------
# ~ ## 3. Формат JSON-LD
# ~ Современный стандарт для интеграции метаданных в веб-страницы, который активно распознается поисковыми роботами (Semantic Web).

# ~ {
  # ~ "@context": {
    # ~ "dc": "http://purl.org"
  # ~ },
  # ~ "@type": "dc:Text",
  # ~ "dc:title": "Архитектура современных веб-приложений",
  # ~ "dc:creator": ["Иванов, П. С.", "Петров, А. В."],
  # ~ "dc:subject": "Веб-разработка, Архитектура ПО, Python, JavaScript",
  # ~ "dc:description": "Учебное пособие по проектированию высоконагруженных веб-систем для студентов вузов.",
  # ~ "dc:publisher": "ТехноМедиа",
  # ~ "dc:date": "2024",
  # ~ "dc:format": "application/pdf",
  # ~ "dc:identifier": "ISBN 978-5-1234-5678-9",
  # ~ "dc:language": "rus",
  # ~ "dc:relation": "Второе издание, переработанное и дополненное.",
  # ~ "dc:rights": "Copyright 2024, Издательство ТехноМедиа."
# ~ }

# ~ ------------------------------

# ~ Вот как это описание выглядит в виде обычной (классической) библиографической записи по действующему стандарту ГОСТ Р 7.0.100–2018:

# ~ Иванов, П. С. Архитектура современных веб-приложений : учебное пособие по проектированию высоконагруженных веб-систем для студентов вузов / П. С. Иванов, А. В. Петров. – 2-е изд., перераб. и доп. – Москва : ТехноМедиа, 2024. – 412 с. – (Первое издание книги «Основы веб-архитектуры» (2020)). – ISBN 978-5-1234-5678-9. – Текст : непосредственный.

# ~ Если вам нужно вставить эту запись в список литературы для диссертации или диплома, то по более простому стандарту ГОСТ Р 7.0.5–2008 (без длинных тире) она оформляется так:

# ~ Иванов П. С., Петров А. В. Архитектура современных веб-приложений: учебное пособие по проектированию высоконагруженных веб-систем для студентов вузов. 2-е изд., перераб. и доп. М.: ТехноМедиа, 2024. 412 с.

# ~ ------------------------------------------
# ~               === URN ===
# ~ ------------------------------------------

# ~ URN (Uniform Resource Name) - это унифицированное имя ресурса, которое служит уникальным постоянным идентификатором объекта в цифровой среде [STEM]. [1, 2, 3, 4] 
# ~ В отличие от URL (который указывает, где лежит файл и по какому протоколу его скачать), URN отвечает на вопрос что это за объект, и не зависит от изменения его местоположения. Если сайт закроется или ссылка сломается, URN книги или документа останется неизменным. [5, 6, 7, 8, 9] 
# ~ ## Структура URN
# ~ Любой URN имеет строго определенный формат:
# ~ urn:<NID>:<NSS> [10, 11] 

# ~ * urn: - обязательный префикс (протоколхема).
# ~ * NID (Namespace Identifier) - идентификатор пространства имен (указывает на тип системы, например: isbn, issn, uuid, ietf).
# ~ * NSS (Namespace Specific String) - уникальная строка внутри этого пространства (номер, код, хэш). [12, 13, 14, 15, 16] 

# ~ ------------------------------
# ~ ## Примеры URN из разных областей:

# ~ * Для книг (на основе ISBN):
# ~ urn:isbn:978-5-1234-5678-9
# ~ (Однозначно идентифицирует конкретное издание книги по всему миру).
# ~ * Для системных идентификаторов (UUID):
# ~ urn:uuid:6e8bc430-9c3a-11d9-9669-0800200c9a66
# ~ (Часто используется в программировании для маркировки уникальных объектов в базах данных).
# ~ * Для научных стандартов и документов RFC:
# ~ urn:ietf:rfc:2648
# ~ (Идентификатор официального интернет-стандарта IETF). [17, 18, 19, 20] 

# ~ ------------------------------
# ~ ## URN в контексте Dublin Core и Библиографии
# ~ В метаданных (таких как Dublin Core, XML, JSON-LD), которые мы рассматривали выше, URN выполняет роль постоянного цифрового паспорта. [21, 22] 
# ~ В коде это выглядит так:
# ~ <dc:identifier xsi:type="dcterms:URI">urn:isbn:978-5-1234-5678-9</dc:identifier>
# ~ Благодаря этому поисковые роботы и библиотечные системы (например, базы данных цитирования Scopus, РИНЦ или eLibrary) понимают, что речь идет об одном и том же физическом объекте, даже если он размещен на десяти разных сайтах.
# ~ Если вы хотите узнать, как URN соотносится с современными DOI (Digital Object Identifier) для научных статей, или вам нужно сгенерировать валидный URN/UUID с помощью Python-скрипта, дайте знать!

# ~ [1] [https://en.wikipedia.org](https://en.wikipedia.org/wiki/Uniform_Resource_Name)
# ~ [2] [https://www.godaddy.com](https://www.godaddy.com/resources/ae/skills/uri-vs-url)
# ~ [3] [https://www.ionos.co.uk](https://www.ionos.co.uk/digitalguide/websites/web-development/uniform-resource-identifier-uri/)
# ~ [4] [https://www.dlib.org](https://www.dlib.org/dlib/february96/02arms.html)
# ~ [5] [https://www.techtarget.com](https://www.techtarget.com/whatis/definition/URN-Uniform-Resource-Name)
# ~ [6] [https://dev.to](https://dev.to/endorama/uri-url-urn-identifying-resources-on-the-web-ebc)
# ~ [7] [https://www.networksolutions.com](https://www.networksolutions.com/blog/uri-vs-url/)
# ~ [8] [https://www.godaddy.com](https://www.godaddy.com/resources/skills/uri-vs-url-vs-urn)
# ~ [9] [https://supertokens.com](https://supertokens.com/blog/url-vs-uri)
# ~ [10] [https://www.techtarget.com](https://www.techtarget.com/whatis/definition/URN-Uniform-Resource-Name)
# ~ [11] [https://docbox.etsi.org](https://docbox.etsi.org/Reference/IETF/RFC/RFC2141.pdf)
# ~ [12] [https://docbox.etsi.org](https://docbox.etsi.org/Reference/IETF/RFC/RFC2141.pdf)
# ~ [13] [https://www.issn.org](https://www.issn.org/services/online-services/urn/)
# ~ [14] [https://dev.to](https://dev.to/endorama/uri-url-urn-identifying-resources-on-the-web-ebc)
# ~ [15] [https://blog.logto.io](https://blog.logto.io/unveiling-uri-url-and-urn)
# ~ [16] [https://www.godaddy.com](https://www.godaddy.com/resources/skills/uri-vs-url-vs-urn)
# ~ [17] [https://www.baeldung.com](https://www.baeldung.com/cs/uniform-resource-identifiers)
# ~ [18] [https://www.techtarget.com](https://www.techtarget.com/whatis/definition/URN-Uniform-Resource-Name)
# ~ [19] [https://www.rfc-editor.org](https://www.rfc-editor.org/info/rfc3553/)
# ~ [20] [https://megamansec.github.io](https://megamansec.github.io/Squid-Security-Audit/urn-memleak.html)
# ~ [21] [https://supertokens.com](https://supertokens.com/blog/url-vs-uri)
# ~ [22] [https://medium.com](https://medium.com/tuanhdotnet/secrets-of-uris-urls-and-urns-understanding-their-differences-and-uses-b2b791af7323)

# ~ === Дублинское ядро === 

# ~ С 1995 года.

# ~ https://www.dublincore.org/
# ~ https://ru.wikipedia.org/wiki/%D0%94%D1%83%D0%B1%D0%BB%D0%B8%D0%BD%D1%81%D0%BA%D0%BE%D0%B5_%D1%8F%D0%B4%D1%80%D0%BE
# ~ https://en.wikipedia.org/wiki/Dublin_Core

# ~ Ду́блинское ядро́ (англ. Dublin Core) - словарь (семантическая сеть) основных понятий английского языка, предназначенный для унификации метаданных для описания широчайшего диапазона ресурсов. С 2005 года словарь представлен и в формате RDF и является популярной основой для описания ресурсов в Семантической паутине.

# ~ Словарь разделён на два уровня:

# ~ простой (неквалифицированный, simple), состоящий из 15 элементов;
# ~ компетентный (квалифицированный, qualified), состоящий из 18 элементов и группы т. н. тонкостей (или квалификаторов), которые уточняют семантику элементов для повышения полезности поиска ресурсов.
# ~ Семантика Дублинского ядра была создана международной междисциплинарной группой профессионалов библиотечного дела, компьютерных наук, кодирования текстов, музейного дела и других смежных групп.

# ~ В России с 1 июля 2011 года действует ГОСТ Р 7.0.10-2010 (ИСО 15836:2003) «Национальный стандарт Российской Федерации. Система стандартов по информации, библиотечному и издательскому делу. Набор элементов метаданных „Дублинское ядро“».

# ~ The Dublin Core vocabulary, also known as the Dublin Core Metadata Terms (DCMT), is a general purpose metadata vocabulary for describing resources of any type. It was first developed for describing web content in the early days of the World Wide Web. The Dublin Core Metadata Initiative (DCMI) is responsible for maintaining the Dublin Core vocabulary.

# ~ In March 1995, in Dublin, Ohio, National Center for Supercomputing Applications and Online Computer Library Center held a joint workshop to discuss metadata semantics.[1]

# ~ Initially developed as fifteen terms in 1998 the set of elements has grown over time and in 2008 was redefined as a Resource Description Framework (RDF) vocabulary.[2]

# ~ Designed with minimal constraints, each Dublin Core element is optional and may be repeated. There is no prescribed order in Dublin Core for presenting or using the elements.

# ~ Дублинское ядро (Dublin Core) получило свое название в честь города Дублин в штате Огайо (США).Именно там в 1995 году прошел рабочий семинар, организованный OCLC (Онлайн-компьютерным библиотечным центром) и Национальным центром суперкомпьютерных приложений. На этой встрече группа специалистов разработала базовый, стандартизированный набор метаданных (информации о данных) для описания сетевых ресурсов, электронных документов и книг.Слово «ядро» отражает суть стандарта: он состоит из минимального, базового списка из 15 элементов (таких как название, автор, дата, тема), которого достаточно для первичного описания любого цифрового объекта.

# ------------------------ конец -----------------------------
