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
import cProfile


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

# Еще один вариант реализации - лаконичен.
def rev_4(num):
    return ''.join([x for x in str(num)[::-1]])

# Профилирование.
# timeit
print('timeit data output: \n')
print(timeit("1413466113623316661, revers_1(1413466113623316661)", globals=globals(), number=100000))
print(timeit("1413466113623316661, revers_2(1413466113623316661)", globals=globals(), number=100000))
print(timeit("1413466113623316661, revers_3(1413466113623316661)", globals=globals(), number=100000))
print(timeit("1413466113623316661, rev_4(1413466113623316661)", globals=globals(), number=100000))
print('---------------------------- \n')
# profile
print('cProfile data output: \n')
cProfile.run('revers_1(1413466113623316661)')
cProfile.run('revers_2(1413466113623316661)')
cProfile.run('revers_3(1413466113623316661)')
cProfile.run('rev_4(1413466113623316661)')
print('---------------------------- \n')

'''
timeit data output: 

0.5044762
0.4024875
0.04026139999999989
0.12977950000000016
---------------------------- 

cProfile data output: 

         23 function calls (4 primitive calls) in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
     20/1    0.000    0.000    0.000    0.000 task_3.py:17(revers_1)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


         4 function calls in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 task_3.py:27(revers_2)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


         4 function calls in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 task_3.py:35(revers_3)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


         6 function calls in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 task_3.py:41(rev_4)
        1    0.000    0.000    0.000    0.000 task_3.py:42(<listcomp>)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        1    0.000    0.000    0.000    0.000 {method 'join' of 'str' objects}


---------------------------- 

cProfile выдает пустой результат - слишком быстрые функции для отображения статистики с точностью до милисекунды.

Самый эффективный алгоритм - 3 в нем нет отдельных арифметических операций, нет циклов, рекурсий.

Алгоритм, который предложен мной - на втором месте, теряет в производительности на конкатенации строк, но решение более
лаконично.
'''
