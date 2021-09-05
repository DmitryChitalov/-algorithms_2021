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


def revers_4(enter_num):
    return int(''.join(reversed(str(enter_num))))


enter_num = 123456


def main():
    revers_1(enter_num)
    revers_2(enter_num)
    revers_3(enter_num)
    revers_4(enter_num)


print(timeit("revers_1(enter_num)", globals=globals(), number=10000))
print(timeit("revers_2(enter_num)", globals=globals(), number=10000))
print(timeit("revers_3(enter_num)", globals=globals(), number=10000))
print(timeit("revers_4(enter_num)", globals=globals(), number=10000))


run('main()')

"""
Измерения timeit:

0.014292
0.010857400000000003
0.004136499999999994
0.011405600000000002


Профилирование:
ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
      7/1    0.000    0.000    0.000    0.000 task_3.py:21(revers_1)
        1    0.000    0.000    0.000    0.000 task_3.py:31(revers_2)
        1    0.000    0.000    0.000    0.000 task_3.py:39(revers_3)
        1    0.000    0.000    0.000    0.000 task_3.py:45(revers_4)
        1    0.000    0.000    0.000    0.000 task_3.py:52(main)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        1    0.000    0.000    0.000    0.000 {method 'join' of 'str' objects}
        
        
Обращаясь к измерениям, можно сделать вывод, что самым эффективным способом реализации 
является revers_3 с помощью срезов. Предложенное мной решение, с помощью встроенной функции reversed
и два другие решения имеют практически одинаковое время исполнения. 
 """