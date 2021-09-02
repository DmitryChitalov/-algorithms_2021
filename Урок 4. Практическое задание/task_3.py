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
import random
from cProfile import run


def revers_1(enter_num, revers_num=0):
    '''
    неэффективна из-за трудоемкости рекурсии
    '''
    if enter_num == 0:
        return revers_num
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        return revers_1(enter_num, revers_num)


def revers_2(enter_num, revers_num=0):
    '''
    вероятно менее эффективна из-за арифметических операций в цикле
    '''
    while enter_num != 0:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
    return revers_num


def revers_3(enter_num):
    '''
    наиболее эффективна из-за отсутствия циклов и арифметических операций.
    идет обращение к строке нативным инструментом среза
    '''
    enter_num = str(enter_num)
    revers_num = enter_num[::-1]
    return revers_num


def revers_4(number, r_number=""):
    '''
    неэффективна из-за трудоемкости рекурсии
    '''
    return r_number if number < 1 else revers_4(number // 10, r_number=r_number + str(number % 10))


num = random.randint(10, 1000)

print(timeit("revers_1(num)", globals=globals()))
print(timeit("revers_2(num)", globals=globals()))
print(timeit("revers_3(num)", globals=globals()))
print(timeit("revers_4(num)", globals=globals()))

run("for _ in range(10**6): revers_1(num)")
run("for _ in range(10**6): revers_2(num)")
run("for _ in range(10**6): revers_3(num)")
run("for _ in range(10**6): revers_4(num)")
