#!/usr/bin/env python
# Mikhail (myke) Kolodin
# 2025-02-14 2025-02-14 1.0
# periodic-weather.py

# ~ Периодическая погода 

# ~ В неком городе каждые 3 дня в течение дня идёт дождь, 
# ~ каждые 13 дней в течение дня идёт снег, 
# ~ каждые 29 дней в течение дня случается ураган, 
# ~ каждые 2 дня в течение дня пасмурно, 
# ~ каждые 7 дней на день пропадает электричество,
# ~ каждые 5 дней в течение дня по городу бегают кусучие ящерицы,
# ~ каждые 4 дня весь день не ходит транспорт.
# ~ каждые 11 дней прилетает метеорит.
# ~ Пусть нынче идеальный день без осадков и происшествий.
# ~ Когда нам снова будет так же хорошо?

LIMIT = 1_000_000

def test(size):
    """проверить на отрезке времени длиной size дней"""

    days = [ 0 for _ in range(size) ]

    for i in range(2, size, 3): days[i] += 1
    for i in range(12, size, 13): days[i] += 1
    for i in range(28, size, 29): days[i] += 1
    for i in range(1, size, 2): days[i] += 1
    for i in range(6, size, 7): days[i] += 1
    for i in range(4, size, 5): days[i] += 1
    for i in range(10, size, 11): days[i] += 1

    for i in range(1, size):
        if days[i] == 0:
            return True, days
    return False, days


def main1():
    """организовать перебор порядков"""

    size = 10
    result, days = test(size)
    print(f"проверяем {size} дней: {result}\n{days}")

    
def main2():
    """организовать перебор порядков"""

    size = 7            # берём вначале 1 неделю...
    while size <= LIMIT:
        result, days = test(size)
        print(f"проверяем {size} дней: {result}")
        if result: break
        size *= 2       # если не повезло, то удваиваем период проверки
    else:
        print("не смогли найти хороших дней")
        return 

    print(f"дни: {days}")
    
main = main2
main()
