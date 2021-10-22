from timeit import default_timer
from memory_profiler import memory_usage, profile


# @profile
def rec_func(number):
    if number < 1:
        return number
    return rec_func(number - 1)


@profile
def wrap_func(num):
    return rec_func(num)


# rec_func(100)
wrap_func(10)

'''
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    12     18.9 MiB     18.9 MiB           1   @profile
    13                                         def wrap_func(num):
    14     18.9 MiB      0.0 MiB           1       return rec_func(num)
'''

# Вывод
# При использовании @profile c рекурсивной функцией замер происходит каждую иттерацию
# Решение: обернуть рекурсию  в простую функцию, и тогда всё пройдёт как положено

