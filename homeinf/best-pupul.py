#!/usr/bin/env python

# Mikhail (myke) Kolodin, 2024
# 2024-12-10 2024-12-10 1.0
# best-pupil.py
# дан текстовый классный журнал.
# определить лучшего ученика (или дать список по этому критерию),
# если а) сначала считаем средний балл (выше => лучше),
# б) для равных баллов считаем, у кого больше оценок (больше активность => лучше),
# в) остальное - случайно.

data = """
Машенька 4 5 5 5 4 3 5 5 4 5 5
Петруха 3 3 5
Васёк 5 4
"""

def avg(arr):
    """подсчитать среднее"""
    
    return sum(arr) / len(arr) if arr else 0


def prepare_data():
    """подготовить данные для обработки"""
    
    out = []
    
    for person in data.strip().split("\n"):
        name, *marks = person.split()
        # print(name, marks)
        marks = map(int, marks)
        line = {'name': name, 'marks': (lst := list(map(int, marks))), 'len': len(lst), 'avg': avg(lst)}
        # print(name, lst, line)
        out.append(line)
    
    return out
   
    
def main():
    """основное вычисление"""
    
    best = prepare_data()
    
    best.sort(reverse=True, key= lambda x: (x['avg'], x['len']))
    
    print(*best, sep='\n')
    
    
main()

# {'name': 'Машенька', 'marks': [4, 5, 5, 5, 4, 3, 5, 5, 4, 5, 5], 'len': 11, 'avg': 4.545454545454546}
# {'name': 'Васёк', 'marks': [5, 4], 'len': 2, 'avg': 4.5}
# {'name': 'Петруха', 'marks': [3, 3, 5], 'len': 3, 'avg': 3.6666666666666665}
