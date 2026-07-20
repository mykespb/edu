#!/usr/bin/env python

# Mikhail (myke) Kolodin, 2021
# 2021-11-16 2021-11-26 1.4
# pentagon.py
# (условие внизу)

SIDE  = 281        # длина стороны, метров

LIMIT = 100_000    # предел блужданий, секунд

total_length = 5 * SIDE * 100    # сторон * длина * см в метре

M_STEP  = 50
L_STEP  = 40

moment   = 1
m_off    = m_total   = M_STEP
l_off    = l_total   = L_STEP

print ("moment %d, misha off %d cm (total %d cm), "
    "lena off %d cm (total %d cm)" %
    (moment, m_off, m_total, l_off, l_total))

while m_off != l_off and moment < LIMIT:
    moment  += 1
    m_total += M_STEP
    l_total += L_STEP
    m_off    = m_total % total_length
    l_off    = l_total % total_length

    print ((moment // 1000 % 10) if moment % 1000 == 0 else
        "." if moment % 100 == 0 else "", end="")

print ("\n\nmoment {:_}, misha off {:_} cm (total {:_}) cm, "
    "lena off {:_} cm (total {:_} cm)"
    .format (moment, m_off, m_total, l_off, l_total))

hours   = moment // (60 * 60)
minutes = moment % (60 * 60) // 60
seconds = moment % 60
print ("total time: {:_} hours, {} minutes, {} seconds"
    .format (hours, minutes, seconds))

print ("we met again!" if m_off == l_off else "We never met!")

# ~ Туристы Миша и Лена решили обойти вокруг здания Пентагона (по
# ~ адресу: Арлингтон, Вирджиния 22202, США.). Длина одной стороны этого
# ~ сооружения - 281 м. Они вышли одновременно от одного угла в одну сторону и
# ~ делают по 1 шагу в секунду. Длина шага Миши - 50 см, Лены - 40 см.
# ~ Когда они снова встретятся и сколько для этого пройдут?
