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
Декоратор использовать не стоит, так как разница в цифрах объясняется аргуметом number в функции timeit.
Timeit запускает функцию 10000 раз с одним и тем же аргументом и уже после первой итерации в кэше хранится ответ.
Благодаря мемоизации после второй и последующие запуски сразу возвращают ответ и не используют рекурсию.

Не стоит использовать, так как он добавляет лишние вычисления и использует дополнительную память.

"""

def built_in_reverse(number):
    number = str(number)
    return number[::-1]


print('Еще одна функция разворота числа')
print(
    timeit(
        'built_in_reverse(num_100)',
        setup='from __main__ import built_in_reverse, num_100',
        number=10000))
print(
    timeit(
        'built_in_reverse(num_1000)',
        setup='from __main__ import built_in_reverse, num_1000',
        number=10000))
print(
    timeit(
        'built_in_reverse(num_10000)',
        setup='from __main__ import built_in_reverse, num_10000',
        number=10000))

"""
написал функцию built_in_reverse
Данное решение намного быстрее рекурсивной функции без мемоизации, так как использует только встроенные функции.

0.0062046000000000046
0.006843600000000005
0.007740799999999992

"""