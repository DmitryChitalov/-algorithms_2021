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

import timeit
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

def revers_4(enter_num):
    enter_num = str(enter_num)
    enter_num = list(enter_num)
    enter_num.reverse()
    revers_num = "".join(enter_num)
    return revers_num

num = randint(100000000, 10000000000000)

print(
    timeit.timeit(
         "revers_1(num)",
         globals=globals(),
         number=10000))

print(
    timeit.timeit(
         "revers_2(num)",
         globals=globals(),
         number=10000))

print(
    timeit.timeit(
         "revers_3(num)",
         globals=globals(),
         number=10000))

print(
    timeit.timeit(
         "revers_4(num)",
         globals=globals(),
         number=10000))

def summer (en_num):
    revers_1(en_num)
    revers_2(en_num)
    revers_3(en_num)
    revers_4(en_num)

run ('summer(num)')

""" Самое оптимальное решение revers_3, выполняется быстрее всех, так как имеет линейную сложность
решение предложенное мной похоже на решение revers_3, поэтому имеет сопоставимое время выполнения, 
но из-за дополнительных операций выполняется медленнее"""