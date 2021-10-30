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
# ==>>47.9482960220048
# # 
# Время выполнения revers_2(arr)
# ==>>36.041991400008556
# # 
# Время выполнения revers_3(arr)
# ==>>1.260988333990099
# # 
# Время выполнения revers_4(arr)
# ==>>4.966254525992554
# # 
#          5789 function calls (2900 primitive calls) in 0.012 seconds

#    Ordered by: standard name

#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.011    0.011 <string>:1(<module>)
#    2890/1    0.007    0.000    0.007    0.007 task_3.py:25(revers_1)
#         1    0.004    0.004    0.004    0.004 task_3.py:35(revers_2)
#         1    0.000    0.000    0.000    0.000 task_3.py:43(revers_3)
#         1    0.000    0.000    0.001    0.001 task_3.py:49(revers_4)
#      2890    0.000    0.000    0.000    0.000 task_3.py:50(<genexpr>)
#         1    0.000    0.000    0.001    0.001 task_3.py:50(<listcomp>)
#         1    0.000    0.000    0.011    0.011 task_3.py:53(main)
#         1    0.000    0.000    0.012    0.012 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#         1    0.000    0.000    0.000    0.000 {method 'join' of 'str' objects}
# 
# Вывод: 
# функция revers_3 мне кажется ее можно сделать только хуже, имея ввиду
# скорость выполнения, собственно чем я и занялся..
#   Рекурсия буксует и переполняет стэк - последнее место в данном забеге.
#   revers_2 - так же задерживается, возможно на математических % // операциях
# а потом еще цикл while, который не просто перебирает, а так же проверяет на 
# истинность условия - всё это время!
#   Победитель revers_3 - без усложнений - числа в строку, а у строки замечательный
# способ [::-1] или даже .revers() - меньше операций, все встроенные,
# краткая запись, просто читаймая - и как итог самая быстрая!
#   revers_4 - а давайте к тому что отлично сработало прикрутим что - нибудь
# этакое...Так получилась идея через  LC пройтись по генератору развернутой строки =)жжжесть
# 
# P.S.: извиняюсь за чрезмерно эмоциональную подачу, я сегодня по другому не мог.
# 


