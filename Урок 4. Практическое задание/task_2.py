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
print(f'num_100={num_100}, num_1000={num_1000}, num_10000={num_10000}')

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
            #  print(f'{args} в кэше')
            return cache[args]
        else:
            #  print(f'{args} НЕ в кэше')
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
Не оптимизированная функция recursive_reverse
0.0285385
0.026969899999999998
0.04906929999999998
Оптимизированная функция recursive_reverse_mem
0.0015167999999999848
0.0015267000000000197
0.0016348999999999947

ВЫВОД:
Существенно меньшие цифры для варианта тестирования с использованием техники мемоизации в данном конкретном примере 
не должны вводить в заблуждение. Дело в том, что кэширование промежуточных результатов работы функций сработало для 
повторных замеров, т.к. они уже забирали готовое значение из кэша, вычисленное в рамках первого вызова функции.
Т.е. мы фактически змеряли скорость обращения к кэшу, а не скорость работы самой функции.
Для данной конкретной задачи использование мемоизации не имеет смысла. 
Более эффективным видится ипользование срезов (см. ниже), где мы видим существенный прирост производительности 
по сравнению с вариантом с рекурсией
"""


def builtin_reverse(number):
    return str(number)[::-1]


print('С использованием среза списка ')
print(
    timeit(
        'builtin_reverse(num_100)',
        setup='from __main__ import builtin_reverse, num_100',
        number=10000))
print(
    timeit(
        'builtin_reverse(num_1000)',
        setup='from __main__ import builtin_reverse, num_1000',
        number=10000))
print(
    timeit(
        'builtin_reverse(num_10000)',
        setup='from __main__ import builtin_reverse, num_10000',
        number=10000))
