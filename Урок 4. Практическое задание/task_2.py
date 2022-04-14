"""
Задание 2.

Приведен код, который формирует из введенного числа
обратное по порядку входящих в него цифр.
Задача решена через рекурсию
Выполнена попытка оптимизировать решение через мемоизацию.
Сделаны замеры обеих реализаций.

Сделайте аналитику, нужна ли здесь мемоизация или нет и почему?!!!
Будьте внимательны, задание хитрое. Не все так просто, как кажется.
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

TRY_NUMS = 100000

print('Не оптимизированная функция recursive_reverse')
print(
    timeit(
        "recursive_reverse(num_100)",
        setup='from __main__ import recursive_reverse, num_100',
        number=TRY_NUMS))
print(
    timeit(
        "recursive_reverse(num_1000)",
        setup='from __main__ import recursive_reverse, num_1000',
        number=TRY_NUMS))
print(
    timeit(
        "recursive_reverse(num_10000)",
        setup='from __main__ import recursive_reverse, num_10000',
        number=TRY_NUMS))


def memoize(f):
    cache = {}

    def decorate(*args):
        nonlocal cache
        if args in cache:
            # print(f'Hit on cache {args}')
            return cache[args]
        else:
            cache[args] = f(*args)
            # print(f'Not hit on cache {args}')
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
        number=TRY_NUMS))
print(
    timeit(
        'recursive_reverse_mem(num_1000)',
        setup='from __main__ import recursive_reverse_mem, num_1000',
        number=TRY_NUMS))
print(
    timeit(
        'recursive_reverse_mem(num_10000)',
        setup='from __main__ import recursive_reverse_mem, num_10000',
        number=TRY_NUMS))

"""
Не оптимизированная функция recursive_reverse
0.1900816
0.22922970000000004
0.4249421
Оптимизированная функция recursive_reverse_mem
0.016651799999999994
0.017601300000000042
0.017204099999999944
После выполнения тестовых запусков создается впечатлние значительного ускорения выполнения функции
с мемоизацией. Но это впечатление обманчиво. Кажущиеся ускорение - результат особенностей метода
работы модуля timeit
"""
