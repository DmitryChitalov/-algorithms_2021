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
from cProfile import run
from random import randint
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


def revers_4(enter_num):
    enter_num = list(str(enter_num))
    enter_num.reverse()
    return ''.join(enter_num)


def main():
    revers_1(randint(1, 10000))
    revers_2(randint(1, 10000))
    revers_3(randint(1, 10000))
    revers_4(randint(1, 10000))


run("main()")
num = randint(1, 10000)
print(timeit("revers_1(num, revers_num=0)", globals=globals(), number=100))
print(timeit("revers_2(num, revers_num=0)", globals=globals(), number=100))
print(timeit("revers_3(num)", globals=globals(), number=100))
print(timeit("revers_4(num)", globals=globals(), number=100))


"""
Наиболее эффективной является реализация №3, так занимает меньшее количество времени за каждый из запусков:

Запуск 1:
         39 function calls (35 primitive calls) in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        4    0.000    0.000    0.000    0.000 random.py:237(_randbelow_with_getrandbits)
        4    0.000    0.000    0.000    0.000 random.py:290(randrange)
        4    0.000    0.000    0.000    0.000 random.py:334(randint)
      5/1    0.000    0.000    0.000    0.000 task_3.py:21(revers_1)
        1    0.000    0.000    0.000    0.000 task_3.py:31(revers_2)
        1    0.000    0.000    0.000    0.000 task_3.py:39(revers_3)
        1    0.000    0.000    0.000    0.000 task_3.py:45(revers_4)
        1    0.000    0.000    0.000    0.000 task_3.py:51(main)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        4    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        9    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
        1    0.000    0.000    0.000    0.000 {method 'join' of 'str' objects}
        1    0.000    0.000    0.000    0.000 {method 'reverse' of 'list' objects}


7.889999999999286e-05
5.3400000000008996e-05
2.6600000000001622e-05
4.500000000000337e-05

Запуск 2: 
         37 function calls (33 primitive calls) in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        4    0.000    0.000    0.000    0.000 random.py:237(_randbelow_with_getrandbits)
        4    0.000    0.000    0.000    0.000 random.py:290(randrange)
        4    0.000    0.000    0.000    0.000 random.py:334(randint)
      5/1    0.000    0.000    0.000    0.000 task_3.py:21(revers_1)
        1    0.000    0.000    0.000    0.000 task_3.py:31(revers_2)
        1    0.000    0.000    0.000    0.000 task_3.py:39(revers_3)
        1    0.000    0.000    0.000    0.000 task_3.py:45(revers_4)
        1    0.000    0.000    0.000    0.000 task_3.py:51(main)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        4    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        7    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
        1    0.000    0.000    0.000    0.000 {method 'join' of 'str' objects}
        1    0.000    0.000    0.000    0.000 {method 'reverse' of 'list' objects}


8.120000000000349e-05
5.2200000000002245e-05
2.6600000000001622e-05
4.600000000000437e-05

Запуск 3:
         36 function calls (32 primitive calls) in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        4    0.000    0.000    0.000    0.000 random.py:237(_randbelow_with_getrandbits)
        4    0.000    0.000    0.000    0.000 random.py:290(randrange)
        4    0.000    0.000    0.000    0.000 random.py:334(randint)
      5/1    0.000    0.000    0.000    0.000 task_3.py:21(revers_1)
        1    0.000    0.000    0.000    0.000 task_3.py:31(revers_2)
        1    0.000    0.000    0.000    0.000 task_3.py:39(revers_3)
        1    0.000    0.000    0.000    0.000 task_3.py:45(revers_4)
        1    0.000    0.000    0.000    0.000 task_3.py:51(main)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        4    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        6    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
        1    0.000    0.000    0.000    0.000 {method 'join' of 'str' objects}
        1    0.000    0.000    0.000    0.000 {method 'reverse' of 'list' objects}


7.939999999999336e-05
5.269999999998887e-05
2.689999999999637e-05
4.609999999999337e-05
"""

