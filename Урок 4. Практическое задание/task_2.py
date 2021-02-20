"""
Задание 2.

Приведен код, который формирует из введенного числа
обратное по порядку входящих в него цифр.
Задача решена через рекурсию
Выполнена попытка оптимизировать решение через мемоизацию.
Сделаны замеры обеих реализаций.

Сделайте аналитику, нужна ли здесь мемоизация или нет и почему?!!!
Если у вас есть идеи, предложите вариант оптимизации, если мемоизация не имеет смысла.
Без аналитики задание считается не принятым
"""

from timeit import timeit
from random import randint


def recursive_reverse(number):
    if number == 0:
        return ''
    return f'{str(number % 10)}{recursive_reverse(number // 10)}'


num_100 = randint(10000, 1000000)
num_1000 = randint(1000000, 10000000)
num_10000 = randint(100000000, 10000000000000)

print('Не оптимизированная функция recursive_reverse')
print(
    timeit(
        "recursive_reverse(num_100)",
        setup='from __main__ import recursive_reverse, num_100',
        number=100000))

print(
    timeit(
        "recursive_reverse(num_1000)",
        setup='from __main__ import recursive_reverse, num_1000',
        number=100000))

print(
    timeit(
        "recursive_reverse(num_10000)",
        setup='from __main__ import recursive_reverse, num_10000',
        number=100000))


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
def recursive_reverse_mem(number):
    if number == 0:
        return ''
    return f'{str(number % 10)}{recursive_reverse_mem(number // 10)}'


print('Оптимизированная функция recursive_reverse_mem')
print(
    timeit(
        'recursive_reverse_mem(num_100)',
        setup='from __main__ import recursive_reverse_mem, num_100',
        number=100000))
print(
    timeit(
        'recursive_reverse_mem(num_1000)',
        setup='from __main__ import recursive_reverse_mem, num_1000',
        number=100000))
print(
    timeit(
        'recursive_reverse_mem(num_10000)',
        setup='from __main__ import recursive_reverse_mem, num_10000',
        number=100000))


'''
Если делать вывод, то можно сказать, что нет смысла реализовывать эту функцию через мемоизацию,
так как, так или иначе, мемоизация просто кэширует данные из функции, то есть, при повторном вызове
данные берутся не из рекурсии, а из кэша. Это, конечно, ускоряет работу функции при очередном вызове,
но, по сути, сложность ее от этого не меняется.
Поэтому рассмотрим еще варианты, которые способны оптимизировать работу этой функции, такие как
цикл или более простые механизмы реверса:
'''


def simple_rev(num):
    return str(num)[::-1]


print('Оптимизированная функция simple_rev')
print(
    timeit(
        'simple_rev(num_100)',
        setup='from __main__ import simple_rev, num_100',
        number=100000))
print(
    timeit(
        'simple_rev(num_1000)',
        setup='from __main__ import simple_rev, num_1000',
        number=100000))
print(
    timeit(
        'simple_rev(num_10000)',
        setup='from __main__ import simple_rev, num_10000',
        number=100000))


def another_simple_rev(num):
    rev_num = ''
    for el in reversed(str(num)):
        rev_num.join(el)
    return rev_num


print('Оптимизированная функция another_simple_rev')
print(
    timeit(
        'another_simple_rev(num_100)',
        setup='from __main__ import another_simple_rev, num_100',
        number=100000))
print(
    timeit(
        'another_simple_rev(num_1000)',
        setup='from __main__ import another_simple_rev, num_1000',
        number=100000))
print(
    timeit(
        'another_simple_rev(num_10000)',
        setup='from __main__ import another_simple_rev, num_10000',
        number=100000))


'''
Видим, что самый действенный и быстрый механизм выполнения реверса - через срез
'''
