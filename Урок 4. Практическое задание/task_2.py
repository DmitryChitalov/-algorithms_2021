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
            print(cache)
            return cache[args]

    return decorate


@memoize
def recursive_reverse_mem(number):
    if number == 0:
        return ''
    return f'{str(number % 10)}{recursive_reverse_mem(number // 10)}'


print('Оптимизированная функция recursive_reverse_mem')
print(print(num_100),
      timeit(
          'recursive_reverse_mem(num_100)',
          setup='from __main__ import recursive_reverse_mem, num_100',
          number=10000))
print(print(num_1000),
      timeit(
          'recursive_reverse_mem(num_1000)',
          setup='from __main__ import recursive_reverse_mem, num_1000',
          number=10000))
print(print(num_10000),
      timeit(
          'recursive_reverse_mem(num_10000)',
          setup='from __main__ import recursive_reverse_mem, num_10000',
          number=10000))

"""Оптимизация не нужна так как она сохраняет не каждый элемент, а результат и это обьясняет скорость работы 
timeit сохраняет результат в первом проходе, а в остальных (9999 повторов) просто печатает ответ сахроненом в словаре.
Еще причина по которой оптимизация не нужна, это то что при каждой вызове новой функции(не предыдущий) словарь 
в мемоизация сбрасыватся сводя на нет все старания прошлого вызыва"""
