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

"""
Memoization is not needed in this solution - there are few repetitions and calls to the cache; in fact,
only writes to the cache are performed.
Memoization is effective when executing a function instance with a large number of repetitions.
Memoization had a positive impact on measurements. they ran for the samevalues num_100, num_1000 and num_10000, 
then in fact we simply retrieved values from the dictionary by key.

Мемоизация в данном решении не нужна - повторов и обращений в кэш мало.Фактически идет только запись в кэш.
Мемоизация эффективна при выполнении экземпляра функции с большим количествам повторений.
Мемоизация повлияла положительно на замеры. они выполнялись для одного и того же 
значения num_100, num_1000 и num_10000, то по сути мы просто извлекали из словаря значения по ключу.
"""
"""
Не оптимизированная функция recursive_reverse
0.020440799999999995
0.022920800000000005
0.04161140000000001
----------------------------------------------------------------------------------------------------
Оптимизированная функция recursive_reverse_mem
0.0014510000000000078
0.0014514000000000193
0.0016419999999999768
from timeit import timeit
from random import randint
"""


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
