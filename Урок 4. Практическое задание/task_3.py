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
from random import random as rnd
from timeit import timeit
from cProfile import run

number_r = int(rnd() * 1000000000000)

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
    return str(enter_num)[::-1]


print('revers_1:', timeit('revers_1(number_r)', globals=globals()))
print('revers_2:', timeit('revers_2(number_r)', globals=globals()))
print('revers_3:', timeit('revers_3(number_r)', globals=globals()))
print('revers_4:', timeit('revers_4(number_r)', globals=globals()))

def main():
    revers_1(number_r)
    revers_2(number_r)
    revers_3(number_r)
    revers_4(number_r)

print()
run('main()')

"""
revers_1: 5.8720907
revers_2: 4.223267700000001
revers_3: 0.5982604000000009
revers_4: 0.5265360000000001

Вывод: из всех 4 вариантов самый долгий - 1, далее по списку - 2, 3, 4. 
Первый варант медленный за счет рекурсии, 2ой варик - цикл быстрее выполняется, т.к. необходим один цикл для решения
3ий - быстрее за счет строки, откуда и берутся сразу элементы. 4ый вариант - предложение по оптимизации решения 3го .

CProfile не эффективен, т.к. выполняется единичный вызов и он очень быстрый, поэтому и результаты при выводе
 получаются ниже:
   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
     13/1    0.000    0.000    0.000    0.000 task_3.py:21(revers_1)
        1    0.000    0.000    0.000    0.000 task_3.py:31(revers_2)
        1    0.000    0.000    0.000    0.000 task_3.py:39(revers_3)
        1    0.000    0.000    0.000    0.000 task_3.py:44(revers_4)
        1    0.000    0.000    0.000    0.000 task_3.py:53(main)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
"""