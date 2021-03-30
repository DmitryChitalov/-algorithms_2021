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

from cProfile import run
from timeit import timeit


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


num_for_reverse = 1234567890

print('measurements through timeit')
print(timeit("revers_1(num_for_reverse)", setup='from __main__ import revers_1, num_for_reverse', number=10000))
print(timeit("revers_2(num_for_reverse)", setup='from __main__ import revers_2, num_for_reverse', number=10000))
print(timeit("revers_3(num_for_reverse)", setup='from __main__ import revers_3, num_for_reverse', number=10000))


def main():
    revers_1(num_for_reverse)
    revers_2(num_for_reverse)
    revers_3(num_for_reverse)


run('main()')

"""
measurements through timeit
0.018965588009450585
0.012329936027526855
0.0022716899984516203

как видим первый вариант (рекурсивный работает дольше), второй через цикл быстрее и третий через срез наиболее быстро
рекурсивный вариант работает больше из-за стека вызовов
вариант через срез самый быстрый, т.к. использует встроенные операторы

еще быстрее можно сделать через reversed(), но в таком случае вернется объект итератор



         17 function calls (7 primitive calls) in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
     11/1    0.000    0.000    0.000    0.000 task_3.py:20(revers_1)
        1    0.000    0.000    0.000    0.000 task_3.py:30(revers_2)
        1    0.000    0.000    0.000    0.000 task_3.py:38(revers_3)
        1    0.000    0.000    0.000    0.000 task_3.py:52(main)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        
На запуск всех функций ушло 0 секунд. Слабых мест нет.
"""
