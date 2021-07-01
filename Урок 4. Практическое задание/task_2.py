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
    ''' Функция разворота числа через рекурсию'''
    if number == 0:
        return str(number % 10)
    return f'{str(number % 10)}{recursive_reverse(number // 10)}'


num_100 = randint(10000, 1000000)
num_1000 = randint(1000000, 10000000)
num_10000 = randint(100000000, 10000000000000)

print(num_100, num_1000, num_10000)

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


def memoize(func):
    '''Функция мемоизации рекурсии'''
    cache = {}

    def decorate(*args):
        if args in cache:
            return cache[args]
        cache[args] = func(*args)
        return cache[args]
    return decorate


@memoize
def recursive_reverse_mem(number):
    '''Функция переворота числа через рекурсию с помощью мемоизации'''
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
Результаты теста
Не оптимизированная функция recursive_reverse
0.0169392
0.0194608
0.035398299999999994
Оптимизированная функция recursive_reverse_mem
0.0013108999999999899
0.001303600000000002
0.001369200000000001
Мемоизация помогла, оптимизированная функция работает очень быстро, за счет того
что у декоратора заполняется кэш при первом вызове (когда число переворачивается полностью)
 рекурсивной функции и во всех остальных вызовах (в timeit-е) уже берется значение из
 сохраненного кэша, так как число всегда одно и то же закидывается в рекурсию, а оно
 уже в перевернутом виде есть в кэше
"""
