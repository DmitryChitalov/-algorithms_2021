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

from cProfile import run
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


def main():
    enter_num = 123456789
    print(str(revers_1(enter_num)))
    print(str(revers_2(enter_num)))
    print(str(revers_3(enter_num)))


enter_num1 = 1234567890

run('main()')
print(timeit('revers_1(enter_num1)', setup='from __main__ import revers_1, enter_num1', number=1000000))
print(timeit('revers_2(enter_num1)', setup='from __main__ import revers_2, enter_num1', number=1000000))
print(timeit('revers_3(enter_num1)', setup='from __main__ import revers_3, enter_num1', number=1000000))


'''
АНАЛИТИКА
результат работы cProfile
   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
     10/1    0.000    0.000    0.000    0.000 HW4_3.py:20(revers_1)
        1    0.000    0.000    0.000    0.000 HW4_3.py:30(revers_2)
        1    0.000    0.000    0.000    0.000 HW4_3.py:38(revers_3)
        1    0.000    0.000    0.000    0.000 HW4_3.py:44(main)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        3    0.000    0.000    0.000    0.000 {built-in method builtins.print}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
Используя  cProfile узнать сравнить время исполнения невозможно, т.к. оно меньше  0.001.         
        

результат работы timeit
3.8047826909999998  для revers_1 рекурсия, с использованием %, //
2.3694993970000002  для revers_2    цикл с использованием %,//
0.5286077339999995   для revers_3  с использованием среза

Используя timeit можно увидеть, что самый медленный вариант это с использованием рекурсии, что логично, т.к. 
имеем два прохода и поворный вызов функции. С мемоизацией этот вариант был бы быстрее.
На втором месте цикл, т.к. у него один проход по всем цифрам числа.
Самый быстрый вариант - вариант с использованием среза. В этом варианте нет дополнительных операций, только срез.
И т.к. срез - это внутренний механизм языка, то он наиболее оптимален, что мы и видим по результатам измерений врмени 
выполнения.


'''