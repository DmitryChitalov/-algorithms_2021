"""
Задание 3 *.
Сделать профилировку для скриптов с рекурсией и сделать описание,
можно ли так профилировать и есть ли 'подводные камни' в профилировании?
Придумать как это решить!
Есть очень простое решение
"""

from cProfile import run
from memory_profiler import memory_usage
from timeit import default_timer


def memory_and_time(func):
    def wrapper(*args, **kwargs):
        start_time = default_timer()
        m1 = memory_usage()
        res = func(*args)
        m2 = memory_usage()
        time_diff = default_timer() - start_time
        mem_diff = m2[0] - m1[0]
        res = func(*args)
        print(f"m1 = {m1} Mib, m2 = {m2} Mib\nВыполнение заняло {mem_diff} Mib, {time_diff} sec")
        return res

    return wrapper


# Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...

# @memory_and_time    # Так профилировать скрипты с рекурсией нельзя,
                      # поскольку происходит нагромождение вызовов функции.
def sum_n(n, i=0, el=1, s=0):
    s += el
    el /= -2
    i += 1
    if n == 1:
        return f'Количество элементов: {i}, их сумма: {s}.'
    return sum_n(n-1, i, el, s)


# Можно профилировать с помощью cProfile.run по количеству вызовов данной функции и наследуемых функций,
# определять слабые места, но на небольших данных сложно делать выводы о времени выполнения.
run('sum_n(5)')

# 8 function calls (4 primitive calls) in 0.000 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#       5/1    0.000    0.000    0.000    0.000 task_3.py:31(sum_n)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}



# Можно, конечно, решить с помощью цикла, но это уже совсем другая функция!!!
# @memory_and_time
# def sum_n2(n):
#     total = 0
#     el = 1
#     for i in range(n):
#         total += el
#         el /= -2
#     return total


# sum_n2(5)


# !!! Вероятнее всего, самый удобный способ делать профилировку для скриптов с рекурсией, это создать функцию
# (или еще один декоратор), вызывающую требуемую рекурсивную функцию. Здесь мы с минимальной погрешностью
# (вызов внешней функции тоже чего-то стоит) можем увидеть суммарные результаты для всего стека вызовов.
@memory_and_time
def tot(n):
    res = sum_n(n)
    return res


tot(5)
# m1 = [18.25] Mib, m2 = [18.25390625] Mib
# Выполнение заняло 0.00390625 Mib, 0.199371731 sec
