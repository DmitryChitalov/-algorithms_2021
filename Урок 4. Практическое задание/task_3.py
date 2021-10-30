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


import sys
from timeit import timeit
from cProfile import run

sys.setrecursionlimit(3000)


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
    return ''.join([str(i) for i in (x for x in str(enter_num)[::-1])])


def main(arr):
    revers_1(arr)
    revers_2(arr)
    revers_3(arr)
    revers_4(arr)


arr = int(''.join([str(el) for el in range(1000)]))


print(f'''Время выполнения revers_1(arr)
==>>{timeit(
        'revers_1(arr)',
        globals=globals(),
        number=10000
    )}
# ''', end='\n')
# run('revers_1')

print(f'''Время выполнения revers_2(arr)
==>>{timeit(
        'revers_2(arr)',
        globals=globals(),
        number=10000
    )}
# ''', end='\n')
# run('revers_2')

print(f'''Время выполнения revers_3(arr)
==>>{timeit(
        'revers_3(arr)',
        globals=globals(),
        number=10000
    )}
# ''', end='\n')
# run('revers_3')

print(f'''Время выполнения revers_4(arr)
==>>{timeit(
        'revers_4(arr)',
        globals=globals(),
        number=10000
    )}
# ''', end='\n')
# run('revers_4')

run('main(arr)')


# Время выполнения revers_1(arr)
# ==>>57.58934165199753
# # 
# Время выполнения revers_2(arr)
# ==>>37.516389247000916
# # 
# Время выполнения revers_3(arr)
# ==>>1.312020579003729
# # 
# Время выполнения revers_4(arr)
# ==>>5.189374495996162
# # 
#          5789 function calls (2900 primitive calls) in 0.013 seconds

#    Ordered by: standard name

#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.013    0.013 <string>:1(<module>)
#    2890/1    0.008    0.000    0.008    0.008 task_3.py:24(revers_1)
#         1    0.004    0.004    0.004    0.004 task_3.py:34(revers_2)
#         1    0.000    0.000    0.000    0.000 task_3.py:42(revers_3)
#         1    0.000    0.000    0.001    0.001 task_3.py:48(revers_4)
#      2890    0.000    0.000    0.000    0.000 task_3.py:49(<genexpr>)
#         1    0.000    0.000    0.001    0.001 task_3.py:49(<listcomp>)
#         1    0.000    0.000    0.013    0.013 task_3.py:52(main)
#         1    0.000    0.000    0.013    0.013 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#         1    0.000    0.000    0.000    0.000 {method 'join' of 'str' objects}
# 
# Вывод: 
# функция revers_3 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
