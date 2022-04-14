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
from random import randint
from cProfile import run

num_100 = randint(10000, 1000000)
num_1000 = randint(1000000, 10000000)
num_10000 = randint(100000000, 10000000000000)


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


for i in range(3):
    func_name = f'revers_{i + 1}'
    print(func_name)
    for j in range(3):
        print(
            timeit(
                f"{func_name}(num_{pow(10, (j + 2))})",
                setup=f'from __main__ import {func_name}, num_100, num_1000, num_10000',
                number=10000
            )
        )


def main():
    for _ in range(pow(10, 4)):
        revers_1(num_100)
        revers_1(num_1000)
        revers_1(num_10000)

        revers_2(num_100)
        revers_2(num_1000)
        revers_2(num_10000)

        revers_3(num_100)
        revers_3(num_1000)
        revers_3(num_10000)


run('main()')

"""
Самая эффективная - revers_3
потому что там используется встроенная функция
"""
