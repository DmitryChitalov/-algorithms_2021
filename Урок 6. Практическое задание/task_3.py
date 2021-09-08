"""
Задание 3 *.
Сделать профилировку для скриптов с рекурсией и сделать описание,
можно ли так профилировать и есть ли 'подводные камни' в профилировании?
Придумать как это решить!
Есть очень простое решение
"""


from timeit import default_timer
from memory_profiler import memory_usage


def decor(func):
    def wrapper(*args):
        m1 = memory_usage()
        t1 = default_timer()
        res = func(*args)
        m2 = memory_usage()
        t2 = default_timer()
        print(f'Memory {m2[0] - m1[0]}\nTime {t2 - t1}')
        return res
    return wrapper


@decor
def wrap():
    def sum_numbers(vol=3, num=1, sum_num=0):
        if vol != 0:
            sum_num += num
            num /= -2
            return sum_numbers(vol - 1, num, sum_num)
        return print(sum_num)
    return sum_numbers()


wrap()

# 0.75
# Memory 0.00390625
# Time 0.10861549999999998
"""
Как и обсуждали на уроке для замера потребляемой памяти функции с рекурсией нужно
обернуть ее в функцию обёртку.
"""
###################################################################################
"""
Или как вариант декорировать функцию при помощи @profile и запустить скрипт через консоль:
python -m memory_profiler task4.py
"""
@profile
def sum_numbers(vol=3, num=1, sum_num=0):
    if vol != 0:
        sum_num += num
        num /= -2
        return sum_numbers(vol - 1, num, sum_num)
    return print(sum_num)


sum_numbers()
"""
Результат вывода:
"""
# PS C:\Users\Slava\PycharmProjects\pythonProject11\venv\lesson6> python -m memory_profiler task4.py
# 0.75
# Filename: task4.py
#
# Line #    Mem usage    Increment  Occurences   Line Contents
# ============================================================
#      2   20.480 MiB   20.480 MiB           4   @profile
#      3                                         def sum_numbers(vol=3, num=1, sum_num=0):
#      4   20.480 MiB    0.000 MiB           4       if vol != 0:
#      5   20.480 MiB    0.000 MiB           3           sum_num += num
#      6   20.480 MiB    0.000 MiB           3           num /= -2
#      7   20.488 MiB    0.000 MiB           3           return sum_numbers(vol - 1, num, sum_num)
#      8   20.488 MiB    0.008 MiB          1       return print(sum_num)
#
#
# PS C:\Users\Slava\PycharmProjects\pythonProject11\venv\lesson6>
