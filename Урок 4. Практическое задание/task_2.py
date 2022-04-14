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

##########
# нужна ли здесь мемоизация или нет и почему?!!!
# ответ: мемоизация нужна только в случае частого повторного вызова функции для хранения
# вычисляемых значений в кэше, что будет экономить ресурсы, затрачиваемые на одни и те же вычисления и,
# тем самым, может перекрыть дополнительные затраты на мемоизацию, то есть на выполнение самого
# декоратора.
# Функция timeit() считает время выполнения recursive_reverse_mem() только от ее вызова и не учитывает
# время выполнения функции декоратора. это было интуитивно понятно, и я попыталась посчитать
# это время отдельно либо вместе с основной функцией. Результаты получились все же не подтверждающие мой
# ответ: время получается все же гораздо меньше, чем без декоратора. Очевидно, есть нюанс, который
# я упускаю из вида, думаю, это то, что основная функция рекурсивная и вызывает саму себя,
# а время выполнения декоратора считается только ОДИН раз, то есть общее время в разы занижается.

print()
print('Попытки вывести время на выполнение основной функции и декоратора: ')
print('Отдельно:')
print(
    timeit(
        'memoize(recursive_reverse_mem(num_10000))',
        globals=globals(), number=10000))

print(
    timeit(
        'recursive_reverse_mem(num_10000)',
        globals=globals(), number=10000))

print()
print('Вместе:')
print(
    timeit(
        'memoize(recursive_reverse_mem(num_10000)), recursive_reverse_mem(num_10000)',
        globals=globals(), number=10000))

