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
from cProfile import run
from random import randint
from timeit import timeit


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
        number=6))
print(
    timeit(
        "recursive_reverse(num_1000)",
        setup='from __main__ import recursive_reverse, num_1000',
        number=6))
print(
    timeit(
        "recursive_reverse(num_10000)",
        setup='from __main__ import recursive_reverse, num_10000',
        number=6))


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
        number=6))
print(
    timeit(
        'recursive_reverse_mem(num_1000)',
        setup='from __main__ import recursive_reverse_mem, num_1000',
        number=6))
print(
    timeit(
        'recursive_reverse_mem(num_10000)',
        setup='from __main__ import recursive_reverse_mem, num_10000',
        number=6))

# def opt():
#     recursive_reverse_mem(num_100)
#     recursive_reverse_mem(num_1000)
#     recursive_reverse_mem(num_10000)
# run('opt()')


# def non_opt():
#     recursive_reverse(num_100)
#     recursive_reverse(num_1000)
#     recursive_reverse(num_10000)
# run('non_opt()')
'''
Шаг 1. Отключил декоратор (# @memoize), скорость выполнения функции стала как у
неоптимизированной.
Шаг 2. Замеры с помощью cProfile говорят о том, что слабых мест ни там, ни там
нет. При этом, при вызове оптимизированной функции происходит функции вызоваются
60 раз (плюс вызов декоратора).
Шаг 3. При замерах timeit с 1 млн операций показывает, что оптимизированная 
функция выполняется на порядок быстрее, при этом все 3 ее вызова с разными числами
выполняются за одинаковое время.
Не оптимизированная функция recursive_reverse
1.7104624
1.8072273
3.1301482000000003
Оптимизированная функция recursive_reverse_mem
0.13454799999999967
0.13021890000000003
0.13872700000000027
Шаг 4. При замерах timeit с 1 операцией показывает, что в оптимизированной 
функции вызов num_100 и num_1000 выполняется медленне, чем в неоптимизированной.
Получается, что при вызове функции 1 раз, мемоизатор только усложняет функцию, 
что сказывается на скорости. 
Шаг 5. При увеличении numbers в timeit оптимизированная функция выполняется гораздо 
быстрее неоптимизированной. Вероятно, что при 2-м и последующих вызовах исользуется кеш
от предыдущих вызовов, что положительно влияет на скорость. 
'''
