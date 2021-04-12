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


#  В качестве дополнительного варианта попробуем решение со встроенной функцией reversed
def revers_4(enter_num):
    return "".join(reversed(str(enter_num)))


v_enter_num = 113231423432454646
v_attempts = 1000000

print('timeit revers_1',
      round(
          timeit(
              'revers_1(v_enter_num)',
              globals=globals(),
              number=v_attempts)
          , 4),
      'seconds')

print('timeit revers_2',
      round(
          timeit(
              'revers_2(v_enter_num)',
              globals=globals(),
              number=v_attempts)
          , 4),
      'seconds')

print('timeit revers_3',
      round(
          timeit(
              'revers_3(v_enter_num)',
              globals=globals(),
              number=v_attempts)
          , 4),
      'seconds')

print('timeit revers_4',
      round(
          timeit(
              'revers_4(v_enter_num)',
              globals=globals(),
              number=v_attempts)
          , 4),
      'seconds')

"""
timeit revers_1 4.3623 seconds
timeit revers_2 2.9849 seconds
timeit revers_3 0.3454 seconds
timeit revers_4 0.9053 seconds

ВЫВОД: использование срезов списка намного эффективнее по скорости, чем другие 
способы, особенно если сравнивать с циклом и рекурсией. Ожидаемо самый медленный способ - через рекурсию. 
Срезы оказались эффективнее техники с использованием встроенного метода reversed, что не удивительно, 
т.к. работа со срезами имеет мимнимальное количество "дополнительного" кода, имплементирующего эту работу. 

"""

#  Для получения сравнимых цифр при использовании техники профилирования и timeit пишем оболочку, где наша функция
#  будет вызываться аналогичное количество раз. Профилируем именно эту функцию.
from cProfile import run


def revers_1_profile():
    for _ in range(v_attempts):
        ret = revers_1(v_enter_num)


def revers_2_profile():
    for _ in range(v_attempts):
        ret = revers_2(v_enter_num)


def revers_3_profile():
    for _ in range(v_attempts):
        ret = revers_3(v_enter_num)


def revers_4_profile():
    for _ in range(v_attempts):
        ret = revers_4(v_enter_num)


print('-------------------------Профилируем  revers_1------------------------------')
run('revers_1_profile()')
print('-------------------------Профилируем  revers_2------------------------------')
run('revers_2_profile()')
print('-------------------------Профилируем  revers_3------------------------------')
run('revers_3_profile()')
print('-------------------------Профилируем  revers_4------------------------------')
run('revers_4_profile()')

"""
-------------------------Профилируем  revers_1------------------------------
         19000004 function calls (1000004 primitive calls) in 7.818 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    7.818    7.818 <string>:1(<module>)
        1    0.223    0.223    7.818    7.818 task_3.py:101(revers_1_profile)
19000000/1000000    7.595    0.000    7.595    0.000 task_3.py:19(revers_1)
        1    0.000    0.000    7.818    7.818 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


-------------------------Профилируем  revers_2------------------------------
         1000004 function calls in 3.268 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    3.268    3.268 <string>:1(<module>)
        1    0.207    0.207    3.268    3.268 task_3.py:106(revers_2_profile)
  1000000    3.060    0.000    3.060    0.000 task_3.py:29(revers_2)
        1    0.000    0.000    3.268    3.268 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


-------------------------Профилируем  revers_3------------------------------
         1000004 function calls in 0.610 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.610    0.610 <string>:1(<module>)
        1    0.213    0.213    0.610    0.610 task_3.py:111(revers_3_profile)
  1000000    0.397    0.000    0.397    0.000 task_3.py:37(revers_3)
        1    0.000    0.000    0.610    0.610 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


-------------------------Профилируем  revers_4------------------------------
         2000004 function calls in 1.267 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    1.267    1.267 <string>:1(<module>)
        1    0.196    0.196    1.267    1.267 task_3.py:115(revers_4_profile)
  1000000    0.479    0.000    1.071    0.000 task_3.py:43(revers_4)
        1    0.000    0.000    1.267    1.267 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
  1000000    0.592    0.000    0.592    0.000 {method 'join' of 'str' objects}



ВЫВОД:
Профилирование вызовов подтверждает вывод, сделанный по рузультатам тестов с помощью метода timeit: 
использование рекурсии - не самое лучшее решение, т.к. замедляет выполнение кода за счет избыточногго количества вызовов
функций. Самым лучшим решением является использование срезов.
"""
