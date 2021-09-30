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
from functools import cache


# @cache
def recursive_reverse(number):
    if number == 0:
        return ''
    return f'{str(number % 10)}{recursive_reverse(number // 10)}'


num_100 = randint(10000, 1000000)
num_1000 = randint(1000000, 10000000)
num_10000 = randint(100000000, 10000000000000)
# num_100 = 123456
# num_1000 = 1234567
# num_10000 = 1234567890

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
        number=1))

# print(recursive_reverse(num_100))
# print(recursive_reverse(num_1000))
# print(recursive_reverse(num_10000))


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
        number=1))

# print(recursive_reverse_mem(num_100))
# print(recursive_reverse_mem(num_1000))
# print(recursive_reverse_mem(num_10000))

'''
Мемоизация в данном случае не нужна, во-первых рекурсивные функции в маленьким числом вызовов (до 13 раз),
во-вторых вычисляет и записывает кэш в свой словарь (хеш-таблицу) и ускорит быстродействие функции только
если число на входе в функцию будет состоять из максимально много повторяющихся цифр, но опять же 13 цифр
это слишком мало, для ощутимого прироста. С мемоизацией кажется, что быстрее так, как число запусков функции
10000, при первом запуске время на выполнение функции без декоратора уходит меньше (видно из эксперимента ниже),
а 9999 запусков уже все цифры есть в кэше функции и вычисления не происходят, а только берутся значения из кэша.

Не оптимизированная функция recursive_reverse
0.018330600000000002
0.020033200000000008
6.899999999990247e-06 #  numbers = 1
Оптимизированная функция recursive_reverse_mem
0.0014903
0.0014805999999999986
1.6900000000000248e-05  # numbers = 1

>>> 6.899999999990247e-06 < 1.6900000000000248e-05
True
>>> 6.899999999990247e-06 * 10000
0.06899309999990248 # реальное время выполнения 
>>> 1.6900000000000248e-05 * 10000
0.1689831000000025 # реальное время выполнения 
'''
