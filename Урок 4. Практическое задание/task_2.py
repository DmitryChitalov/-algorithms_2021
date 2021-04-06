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
big_num = 12345678911234567

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
        'recursive_reverse_mem(big_num)',
        setup='from __main__ import recursive_reverse_mem, big_num',
        number=10000))

##########################################################################
'''
Мемоизация оптимизирует рекурсивный алгоритм
за счёт исключения повторяющихся пересчётов.
Время выполнения рекурсии с кешированием данных
на порядок меньше времени выполнения обычной рекурсии
что демонстрируют замеры

Не оптимизированная функция recursive_reverse
0.0696501
0.050409499999999996
0.08882949999999998

Оптимизированная функция recursive_reverse_mem
0.002963500000000008
0.0033017000000000185
0.004825499999999983
'''
##########################################################################
def cicle_reverse(num):
    ''' 
        Переворот числа в цикле работает быстрее рекурсии 
        т.к. не требует настройки параметров и работы со стеком при каждой итерации
        и медленнее мемоизированной рекурсии т.к при кешировании
        сокращается объем расчетов
    '''
    reverse_num = 0
    while num > 0:        
        reverse_num = reverse_num * 10 + num % 10
        num = num//10
    return f"num revers to -> {reverse_num}"

def string_reverse(num):
    '''
    Переворот через преобразование к строке
    работает быстрее рекурсии и медленнее мемоизированной рекурсии
    '''
    reverse_num = int(str(num)[::-1])
    return f"{num} revers to -> {reverse_num}"
############################################################################

print('Реверс в цикле cicle_reverse')
print(
    timeit(
        'cicle_reverse(num_100)',
        setup='from __main__ import cicle_reverse, num_100',
        number=10000))
print(
    timeit(
        'cicle_reverse(num_1000)',
        setup='from __main__ import cicle_reverse, num_1000',
        number=10000))
print(
    timeit(
        'cicle_reverse(big_num)',
        setup='from __main__ import cicle_reverse, big_num',
        number=10000))

#################################################################

print('Реверс через строку string_reverse(num)')
print(
    timeit(
        'string_reverse(num_100)',
        setup='from __main__ import string_reverse, num_100',
        number=10000))
print(
    timeit(
        'string_reverse(num_1000)',
        setup='from __main__ import string_reverse, num_1000',
        number=10000))
print(
    timeit(
        'string_reverse(big_num)',
        setup='from __main__ import string_reverse, big_num',
        number=10000))

print(cicle_reverse(34567))
