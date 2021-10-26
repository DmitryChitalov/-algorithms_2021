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


# Аналитика:

print('Замеры реального времени выполнения кода функции memoize от recursive_reverse')
print(
    timeit(
        'memoize(recursive_reverse(num_100))',
        setup='from __main__ import memoize, recursive_reverse, num_100',
        number=10000))

print(
    timeit(
        'memoize(recursive_reverse(num_1000))',
        setup='from __main__ import memoize, recursive_reverse, num_1000',
        number=10000))

print(
    timeit(
        'memoize(recursive_reverse(num_10000))',
        setup='from __main__ import memoize, recursive_reverse, num_10000',
        number=10000))

# Не оптимизированная функция recursive_reverse
# 0.030561654
# 0.034070334
# 0.06593753399999999
# Оптимизированная функция recursive_reverse_mem
# 0.0024293489999999973
# 0.002381454999999977
# 0.002706879999999995
# Замеры реального времени выполнения кода функции memoize от recursive_reverse
# 0.035258282
# 0.03818239600000001
# 0.07080606900000003

# Расходы на мемоизацию не обоснованы ввиду того, что каждый раз аргументом рекурсивной функции является новое число,
# а "Оптимизированная функция recursive_reverse_mem" просто берет результат из кэша, который вычисляется примерно
# столко же, сколько и сама функция - "Не оптимизированная функция recursive_reverse".
