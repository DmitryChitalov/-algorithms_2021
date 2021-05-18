"""
Задание 3 *.
Сделать профилировку для скриптов с рекурсией и сделать описание,
можно ли так профилировать и есть ли 'подводные камни' в профилировании?
Придумать как это решить!
Есть очень простое решение!
"""

from random import randint
import timeit
import memory_profiler
from memory_profiler import profile


def decor(func):
    def wrapper(*args):
        start_time = timeit.default_timer()
        m1 = memory_profiler.memory_usage()
        res1 = func(args[0])
        m2 = memory_profiler.memory_usage()
        end_time = timeit.default_timer()
        return res1, m2[0] - m1[0], end_time - start_time
    return wrapper


def memoize(f):
    cache = {}

    def decorate(*args):
        if args in cache:
            return cache[args]
        else:
            cache[args] = f(*args)
            return cache[args]

    return decorate


@memoize
def recursive_reverse_mem(number):
    if number == 0:
        return ''
    return f'{str(number % 10)}{recursive_reverse_mem(number // 10)}'


# Придумал вот такое решение: создал еще одну функцию для вызова нужной функции,
# обернул ее всеми возможными декораторами. Результат ниже.
# Т.е. таблиц профайлера при вызове рекурсивной функции одна.
# Правда сама таблица малоинформативна, вероятно из-за того, что функция в одну строку
@profile
@decor
def call_reverse_mem(num):
    return recursive_reverse_mem(num)


num = randint(100000000, 10000000000000)
print('num =', num)
el, mem_diff, exec_time = call_reverse_mem(num)
print('el  =', el)
print(f'call_reverse. Использовано {mem_diff} Mib памяти')
print(f'Время выполнения simple_1 = {exec_time}')

# num = 5691973753489
# Filename: ...\-algorithms_2021\Урок 6. Практическое задание\task_3.py
#
# Line #    Mem usage    Increment  Occurences   Line Contents
# ============================================================
#     16     21.5 MiB     21.5 MiB           1       def wrapper(*args):
#     17     21.5 MiB      0.0 MiB           1           start_time = timeit.default_timer()
#     18     21.5 MiB      0.0 MiB           1           m1 = memory_profiler.memory_usage()
#     19     21.5 MiB      0.0 MiB           1           res1 = func(args[0])
#     20     21.5 MiB      0.0 MiB           1           m2 = memory_profiler.memory_usage()
#     21     21.5 MiB      0.0 MiB           1           end_time = timeit.default_timer()
#     22     21.5 MiB      0.0 MiB           1           return res1, m2[0] - m1[0], end_time - start_time
#
#
# el  = 9843573791965
# call_reverse. Использовано 0.0078125 Mib памяти
# Время выполнения simple_1 = 0.22677699999999995
