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


def reverse_slice(number):
    return str(number)[::-1]


print('Функция со срезом reverse_slice')
print(
    timeit(
        'reverse_slice(num_100)',
        setup='from __main__ import reverse_slice, num_100',
        number=10000))
print(
    timeit(
        'reverse_slice(num_1000)',
        setup='from __main__ import reverse_slice, num_1000',
        number=10000))
print(
    timeit(
        'reverse_slice(num_10000)',
        setup='from __main__ import reverse_slice, num_10000',
        number=10000))
print('Вывод:  Была теория, что функция с использованием среза будет "переворачивать" число быстрее, поэтому \n'
      'мемоизация окажется бесполезной, НО это не так!!! Более того ')


@memoize
def optimized_reverse_slice(number):
    return str(number)[::-1]


print('Попробуем такой вариант: ')
print('Оптимизированная функция со срезом optimized_reverse_slice')
print(
    timeit(
        'optimized_reverse_slice(num_100)',
        setup='from __main__ import optimized_reverse_slice, num_100',
        number=10000))
print(
    timeit(
        'optimized_reverse_slice(num_1000)',
        setup='from __main__ import optimized_reverse_slice, num_1000',
        number=10000))
print(
    timeit(
        'optimized_reverse_slice(num_10000)',
        setup='from __main__ import optimized_reverse_slice, num_10000',
        number=10000))
print('Если к функции со срезом применить мемоизацию, то она покажет более высокие результаты, чем функция со срезом \n'
      'БЕЗ мемоизации, поэтому считаю мемоизацию уместной, потому что она сильно сокращает время выполнения функции')
