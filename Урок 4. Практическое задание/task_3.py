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
    
    
import cProfile
from timeit import timeit

print(timeit("987654321, revers_1(987654321)", globals=globals(), number=100000))
print(timeit("987654321, revers_2(987654321)", globals=globals(), number=100000))
print(timeit("987654321, revers_3(987654321)", globals=globals(), number=100000))

"""Спрофилируем данные функции через timeit
0.31722449999999996
0.16098750000000006
0.04283939999999997
"""

"""Теперь через cProfile"""
cProfile.run('revers_1(987654321)')
cProfile.run('revers_2(987654321)')
cProfile.run('revers_3(987654321)')
"""
Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
     10/1    0.000    0.000    0.000    0.000 t_i_m_e.py:194(revers_1)
        1    0.002    0.002    0.002    0.002 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


         4 function calls in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 t_i_m_e.py:204(revers_2)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


         4 function calls in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 t_i_m_e.py:212(revers_3)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

На выходе получаем одни нули. Вывод: для простых замеров cProfile не используем, ибо придется
писать цикл для многочисленных замеров. Есть более лаконичные методики.
"""
"""Предлагаю свой вариант алгоритма"""


def revers_4(enter_num):
    return ''.join(i for i in str(enter_num))


print(timeit("987654321, revers_1(987654321)", globals=globals(), number=100000))
print(timeit("987654321, revers_2(987654321)", globals=globals(), number=100000))
print(timeit("987654321, revers_3(987654321)", globals=globals(), number=100000))
print(timeit("987654321, revers_4(987654321)", globals=globals(), number=100000))

"""
Результаты замеров такие:
0.2600239
0.1691016999999999
0.04368770000000011
0.13656080000000004

Функция 3 самая быстрая, причины:
 - наименьшее количество функций, а если есть, то встроенные.
 - наименьшее количество математических операций
 - отсутствие циклов
 Но самая лучшая функция это 4 потому как ее придумал я =)
"""