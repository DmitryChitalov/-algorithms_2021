"""
Задание 2.*
Предложить еще какие-либо варианты (механизмы, подходы, библиотеки, идеи)
для оптимизации памяти и
доказать!!! (наглядно, кодом) их эффективность (на примере профилировщика).
"""
from memory_profiler import profile


@profile()
def concat1(strings: list):
    string = ''
    for i in strings:
        string += i
    return string


@profile()
def concat2(strings: list):
    string = ''.join(strings)
    return string


strings = []
for i in range(100000):
    strings.append(str(i))


concat1(strings)
concat2(strings)

'''
Конкатенация длинных строк выгоднее с помощью ''.join()

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    10     26.3 MiB     26.3 MiB           1   @profile()
    11                                         def concat1(strings: list):
    12     26.3 MiB      0.0 MiB           1       string = ''
    13     28.2 MiB      0.0 MiB      100001       for i in strings:
    14     28.2 MiB      1.9 MiB      100000           string += i
    15     28.2 MiB      0.0 MiB           1       return string


Filename: D:\IT\!Study Projects\-algorithms_2021\Урок 6. Практическое задание\task_2.py

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    18     26.1 MiB     26.1 MiB           1   @profile()
    19                                         def concat2(strings: list):
    20     26.5 MiB      0.5 MiB           1       string = ''.join(strings)
    21     26.5 MiB      0.0 MiB           1       return string

'''