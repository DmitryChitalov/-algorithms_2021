"""
Задание 3 *.
Сделать профилировку для скриптов с рекурсией и сделать описание,
можно ли так профилировать и есть ли 'подводные камни' в профилировании?
Придумать как это решить!
Есть очень простое решение
"""
from memory_profiler import profile
from functools import wraps


def recursion(number):
    if number == 0:
        return number
    else:
        return number + recursion(number-1)


@profile()
def recursion_wrap(func, number):
    return func(number)


recursion_wrap(recursion, 3)

'''
Если использовать только декоратор @profile для рекурсивной функции то получим отдельную таблицу профилировщика на
каждый вызов рекурсии.
Чтобы получить одну таблицу оборачиваем рекурсивную функцию в другую функцию и уже это функцию-обертку дкорируем.

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    19     18.6 MiB     18.6 MiB           1   @profile()
    20                                         def recursion_wrap(func, number):
    21     18.6 MiB      0.0 MiB           1       return func(number)
    
'''
