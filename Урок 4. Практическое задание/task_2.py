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
        number=1))
print(
    timeit(
        "recursive_reverse(num_1000)",
        setup='from __main__ import recursive_reverse, num_1000',
        number=1))
print(
    timeit(
        "recursive_reverse(num_10000)",
        setup='from __main__ import recursive_reverse, num_10000',
        number=1))


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
        number=1))
print(
    timeit(
        'recursive_reverse_mem(num_1000)',
        setup='from __main__ import recursive_reverse_mem, num_1000',
        number=1))
print(
    timeit(
        'recursive_reverse_mem(num_10000)',
        setup='from __main__ import recursive_reverse_mem, num_10000',
        number=1))
"""
замер 1
Не оптимизированная функция recursive_reverse
2.5999999999998247e-05
1.9100000000008e-05
2.4300000000004873e-05
Оптимизированная функция recursive_reverse_mem
2.540000000000875e-05
3.199999999999037e-05
4.4399999999999995e-05
замер 2
Не оптимизированная функция recursive_reverse
2.9299999999982118e-05
1.7200000000022753e-05
2.7199999999977242e-05
Оптимизированная функция recursive_reverse_mem
3.4599999999995745e-05
2.9299999999982118e-05
4.78000000000145e-05
замер 3
Не оптимизированная функция recursive_reverse
3.249999999999087e-05
2.1099999999996122e-05
3.540000000001875e-05
Оптимизированная функция recursive_reverse_mem
3.390000000000337e-05
3.700000000000925e-05
4.7699999999983866e-05

Замеры при числе запусков кода number = 1 (приведены выше) показывают, что смысла в мемоизации нет.
При одном запуске кода вариант с мемоизацией даже проигрывает обычной рекурсии. При большем же повторе 
запусков кода мы видим (number = 1000000), что мемоизация якобы в десятки раз быстрее. Но это быстродействие
мнимое. При обычной рекурсии при каждом запуске кода вычисление значения функции происходит заново. При
мемоизации кэш генерируется всего 1 раз при первом запуске кода. Во все остальные запуски итоговое значение
функции сразу же берется кэша, а не высчитывается заново.

"""