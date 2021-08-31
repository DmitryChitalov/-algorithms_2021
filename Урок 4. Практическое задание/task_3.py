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
    if enter_num == 0:
        return ''
    else:
        revers = str(enter_num % 10)
        enter_num = enter_num // 10
        return revers + revers_4(enter_num)


num = 13840

print(timeit(stmt="revers_1(num)", setup="from __main__ import revers_1, num"))     # 1.5491
print(timeit(stmt="revers_2(num)", setup="from __main__ import revers_2, num"))     # 1.1577
print(timeit(stmt="revers_3(num)", setup="from __main__ import revers_3, num"))     # 0.4387
print(timeit(stmt="revers_4(num)", setup="from __main__ import revers_4, num"))     # 2.1658

# Самая быстрая функция - revers_3. С использованием среза. Самая медленная - revers_4 т.к. О(n!)

def main():
    revers_1()
    revers_2()
    revers_3()
    revers_4()

run('main()')

"""         4 function calls in 0.000 seconds              

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 task_3.py:64(main)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
"""

# насчитал 4 вызова функции. Не нашел узких мест, на выполнение кода потрачено 0,000 сек., отсекая числа после 0,000