"""
Задание 3 *.
Сделать профилировку для скриптов с рекурсией и сделать описание,
можно ли так профилировать и есть ли 'подводные камни' в профилировании?
Придумать как это решить!
Есть очень простое решение!
"""
from timeit import default_timer
from memory_profiler import memory_usage, profile

#@profile
def rec_func(num):
    #print(num)
    if num < 1:
        return num
    return rec_func(num - 1)

@profile
def wrapp(num):
    return rec_func(num)

#rec_func(100)
wrapp(10)

'''
При использовании @profile c рекурсивной функцией замер происходит каждую иттерацию

Но если рекурсию обернуть в простую функцию то замер пройдёт как положено
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    18     19.5 MiB     19.5 MiB           1   @profile
    19                                         def wrapp(num):
    20     19.5 MiB      0.0 MiB           1       return rec_func(num)
'''