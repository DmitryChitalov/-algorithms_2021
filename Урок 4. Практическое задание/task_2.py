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


# num_100 = randint(10000, 1000000)
# num_1000 = randint(1000000, 10000000)
# num_10000 = randint(100000000, 10000000000000)
#
# print('Не оптимизированная функция recursive_reverse')
# print(
#     timeit(
#         "recursive_reverse(num_100)",
#         setup='from __main__ import recursive_reverse, num_100',
#         number=10000))
# print(
#     timeit(
#         "recursive_reverse(num_1000)",
#         setup='from __main__ import recursive_reverse, num_1000',
#         number=10000))
# print(
#     timeit(
#         "recursive_reverse(num_10000)",
#         setup='from __main__ import recursive_reverse, num_10000',
#         number=10000))


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


# print('Оптимизированная функция recursive_reverse_mem')
# print(
#     timeit(
#         'recursive_reverse_mem(num_100)',
#         setup='from __main__ import recursive_reverse_mem, num_100',
#         number=10000))
# print(
#     timeit(
#         'recursive_reverse_mem(num_1000)',
#         setup='from __main__ import recursive_reverse_mem, num_1000',
#         number=10000))
# print(
#     timeit(
#         'recursive_reverse_mem(num_10000)',
#         setup='from __main__ import recursive_reverse_mem, num_10000',
#         number=10000))


def slice_1(number):
    """ Как вариант вместо реверса можно сделать 'обратный срез'
    в целом по замерам есть прирост производительности этит методом"""
    return str(number)[::-1]


if __name__ == '__main__':
    # num_100 = randint(10000, 1000000)
    # num_1000 = randint(1000000, 10000000)
    num_10000 = randint(100000000, 10000000000000)

    for execut in [1, 2, 100, 1000, 10000]:
        print(f'************* Количество выполнений {execut} ************')
        print(f'1) Не оптимизированная функция '
              f'{timeit("recursive_reverse(num_10000)", number=execut, globals=globals())}')
        print(f'2) Оптимизированная функция___ '
              f'{timeit("recursive_reverse_mem(num_10000)", number=execut, globals=globals())}')
        print(f'3) СРЕЗ_______________________ '
              f'{timeit("slice_1(num_10000)", number=execut, globals=globals())}')

"""
Очевидно что мемоизация в данном случае не нужна, если этот код буден запущен одни раз. Мемоизация - это кеширование 
для дальнейшего ускорения и на это уходит время, так что по началу с ней будет работать медленно, а на большом кол-ве
использования, конечно будет выгодно.
"""