"""
Задание 2.*
Предложить еще какие-либо варианты (механизмы, подходы, библиотеки, идеи)
для оптимизации памяти и
доказать!!! (наглядно, кодом) их эффективность (на примере профилировщика).
"""

#  Как говорилось на занятии, выигрыш в памяти дают f-строки.


from memory_profiler import profile


@profile
def format_str(a, b, c):
    res = f'{a}_{b}_{c}_{a}_{b}_{c}_{a}'
    return res


@profile
def concat_str(a, b, c):
    res = (a + '_' + b + '_' + c + '_' + a + '_' + b + '_' + c + '_' + a)
    return res


format_str('azazaz' * 1111122, 'sxsxsxsx' * 22220002, 'fvfvfv' * 33444333)
concat_str('azazaz' * 1111122, 'sxsxsxsx' * 22220002, 'fvfvfv' * 33444333)
'''
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    14    386.3 MiB    386.3 MiB           1   @profile
    15                                         def format_str(a, b, c):
    16   1127.2 MiB    740.9 MiB           1       res = f'{a}_{b}_{c}_{a}_{b}_{c}_{a}'
    17   1127.2 MiB      0.0 MiB           1       return res


Filename: L:\GeekBrains\Алгоритмы и структуры данных на Python\Lesson 6\Lesson 6 HW\task_2.py

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    20    386.4 MiB    386.4 MiB           1   @profile
    21                                         def concat_str(a, b, c):
    22   1127.2 MiB    740.9 MiB           1       res = a + '_' + b + '_' + c + '_' + a + '_' + b + '_' + c + '_' + a
    23   1127.2 MiB      0.0 MiB           1       return res

Однако мои результаты (как и результаты на уроке) показывают практически одно и то же. 
Выигрыш в памяти все же не очень существенный.
'''

