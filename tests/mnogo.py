#!/usr/bin/env python3.10
# mnogo.py
# (C) Mikhail Kolodin, 2021
# ver. 2021-09-29 2021-09-29 1.5
# updated 2021-10-05 to py3.10

# дано натуральное число или 0
# (задаётся случайным образом)
# напечатать его словами

import random

# ----------------------- программа

def slovami(n):
    """ печать словами """

    if n == 0:
        return "нуль"

    razrady = [
        "",
        "тысяч(a,и)",
        "миллион(a,ов)",
        "миллиард(a,ов)",
        "триллион(a,ов)",
        "квадриллион(a,ов)",
        "квинтиллион(a,ов)",
        "секстиллион(a,ов)",
        "септиллион(a,ов)",
        "октиллион(a,ов)",
        "нониллион(a,ов)",
        "дециллион(a,ов)",
        "ундециллион(a,ов)",
        "много"
        ]

    edinicy = {
        0: "",
        1: "один",
        2: "два",
        3: "три",
        4: "четыре",
        5: "пять",
        6: "шесть",
        7: "семь",
        8: "восемь",
        9: "девять"
        }

    desatki = {
        0: "",
        1: "десять",
        2: "двадцать",
        3: "тридцать",
        4: "сорок",
        5: "пятьдесят",
        6: "шестьдесят",
        7: "семьдесят",
        8: "восемьдесят",
        9: "девяносто"
        }

    sotni = {
        0: "",
        1: "сто",
        2: "двести",
        3: "триста",
        4: "четыреста",
        5: "пятьсот",
        6: "шестьсот",
        7: "семьсот",
        8: "восемьсот",
        9: "девятьсот"
        }

    spec = {
        0:  "нуль",
        10: "десять",
        11: "одиннадцать",
        12: "двенадцать",
        13: "тринадцать",
        14: "четырнадцать",
        15: "пятнадцать",
        16: "шестнадцать",
        17: "семнадцать",
        18: "восемнадцать",
        19: "девятнадцать"
        }

    razr = n
    por = 0
    allresult = ""

    while razr:

        n = razr % 1000

        if n == 0:
            result = "ноль"
        else:

            soten = n // 100
            desatkov = (n // 10) % 10
            edinic = n % 10
            des1 = n % 100

            result = sotni[soten] + " " if soten else ""

            if desatkov == 1:
                result += spec[des1]
            else:
                result += desatki[desatkov] + " " if desatkov else ""
                result += edinicy[edinic]

        result = " " +  result + " " + razrady[por] + " "
        por += 1
        razr //= 1000

        allresult = result + allresult

    allresult = allresult.strip()

    return allresult

# ----------------------- тесты

def tests1():
    """ проверка печать """

    nabor = 0, 1, 2, 10, 11, 20, 21, 35, 99, 100, 101, 110, 111, 150, 500, 999

    for i in nabor:
        print("%3d" % i, "->", slovami(i))

def tests2():
    """ проверка печать """

    nabor = [random.randint(1, 999999999999999999999999999999999999999) for _ in range(20)]

    for i in nabor:
        print("{:_}".format(i), "->", slovami(i))

#
tests1()
tests2()

# ----------------------- результаты

  # ~ 0 -> нуль
  # ~ 1 -> один
  # ~ 2 -> два
 # ~ 10 -> десять
 # ~ 11 -> одиннадцать
 # ~ 20 -> двадцать
 # ~ 21 -> двадцать один
 # ~ 35 -> тридцать пять
 # ~ 99 -> девяносто девять
# ~ 100 -> сто
# ~ 101 -> сто один
# ~ 110 -> сто десять
# ~ 111 -> сто одиннадцать
# ~ 150 -> сто пятьдесят
# ~ 500 -> пятьсот
# ~ 999 -> девятьсот девяносто девять

# ~ 228 -> двести двадцать восемь
# ~ 684 -> шестьсот восемьдесят четыре
# ~ 542 -> пятьсот сорок два
# ~ 926 -> девятьсот двадцать шесть
# ~ 320 -> триста двадцать
# ~ 709 -> семьсот девять
# ~  13 -> тринадцать
# ~ 921 -> девятьсот двадцать один
# ~ 376 -> триста семьдесят шесть
# ~ 370 -> триста семьдесят
# ~ 123 -> сто двадцать три
# ~ 335 -> триста тридцать пять
# ~ 197 -> сто девяносто семь
# ~ 715 -> семьсот пятнадцать
# ~ 670 -> шестьсот семьдесят
# ~ 389 -> триста восемьдесят девять
# ~  70 -> семьдесят
# ~ 519 -> пятьсот девятнадцать
# ~ 994 -> девятьсот девяносто четыре
# ~ 949 -> девятьсот сорок девять

# ~ 244_062_670_141_751_160_317_869_120_075_081_112_662 -> двести сорок четыре ундециллион(a,ов)  шестьдесят два дециллион(a,ов)  шестьсот семьдесят  нониллион(a,ов)  сто сорок один октиллион(a,ов)  семьсот пятьдесят один септиллион(a,ов)  сто шестьдесят  секстиллион(a,ов)  триста семнадцать квинтиллион(a,ов)  восемьсот шестьдесят девять квадриллион(a,ов)  сто двадцать  триллион(a,ов)  семьдесят пять миллиард(a,ов)  восемьдесят один миллион(a,ов)  сто двенадцать тысяч(a,и)  шестьсот шестьдесят два
# ~ 788_117_856_872_811_269_376_829_487_223_663_597_142 -> семьсот восемьдесят восемь ундециллион(a,ов)  сто семнадцать дециллион(a,ов)  восемьсот пятьдесят шесть нониллион(a,ов)  восемьсот семьдесят два октиллион(a,ов)  восемьсот одиннадцать септиллион(a,ов)  двести шестьдесят девять секстиллион(a,ов)  триста семьдесят шесть квинтиллион(a,ов)  восемьсот двадцать девять квадриллион(a,ов)  четыреста восемьдесят семь триллион(a,ов)  двести двадцать три миллиард(a,ов)  шестьсот шестьдесят три миллион(a,ов)  пятьсот девяносто семь тысяч(a,и)  сто сорок два
# ~ 54_352_361_438_231_627_582_153_430_198_206_823_617 -> пятьдесят четыре ундециллион(a,ов)  триста пятьдесят два дециллион(a,ов)  триста шестьдесят один нониллион(a,ов)  четыреста тридцать восемь октиллион(a,ов)  двести тридцать один септиллион(a,ов)  шестьсот двадцать семь секстиллион(a,ов)  пятьсот восемьдесят два квинтиллион(a,ов)  сто пятьдесят три квадриллион(a,ов)  четыреста тридцать  триллион(a,ов)  сто девяносто восемь миллиард(a,ов)  двести шесть миллион(a,ов)  восемьсот двадцать три тысяч(a,и)  шестьсот семнадцать
# ~ 800_596_532_335_508_965_803_181_692_564_853_896_824 -> восемьсот  ундециллион(a,ов)  пятьсот девяносто шесть дециллион(a,ов)  пятьсот тридцать два нониллион(a,ов)  триста тридцать пять октиллион(a,ов)  пятьсот восемь септиллион(a,ов)  девятьсот шестьдесят пять секстиллион(a,ов)  восемьсот три квинтиллион(a,ов)  сто восемьдесят один квадриллион(a,ов)  шестьсот девяносто два триллион(a,ов)  пятьсот шестьдесят четыре миллиард(a,ов)  восемьсот пятьдесят три миллион(a,ов)  восемьсот девяносто шесть тысяч(a,и)  восемьсот двадцать четыре
# ~ 995_293_298_301_822_061_317_535_218_356_351_823_762 -> девятьсот девяносто пять ундециллион(a,ов)  двести девяносто три дециллион(a,ов)  двести девяносто восемь нониллион(a,ов)  триста один октиллион(a,ов)  восемьсот двадцать два септиллион(a,ов)  шестьдесят один секстиллион(a,ов)  триста семнадцать квинтиллион(a,ов)  пятьсот тридцать пять квадриллион(a,ов)  двести восемнадцать триллион(a,ов)  триста пятьдесят шесть миллиард(a,ов)  триста пятьдесят один миллион(a,ов)  восемьсот двадцать три тысяч(a,и)  семьсот шестьдесят два
# ~ 114_294_699_292_716_588_285_808_992_272_728_442_930 -> сто четырнадцать ундециллион(a,ов)  двести девяносто четыре дециллион(a,ов)  шестьсот девяносто девять нониллион(a,ов)  двести девяносто два октиллион(a,ов)  семьсот шестнадцать септиллион(a,ов)  пятьсот восемьдесят восемь секстиллион(a,ов)  двести восемьдесят пять квинтиллион(a,ов)  восемьсот восемь квадриллион(a,ов)  девятьсот девяносто два триллион(a,ов)  двести семьдесят два миллиард(a,ов)  семьсот двадцать восемь миллион(a,ов)  четыреста сорок два тысяч(a,и)  девятьсот тридцать
# ~ 402_562_220_674_446_016_603_158_101_612_505_264_546 -> четыреста два ундециллион(a,ов)  пятьсот шестьдесят два дециллион(a,ов)  двести двадцать  нониллион(a,ов)  шестьсот семьдесят четыре октиллион(a,ов)  четыреста сорок шесть септиллион(a,ов)  шестнадцать секстиллион(a,ов)  шестьсот три квинтиллион(a,ов)  сто пятьдесят восемь квадриллион(a,ов)  сто один триллион(a,ов)  шестьсот двенадцать миллиард(a,ов)  пятьсот пять миллион(a,ов)  двести шестьдесят четыре тысяч(a,и)  пятьсот сорок шесть
# ~ 198_624_694_012_724_900_422_966_428_896_325_839_463 -> сто девяносто восемь ундециллион(a,ов)  шестьсот двадцать четыре дециллион(a,ов)  шестьсот девяносто четыре нониллион(a,ов)  двенадцать октиллион(a,ов)  семьсот двадцать четыре септиллион(a,ов)  девятьсот  секстиллион(a,ов)  четыреста двадцать два квинтиллион(a,ов)  девятьсот шестьдесят шесть квадриллион(a,ов)  четыреста двадцать восемь триллион(a,ов)  восемьсот девяносто шесть миллиард(a,ов)  триста двадцать пять миллион(a,ов)  восемьсот тридцать девять тысяч(a,и)  четыреста шестьдесят три
# ~ 290_608_805_679_304_441_516_920_316_140_554_081_077 -> двести девяносто  ундециллион(a,ов)  шестьсот восемь дециллион(a,ов)  восемьсот пять нониллион(a,ов)  шестьсот семьдесят девять октиллион(a,ов)  триста четыре септиллион(a,ов)  четыреста сорок один секстиллион(a,ов)  пятьсот шестнадцать квинтиллион(a,ов)  девятьсот двадцать  квадриллион(a,ов)  триста шестнадцать триллион(a,ов)  сто сорок  миллиард(a,ов)  пятьсот пятьдесят четыре миллион(a,ов)  восемьдесят один тысяч(a,и)  семьдесят семь
# ~ 573_151_514_111_744_328_208_459_367_550_672_132_335 -> пятьсот семьдесят три ундециллион(a,ов)  сто пятьдесят один дециллион(a,ов)  пятьсот четырнадцать нониллион(a,ов)  сто одиннадцать октиллион(a,ов)  семьсот сорок четыре септиллион(a,ов)  триста двадцать восемь секстиллион(a,ов)  двести восемь квинтиллион(a,ов)  четыреста пятьдесят девять квадриллион(a,ов)  триста шестьдесят семь триллион(a,ов)  пятьсот пятьдесят  миллиард(a,ов)  шестьсот семьдесят два миллион(a,ов)  сто тридцать два тысяч(a,и)  триста тридцать пять
# ~ 570_741_307_300_851_481_542_455_112_554_152_672_395 -> пятьсот семьдесят  ундециллион(a,ов)  семьсот сорок один дециллион(a,ов)  триста семь нониллион(a,ов)  триста  октиллион(a,ов)  восемьсот пятьдесят один септиллион(a,ов)  четыреста восемьдесят один секстиллион(a,ов)  пятьсот сорок два квинтиллион(a,ов)  четыреста пятьдесят пять квадриллион(a,ов)  сто двенадцать триллион(a,ов)  пятьсот пятьдесят четыре миллиард(a,ов)  сто пятьдесят два миллион(a,ов)  шестьсот семьдесят два тысяч(a,и)  триста девяносто пять
# ~ 90_819_846_183_763_236_074_915_055_909_242_053_706 -> девяносто  ундециллион(a,ов)  восемьсот девятнадцать дециллион(a,ов)  восемьсот сорок шесть нониллион(a,ов)  сто восемьдесят три октиллион(a,ов)  семьсот шестьдесят три септиллион(a,ов)  двести тридцать шесть секстиллион(a,ов)  семьдесят четыре квинтиллион(a,ов)  девятьсот пятнадцать квадриллион(a,ов)  пятьдесят пять триллион(a,ов)  девятьсот девять миллиард(a,ов)  двести сорок два миллион(a,ов)  пятьдесят три тысяч(a,и)  семьсот шесть
# ~ 361_658_577_201_258_778_032_849_025_309_596_836_790 -> триста шестьдесят один ундециллион(a,ов)  шестьсот пятьдесят восемь дециллион(a,ов)  пятьсот семьдесят семь нониллион(a,ов)  двести один октиллион(a,ов)  двести пятьдесят восемь септиллион(a,ов)  семьсот семьдесят восемь секстиллион(a,ов)  тридцать два квинтиллион(a,ов)  восемьсот сорок девять квадриллион(a,ов)  двадцать пять триллион(a,ов)  триста девять миллиард(a,ов)  пятьсот девяносто шесть миллион(a,ов)  восемьсот тридцать шесть тысяч(a,и)  семьсот девяносто
# ~ 159_924_169_452_382_303_537_412_438_104_648_886_985 -> сто пятьдесят девять ундециллион(a,ов)  девятьсот двадцать четыре дециллион(a,ов)  сто шестьдесят девять нониллион(a,ов)  четыреста пятьдесят два октиллион(a,ов)  триста восемьдесят два септиллион(a,ов)  триста три секстиллион(a,ов)  пятьсот тридцать семь квинтиллион(a,ов)  четыреста двенадцать квадриллион(a,ов)  четыреста тридцать восемь триллион(a,ов)  сто четыре миллиард(a,ов)  шестьсот сорок восемь миллион(a,ов)  восемьсот восемьдесят шесть тысяч(a,и)  девятьсот восемьдесят пять
# ~ 497_532_216_761_948_185_446_242_267_146_992_414_741 -> четыреста девяносто семь ундециллион(a,ов)  пятьсот тридцать два дециллион(a,ов)  двести шестнадцать нониллион(a,ов)  семьсот шестьдесят один октиллион(a,ов)  девятьсот сорок восемь септиллион(a,ов)  сто восемьдесят пять секстиллион(a,ов)  четыреста сорок шесть квинтиллион(a,ов)  двести сорок два квадриллион(a,ов)  двести шестьдесят семь триллион(a,ов)  сто сорок шесть миллиард(a,ов)  девятьсот девяносто два миллион(a,ов)  четыреста четырнадцать тысяч(a,и)  семьсот сорок один
# ~ 664_164_361_817_078_085_719_862_487_009_689_340_382 -> шестьсот шестьдесят четыре ундециллион(a,ов)  сто шестьдесят четыре дециллион(a,ов)  триста шестьдесят один нониллион(a,ов)  восемьсот семнадцать октиллион(a,ов)  семьдесят восемь септиллион(a,ов)  восемьдесят пять секстиллион(a,ов)  семьсот девятнадцать квинтиллион(a,ов)  восемьсот шестьдесят два квадриллион(a,ов)  четыреста восемьдесят семь триллион(a,ов)  девять миллиард(a,ов)  шестьсот восемьдесят девять миллион(a,ов)  триста сорок  тысяч(a,и)  триста восемьдесят два
# ~ 436_115_486_923_916_159_550_393_882_741_149_825_711 -> четыреста тридцать шесть ундециллион(a,ов)  сто пятнадцать дециллион(a,ов)  четыреста восемьдесят шесть нониллион(a,ов)  девятьсот двадцать три октиллион(a,ов)  девятьсот шестнадцать септиллион(a,ов)  сто пятьдесят девять секстиллион(a,ов)  пятьсот пятьдесят  квинтиллион(a,ов)  триста девяносто три квадриллион(a,ов)  восемьсот восемьдесят два триллион(a,ов)  семьсот сорок один миллиард(a,ов)  сто сорок девять миллион(a,ов)  восемьсот двадцать пять тысяч(a,и)  семьсот одиннадцать
# ~ 206_813_647_639_158_361_889_892_366_153_723_397_120 -> двести шесть ундециллион(a,ов)  восемьсот тринадцать дециллион(a,ов)  шестьсот сорок семь нониллион(a,ов)  шестьсот тридцать девять октиллион(a,ов)  сто пятьдесят восемь септиллион(a,ов)  триста шестьдесят один секстиллион(a,ов)  восемьсот восемьдесят девять квинтиллион(a,ов)  восемьсот девяносто два квадриллион(a,ов)  триста шестьдесят шесть триллион(a,ов)  сто пятьдесят три миллиард(a,ов)  семьсот двадцать три миллион(a,ов)  триста девяносто семь тысяч(a,и)  сто двадцать
# ~ 75_851_396_365_305_058_864_686_197_893_514_336_422 -> семьдесят пять ундециллион(a,ов)  восемьсот пятьдесят один дециллион(a,ов)  триста девяносто шесть нониллион(a,ов)  триста шестьдесят пять октиллион(a,ов)  триста пять септиллион(a,ов)  пятьдесят восемь секстиллион(a,ов)  восемьсот шестьдесят четыре квинтиллион(a,ов)  шестьсот восемьдесят шесть квадриллион(a,ов)  сто девяносто семь триллион(a,ов)  восемьсот девяносто три миллиард(a,ов)  пятьсот четырнадцать миллион(a,ов)  триста тридцать шесть тысяч(a,и)  четыреста двадцать два
# ~ 554_345_710_297_930_460_130_174_142_174_642_447_304 -> пятьсот пятьдесят четыре ундециллион(a,ов)  триста сорок пять дециллион(a,ов)  семьсот десять нониллион(a,ов)  двести девяносто семь октиллион(a,ов)  девятьсот тридцать  септиллион(a,ов)  четыреста шестьдесят  секстиллион(a,ов)  сто тридцать  квинтиллион(a,ов)  сто семьдесят четыре квадриллион(a,ов)  сто сорок два триллион(a,ов)  сто семьдесят четыре миллиард(a,ов)  шестьсот сорок два миллион(a,ов)  четыреста сорок семь тысяч(a,и)  триста четыре
