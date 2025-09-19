#!/usr/bin/env python

# Mikhail (myke) Kolodin, 2025
# 2025-09-19 2025-09-19 1.0
# pascal-be.py

# ~ Дана программа на языке Pascal.
# ~ Определить, правильно ли в ней открыты-закрыты блоки begin-end.
# ~ Считаем что строк с этими словами внутри и комментариев в программе нет.

# ~ DEBUG = True
DEBUG = False

# data for tests

progs = (
"""
program mist(input, output);
var a: integer;
begin
    print("start");
    a := 1;
    while a < 99 do
        begin
            a :=  a+1;
            print(a)
        end
    print("stop")
end.
"""
,
"""
program mist(input, output);
type
    group = array [1..100] of integer;
var a: integer;
    g1, g2: group;
begin
    print("start: ");
    for i:=1 to 100 do
        begin
            if i < 10
            then
                begin
                    g1[i] := i;
                    g2[i] := -1
                end
            else
                begin
                    g1[i] := i*2;
                    g2[i] := -i
                end
    print("stop.")
end.
"""
)


def test_prog(prog : str) -> bool:
    """test 1 program"""

    cnt = 0
    par = ""

    pos = 0

    while pos < len(prog):

        if prog[pos:].startswith('begin'):
            cnt += 1
            if DEBUG: print('(', end="")

        elif prog[pos:].startswith('end'):
            cnt -= 1
            if DEBUG: print(')', end="")
            if cnt < 0:
                if DEBUG: print('?')
                return False
        pos += 1            

    if DEBUG: print('!')

    return cnt == 0


def main():
    """run all tests"""

    for num, test in enumerate(progs):
        print(f"prog #{num+1} : tested as {test_prog(test)}")

main()
