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


"""
При запуске видно, что оптимизированная функция отрабатывает больше чем в 10 раз быстрее.
Однако, если подумать, меморизация для реверса не нужна, ведь для каждого значения функция вызовется только один раз.
Возникает гипотеза, что подвох в том как выполняются замеры. Выводим логи для 10 вызовов и видим, что функция timeit 
выполняет полный замер только для первого вызова в пачке, а для последующих значения берет из уже сохраненного кэша.
Поэтому суммарное время измерений меньше.
Но данное измерение никакой полезной информации о реальном быстродействии функции не несет.
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
            print('return_from_cache', args)
            return cache[args]
        else:
            print('add_to_cache', args)
            cache[args] = f(*args)
            print('addED_to_cache', args)
            return cache[args]
    return decorate


@memoize
def recursive_reverse_mem(number):
    print('run', number)
    if number == 0:
        return ''
    return f'{str(number % 10)}{recursive_reverse_mem(number // 10)}'


print('Оптимизированная функция recursive_reverse_mem')
print(
    timeit(
        stmt=
'''
recursive_reverse_mem(num_100) 
print("END")
''',
        setup='from __main__ import recursive_reverse_mem, num_100, memoize',
        number=10))



'''
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
'''
