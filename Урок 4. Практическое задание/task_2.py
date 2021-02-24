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
        return str(number % 10)
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
Ниже приведено решение задачи через цикл. Такж произвел замеры для такого решения:
"""


def cycle(num):
    lst = str(num).split()
    for i in range(len(lst)):
        result = lst.pop()
    return result


print('Функция cycle. Решение через цикл.')
print(
    timeit(
        'cycle(num_100)',
        setup='from __main__ import cycle, num_100',
        number=10000))
print(
    timeit(
        'cycle(num_1000)',
        setup='from __main__ import cycle, num_1000',
        number=10000))
print(
    timeit(
        'cycle(num_10000)',
        setup='from __main__ import cycle, num_10000',
        number=10000))
"""
Вывод:
Мемоизация ускорила выполнение функции, 
т.к в вычисление функции производится многократно для одних и тех же значиени
и фактически вычисления не производились, а соответсвующий результат просто выбирался из кеша.
Решение задачи через цикл также уступило в скорости функции recursive_reverse_mem с мемоизацией.
Но в то же время оказалось быстрее чем решение через рекурсию, без использования кеша.
"""
