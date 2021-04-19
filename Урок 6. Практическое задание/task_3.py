"""
Задание 3 *.
Сделать профилировку для скриптов с рекурсией и сделать описание,
можно ли так профилировать и есть ли 'подводные камни' в профилировании?
Придумать как это решить!
Есть очень простое решение!
"""

from memory_profiler import profile
from timeit import default_timer
from memory_profiler import memory_usage


def decor(func):
    def wrapper(*args, **kwargs):
        start_time = default_timer()
        m1 = memory_usage()
        res = func(*args, **kwargs)
        m2 = memory_usage()
        fin_time = default_timer()
        print(f"\nФункция: {func.__name__}")
        print(f"Memory: {m2[0] - m1[0]:0.5f} ")
        print(f"Time: {fin_time - start_time:0.5f} ")
        return res
    return wrapper


# @decor
# @profile
def reverse_num(num):
    if num == 0:
        return ''
    else:
        revers = str(num % 10)
        num //= 10
        return revers + reverse_num(num)


@decor
# @profile
def decor_recurse(num):
    return reverse_num(num)


# reverse_num(12323326599491991919)
decor_recurse(12323326599491991919)

"""
Ели как обычно профилировать рекурсивную фун-ю, то каждый вызов фун-и мы будем получать результат декоратора @decor
или @profile, это можно избежать создав еще одну фун-ю в которая будет возвращать результат нужной нам фу-и и 
обернуть её декоратором.

"""
