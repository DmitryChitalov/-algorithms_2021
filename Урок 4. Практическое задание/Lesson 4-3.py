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


def memoize(f):
    cache = {}

    def decorate(*args):

        if args in cache:
            return cache[args]
        else:
            cache[args] = f(*args)
            return cache[args]
    return decorate


@memoize
def revers_1_mem(enter_num, revers_num=0):
    if enter_num == 0:
        return revers_num
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        return revers_1(enter_num, revers_num)


@memoize
def revers_2_mem(enter_num, revers_num=0):
    while enter_num != 0:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
    return revers_num


@memoize
def revers_3_mem(enter_num):
    enter_num = str(enter_num)
    revers_num = enter_num[::-1]
    return revers_num


num_100 = randint(10000, 1000000)
num_1000 = randint(1000000, 10000000)
num_10000 = randint(100000000, 10000000000000)


def main(num_1, num_2, num_3):
    revers_1(num_1)
    revers_1(num_2)
    revers_1(num_3)
    revers_2(num_1)
    revers_2(num_2)
    revers_2(num_3)
    revers_3(num_1)
    revers_3(num_2)
    revers_3(num_3)
    revers_1_mem(num_1)
    revers_1_mem(num_2)
    revers_1_mem(num_3)
    revers_2_mem(num_1)
    revers_2_mem(num_2)
    revers_2_mem(num_3)
    revers_3_mem(num_1)
    revers_3_mem(num_2)
    revers_3_mem(num_3)


run('main(num_100, num_1000, num_10000)')

print('Функция revers_1')
print(
    timeit(
        'revers_1(num_100)',
        setup='from __main__ import revers_1, num_100',
        number=10000))
print(
    timeit(
        'revers_1(num_1000)',
        setup='from __main__ import revers_1, num_1000',
        number=10000))
print(
    timeit(
        'revers_1(num_10000)',
        setup='from __main__ import revers_1, num_10000',
        number=10000))
print('-------------------------')
print('Функция revers_2')
print(
    timeit(
        'revers_2(num_100)',
        setup='from __main__ import revers_2, num_100',
        number=10000))
print(
    timeit(
        'revers_2(num_1000)',
        setup='from __main__ import revers_2, num_1000',
        number=10000))
print(
    timeit(
        'revers_2(num_10000)',
        setup='from __main__ import revers_2, num_10000',
        number=10000))
print('-------------------------')
print('Функция revers_3')
print(
    timeit(
        'revers_3(num_100)',
        setup='from __main__ import revers_3, num_100',
        number=10000))
print(
    timeit(
        'revers_3(num_1000)',
        setup='from __main__ import revers_3, num_1000',
        number=10000))
print(
    timeit(
        'revers_3(num_10000)',
        setup='from __main__ import revers_3, num_10000',
        number=10000))
print('-------------------------')
print('По результатам замеров вариант со срезом оказался самым быстрым, но что если мы применим мемоизацию?')
print('-------------------------МЕМОИЗАЦИЯ-------------------------')
print('Функция revers_1_mem')
print(
    timeit(
        'revers_1_mem(num_100)',
        setup='from __main__ import revers_1_mem, num_100',
        number=10000))
print(
    timeit(
        'revers_1_mem(num_1000)',
        setup='from __main__ import revers_1_mem, num_1000',
        number=10000))
print(
    timeit(
        'revers_1_mem(num_10000)',
        setup='from __main__ import revers_1_mem, num_10000',
        number=10000))
print('-------------------------')
print('Функция revers_2_mem')
print(
    timeit(
        'revers_2_mem(num_100)',
        setup='from __main__ import revers_2_mem, num_100',
        number=10000))
print(
    timeit(
        'revers_2_mem(num_1000)',
        setup='from __main__ import revers_2_mem, num_1000',
        number=10000))
print(
    timeit(
        'revers_2_mem(num_10000)',
        setup='from __main__ import revers_2_mem, num_10000',
        number=10000))
print('-------------------------')
print('Функция revers_3_mem')
print(
    timeit(
        'revers_3_mem(num_100)',
        setup='from __main__ import revers_3_mem, num_100',
        number=10000))
print(
    timeit(
        'revers_3_mem(num_1000)',
        setup='from __main__ import revers_3_mem, num_1000',
        number=10000))
print(
    timeit(
        'revers_3_mem(num_10000)',
        setup='from __main__ import revers_3_mem, num_10000',
        number=10000))
print('ВЫВОД: Варианты с мемоизацией гораздо быстрее, а между собой они практически идентичны, \n'
      'но всё таки вариант со срезом оказывается быстрее!')
