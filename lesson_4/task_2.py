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

        if args == (-1,):
            cache.clear()
            # print('clear')
            return

        if args in cache:
            # print('yes')
            return cache[args]
        else:
            # print('no')
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
        'recursive_reverse_mem(num_100);recursive_reverse_mem(-1)',
        setup='from __main__ import recursive_reverse_mem, num_100',
        number=10000))
print(
    timeit(
        'recursive_reverse_mem(num_1000);recursive_reverse_mem(-1)',
        setup='from __main__ import recursive_reverse_mem, num_1000',
        number=10000))
print(
    timeit(
        'recursive_reverse_mem(num_10000);recursive_reverse_mem(-1)',
        setup='from __main__ import recursive_reverse_mem, num_10000',
        number=10000))

"""
Если запустить замеры кода, как есть, то получим следующие значения

Не оптимизированная функция recursive_reverse
0.021705186
0.027541867999999997
0.050885807000000005
Оптимизированная функция recursive_reverse_mem
0.0018804389999999976
0.0018227059999999934
0.0019026520000000047

С первого взгляда кажется, что оптимизация удалась, однако нужно учесть, что кэш мемоизации наполняется при первом
проходе из 1000, и остается актуальным для всех последующих проверок - 999 из 1000. Поэтому такие замеры нельзя
считать правильными. Чтобы получить более правдивые результаты нужно очищать кэш каждый раз перед началом нового теста.
В этом случае данные таковы

Не оптимизированная функция recursive_reverse
0.021363436
0.025899967000000003
0.051986520999999994
Оптимизированная функция recursive_reverse_mem
0.038834041999999985
0.04509390199999999
0.08627809000000003

Получается что применение мемоизации вредит алгоритму
"""
