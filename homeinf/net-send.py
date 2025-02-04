#!/usr/bin/env python
# Mikhail (myke) Kolodin

# net-send.py
# 2025-02-03 2025-02-03 1.1

# ~ Сетевые посылки простые
# ~ ------------------------------------------------

# ~ По сети передаются байты.
# ~ Они содержат порции информации, котоорые нужно распознать и обработать.
# ~ Каждая порция состоит из префикса, заголовка, содержимого, суффикса.
# ~ Каждая из этих частей - последовательность байтов.
# ~ В полученном наборе данных не отмечены начала,
# ~ это просто кусок передаваемой по сети информации.
# ~ Мусор - шум - ошибки - есть только между сообщениями.
# ~ В содержимом есть сообщение, записанное латиницей в коде ASCII.
# ~ Прочитать всё, что получится.
# ~ Префикс = 0 1
# ~ Суффикс = 0 2
# ~ Заголовок = 0 3 длина
# ~ где длина есть длина сообщения в байтах.
# ~ Содержимое = байты (не 0)... 

# ~ Пример:
# ~ 45 56 22 0 45 0 23 0 1 0 3 5 72 69 76 7 679 0 0 0 2 34 34 0 1 0 3 32 33 126 0 3 1 2 3 1 2 1
# ~ HELLO !~

# ~ Декодировать полученные сообщения.

# -------------------------------------------------------------
# message

message = 45, 56, 22, 1, 45, 1, 23, 0, 1, 0, 3, 5, 72, 69, 76, 76, 79, 0, 2, 34, 34, 0, 1, 0, 3, 3, 32, 33, 126, 0, 2, 1, 2, 3, 1, 2, 1

# -------------------------------------------------------------
# decoder

def decode(arr : tuple[int]) -> tuple[str, str]:
    """decode message in arr"""

    state = 'out'
    result = 'ok'
    answer = ''
    tolen = waslen = 0

    for i, b in enumerate(arr):

        # ~ print(f"{i=}, {b=}, {state=}, {tolen=}, {waslen=}")

        if state == 'out':
            
            if b == 0:
                state = 'prefix'

        elif state == 'prefix':

            if b == 1:
                state = 'prefixok'
            else:
                state = 'stop'
                result = 'error'
                answer = 'bad prefix'
                break

        elif state == 'prefixok':

            if b == 0:
                state = 'toheader'
            else:
                state = 'stop'
                result = 'error'
                answer = 'bad header1'
                break

        elif state == 'toheader':

            if b == 3:
                state = 'getlen'
            else:
                state = 'stop'
                result = 'error'
                answer = 'bad header2'
                break

        elif state == 'getlen':

            if b != 0:
                tolen = b
                waslen = 0
                # ~ answer = ''
                state = 'in'
            else:
                state = 'stop'
                result = 'error'
                answer = 'bad length'
                break

        elif state == 'in':

            if b != 0:
                answer += chr(b)
                waslen += 1

                if tolen == waslen:
                    state = 'after'
                    result = 'ok'

            else:
                state = 'stop'
                result = 'error'
                answer = 'bad message'
                break
                
        elif state == 'after':

            if b == 0:
                state = 'suffix'
            else:
                state = 'stop'
                result = 'error'
                answer = 'bad suffix1'
                break
                
        elif state == 'suffix':

            if b == 2:
                state = 'out'
            else:
                state = 'stop'
                result = 'error'
                answer = 'bad suffix2'
                break
                
    return result, answer

# -------------------------------------------------------------
# tester

def tester(arr : tuple[int]) -> tuple[str, str]:

    res, out = decode(arr)
    
    print(f"""
input sequence: {tuple(enumerate(arr))}
result:         {res}
output string:  {out}
""")

# -------------------------------------------------------------
# testing

tester(message)

# -------------------------------------------------------------
# results

# ~ input sequence: ((0, 45), (1, 56), (2, 22), (3, 1), (4, 45), (5, 1), (6, 23), (7, 0), (8, 1), (9, 0), (10, 3), (11, 5), (12, 72), (13, 69), (14, 76), (15, 76), (16, 79), (17, 0), (18, 2), (19, 34), (20, 34), (21, 0), (22, 1), (23, 0), (24, 3), (25, 3), (26, 32), (27, 33), (28, 126), (29, 0), (30, 2), (31, 1), (32, 2), (33, 3), (34, 1), (35, 2), (36, 1))
# ~ result:         ok
# ~ output string:  HELLO !~

# -------------------------------------------------------------
