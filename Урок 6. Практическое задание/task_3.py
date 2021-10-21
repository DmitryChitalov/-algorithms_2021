"""
Задание 3 *.
Сделать профилировку для скриптов с рекурсией и сделать описание,
можно ли так профилировать и есть ли 'подводные камни' в профилировании?
Придумать как это решить!
Есть очень простое решение
"""

from timeit import default_timer
from memory_profiler import profile, memory_usage


def decor(func):
    """Функция декортатор для замеров времени и памяти"""

    def wrapper(*args, **kwargs):
        t1 = default_timer()
        m1 = memory_usage()
        res = func(args[0])
        m2 = memory_usage()
        t2 = default_timer()
        mem_diff = m2[0] - m1[0]
        time_dif = t2 - t1
        print(f'Функция - {func.__name__}\n Время заняло: {time_dif}\n Памяти заняло:{mem_diff}\n\n')
        return res

    return wrapper


def revert(num):
    if num == 0:
        return ''
    else:
        return str(num % 10) + str(revert(num // 10))


@profile
@decor
def call_recursion(num):
    revert(num)


"""При попытке профилировать рекурсию, профилирование выполняется несколько раз 
(в зафисимости от колличества вызовов функцией самой себя), достаточно обернуть рекурсию в функцию обертку и 
профилировать уже во вложенном виде:

Функция - call_recursion
 Время заняло: 0.2243594
 Памяти заняло:0.0


Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    16     16.1 MiB     16.1 MiB           1       def wrapper(*args, **kwargs):
    17     16.1 MiB      0.0 MiB           1           t1 = default_timer()
    18     16.1 MiB      0.0 MiB           1           m1 = memory_usage()
    19     16.1 MiB      0.0 MiB           1           res = func(args[0])
    20     16.1 MiB      0.0 MiB           1           m2 = memory_usage()
    21     16.1 MiB      0.0 MiB           1           t2 = default_timer()
    22     16.1 MiB      0.0 MiB           1           mem_diff = m2[0] - m1[0]
    23     16.1 MiB      0.0 MiB           1           time_dif = t2 - t1
    24     16.1 MiB      0.0 MiB           1           print(f'Функция - {func.__name__}\n Время заняло: {time_dif}\n Памяти заняло:{mem_diff}\n\n')
    25     16.1 MiB      0.0 MiB           1           return res



Process finished with exit code 0

"""

revert(35100)
call_recursion(35100)
