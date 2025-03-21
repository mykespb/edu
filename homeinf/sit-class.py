#!/usr/bin/env python
# Mikhail (myke) Kolodin
# 2025-03-21 2025-03-21 1.0
# sit-class.py

# ~ Есть школьники, мальчики и девочки.
# ~ Рассадить их так, чтобы за каждой партой сидели мальчик и девочка,
# ~ либо сообщить, что это невозможно.

boys1  = "Вася Петя Гриша Боря Саша" . split()
girls1 = "Маша Вера Катя Инга Яна" . split()
girls2 = "Маша Вера Катя Яна" . split()


def sit(boys, girls):
    """рассадка 1"""

    print(f"\n{boys=}, {girls=}")

    if len(boys) != len(girls):
        print("Нельзя рассадить.")

    else:
        join = list( zip (boys, girls) )
        print(f"Получилось: {join}.")
    

def main():
    """запуск"""

    sit(boys1, girls1)
    sit(boys1, girls2)

    
main()
