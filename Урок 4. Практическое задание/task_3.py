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


def revers_1(input_num, revers_num=0):
    if input_num == 0:

        return revers_num

    else:
        num = input_num % 10

        revers_num = (revers_num + num / 10) * 10

        input_num //= 10

        return revers_1(input_num, revers_num)


def revers_2(input_num, revers_num=0):
    while input_num != 0:
        num = input_num % 10

        revers_num = (revers_num + num / 10) * 10

        input_num //= 10

    return revers_num


def revers_3(input_num):
    input_num = str(input_num)

    revers_num = input_num[::-1]

    return revers_num


def main():
    input_num = 123456789

    print(str(revers_1(input_num)))

    print(str(revers_2(input_num)))

    print(str(revers_3(input_num)))


input_num_second = 1234567890

run('main()')

print(timeit('revers_1(input_num_second)', setup='from __main__ import revers_1, input_num_second', number=1000000))

print(timeit('revers_2(input_num_second)', setup='from __main__ import revers_2, input_num_second', number=1000000))

print(timeit('revers_3(input_num_second)', setup='from __main__ import revers_3, input_num_second', number=1000000))

'''
Результат cProfile:
ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
     10/1    0.000    0.000    0.000    0.000 task_3.py:16(revers_1)
        1    0.000    0.000    0.000    0.000 task_3.py:26(revers_2)
        1    0.000    0.000    0.000    0.000 task_3.py:34(revers_3)
        1    0.000    0.000    0.000    0.000 task_3.py:40(main)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        3    0.000    0.000    0.000    0.000 {built-in method builtins.print}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

Так как время в cProfile меньше 0.001, сравнить или измерить время не выйдет.
'''
