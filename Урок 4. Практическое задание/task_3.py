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
from random import randint


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


num = randint(100000000, 1000000000000)


print('revers_1:', timeit('revers_1(num)', globals=globals()))
print('revers_2:', timeit('revers_2(num)', globals=globals()))
print('revers_3:', timeit('revers_3(num)', globals=globals()))
print('revers_4:', timeit('revers_4(num)', globals=globals()))


"""Самый быстрый варинт из предложенны третий.
Но можно ускорить его незначительно, убрав лишние присваивания и сразу возвратив результат

revers_1: 3.3313432
revers_2: 2.3091881000000005
revers_3: 0.40609440000000063
revers_4: 0.38985429999999965
"""