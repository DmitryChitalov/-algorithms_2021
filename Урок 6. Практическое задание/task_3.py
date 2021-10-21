#!/usr/bin/env python3

from memory_profiler import profile

"""
Задание 3 *.
Сделать профилировку для скриптов с рекурсией и сделать описание,
можно ли так профилировать и есть ли 'подводные камни' в профилировании?
Придумать как это решить!
Есть очень простое решение
"""

'''

@profile
def factorial(n):
    return 1 if n == 0 else factorial(n - 1) * n

print(factorial(7))

Выводит много лишней информации вызывая провилировщик при каждом вызове функции.
Для того чтобы этого избежать можно обернуть рекурсивную функию в другую фунцию
'''


def factorial(n):
    return 1 if n == 0 else factorial(n - 1) * n


@profile
def factorial_wrapper(n):
    return factorial(n)


print(factorial_wrapper(7))
