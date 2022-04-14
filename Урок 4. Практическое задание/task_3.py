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


def revers_4(enter_num: int):

    return "".join(reversed(str(enter_num)))


test_num = 12345678
print(f'профилировка через сProfile')

run('revers_1(test_num)')
run('revers_2(test_num)')
run('revers_3(test_num)')
run('revers_4(test_num)')

print(f'профилировка через timeit')

print('reverse_1',
      timeit(
          "revers_1(test_num)",
          setup='from __main__ import revers_1, test_num',
          number=1))
print('reverse_2',
      timeit(
          "revers_2(test_num)",
          setup='from __main__ import revers_2, test_num',
          number=1))
print('reverse_3',
      timeit(
          "revers_3(test_num)",
          setup='from __main__ import revers_3, test_num',
          number=1))
print('reverse_4',
      timeit(
          "revers_4(test_num)",
          setup='from __main__ import revers_4, test_num',
          number=1))

# ### Результаты ###
# профилировка через сProfile
#          12 function calls (4 primitive calls) in 0.000 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#       9/1    0.000    0.000    0.000    0.000 task_3.py:20(revers_1)
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
#          5 function calls in 0.000 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 task_3.py:44(revers_4)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#         1    0.000    0.000    0.000    0.000 {method 'join' of 'str' objects}
#
#
# профилировка через timeit
# reverse_1 3.4000000000006247e-06
# reverse_2 2.300000000003688e-06
# reverse_3 1.3999999999986246e-06
# reverse_4 2.599999999998437e-06
# Выводы: как мы видим, для оценки времени исполнения функции удобнее использовать timeit,
# а для просмотра какие функции фызывались и в каком количестве, очень удобно использовать cProfile.
# По итогам выполнения функций, самой быстрой оказалась reverse_3, при этом она вызывает всего 4 функции,
# самой медленной оказалась reverse_1, т.к. это рекурсивная функция.
# Собственная реализации reverse_4 оказалась весьма эффективной, но все же реализация через срез строки работает быстрее
# и проще.
