"""
Задание 3.

Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.

Сделайте профилировку каждого алгоритма через cProfile и через timeit

Обязательно предложите еще свой вариант решения и также запрофилируйте!

Сделайте вывод, какая из четырех реализаций эффективнее и почему!!!

Без аналитики задание считается не принятым
"""

from timeit import Timer
from random import randint as randint
from cProfile import run


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


def my_revers(enter_num):
    return ''.join(reversed(str(enter_num)))


t1 = Timer("revers_1(randint(1000000, 1000000000))", "from __main__ import revers_1, randint")
print('t1', t1.timeit(number=1000000))

t2 = Timer("revers_2(randint(1000000, 1000000000))", "from __main__ import revers_2, randint")
print('t2', t2.timeit(number=1000000))

t3 = Timer("revers_3(randint(1000000, 1000000000))", "from __main__ import revers_3, randint")
print('t3', t3.timeit(number=1000000))

t4 = Timer("my_revers(randint(1000000, 1000000000))", "from __main__ import my_revers, randint")
print('t4', t4.timeit(number=1000000))

run('revers_1(randint(1000000, 1000000000))')

run('revers_2(randint(1000000, 1000000000))')

run('revers_3(randint(1000000, 1000000000))')

run('my_revers(randint(1000000, 1000000000))')


# Результаты измерений показаны ниже. При использовании timeit наилучшую производительность
# показал третий алгоритм. Четвертый алгоритм так же имеет право на существование с учетом скорости его
# выполнения в сравнении с первыми двумя алгоритмами
# cProfile выдал результат, на основании которого сложно сделать вывод о производительности
# всех четырех алгоритмов


# t1 3.330165898
# t2 2.4815765560000003
# t3 1.3377762730000002
# t4 1.7683113179999994
#          18 function calls (9 primitive calls) in 0.000 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 random.py:237(_randbelow_with_getrandbits)
#         1    0.000    0.000    0.000    0.000 random.py:290(randrange)
#         1    0.000    0.000    0.000    0.000 random.py:334(randint)
#      10/1    0.000    0.000    0.000    0.000 task_3.py:21(revers_1)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#         1    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
#
#
#          9 function calls in 0.000 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 random.py:237(_randbelow_with_getrandbits)
#         1    0.000    0.000    0.000    0.000 random.py:290(randrange)
#         1    0.000    0.000    0.000    0.000 random.py:334(randint)
#         1    0.000    0.000    0.000    0.000 task_3.py:31(revers_2)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#         1    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
#
#
#          9 function calls in 0.000 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 random.py:237(_randbelow_with_getrandbits)
#         1    0.000    0.000    0.000    0.000 random.py:290(randrange)
#         1    0.000    0.000    0.000    0.000 random.py:334(randint)
#         1    0.000    0.000    0.000    0.000 task_3.py:39(revers_3)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#         1    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
#
#
#          10 function calls in 0.000 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 random.py:237(_randbelow_with_getrandbits)
#         1    0.000    0.000    0.000    0.000 random.py:290(randrange)
#         1    0.000    0.000    0.000    0.000 random.py:334(randint)
#         1    0.000    0.000    0.000    0.000 task_3.py:45(my_revers)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#         1    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
#         1    0.000    0.000    0.000    0.000 {method 'join' of 'str' objects}
#
