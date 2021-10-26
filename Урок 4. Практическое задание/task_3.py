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


def revers_4(number):
    return f"{number % 10}{revers_4(number // 10)}" if number else ''


def revers_5(number):
    num_lst = list(str(number))
    num_lst.reverse()
    revers_num = "".join(num_lst)
    return revers_num


num = 12034
print(revers_1(num), revers_2(num), revers_3(num), revers_4(num), revers_5(num))

run('revers_1(num)')
run('revers_2(num)')
run('revers_3(num)')
run('revers_4(num)')
run('revers_5(num)')
print(timeit("revers_1(num)", globals=globals()))
print(timeit("revers_2(num)", globals=globals()))
print(timeit("revers_3(num)", globals=globals()))
print(timeit("revers_4(num)", globals=globals()))
print(timeit("revers_5(num)", globals=globals()))

# 43021.0 43021.0 43021 43021 43021

#          9 function calls (4 primitive calls) in 0.000 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#       6/1    0.000    0.000    0.000    0.000 task_3.py:20(revers_1)
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
#          9 function calls (4 primitive calls) in 0.000 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#       6/1    0.000    0.000    0.000    0.000 task_3.py:44(revers_4)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#
#
#          6 function calls in 0.000 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 task_3.py:48(revers_5)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#         1    0.000    0.000    0.000    0.000 {method 'join' of 'str' objects}
#         1    0.000    0.000    0.000    0.000 {method 'reverse' of 'list' objects}
#
#
# 3.259891657 <- рекурсия (9 вызовов)
# 2.0695475620000003 <- цикл (4)
# 0.8344578500000006 <- срезы (4)
# 3.2576859560000004 <- рекурсия с тернарным оператором (9)
# 1.3911851520000003 <- список - реверс списка -джоин (6)

# Из пяти реализаций, эффективнее всего реализация через 'срезы' ввиду наименьшей сложности (O(n)) и наименьшего
# числа вызовов функций (4, с такой же или меньшей сложностью). Далее, по возрастанию времени выполнения кода,
# реализация через "список - реверс списка -джоин" (та же сложность, но больше вызовов). Далее, операции в цикле.
# И, реализации через рекурсивную функцию, самые медлительные ввиду использования стека и числа вызовов.
