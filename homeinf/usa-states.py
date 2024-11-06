#!/usr/bin/env python

# Mikhail (myke) Kolodin, 2022
# 2024-11-06 2024-11-06 1.1
# usa-states.py

# ~ Даны данные о штатах США.
# 1. в каких штатах различаются крупнейший город и столица?

data_file = "usa-states.tab"

def read_states():
    """read data from tab file"""

    caps = []

    with open(data_file) as data:
        for num, line in enumerate(data):
            if num == 0: continue
            info = line.strip().split('\t')
            if info[-2] != info[-1]:
                caps.append((info[1], info[-2], info[-1]))

    return caps
        

def capitals():
    """select and print needed states"""
    
    states = read_states()

    for num, state in enumerate(states):
        print(f"{num+1}. штат: {state[0]}, столица: {state[1]}, крупнейший город: {state[2]}")


capitals()

# ~ https://ru.wikipedia.org/wiki/%D0%90%D0%B4%D0%BC%D0%B8%D0%BD%D0%B8%D1%81%D1%82%D1%80%D0%B0%D1%82%D0%B8%D0%B2%D0%BD%D0%BE%D0%B5_%D0%B4%D0%B5%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5_%D0%A1%D0%A8%D0%90

# ~ 1. штат: Алабама, столица: Монтгомери, крупнейший город: Бирмингем
# ~ 2. штат: Аляска, столица: Джуно, крупнейший город: Анкоридж
# ~ 3. штат: Вашингтон, столица: Олимпия, крупнейший город: Сиэтл
# ~ 4. штат: Вермонт, столица: Монтпилиер, крупнейший город: Берлингтон
# ~ 5. штат: Виргиния, столица: Ричмонд, крупнейший город: Верджиния-Бич
# ~ 6. штат: Висконсин, столица: Мадисон, крупнейший город: Милуоки
# ~ 7. штат: Делавэр, столица: Довер, крупнейший город: Уилмингтон
# ~ 8. штат: Иллинойс, столица: Спрингфилд, крупнейший город: Чикаго
# ~ 9. штат: Калифорния, столица: Сакраменто, крупнейший город: Лос-Анджелес
# ~ 10. штат: Канзас, столица: Топика, крупнейший город: Уичито
# ~ 11. штат: Кентукки, столица: Франкфорт, крупнейший город: Луисвилл
# ~ 12. штат: Коннектикут, столица: Хартфорд, крупнейший город: Бриджпорт
# ~ 13. штат: Луизиана, столица: Батон-Руж, крупнейший город: Новый Орлеан
# ~ 14. штат: Миннесота, столица: Сент-Пол, крупнейший город: Миннеаполис
# ~ 15. штат: Миссури, столица: Джефферсон-Сити, крупнейший город: Канзас-Сити
# ~ 16. штат: Мичиган, столица: Лансинг, крупнейший город: Детройт
# ~ 17. штат: Монтана, столица: Хелена, крупнейший город: Биллингс
# ~ 18. штат: Мэн, столица: Огаста, крупнейший город: Портленд
# ~ 19. штат: Мэриленд, столица: Аннаполис, крупнейший город: Балтимор
# ~ 20. штат: Небраска, столица: Линкольн, крупнейший город: Омаха
# ~ 21. штат: Невада, столица: Карсон-Сити, крупнейший город: Лас-Вегас
# ~ 22. штат: Нью-Гэмпшир, столица: Конкорд, крупнейший город: Манчестер
# ~ 23. штат: Нью-Джерси, столица: Трентон, крупнейший город: Ньюарк
# ~ 24. штат: Нью-Йорк, столица: Олбани, крупнейший город: Нью-Йорк
# ~ 25. штат: Нью-Мексико, столица: Санта-Фе, крупнейший город: Альбукерке
# ~ 26. штат: Огайо, столица: Колумбус, крупнейший город: Кливленд
# ~ 27. штат: Орегон, столица: Сейлем, крупнейший город: Портленд
# ~ 28. штат: Пенсильвания, столица: Гаррисберг, крупнейший город: Филадельфия
# ~ 29. штат: Северная Дакота, столица: Бисмарк, крупнейший город: Фарго
# ~ 30. штат: Северная Каролина, столица: Роли, крупнейший город: Шарлотт
# ~ 31. штат: Теннесси, столица: Нашвилл, крупнейший город: Мемфис
# ~ 32. штат: Техас, столица: Остин, крупнейший город: Хьюстон
# ~ 33. штат: Флорида, столица: Таллахасси, крупнейший город: Джэксонвилл
# ~ 34. штат: Южная Дакота, столица: Пирр, крупнейший город: Су-Фолс

