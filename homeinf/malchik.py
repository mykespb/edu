#!/usr/vin/env python

# Mikhail (myke) Kolodin, 2021
# 2021-11-15 2021-11-15 1.1

# Домашнее задание - конфетки и шарики

# Очень замечательный и умный мальчик получает каждый год
# на день рождения конфетки и шарики.
# Как очень замечательный, он получает шариков столько,
# сколько ему лет, а конфеток в 5 раз больше.
# Как очень умный, он все подарки подсчитывает.
# Сколько накопится конфеток и шариков за первые 50 лет жизни
# очень замечательного и умного мальчика?

all_sweets = all_baloons = 0

for age in range(1, 51):
    all_baloons += age
    all_sweets  += age * 5
    print("возраст %d, шариков %d, всего %d, конфет %d, всего %d" %
        (age, age, all_baloons, age*5, all_sweets))
