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

def revers_4(enter_num):
    return ''.join(reversed((str(enter_num))))


num_1000 = randint(1000000, 10000000)
print(f'revers_1(num_1000) - {timeit("revers_1(num_1000)", globals=globals())}')
print(f'new_revers_1(num_1000) - {timeit("new_revers_1(num_1000)", globals=globals())}')
print(f'revers_2(num_1000) - {timeit("revers_2(num_1000)", globals=globals())}')
print(f'revers_3(num_1000) - {timeit("revers_3(num_1000)", globals=globals())}')
print(f'revers_4(num_1000) - {timeit("revers_4(num_1000)", globals=globals())}')


test_1 = """
for i in range(1000000):
    revers_1(num_1000)
"""
test_2 = """
for i in range(1000000):
    revers_2(num_1000)
"""
test_3 = """
for i in range(1000000):
    revers_3(num_1000)
"""
test_4 = """
for i in range(1000000):
    revers_4(num_1000)
"""

run(test_1)
print("-" * 100)
run(test_2)
print("-" * 100)
run(test_3)
print("-" * 100)
run(test_4)


"""
1. revers_1 and revers_2 do not work on chiles ending in the digit "0".
2.revers_1, new_revers_1 - the slowest, because work through recursion
3. revers_3 is the fastest.
4. revers_4 works slower than the cutoff, but faster than the other two, because no cycles
5. The profiler shows that the slowdown in revers_1 is caused by a significant number of
recursion calls: ncalls: 8000000/1000000. revers_4, in turn, is slowed down by an additional
by calling the join method

1. revers_1 и revers_2 не работают на чилах, оканчивающихся на цифру "0".
2. revers_1, new_revers_1 - самые медленные, т.к. работают через рекурсию 
3. revers_3 - самая быстрая. 
4. revers_4 работает медленнее среза, но быстрее двух остальных, т.к. нет циклов
5. Профайлер показывает, что замедление revers_1 вызвано значительным кол-вом 
вызовов рекурсии: ncalls: 8000000/1000000. revers_4 в свою очередь замедляется дополнительным 
вызовом метода join
___________________________________________________________________________________________________________________________
revers_1(num_1000) - 1.5211104999999998
new_revers_1(num_1000) - 2.1187229
revers_2(num_1000) - 1.0060113999999998
revers_3(num_1000) - 0.2924029999999993
revers_4(num_1000) - 0.5686131000000003
         8000003 function calls (1000003 primitive calls) in 3.113 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.253    0.253    3.113    3.113 <string>:2(<module>)
8000000/1000000    2.860    0.000    2.860    0.000 Algorithm4.3.py:6(revers_1)
        1    0.000    0.000    3.113    3.113 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


----------------------------------------------------------------------------------------------------
         1000003 function calls in 1.198 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.208    0.208    1.198    1.198 <string>:2(<module>)
  1000000    0.990    0.000    0.990    0.000 Algorithm4.3.py:22(revers_2)
        1    0.000    0.000    1.198    1.198 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


----------------------------------------------------------------------------------------------------
         1000003 function calls in 0.522 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.205    0.205    0.522    0.522 <string>:2(<module>)
  1000000    0.317    0.000    0.317    0.000 Algorithm4.3.py:30(revers_3)
        1    0.000    0.000    0.522    0.522 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


----------------------------------------------------------------------------------------------------
         2000003 function calls in 1.030 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.227    0.227    1.029    1.029 <string>:2(<module>)
  1000000    0.454    0.000    0.803    0.000 Algorithm4.3.py:36(revers_4)
        1    0.000    0.000    1.030    1.030 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
  1000000    0.348    0.000    0.348    0.000 {method 'join' of 'str' objects}
"""
