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
import random
from timeit import timeit
from cProfile import run
from time import sleep

enter_num = random.randint(100, 10000)


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


def revers_1_cp(enter_num, revers_num=0):
    if enter_num == 0:
        return revers_num
    else:
        sleep(0.1)
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        return revers_1_cp(enter_num, revers_num)


def revers_2_cp(enter_num, revers_num=0):
    while enter_num != 0:
        sleep(0.1)
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
    return revers_num


def revers_3_cp(enter_num):
    sleep(0.1)
    enter_num = str(enter_num)
    revers_num = enter_num[::-1]
    return revers_num


def revers_4_cp(enter_num):
    """свой вариант через функцию reversed"""
    sleep(0.1)
    return ''.join(reversed(str(enter_num)))


print('Время выполнения (timeit) revers_1:')
print(timeit(stmt="revers_1(enter_num)",
             setup="from __main__ import revers_1, enter_num",
             number=10000))

print('Время выполнения (timeit) revers_2:')
print(timeit(stmt="revers_2(enter_num)",
             setup="from __main__ import revers_2, enter_num",
             number=10000))

print('Время выполнения (timeit) revers_3:')
print(timeit(stmt="revers_3(enter_num)",
             setup="from __main__ import revers_3, enter_num",
             number=10000))

# добавил отдельные функции с добавленным слипом
print('Время выполнения (cProfile) revers_1_cp:')
run('revers_1_cp(enter_num)')
print('Время выполнения (cProfile) revers_2_cp:')
run('revers_2_cp(enter_num)')
print('Время выполнения (cProfile) revers_3_cp:')
run('revers_3_cp(enter_num)')

print('Время выполнения (cProfile) revers_4_cp:')
run('revers_4_cp(enter_num)')

"""
Время выполнения (timeit) revers_1:
0.010566454000000003
Время выполнения (timeit) revers_2:
0.007158786
Время выполнения (timeit) revers_3:
0.0031475130000000046
Время выполнения (cProfile) revers_1_cp:
         12 function calls (8 primitive calls) in 0.430 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.430    0.430 <string>:1(<module>)
      5/1    0.000    0.000    0.430    0.430 task_3.py:45(revers_1_cp)
        1    0.000    0.000    0.430    0.430 {built-in method builtins.exec}
        4    0.430    0.107    0.430    0.107 {built-in method time.sleep}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


Время выполнения (cProfile) revers_2_cp:
         8 function calls in 0.427 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.427    0.427 <string>:1(<module>)
        1    0.000    0.000    0.427    0.427 task_3.py:56(revers_2_cp)
        1    0.000    0.000    0.427    0.427 {built-in method builtins.exec}
        4    0.427    0.107    0.427    0.107 {built-in method time.sleep}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
Время выполнения (cProfile) revers_3_cp:
         5 function calls in 0.109 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.109    0.109 <string>:1(<module>)
        1    0.000    0.000    0.109    0.109 task_3.py:65(revers_3_cp)
        1    0.000    0.000    0.109    0.109 {built-in method builtins.exec}
        1    0.109    0.109    0.109    0.109 {built-in method time.sleep}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        
        
reverse_3_cp функция выполняется быстрее, т.к. использует срез и вызывается всего 5 функций 
в отличии от рекурсии в reverse_1_cp (12 вызовов) и цикла в  reverse_2_cp (8 функций)

Свой вариант (6 вызовов) с инвертированием строки получился лучше чем рекурсивного и цикла, но хуже среза:

Время выполнения (cProfile) revers_4_cp:
         6 function calls in 0.109 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.108    0.108 <string>:1(<module>)
        1    0.000    0.000    0.108    0.108 task_3.py:74(revers_4_cp)
        1    0.000    0.000    0.109    0.109 {built-in method builtins.exec}
        1    0.108    0.108    0.108    0.108 {built-in method time.sleep}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        1    0.000    0.000    0.000    0.000 {method 'join' of 'str' objects}
"""