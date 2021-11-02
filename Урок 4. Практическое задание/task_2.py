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

# for debug
print(recursive_reverse(123456789))
print(recursive_reverse_mem(123456789))
print(recursive_reverse(1002009))
print(recursive_reverse_mem(1002009))

# '''
# Как я понял после просмотра вебинара, мемоизация эффективна при одинаковых
# вызовах функции, одинаковый вызов = одинаковый результат.. И если это так,
# то мы подсмотрим и не будем вызываться а сразу дадим результат...
# Тут же вызовы разные, ну то есть входной параметр меняется от вызова к 
# вызову...а зезультат вернет может и такой же, а может и другой.
# В общем какие то базовые принципы нарушены - то есть мемоизация здесь не применяется 
# скорей всего как таковая..
# За счет чего же такой прирост в скорости?..я очень долго дебажил=)), пока не дошло
# что мы результат функции все равно записываем, откуда его быстрей возращаем, а не расчитываем.
# Спорный у меня вывод..мне еще подтянуть нужно это.
# Заключение: тут нет мемоизации, она в этой функции не эффективна..
# '''