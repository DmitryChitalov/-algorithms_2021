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


def revers_4(enter_num):
    return str(enter_num) if enter_num < 10 else str(enter_num % 10) + revers_4(enter_num // 10)


print('Рекурсия: ', timeit('revers_1(100000)', globals=globals()))
print('Цикл: ', timeit('revers_2(100000)', globals=globals()))
print('Срез: ', timeit('revers_3(100000)', globals=globals()))
print('Тернарный оператор + рекурсия: ', timeit('revers_4(100000)', globals=globals()))

run('revers_1(100000)')
run('revers_2(100000)')
run('revers_3(100000)')
run('revers_4(100000)')


# Вывод: Из-за среза функция 3 сработала быстрее всех.
# На втором месте оказалась функция 2 с циклом while.
# Самым медленным оказалось решение в одну строку с тернарным оператором.
