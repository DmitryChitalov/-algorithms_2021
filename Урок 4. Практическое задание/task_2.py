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
import functools, time


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


@functools.lru_cache(maxsize=50)
def recursive_reverse_cache(number):
    if number == 0:
        return ''
    return f'{str(number % 10)}{recursive_reverse_cache(number // 10)}'


print('Оптимизированная функция recursive_reverse_cache')
print(
    timeit(
        'recursive_reverse_cache(num_100)',
        setup='from __main__ import recursive_reverse_cache, num_100',
        number=10000))
print(
    timeit(
        'recursive_reverse_cache(num_1000)',
        setup='from __main__ import recursive_reverse_cache, num_1000',
        number=10000))
print(
    timeit(
        'recursive_reverse_cache(num_10000)',
        setup='from __main__ import recursive_reverse_cache, num_10000',
        number=10000))

"""
Не оптимизированная функция recursive_reverse
0.0274507
0.0284991
0.05245090000000001

Оптимизированная функция recursive_reverse_mem
0.0019438999999999984
0.0019444000000000128
0.0020792999999999784

Оптимизированная функция recursive_reverse_cache
0.0006347000000000158
0.0006375999999999882
0.0006919999999999982


Мемоизация здесь не нужна, она не поможет, т.к. декоратор выступает в качестве кэша, при первом запуске в нем создается кэш
и при последующих запусках числа берутся из кэша
Можно использовать встроенную функцию кэширования @functools.lru_cache,
что заметно увеличивает производительность
"""
