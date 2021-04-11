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


def reverse(number):
    return str(number)[::-1]


print('Не оптимизированная функция recursive_reverse_mem при запуске 1 раз num_10000')
print(
    timeit(
        "recursive_reverse(num_10000)",
        setup='from __main__ import recursive_reverse, num_10000',
        number=1))

print('Оптимизированная функция recursive_reverse_mem при запуске 1 раз num_10000')
print(
    timeit(
        'recursive_reverse_mem(num_10000)',
        setup='from __main__ import recursive_reverse_mem, num_10000',
        number=1))

print('Не рекурсивная функция при запуске 1 раз num_10000')
print(
    timeit(
        'reverse(num_10000)',
        setup='from __main__ import reverse, num_10000',
        number=1))

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

print('Не рекурсивная функция')
print(
    timeit(
        'reverse(num_100)',
        setup='from __main__ import reverse, num_100',
        number=10000))
print(
    timeit(
        'reverse(num_1000)',
        setup='from __main__ import reverse, num_1000',
        number=10000))
print(
    timeit(
        'reverse(num_10000)',
        setup='from __main__ import reverse, num_10000',
        number=10000))

# Не оптимизированная функция recursive_reverse_mem при запуске 1 раз num_10000
# 2.1300000000001873e-05
# Оптимизированная функция recursive_reverse_mem при запуске 1 раз num_10000
# 2.6800000000000435e-05
# при однакратнм запуске функций мемоизация recursive_reverse не ускоряет выполнение, наоборот затрачивется
# больше времни на сохранение разультатов работы функции. При многократном вызове время работы с мемоизацией
# значительно уменьшается. Вряд ли понадобится выполнять эту функцию многократно на одних и тех же данных так
# что в данном случае мемоизация не нужна.
# Не рекурсивная функция при запуске 1 раз num_10000
# 4.099999999999937e-06
# без рекурсии или рекурсии с мемоизацией время работы еще меньше
