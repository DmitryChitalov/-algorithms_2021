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


# Фенкция с использованием итераций
def recursive_reverse_new(number):
    reversed_number = ''
    while number != 0:
        reversed_number = f"{reversed_number}{number % 10}"
        number = number // 10
    return reversed_number


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

print('Не оптимизированная функция recursive_reverse_new')
print(
    timeit(
        "recursive_reverse_new(num_100)",
        setup='from __main__ import recursive_reverse_new, num_100',
        number=10000))
print(
    timeit(
        "recursive_reverse_new(num_1000)",
        setup='from __main__ import recursive_reverse_new, num_1000',
        number=10000))
print(
    timeit(
        "recursive_reverse_new(num_10000)",
        setup='from __main__ import recursive_reverse_new, num_10000',
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


@memoize
def recursive_reverse_new_mem(number):
    reversed_number = ''
    while number != 0:
        reversed_number = f"{reversed_number}{number % 10}"
        number = number // 10
    return reversed_number


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


print('Оптимизированная функция recursive_reverse_mem')
print(
    timeit(
        'recursive_reverse_new_mem(num_100)',
        setup='from __main__ import recursive_reverse_new_mem, num_100',
        number=10000))
print(
    timeit(
        'recursive_reverse_new_mem(num_1000)',
        setup='from __main__ import recursive_reverse_new_mem, num_1000',
        number=10000))
print(
    timeit(
        'recursive_reverse_new_mem(num_10000)',
        setup='from __main__ import recursive_reverse_new_mem, num_10000',
        number=10000))


'''
Для запуска timeit с одним повторением особого смысла в декораторе нет, так как декоратор тратит время на занесение
значений в словарь, что теоретически увеличивает время выполнения. Так как ВСЕ значения при одном посторении заносятся
в словарь и не извлекаются из него то теоретически с декоратором выполнение происходит даже медленнее в таком случае.
Особенно явно это видно при большом значении которе передается в функцию.

В случае если повторений в timeit много, смысл применить декоратор есть, так как при повторении будут выполняться
вызовы функции которые уже были выполнены при первом прогоне. А так как декоратор уже сохранил результаты вызовов при 
первоначальном прогоне, то результаты следующих прогонов уже отражены в словаре и соответственно будут взяты из словаря
и запуска самих функций не произойдет, что соответственно ускорит выполнение.
'''

n = 9182736459182736450
print('---')
t = timeit('recursive_reverse(n)', 'from __main__ import recursive_reverse, n', number=1)
t_mem = timeit('recursive_reverse_mem(n)', 'from __main__ import recursive_reverse_mem, n', number=1)
print(f"Быстрее -- > {'Normal' if t < t_mem else 'Memorize'}")

'''
Реализация фенкции с итерациями работает быстрее чем функция с рекурсией. Оптимизированная функция с итерацией 
работает быстрее оптимизированной функции с рекурсией.
'''



