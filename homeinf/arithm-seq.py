#!/usr/bin/env python

# Mikhail (myke) Kolodin, 2025
# arythm-seq.py
# 2025-02-14 2025-02-23 1.1

# работа с файлами. учебное
# адаптировано для работы с interview.cups
# ~ прочитать из файла арифметическую прогрессию,
# ~ дополнить следующим числом
# ~ и записать его в тот же файл,
# ~ не забываем про пробелы
# ~ если файл пустой, то сами создаём случайную ар. прогрессию
# ~ и записываем её в файл.


from random import randint

asfile  = 'tmp/arithm-seq.txt'


def process():
    """работаем..."""

    start = randint(1, 100)
    step  = randint(1, 10)

    with open(asfile, 'at+') as fin:

        fin.seek(0)

        text = fin.read()
        text = text.strip()
        tlen = len(text)

        print(f"text read {tlen=}:", text)

        if tlen == 0:
            for i in range( randint(3, 5) ):
                print(start + i * step, file = fin, end = " ")

        else:
            seq = [ int(x) for x  in text.split()]

            plus = seq[-1] - seq[-2]
            cont = seq[-1] + plus
            
            fin.seek(0, 2)
            fin.write(f" {cont}")
            
            print(f"added {cont} with step {plus}")


process()


# ~ text read tlen=28: 72 80 88 96  104 112 120 128
# ~ added 136 with step 8

# ~ Для файлов, открытых в текстовом режиме (тех, которые открыты без 'b' в строке mode функции open()) разрешены только запросы относительно начала файла (или быстрое перемещение указателя в конец файла с помощью fp.seek(0, 2)). Допустимыми значениями смещения offset от начала файла являются те, которые возвращаются из fp.tell() или 0. Любое другое значение смещения приводит к неопределенному поведению.
# ~ https://docs-python.ru/tutorial/metody-fajlovogo-obekta-potoka-python/metod-file-seek/
