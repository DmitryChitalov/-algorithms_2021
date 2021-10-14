"""
Задание 2.
Приведен код, который формирует из введенного числа
обратное по порядку входящих в него цифр.
Задача решена через рекурсию
Выполнена попытка оптимизировать решение через мемоизацию.
Сделаны замеры обеих реализаций.
Сделайте аналитику, нужна ли здесь мемоизация или нет и почему?!!!
Будьте внимательны, задание хитрое. Не все так просто, как кажется.

Я не заметил пока не проверил, но тут черт пойми что, при выводе
        if args in cache:
            print(f'зачем-то снова спросили {args}')
            return cache[args],

и выглядит это так словно это только больше
нагружает. Дополнение:  в словарь добавляется не просто ключ значения одного числа, а оно добавляется каждый раз,
как падает новый остаток, что занимает больше памяти
{(0,): ''}
{(0,): '', (2,): '2'}
{(0,): '', (2,): '2', (22,): '22'}
{(0,): '', (2,): '2', (22,): '22', (222,): '222'}
{(0,): '', (2,): '2', (22,): '22', (222,): '222', (2220,): '0222'}
{(0,): '', (2,): '2', (22,): '22', (222,): '222', (2220,): '0222', (22201,): '10222'}
{(0,): '', (2,): '2', (22,): '22', (222,): '222', (2220,): '0222', (22201,): '10222', (222017,): '710222'}
Не знаю есть ли тут что-нибудь еще
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
            # print(f'зачем-то снова спросили {args}') ПРОСТО РАСКОМЕНТИРУЙТЕ))))
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

print(
    timeit(
        'recursive_reverse_mem(num_10000)',
        setup='from __main__ import recursive_reverse_mem, num_10000',
        number=10000))