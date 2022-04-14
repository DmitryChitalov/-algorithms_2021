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
from cProfile import run


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

run('recursive_reverse(num_10000)')
run('recursive_reverse_mem(num_10000)')


'''
Сравним выводы программы и профайлера для num_10000.

То, что выводит исходный код:
Программа:
В первом случае: 0.0418915
Во втором случае: 0.001718299999999992

Вроде бы из выводов видно, что мемоизация помогает, но все не просто так)

Присмотревишсь к количеству вызовов в профайлере, мы можем заметить, что их там во втором случае всего 4, против 17 
(включая 14 рекурсивных) в первом. 
Кроме того, видно, что, если время выполнения части кода без мемоизации существенно растет в зависимости от количества 
символов в числе. Во части же с мемоизацией время выполнения (вывод timeit) меняется не существенно.

В этом все и дело. Декоратор подменяет собою функцию. И на выходе мы имеем время работы декоратора, а не время работы 
декорируемой функции.

Вывод: 
Мемоизация нужна только в случаях, когда значения повторяются часто. Здесь же при развороте 1 числа, она не только 
не полезна, но и вредна, т.к. добавляет лишнее действие (декорирование), а так же путает значения при замере времени.
'''