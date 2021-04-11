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
        return str(number % 10)
    return f'{str(number % 10)}{recursive_reverse(number // 10)}'


num_100 = randint(10000, 1000000)
num_1000 = randint(1000000, 10000000)
num_10000 = randint(100000000, 10000000000000)

print('Не оптимизированная функция recursive_reverse')
print(
    timeit(
        "recursive_reverse(num_100)",
        setup='from __main__ import recursive_reverse, num_100',
        number=10000))
print(
    timeit(
        "recursive_reverse(num_1000)",
        setup='from __main__ import recursive_reverse, num_1000',
        number=10000))
print(
    timeit(
        "recursive_reverse(num_10000)",
        setup='from __main__ import recursive_reverse, num_10000',
        number=10000))


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
        number=10000))
print(
    timeit(
        'recursive_reverse_mem(num_1000)',
        setup='from __main__ import recursive_reverse_mem, num_1000',
        number=10000))
print(
    timeit(
        'recursive_reverse_mem(num_10000)',
        setup='from __main__ import recursive_reverse_mem, num_10000',
        number=10000))
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

from copy import copy


num_100 = randint(10000, 1000000)

num_1000 = randint(1000000, 10000000)

num_10000 = randint(100000000, 10000000000000)


# Без мемоизации
def recursive_reverse(number):

    if number == 0:

        return ''

    return f'{str(number % 10)}{recursive_reverse(number // 10)}'


print('Не оптимизированная функция recursive_reverse')

print(
    timeit(
        "recursive_reverse(copy(num_100))",
        globals=globals(),
        number=100000))

print(
    timeit(
        "recursive_reverse(copy(num_1000))",
        globals=globals(),
        number=100000))

print(
    timeit(
        "recursive_reverse(copy(num_10000))",
        globals=globals(),
        number=100000))

print()


# С мемоизацией
def function_2(f):
    cache = {}

    def decorate(*args):
        if args in cache:
            print(cache[args])
            return cache[args]
        else:

            cache[args] = f(*args)
            print(cache[args])
            return cache[args]
    return decorate


@memoize
def recursive_reverse_memoize(number):
    if number == 0:
        return ''
    return f'{str(number % 10)}{recursive_reverse_memoize(number // 10)}'


print('Оптимизированная функция recursive_reverse_memoize')
print(
    timeit(
        'recursive_reverse_memoize(copy(num_100))',
        globals=globals(),
        number=100000))

print(
    timeit(
        'recursive_reverse_memoize(copy(num_1000))',
        globals=globals(),
        number=100000))
print(
    timeit(
        'recursive_reverse_memoize(copy(num_10000))',
        globals=globals(),
        number=100000))


"""
Я думаю что в данном номере мемоизаци не нужна, так как в кеш не будут вмещаться значения которые используются вновь.
Замеры отличаются (их данные), так как мемоизация содает кеш.
"""
