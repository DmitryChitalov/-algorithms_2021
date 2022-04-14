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

# Мемоизация на приведенном примере действительно показывает время выполнения быстрее.
# первоначальные результаты:

# Не оптимизированная функция recursive_reverse
# 0.0341973
# 0.04163829999999999
# 0.06701570000000001
# Оптимизированная функция recursive_reverse_mem
# 0.0024643000000000026
# 0.002379299999999973
# 0.002543099999999992

# Это связано с тем, чтов случае с мемоизацией, когда функция вызыывается многократно с одним и тем же аргументом,
# данные о предыдущих результатах быстро извлекаются из кэша.

# Однако, если вызывать функцию, вызывая разные аргументы, результат совсем другой:

from timeit import timeit
from random import randint


def recursive_reverse(number):
    if number == 0:
        return ''
    return f'{str(number % 10)}{recursive_reverse(number // 10)}'


print('Не оптимизированная функция recursive_reverse')
print(
    timeit(
        "recursive_reverse(randint(10000, 1000000))",
        setup='from __main__ import recursive_reverse, randint',
        number=10000))
print(
    timeit(
        "recursive_reverse(randint(1000000, 10000000))",
        setup='from __main__ import recursive_reverse, randint',
        number=10000))
print(
    timeit(
        "recursive_reverse(randint(100000000, 10000000000000))",
        setup='from __main__ import recursive_reverse, randint',
        number=10000))


def memoize(f):
    cache = {}
    def decorate(*args):
        # print(len(cache))
        if args in cache:
            return cache[args]
        else:
            cache[args] = f(*args)
            return cache[args]

    return decorate


@memoize
def recursive_reverse_mem(number, show_size=False):
    if number == 0:
        return ''
    return f'{str(number % 10)}{recursive_reverse_mem(number // 10)}'


print('Оптимизированная функция recursive_reverse_mem')
print(
    timeit(
        'recursive_reverse_mem(randint(10000, 1000000))',
        setup='from __main__ import recursive_reverse_mem, randint',
        number=10000))
print(
    timeit(
        'recursive_reverse_mem(randint(1000000, 10000000))',
        setup='from __main__ import recursive_reverse_mem, randint',
        number=100000))
print(
    timeit(
        'recursive_reverse_mem(randint(100000000, 10000000000000))',
        setup='from __main__ import recursive_reverse_mem, randint',
        number=10000))

# В данном случае результаты:

# Не оптимизированная функция recursive_reverse
# 0.055697300000000005
# 0.05764910000000001
# 0.098964
# Оптимизированная функция recursive_reverse_mem
# 0.05669030000000003
# 0.5931246000000001
# 0.1622345999999999

# Теперь мемоизация порой и замедляет работу. Это связано с тем, что функция редко будет вызываться с одними и теми же
# аргументами, и больше времени уйдет на запись в кэш и поиск в кэше, потому что чаще мы там не найдем то, что ищем.

# Однако, если увеличить количество вызова функции, например до десяти миллионов, то число вызовов функции с теми же
# аргументами возрастет и мы получим преимущество по времени выполнения:

print(
    timeit(
        "recursive_reverse(randint(1000000, 10000000))",
        setup='from __main__ import recursive_reverse, randint',
        number=10_000_000))

print(
    timeit(
        'recursive_reverse_mem(randint(1000000, 10000000))',
        setup='from __main__ import recursive_reverse_mem, randint',
        number=10_000_000))

# результат 54.5475029 без мемоизации и 38.04105860000001 с мемоизацией

# Иными словами если число вызвов сопоставимо с размерами аргумента функции, то конкретно для данной функции
# использовать мемоизацию смысл есть. Если же мы планируем вызывать функцию в рамках одного модуля малое количество раз,
# в мемоизации смысла нет для данной функции.
