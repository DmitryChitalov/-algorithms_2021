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


def my_reverse(number):
    return str(number)[::-1]


print('Оптимизированная функция my_reverse')
print(
    timeit(
        'my_reverse(num_100)',
        setup='from __main__ import my_reverse, num_100',
        number=10000))
print(
    timeit(
        'my_reverse(num_1000)',
        setup='from __main__ import my_reverse, num_1000',
        number=10000))
print(
    timeit(
        'my_reverse(num_10000)',
        setup='from __main__ import my_reverse, num_10000',
        number=10000))

"""
АНАЛИТИКА:
Не оптимизированная функция recursive_reverse
0.048313388000000006
0.041121426000000016
0.075030605                        с увеличением кол-ва цифр, время растет существенно

Оптимизированная функция recursive_reverse_mem
0.0027122559999999962
0.00276812500000001
0.002830800000000022        с увеличением кол-ва цифр время почти не меняется

Оптимизированная функция my_reverse
0.004894270000000006
0.004861649000000023
0.005286014999999977        с увеличением количества цифр, время почти не меняется

мемоизация здесь нужна, т.к. при обратном проходе не нужно повторно вычислять значения функции, которые уже вычислялись
до этого. Эти значения запоминаются в кэше и при повторном вызове функции с уже вызывавшемся аргументом, функция не
вычисляется, а ей присваивается значение из кэша. Кэш в нашем случае это словарь, т.е. хеш таблица, извлечение 
значений из которой происходит по ключу (нет поиска), что является быстрым.

Я предложил свою функцию реверса числа, через срез. 

При профилировке через timeit получил, что самая медленная это рекурсия без мемоизации, 
самая быстрая это рекурсия с мемоизацией,  функция через срез на порядок быстрее рекурсии
без мемоизации,но в два раза медленее рекурсии с мемоизацией. Это происходит, потому что  срез тяжелее O(b-a), 
чем операции %, // O(1). А  количество вызовов этих операций  одного порядка. При рекурсии же, очень много повторных
вызвовов, которые и забирают временной ресурс.  

"""
