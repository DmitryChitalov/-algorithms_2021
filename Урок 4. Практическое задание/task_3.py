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
from random import randint
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


def main(count_iter, number):
    for i in range(count_iter):
        revers_1(number)
        revers_2(number)
        revers_3(number)


print('Замеры Timeit:')
numb = randint(1000000, 1000000000)
func_list = ['revers_1', 'revers_2', 'revers_3']
for func in func_list:
    print(f'Функция {func}:', timeit(func + '(numb)', number=1000000, globals=globals()))

print('\nЗамеры cProfile:')
run('main(1000000, numb)')

"""
Замеры Timeit:
Функция revers_1: 2.9163433
Функция revers_2: 1.7984789
Функция revers_3: 0.3989035000000003

Замеры cProfile:
         12000004 function calls (3000004 primitive calls) in 7.723 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    7.723    7.723 <string>:1(<module>)
10000000/1000000    4.497    0.000    4.497    0.000 task_3.py:21(revers_1)
  1000000    2.060    0.000    2.060    0.000 task_3.py:31(revers_2)
  1000000    0.441    0.000    0.441    0.000 task_3.py:39(revers_3)
        1    0.725    0.725    7.723    7.723 task_3.py:45(main)
        1    0.000    0.000    7.723    7.723 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

        
revers_3 - оптимальный вариант O(n). Срез наиболее быстрый в плане выполнения
задачи.  
Рекурсия и цикл имеют арифмитические действия поэтому они проигрывают
в скорости по сравнению со срезом в котором отсутствуют арифмитические действия.
"""
