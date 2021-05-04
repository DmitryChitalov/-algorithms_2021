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

from cProfile import run
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


#  4 вариант решения при помощи reversed строки
def revers_4(enter_num):
    return ''.join(reversed(str(enter_num)))


rnd_num = randint(1000000, 100000000)

print('timeit revers_1', round(timeit('revers_1(rnd_num)', globals=globals(), number=1000000), 4), 'sec.')
print('timeit revers_2', round(timeit('revers_2(rnd_num)', globals=globals(), number=1000000), 4), 'sec.')
print('timeit revers_3', round(timeit('revers_3(rnd_num)', globals=globals(), number=1000000), 4), 'sec.')
print('timeit revers_4', round(timeit('revers_4(rnd_num)', globals=globals(), number=1000000), 4), 'sec.')

"""
timeit revers_1 1.7989 sec.
timeit revers_2 1.2286 sec.
timeit revers_3 0.2983 sec.
timeit revers_4 0.6093 sec.
"""

#  Добавим в cProfile аналогичное с timeit количество вызовов функции.


def revers_1_profile():
    for i in range(1000000):
        revers_1(rnd_num)


def revers_2_profile():
    for i in range(1000000):
        revers_2(rnd_num)


def revers_3_profile():
    for i in range(1000000):
        revers_3(rnd_num)


def revers_4_profile():
    for i in range(1000000):
        revers_4(rnd_num)


run('revers_1_profile()')
run('revers_2_profile()')
run('revers_3_profile()')
run('revers_4_profile()')

"""
______________________________________________________________________________________________
         9000004 function calls (1000004 primitive calls) in 3.490 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    3.490    3.490 <string>:1(<module>)
9000000/1000000    3.262    0.000    3.262    0.000 task_3.py:22(revers_1)
        1    0.228    0.228    3.490    3.490 task_3.py:72(revers_1_profile)
        1    0.000    0.000    3.490    3.490 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
______________________________________________________________________________________________

         1000004 function calls in 1.409 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    1.409    1.409 <string>:1(<module>)
  1000000    1.229    0.000    1.229    0.000 task_3.py:32(revers_2)
        1    0.181    0.181    1.409    1.409 task_3.py:77(revers_2_profile)
        1    0.000    0.000    1.409    1.409 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
______________________________________________________________________________________________

         1000004 function calls in 0.482 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.482    0.482 <string>:1(<module>)
  1000000    0.305    0.000    0.305    0.000 task_3.py:40(revers_3)
        1    0.177    0.177    0.482    0.482 task_3.py:82(revers_3_profile)
        1    0.000    0.000    0.482    0.482 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
______________________________________________________________________________________________

         2000004 function calls in 1.042 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    1.042    1.042 <string>:1(<module>)
  1000000    0.459    0.000    0.831    0.000 task_3.py:47(revers_4)
        1    0.211    0.211    1.042    1.042 task_3.py:87(revers_4_profile)
        1    0.000    0.000    1.042    1.042 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
  1000000    0.372    0.000    0.372    0.000 {method 'join' of 'str' objects}
______________________________________________________________________________________________
    Профилировка через timeit и cProfile показывает, что лучшее решение задачи
это решение через срезы, т.к. количество операций с данными самое минимальное.
    Использование рекурсии - не самое лучшее решение, т.к. замедляет выполнение кода
за счет стека вызовов функций.
    Цикл работает медленее из за перебора символов в числе.
    Реверс функция работает медленее из за необходимости сперва разбить, а потом склеить
в обратном порядке символы числа.
"""