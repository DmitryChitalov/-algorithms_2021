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
from timeit import repeat
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


def revers_4(enter_num):
    enter_num = str(enter_num)
    revers_num = ''
    for i in range(1, len(enter_num) + 1):
        revers_num += enter_num[-i]
    return revers_num


print(revers_1(52896345))
print(revers_2(52896345))
print(revers_3(52896345))
print(revers_4(52896345))

stmt = ["revers_1(enter_num, revers_num=0)",
        "revers_2(enter_num, revers_num=0)",
        "revers_3(enter_num)",
        "revers_4(enter_num)"]


for st in stmt:
    print(f'на выполение функции {st} затрачено времени: '
          f'{min(repeat(st, setup="enter_num=52896345", globals=globals()))}')

func = [revers_1,
        revers_2,
        revers_3,
        revers_4]

for f in func:
    print('-' * 30)
    print(f'Profiling: {f.__name__}')
    print('-' * 30)
    pr = cProfile.Profile()
    for i in range(10 ** 5):
        pr.runcall(f, 52896345)
    pr.create_stats()
    pr.print_stats()


"""
Из полученных данных можно сделать вывод о том, что функция со срезом наиболее эффективна для создания реверса числа.
Наименее эффективна же рекурсия. Циклы показывают результат хуже, чем срез из-за обилия арифметических действий. 


на выполение функции revers_1(enter_num, revers_num=0) затрачено времени: 1.3967877999999994
на выполение функции revers_2(enter_num, revers_num=0) затрачено времени: 0.9809124000000011
на выполение функции revers_3(enter_num) затрачено времени: 0.2455248999999995
на выполение функции revers_4(enter_num) затрачено времени: 0.881807199999999
------------------------------
Profiling: revers_1
------------------------------
         1000000 function calls (200000 primitive calls) in 0.266 seconds

   Ordered by: standard name

       ncalls  tottime  percall  cumtime  percall filename:lineno(function)
900000/100000    0.261    0.000    0.261    0.000 task_3.py:20(revers_1)
       100000    0.005    0.000    0.005    0.000 {method 'disable' of '_lsprof.Profiler' objects}


------------------------------
Profiling: revers_2
------------------------------
         200000 function calls in 0.105 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
   100000    0.101    0.000    0.101    0.000 task_3.py:30(revers_2)
   100000    0.004    0.000    0.004    0.000 {method 'disable' of '_lsprof.Profiler' objects}


------------------------------
Profiling: revers_3
------------------------------
         200000 function calls in 0.032 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
   100000    0.027    0.000    0.027    0.000 task_3.py:38(revers_3)
   100000    0.004    0.000    0.004    0.000 {method 'disable' of '_lsprof.Profiler' objects}


------------------------------
Profiling: revers_4
------------------------------
         300000 function calls in 0.113 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
   100000    0.103    0.000    0.109    0.000 task_3.py:44(revers_4)
   100000    0.005    0.000    0.005    0.000 {built-in method builtins.len}
   100000    0.005    0.000    0.005    0.000 {method 'disable' of '_lsprof.Profiler' objects}
"""

