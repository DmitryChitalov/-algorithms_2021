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


def reverse(numb):
    if numb == 0:
        return ''
    return f'{str(numb % 10)}{reverse(numb // 10)}'


num_100 = randint(10000, 1000000)
num_1000 = randint(1000000, 10000000)
num_10000 = randint(100000000, 10000000000000)

print('Non-optimized function')
print(
    timeit(
        "reverse(num_100)",
        setup='from __main__ import reverse, num_100',
        number=10000))
print(
    timeit(
        "reverse(num_1000)",
        setup='from __main__ import reverse, num_1000',
        number=10000))
print(
    timeit(
        "reverse(num_10000)",
        setup='from __main__ import reverse, num_10000',
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
def reverse_memo(numb):
    if numb == 0:
        return ''
    return f'{str(numb % 10)}{reverse_memo(numb // 10)}'


print('Optimized function')
print(
    timeit(
        'reverse_memo(num_100)',
        setup='from __main__ import reverse_memo, num_100',
        number=10000))
print(
    timeit(
        'reverse_memo(num_1000)',
        setup='from __main__ import reverse_memo, num_1000',
        number=10000))
print(
    timeit(
        'reverse_memo(num_10000)',
        setup='from __main__ import reverse_memo, num_10000',
        number=10000))