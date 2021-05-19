"""
Задание 3 *.
Сделать профилировку для скриптов с рекурсией и сделать описание,
можно ли так профилировать и есть ли 'подводные камни' в профилировании?
Придумать как это решить!
Есть очень простое решение
"""

#  Решение - просто обернуть рекурсию в еще одну функцию и ее профилировать.

#  Уже показано в 4-м примере первого задания. Скопируем сюда.

import memory_profiler
from random import randint
from itertools import cycle
from time import sleep
from pympler import asizeof
from numpy import array
from timeit import default_timer, timeit


def decor(func):  # Декоратор доработан
    def wrapper(*args, **kwargs):
        m1 = memory_profiler.memory_usage()
        start_time = default_timer()
        res = func(args[0])
        time_diff = default_timer() - start_time
        m2 = memory_profiler.memory_usage()
        mem_diff = m2[0] - m1[0]
        return res, mem_diff, time_diff

    return wrapper


@decor
def wrap(number):
    def even_odd(number):
        values = [0, 0]
        if not number // 10:
            if number % 2:
                values[1] += 1
            else:
                values[0] += 1
            return values
        return tuple(x + y for x, y in zip(even_odd(number // 10), even_odd(number % 10)))

    return even_odd(number)


a = 1
for i in range(200):
    a *= randint(2, 1000)

print('Затраты памяти при решении задачи через рекурсию:', wrap(a)[1])
'''
Задача решена. Рекурсия профилирована.
'''