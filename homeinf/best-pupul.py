#!/usr/bin/env python

# Mikhail (myke) Kolodin, 2024
# 2024-12-10 2024-12-24 1.5
# best-pupil.py
# дан текстовый классный журнал.
# определить лучшего ученика (или дать список по этому критерию),
# если а) сначала считаем средний балл (выше => лучше),
# б) для равных баллов считаем, у кого больше оценок (больше активность => лучше),
# в) для равных - у кого последние оценки выше,
# г) для равных - по алфавиту,
# д) остальное - случайно.
# можно просто показать отсортированный список (любого формата).

data = """
Прохор 5 4 5 4
Машенька 4 5 5 5 4 3 5 5 4 5 5
Петруха 3 3 5
Васёк 5 4
Сыч 4 5 4 5
"""

def avg(arr):
    """подсчитать среднее"""
    
    return sum(arr) / len(arr) if arr else 0


def prepare_data():
    """подготовить данные для обработки"""
    
    out = []
    
    for person in data.strip().split("\n"):
        name, *marks = person.split()
        marks = list(map(int, marks))
        line = {'name': name, 
            'marks': marks, 
            'len': len(marks), 
            'avg': avg(marks)}
        out.append(line)
    
    return out


def main():
    """основное вычисление"""
    
    best = prepare_data()
    
    best.sort(reverse = True, 
        key = lambda x: 
            (x['avg'], 
            x['len'], 
            x['marks'][::-1],
            x['name']
            ))
    
    print( *(enumerate(best, 1)), sep='\n')


main()

# (1, {'name': 'Машенька', 'marks': [4, 5, 5, 5, 4, 3, 5, 5, 4, 5, 5], 'len': 11, 'avg': 4.545454545454546})
# (2, {'name': 'Сыч', 'marks': [4, 5, 4, 5], 'len': 4, 'avg': 4.5})
# (3, {'name': 'Прохор', 'marks': [5, 4, 5, 4], 'len': 4, 'avg': 4.5})
# (4, {'name': 'Васёк', 'marks': [5, 4], 'len': 2, 'avg': 4.5})
# (5, {'name': 'Петруха', 'marks': [3, 3, 5], 'len': 3, 'avg': 3.6666666666666665})
