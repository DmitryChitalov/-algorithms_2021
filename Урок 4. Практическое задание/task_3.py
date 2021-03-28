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

def reverse_integrated(number):
    return reversed(str(number))

def main(count_iteration):
    for i in range(count_iteration):
        number = randint(100000000, 10000000000000)
        revers_1(number)
        revers_2(number)
        revers_3(number)
        reverse_integrated(number)

number = 1234567890
count_iteration = 100000
func_list = ['revers_1', 'revers_2', 'revers_3', 'reverse_integrated']

print('Сравним варианты :')
for el in func_list:
    print(f'Функция {el}:', timeit(el+'(number)', number=count_iteration, globals=globals()))

run('main(count_iteration)')

'''
При сравнении скорости методов через timeit, результаты:
Функция revers_1: 0.5272178200000001
Функция revers_2: 0.370732037
Функция revers_3: 0.07003947900000007
Профилировка через cProfile дает подобные результаты:
   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
1389003/100000    1.327    0.000    1.327    0.000 task_3.py:21(revers_1)
   100000    0.512    0.000    0.512    0.000 task_3.py:31(revers_2)
   100000    0.096    0.000    0.096    0.000 task_3.py:39(revers_3)
Учитывая рекурсивность вызова revers_1, в количестве вызовов указаны оба, как из сторонней функции, так и самовызов.
Ответ:
    самая эффективная из представленных реализация - revers_3 
Естественно, лучшей реализацией механизма является встроенный реверс *см. задачу №2 
В качестве подтверждения, привожу замеры:
Функция reverse_integrated: 0.0632787210000001
   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
   100000    0.079    0.000    0.079    0.000 task_3.py:44(reverse_integrated)
'''