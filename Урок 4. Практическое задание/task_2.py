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
        return ""
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


def recursive_reverse_slice(number):
    if number == 0:
        return ""
    res = str(number)[::-1]
    return res


print('Оптимизированная функция recursive_reverse_slice')
print(
    timeit(
        'recursive_reverse_slice(num_100)',
        setup='from __main__ import recursive_reverse_slice, num_100',
        number=10000))
print(
    timeit(
        'recursive_reverse_slice(num_1000)',
        setup='from __main__ import recursive_reverse_slice, num_1000',
        number=10000))
print(
    timeit(
        'recursive_reverse_slice(num_10000)',
        setup='from __main__ import recursive_reverse_slice, num_10000',
        number=10000))

'''
Первая фукнция recursive_reverse реализована неправильно - добавляет 0 в конце.
Мемоизация наиболее эффективна при больших количествах дублей, например чтобы не проводить
сложные математические операций, а один раз записать их в кэш и к ним обращаться.
Мемоизация в данном решении не нужна ввиду малого количества дублей, т.е обращений в кеш мало,
идет только запись в кэш.
Оптимизировал решение через срезы строк. Такое решение во много раз эффективней рекурсии, что и подтвердили замеры.  
'''
