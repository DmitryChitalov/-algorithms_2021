"""
Задание 3 *.
Сделать профилировку для скриптов с рекурсией и сделать описание,
можно ли так профилировать и есть ли 'подводные камни' в профилировании?
Придумать как это решить!
Есть очень простое решение!
"""

from memory_profiler import profile


# @profile
def progress(count_of_numbers):
    if count_of_numbers == 1:
        return 1
    result = 1
    result += (-1) * (progress(count_of_numbers - 1) / 2)
    return result


"""
Профилирование рекурсий даёт таблицу на каждый вызов рекурсии, в данном случае следующая таблица выводится 5 раз:
_________________________________________________________________________________________________________________
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    12     18.8 MiB     18.8 MiB           5   @profile
    13                                         def progress(count_of_numbers):
    14     18.8 MiB      0.0 MiB           5       if count_of_numbers == 1:
    15     18.8 MiB      0.0 MiB           1           return 1
    16     18.8 MiB      0.0 MiB           4       result = 1
    17     18.8 MiB      0.0 MiB           4       result += (-1) * (progress(count_of_numbers - 1) / 2)
    18     18.8 MiB      0.0 MiB           4       return result
"""


@profile
def wrapp(num):
    return progress(num)


"""
Завернув функцию в ещё один слой мы избавимся от многократных вызовов таблицы.
______________________________________________________________________________
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    21     18.8 MiB     18.8 MiB           1   @profile
    22                                         def wrapp(num):
    23     18.8 MiB      0.0 MiB           1       return progress(num)
"""

wrapp(5)
