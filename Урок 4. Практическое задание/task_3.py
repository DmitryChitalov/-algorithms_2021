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


def revers_4(num):
    return int("".join(reversed(str(num))))


print(f"Время работы функции {revers_1.__name__} составило {timeit('revers_1', globals=globals())} сек.")
print(f"Время работы функции {revers_2.__name__} составило {timeit('revers_2', globals=globals())} сек.")
print(f"Время работы функции {revers_3.__name__} составило {timeit('revers_3', globals=globals())} сек.")
print(f"Время работы функции {revers_4.__name__} составило {timeit('revers_4', globals=globals())} сек.")

run("revers_1(123456789)")
run("revers_2(123456789)")
run("revers_3(123456789)")
run("revers_4(123456789)")
"""
Отчет из модуля профилирования timeit:
Время работы функции revers_1 составило 0.1052572 сек.
Время работы функции revers_2 составило 0.09989810000000002 сек.
Время работы функции revers_3 составило 0.08532410000000001 сек.
Время работы функции revers_4 составило 0.0815304 сек.
Отчет из модуля профилирования cProfile:

Revers_1:
ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
     10/1    0.000    0.000    0.000    0.000 task_3.py:20(revers_1)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

Revers_2:
 ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 task_3.py:30(revers_2)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        
Revers_3:
ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 task_3.py:38(revers_3)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        
Revers_4:
ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 task_3.py:44(revers_4)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        1    0.000    0.000    0.000    0.000 {method 'join' of 'str' objects}
        
Вывод: исходя статистки cProfile не чего, не ясно так как функция вызвается один раз и общее время выполнения 
составляет 0.000 сек.
Но исходя данных из модуля timeit видно что мой вариант через встроенные функции самый эфективный, 
на втором месте идет вариант через срез, так как выполняется гораздо быстрее, чем например цикл,
на третьем месте через цикл while, проигрывает срезу, т.к. гораздо больше операций надо выполнить,
ну а последние место через арифметические действия, т.к. много времени тратиться на лишние действия.
"""