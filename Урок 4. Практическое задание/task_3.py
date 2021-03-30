"""
Задание 3.

Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.

Сделайте профилировку каждого алгоритма через cProfile и через timeit

Сделайте вывод, какая из трех реализаций эффективнее и почему!!!

И можете предложить еще свой вариант решения!
Без аналитики задание считается не принятым
"""

from cProfile import runctx
from timeit import timeit
from random import randint


def revers_1(enter_num, revers_num=0):
    if enter_num == 0:
        return revers_num
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        return revers_1(enter_num, revers_num)


def revers_2(enter_num, revers_num=0):
    while enter_num != 0:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
    return revers_num


def revers_3(enter_num):
    enter_num = str(enter_num)
    revers_num = enter_num[::-1]
    return revers_num


def revers_4(enter_num):
    return ''.join(reversed(str(enter_num)))


num = randint(100000000, 10000000000000)
print(
    timeit(
        'revers_1(num)',
        setup='from __main__ import revers_1, num',
        number=10000))
print(
    timeit(
        'revers_2(num)',
        setup='from __main__ import revers_2, num',
        number=10000))
print(
    timeit(
        'revers_3(num)',
        setup='from __main__ import revers_3, num',
        number=10000))
print(
    timeit(
        'revers_4(num)',
        setup='from __main__ import revers_4, num',
        number=10000))

"""
timeit показал следубщие результаты.
1 решение: 0.057336
2 решение: 0.03936769999999999
3 решение: 0.005734199999999995

1е решение с рекурсией самое медленное (рекурсия - модно, но медленнее простого цикла)
3е решение лучшее, так как использует встроенные функции.
"""

runctx('revers_1(num)', {'num': num, 'revers_1': revers_1}, {})
runctx('revers_2(num)', {'num': num, 'revers_2': revers_2}, {})
runctx('revers_3(num)', {'num': num, 'revers_3': revers_3}, {})
runctx('revers_4(num)', {'num': num, 'revers_4': revers_4}, {})

"""
cProfile здесь не помог, так как даже на длинном числе функции отрабатывабт достаточно быстро.
Можно сделать сделать вывод, что решения, которые делают меньшее количество вызовов различных функций лучше жругих.
Однако это утверждение стоит подкреплять timeit'ом

17 function calls (4 primitive calls) in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
     14/1    0.000    0.000    0.000    0.000 task_3.py:21(revers_1)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


         4 function calls in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 task_3.py:31(revers_2)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


         4 function calls in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 task_3.py:39(revers_3)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


Написал функцию revers_4. Она менее эффективна чем revers_3, однако обгоняет по эффективности другие два примера.

"""
