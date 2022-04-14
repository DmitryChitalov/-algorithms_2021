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

from timeit import timeit
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

def revers_my(enter_num):
    return ''.join(reversed(str(enter_num)))

user_num = int(input('Введите число: '))
print('-- timeit --')
print('revers_1:',
        timeit('revers_1(user_num)',
            setup='from __main__ import revers_1, user_num',
            number=10000))
print('revers_2:',
        timeit('revers_2(user_num)',
            setup='from __main__ import revers_2, user_num',
            number=10000))
print('revers_3:',
        timeit('revers_3(user_num)',
            setup='from __main__ import revers_3, user_num',
            number=10000))
print('revers_my:',
        timeit('revers_my(user_num)',
            setup='from __main__ import revers_my, user_num',
            number=10000))
print('-- Профайлер --')
run('revers_1(user_num)')
run('revers_2(user_num)')
run('revers_3(user_num)')
run('revers_my(user_num)')

# Введите число: 765765754220
# -- timeit --
# revers_1: 0.0335005000000006 - самый медленный вариант. Рекурсия
# revers_2: 0.015302799999999728 - тот же алгортм, но без рекурсии работает быстрее
# revers_3: 0.002660600000000457 - самый быстрый вариант. Работаем только с элементами списка, читаем его наоборот
# revers_my: 0.005963799999999964 - второй по скорости. Используем встроенные функции питона
# -- Профайлер -- ПРофайлер ничего не показал. Видимо очень маленький кусок для профилирования и работает быстро
#          16 function calls (4 primitive calls) in 0.000 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#      13/1    0.000    0.000    0.000    0.000 task_3.py:20(revers_1)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#
#
#          4 function calls in 0.000 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 task_3.py:30(revers_2)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#
#
#          4 function calls in 0.000 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 task_3.py:38(revers_3)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#
#
#          5 function calls in 0.000 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 task_3.py:43(revers_my)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#         1    0.000    0.000    0.000    0.000 {method 'join' of 'str' objects}
#
#
#
# Process finished with exit code 0


