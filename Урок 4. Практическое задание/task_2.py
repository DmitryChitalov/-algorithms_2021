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


# Добавил функцию для замеров без декоратора
def recursive_reverse_mem_no_decor(number):
    if number == 0:
        return ''
    return f'{str(number % 10)}{recursive_reverse_mem_no_decor(number // 10)}'

print('Функция recursive_reverse_mem без декоратора:')
print(
    timeit(
        'recursive_reverse_mem_no_decor(num_100)',
        setup='from __main__ import recursive_reverse_mem_no_decor, num_100',
        number=10000))
print(
    timeit(
        'recursive_reverse_mem_no_decor(num_1000)',
        setup='from __main__ import recursive_reverse_mem_no_decor, num_1000',
        number=10000))
print(
    timeit(
        'recursive_reverse_mem_no_decor(num_10000)',
        setup='from __main__ import recursive_reverse_mem_no_decor, num_10000',
        number=10000))

''' 
Вывод: 
В данном случае мемоизатор не нужен по причине того, что мы передаем каждый раз урезанное число, которое
уже никогда не повторится в аргументы и храниить это в кэше, а тем более искать каждый элемент при запуске функции,
бессмысленно.  
Если посмотреть внимателнее на представленный декоратор, то видно, что функция прячется в обёртку, а имя функции
теперь указывает на обертку при замерах. Т.е. мы получаем функцию, которая учавствует в замере, но сама рекурсия в
данном случае не вызывается, а возвращает значения из cache[] n-ое количество раз - т.е. будет эллюзия того, 
что все получилось и время работы алгоритма улучшилось.

Данные выводы подтерждаются следующими результатами:

Не оптимизированная функция recursive_reverse
    0.025353100000000003
    0.022826399999999997
    0.05734399999999999
Оптимизированная функция recursive_reverse_mem
    0.001805199999999979
    0.002442799999999995
    0.0016771000000000147
Функция recursive_reverse_mem без декоратора:
    0.02364770000000002
    0.027170100000000003
    0.054009
'''