# happy numbers via product

from itertools import product

def happy(size=6):
    num = 0
    half = size // 2
    digits = range(10)
    
    for left in product(digits, repeat=3):
        for right in product(digits, repeat=3):
            if sum(left) == sum(right):
                num += 1
                
    print(f"{size=}, {num=}")
    

happy()
# size=6, num=55252
