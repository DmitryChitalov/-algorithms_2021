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
# Эмпирическим путем и долгим обсуждением в группе в телеграме, будучи посаженным несколько раз филейной частью
# в лужу пришел к выводу, вернее был подтащен за уши к выводу, что мемоизация-кэширование тут является просто
# жульничеством обманывающим timeit. Кэш сохраняется и используется на протяжении всех повторов. И фактически
# время почти не изменяется от последующих проверок т.к. все уже в словаре.
# Само по себе кэширование тут не нужно т.к. рекурсия тут с моей точки зрения искуственная т.к. на каждом шаге
# у нас есть конкретный результат - последняя буква, а не ссылка на вычисление предыдущих шагов. Время на вычисление
# которого - константа. Т.е. рекурсия тут используется чтобы исключительно заменить простой цикл. Мемоизация тут,
# как собаке 5-ая нога т.к. вычисление нужно провести один раз.


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
        number=100000))
print(
    timeit(
        "recursive_reverse(num_1000)",
        setup='from __main__ import recursive_reverse, num_1000',
        number=100000))
print(
    timeit(
        "recursive_reverse(num_10000)",
        setup='from __main__ import recursive_reverse, num_10000',
        number=100000))


def memoize(f):
    cache = {}

    def decorate(*args):
        print(cache)
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
        number=100000))
print(
    timeit(
        'recursive_reverse_mem(num_1000)',
        setup='from __main__ import recursive_reverse_mem, num_1000',
        number=100000))
print(
    timeit(
        'recursive_reverse_mem(num_10000)',
        setup='from __main__ import recursive_reverse_mem, num_10000',
        number=100000))
