#!python3.10

# Mikhail (myke) Kolodin, 2021
# 2021-11-16 2021-11-16 1.2
# populaty.py

# ~ В некотором лесу, в некотором бору живёт популяция популятов.
# ~ Наблюдательные биологи пронаблюдали и заметили,
# ~ что если популятов больше нормы (или ровно норма),
# ~ то к следующему сезону лишние вымирают и их остаётся
# ~ на 10% меньше от прежнего (депопулируют),
# ~ а если меньше нормы, то они прирастают на 10% (популируют).
# ~ Показать размер популяции популятов за 10 лет
# ~ (если поначалу была как раз норма).

# зададим начальное значение популяции
pop = 1.0
print ("%d\t%f" % (0, pop))

# перебираем по годам
for year in range(1, 11):
    if pop >= 1.:
        pop *= 0.9
    elif pop < 1.:
        pop *= 1.1
    print ("%d\t%f" % (year, pop))
