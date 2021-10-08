"""
Задание 1.

Выполните профилирование памяти в скриптах.
Проанализируйте результат и определите программы с
наиболее эффективным использованием памяти.

Примечание: Для анализа возьмите любые 3-5 ваших РАЗНЫХ скриптов!
(хотя бы 3 разных для получения оценки отл).
На каждый скрипт вы должны сделать как минимум по две реализации.

Можно взять только домашние задания с курса Основ
или с текущего курса Алгоритмов

Результаты профилирования добавьте в виде комментариев к коду.
Обязательно сделайте аналитику (что с памятью в ваших скриптах, в чем ваша оптимизация и т.д.)

ВНИМАНИЕ: ЗАДАНИЯ, В КОТОРЫХ БУДУТ ГОЛЫЕ ЦИФРЫ ЗАМЕРОВ (БЕЗ АНАЛИТИКИ)
БУДУТ ПРИНИМАТЬСЯ С ОЦЕНКОЙ УДОВЛЕТВОРИТЕЛЬНО

Попытайтесь дополнительно свой декоратор используя ф-цию memory_usage из memory_profiler
С одновременным замером времени (timeit.default_timer())!
"""

from memory_profiler import profile
from numpy import array


@profile
def sieve_erato_old(i):
    n = 2
    l = i * 12
    sieve = [x for x in range(l)]
    sieve[1] = 0
    while n < l:
        if sieve[n] != 0:
            m = n * 2
            while m < l:
                sieve[m] = 0
                m += n
        n += 1
    return [p for p in sieve if p != 0][i - 1]


@profile
def sieve_erato_array(i):
    n = 2
    l = i * 12
    sieve = array(range(l))
    sieve[1] = 0
    while n < l:
        if sieve[n] != 0:
            m = n * 2
            while m < l:
                sieve[m] = 0
                m += n
        n += 1
    return [p for p in sieve if p != 0][i - 1]


# Проверка sieve_erato_old()
sieve_erato_old(10000)
'''
    11     30.4 MiB     30.4 MiB           1   @profile
    12                                         def sieve_erato_old(i):
    13     30.4 MiB      0.0 MiB           1       n = 2
    14     30.4 MiB      0.0 MiB           1       l = i * 12
    15     35.9 MiB      5.5 MiB      120003       sieve = [x for x in range(l)]
    16     35.9 MiB      0.0 MiB           1       sieve[1] = 0
    17     35.9 MiB      0.0 MiB      119999       while n < l:
    18     35.9 MiB      0.0 MiB      119998           if sieve[n] != 0:
    19     35.9 MiB      0.0 MiB       11301               m = n * 2
    20     35.9 MiB      0.0 MiB      321649               while m < l:
    21     35.9 MiB      0.0 MiB      310348                   sieve[m] = 0
    22     35.9 MiB      0.0 MiB      310348                   m += n
    23     35.9 MiB      0.0 MiB      119998           n += 1
    24     35.9 MiB      0.0 MiB      120003       return [p for p in sieve if p != 0][i - 1]
'''


# Проверка sieve_erato_array()
sieve_erato_array(10000)
'''
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    27     30.1 MiB     30.1 MiB           1   @profile
    28                                         def sieve_erato_array(i):
    29     30.1 MiB      0.0 MiB           1       n = 2
    30     30.1 MiB      0.0 MiB           1       l = i * 12
    31     30.7 MiB      0.6 MiB           1       sieve = array(range(l))
    32     30.7 MiB      0.0 MiB           1       sieve[1] = 0
    33     30.7 MiB      0.0 MiB      119999       while n < l:
    34     30.7 MiB      0.0 MiB      119998           if sieve[n] != 0:
    35     30.7 MiB      0.0 MiB       11301               m = n * 2
    36     30.7 MiB      0.0 MiB      321649               while m < l:
    37     30.7 MiB      0.0 MiB      310348                   sieve[m] = 0
    38     30.7 MiB      0.0 MiB      310348                   m += n
    39     30.7 MiB      0.0 MiB      119998           n += 1
    40     31.1 MiB      0.3 MiB      120003       return [p for p in sieve if p != 0][i - 1]
'''

"""
Вывод: разница между размерами используемой памяти между list и numpy.array огромна.
Для хранения больших объемов данных, или при использовании в программах больших массивов,
оптимальнее использовать numpy.array.
"""