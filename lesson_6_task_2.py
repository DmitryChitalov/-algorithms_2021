"""
Задание 2.*
Предложить еще какие-либо варианты (механизмы, подходы, библиотеки, идеи)
для оптимизации памяти и
доказать!!! (наглядно, кодом) их эффективность (на примере профилировщика).
"""

# своего не придумала, для закрепления использовала пример с урока
from memory_profiler import profile


@profile
def format_str(a, b, c, d, e):
    res = f'{a}_{b}_{c}_{d}_{e}_{a}_{b}_{c}_{d}_{a}_{b}_{c}_{a}_{b}_{a}'
    return res


@profile
def concat_str(a, b, c, d, e):
    res = (a + '_' + b + '_' + c + '_' + d + '_' + e + '_' + a + '_' + b + '_' + c + '_' + d + '_'
           + a + '_' + b + '_' + c + '_' + a + '_' + b + '_' + a)
    return res


concat_str('one' * 10, 'two' * (10 ** 2), 'three' * (10 ** 3), 'four' * (10 ** 4), 'five' * (10 ** 5))
format_str('one' * 10, 'two' * (10 ** 2), 'three' * (10 ** 3), 'four' * (10 ** 4), 'five' * (10 ** 5))

'''
Как видно из замеров, f-строки требуют меньше памяти, чем конкатенация (в примере разница составила 0.5 MiB
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    18     15.6 MiB     15.6 MiB           1   @profile
    19                                         def concat_str(a, b, c, d, e):
    20     16.1 MiB      0.5 MiB          12       res = (a + '_' + b + '_' + c + '_' + d + '_' + e + '_' + a + '_' + b + '_' + c + '_' + d + '_'
    21     16.1 MiB      0.0 MiB          11              + a + '_' + b + '_' + c + '_' + a + '_' + b + '_' + a)
    22     16.1 MiB      0.0 MiB           1       return res


Filename: D:/Олеся/Python/GEEK BRAINS/Algorithms/Lesson_6/доработанные/lesson_6_task_2.py

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    12     16.1 MiB     16.1 MiB           1   @profile
    13                                         def format_str(a, b, c, d, e):
    14     16.1 MiB      0.0 MiB           1       res = f'{a}_{b}_{c}_{d}_{e}_{a}_{b}_{c}_{d}_{a}_{b}_{c}_{a}_{b}_{a}'
    15     16.1 MiB      0.0 MiB           1       return res


'''

