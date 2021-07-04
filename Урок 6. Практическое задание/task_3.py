"""
Задание 3 *.
Сделать профилировку для скриптов с рекурсией и сделать описание,
можно ли так профилировать и есть ли 'подводные камни' в профилировании?
Придумать как это решить!
Есть очень простое решение
"""

"""
При прфоилировании через рекурсию, если не принять меры,
то будет показываться профилировка при каждом новом вызове функции внутри рекурсии.
Решить это можно, если рекурсию оберунть еще одной функцией
"""
from collections import namedtuple
from recordclass import recordclass
from timeit import default_timer
import memory_profiler
from random import randint


def decor(func):
    def wrapper(*args, **kwargs):
        start_time = default_timer()
        m1 = memory_profiler.memory_usage()
        res = func(args[0])
        m2 = memory_profiler.memory_usage()
        mem_diff = m2[0] - m1[0]
        time_diff = default_timer() - start_time
        return res, mem_diff, time_diff
    return wrapper


@decor
def my_func(number):
    def flip_the_number(number):
        if (number // 10) == 0:
            return str(number % 10)
        else:
            return str(number % 10) + flip_the_number(number // 10)


if __name__ == '__main__':

    res, mem_diff, time_diff = my_func(765887658497863456786345786584754678058648677843586780658473456876079806587)
    print(f"Выполнение заняло {mem_diff} Mib и {time_diff} sec")


"""
Выполнение заняло 0.00390625 Mib и 0.20471709999999999 sec
"""