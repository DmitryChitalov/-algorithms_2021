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

"""
Мемоизация здесь не нужна и даже немного вредна.
Кэш полезен когда нужно возращать значение функции от одних и тех же входных данных.
В данной задаче входные данные всегда разные и из кэша брать нечего.
Результат же обосновывается тем, что кэш заполняется при первом запуске функции в ходе замера веремени, а остальные
результаты возвращаются из кэша.

Результат для количетсва запусков теста = 10000:
Не оптимизированная функция recursive_reverse
0.081918212
0.05645599599999998
0.09853735599999999
Оптимизированная функция recursive_reverse_mem
0.0038617679999999877
0.0040062390000000225
0.004270724999999975


Результат для количетсва запусков теста = 1:
Не оптимизированная функция recursive_reverse
2.083299999999788e-05
1.5850999999997284e-05
2.4908000000004038e-05
Оптимизированная функция recursive_reverse_mem
2.5362000000000995e-05
2.4002999999994667e-05
4.030700000000331e-05
"""
