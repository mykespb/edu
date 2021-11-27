#!/python3.10

# Mikhail (myke) Kolodin, 2021
# 2021-11-26 2021-11-26 1.0
# longstr.py


print ("""
Привет!
Давай поиграем в игру!

Человек и машина играют в слова так:
человек вводит строку,
а машина определяет,
какое слово в ней самое длинное
(если таких несколько, подойдёт любое).
Игра идёт по кругу, пока человек не введёт пустую строку
или строку из одной точки.
(Подсказка. Длина строки определяется функцией len.)""")

while True:
    human = input("\nвведи строку: ")
    if human == "" or human == ".":
        break

    maxlen = 0
    maxword = ""
    for word in human.split():
        thislen = len(word)

        if thislen > maxlen:
            maxlen = thislen
            maxword = word

    print (f"самое длинное слово: '{maxword}' с длиной {maxlen}")

print ("\nПока...")
