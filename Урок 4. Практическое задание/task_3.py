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


number = 102345678900
print(timeit("revers_1(number)", globals=globals(), number=10000))
print(revers_1(number))
print(timeit("revers_2(number)", globals=globals(), number=10000))
print(revers_2(number))
print(timeit("revers_3(number)", globals=globals(), number=10000))
print(revers_3(number))
run("revers_1(number)")
run("revers_2(number)")
run("revers_3(number)")

'''
Функция revers_1 неправильно переворачивают число, добавляя .0 на конце
и игнорируют любое колво нулей в конце заданного числа. Работает медленно из-за рекурсии.

Функция revers_2 неправильно переворачивают число, добавляя .0 на конце
и игнорируют любое колво нулей в конце заданного числа. Работает быстрее рекурсии,
потому что цикл

Функция revers_3 единственная кто правильно переворачивает число
делая это быстрее первых двух функций через срез строки

cProfile показывает по трем функциям нули
'''
