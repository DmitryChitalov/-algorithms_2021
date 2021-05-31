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


def revers_1(enter_num, revers_num=0):
    if enter_num == 0:
        return revers_num
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        return revers_1(enter_num, revers_num)


t1 = timeit('revers_1', 'from __main__ import revers_1')
print(f'Результат замера revers_1: {t1} мс.')


def revers_2(enter_num, revers_num=0):
    while enter_num != 0:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
    return revers_num


t2 = timeit('revers_2', 'from __main__ import revers_2')
print(f'Результат замера revers_2: {t2} мс.')


def revers_3(enter_num):
    enter_num = str(enter_num)
    revers_num = enter_num[::-1]
    return revers_num


t3 = timeit('revers_3', 'from __main__ import revers_3')
print(f'Результат замера revers_3: {t3} мс.')


def main():
    revers_1(123456789)
    revers_2(123456789)
    revers_3(123456789)


run('main()')

# Наиболее быстрый алгоритм - revers_3, поскольку он берет срезы,
# не использует рекурсий, циклов и т.д.