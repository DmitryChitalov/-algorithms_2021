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
Анализ и предложение:
===================================================================================================
Анализ:
Мемоизация здесь не нужна, поскольку функция выполняется один раз и
повторное обращение к аргументам не происходит.
Цифры получаются меньше, потому что при добавлении результата вычисления в кеш
используется словарь (хэш-таблица). Значит выполнение операции происходит
за константное время O(1) - следовательно это существенно снижает стоимость выполнения функции.

Предложение:
В принципе, можно совсем уйти от использования рекурсии в этом случае и
реализовать всё через срез строки. Временные потери в сравнении с мемоизацией будут не существенные,
но серьезно ниже будут в сравнении с не оптимизированной рекурсией.
===================================================================================================

Пример кода предложения:

def slice_reverse(number):
    reverse = str(number)[::-1]
    return reverse

print('Функция разворота числа через срез строки')
print(
    timeit(
        'slice_reverse(num_100)',
        setup='from __main__ import slice_reverse, num_100',
        number=10000))
print(
    timeit(
        'slice_reverse(num_1000)',
        setup='from __main__ import slice_reverse, num_1000',
        number=10000))
print(
    timeit(
        'slice_reverse(num_10000)',
        setup='from __main__ import slice_reverse, num_10000',
        number=10000))
"""

