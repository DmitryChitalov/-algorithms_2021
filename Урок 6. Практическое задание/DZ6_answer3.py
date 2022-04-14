"""
Задание 3 *.
Сделать профилировку для скриптов с рекурсией и сделать описание,
можно ли так профилировать и есть ли 'подводные камни' в профилировании?
Придумать как это решить!
Есть очень простое решение
"""

from memory_profiler import profile


@profile
def measure_fun_for_recursion(rec_func):
    return rec_func


def symbol(start=32, end=127, str_len_max=10):
    symbol_number = end
    symbol_position = symbol_number - start + 1
    if symbol_number == start:
        return f'{symbol_number} - {chr(symbol_number)} '
    return symbol(end=end - 1) + f'{symbol_number} - {chr(symbol_number)} ' + (
        '\n' if symbol_position % str_len_max == 0 else '')


measure_fun_for_recursion(symbol())

'''
Для измерения памяти потребляемой рекурсивной функцией её можно вложить в другую функцию и 
измерять память для этой функции, что бы предотвратить вызов профилировщика для каждого уровня рекурсии 

Результаты замеров:
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    12     19.9 MiB     19.9 MiB           1   @profile
    13                                         def measure_fun_for_recursion(rec_func):
    14     19.9 MiB      0.0 MiB           1       return rec_func'''
