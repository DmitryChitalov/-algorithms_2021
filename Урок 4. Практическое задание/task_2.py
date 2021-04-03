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
Не оптимизированная функция recursive_reverse
0.032300499999999996
0.0350771
0.058264999999999983
Оптимизированная функция recursive_reverse_mem
0.002461700000000011
0.002575799999999989
0.0020073000000000174

Мемоизация положительно влияет на оптимазацию функци, 
но Мемоизаци пригодится, если после наполнения кэша,
потребуются новые вызовы функции.
"""
# Оптимизиация через встроенную функцию reversed


def func_reversed(number):
    return reversed(str(number))


print('Использование reversed')
print(
    timeit(
        'func_reversed(num_100)',
        setup='from __main__ import func_reversed, num_100',
        number=10000))
print(
    timeit(
        'func_reversed(num_1000)',
        setup='from __main__ import func_reversed, num_1000',
        number=10000))
print(
    timeit(
        'func_reversed(num_10000)',
        setup='from __main__ import func_reversed, num_10000',
        number=10000))

"""
Не оптимизированная функция recursive_reverse
0.029893799999999998
0.025449
0.047757200000000014
Использование reversed
0.003132700000000016
0.0029993000000000103
0.0031241000000000185
"""
