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


for i in range(1, 10001, 1000):
    print(f'Количество вызовов {i}')
    print('Не оптимизированная функция recursive_reverse')
    print(
        timeit(
            "recursive_reverse(num_100)",
            setup='from __main__ import recursive_reverse, num_100',
            number=i))
    print(
        timeit(
            "recursive_reverse(num_1000)",
            setup='from __main__ import recursive_reverse, num_1000',
            number=i))
    print(
        timeit(
            "recursive_reverse(num_10000)",
            setup='from __main__ import recursive_reverse, num_10000',
            number=i))

    print('Оптимизированная функция recursive_reverse_mem')
    print(
        timeit(
            'recursive_reverse_mem(num_100)',
            setup='from __main__ import recursive_reverse_mem, num_100',
            number=i))
    print(
        timeit(
            'recursive_reverse_mem(num_1000)',
            setup='from __main__ import recursive_reverse_mem, num_1000',
            number=i))
    print(
        timeit(
            'recursive_reverse_mem(num_10000)',
            setup='from __main__ import recursive_reverse_mem, num_10000',
            number=i))

"""
Вывод: решение при помощи мемоизации позволяет создать иллюзию более быстрого выполнения, так как по мере роста
number, мы просто осуществляем доступ к кэшу для конкретного числа. Однако при единичном вызове функции для переворота
числа рекурсия с мемоизацией зачастую показывает худшие результаты, так как тратит время для наполнения кэша.
Таким образом, если нам необходимо один раз перевернуть число и получить результат, мемоизация никак не ускорит работу,
но при многократных повторениях  вызова, позволит получить реверс быстрее при помощи кэша, также если у нас уже есть
наполненный кэш предыдущими вызовами, возрастает вероятность, что число уже перевернуто в нём.
"""
