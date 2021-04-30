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


def call_reverse_func(num_len):
    if num_len == 100:
        num = randint(10000, 1000000)
        # print(f'num_100 {num}')
        recursive_reverse(num)

    elif num_len == 1000:
        num = randint(1000000, 10000000)
        # print(f'num_1000 {num}')
        recursive_reverse(num)

    elif num_len == 10000:
        num = randint(100000000, 10000000000000)
        # print(f'num_10000 {num}')
        recursive_reverse(num)

# num_100 = randint(10000, 1000000)
# num_1000 = randint(1000000, 10000000)
# num_10000 = randint(100000000, 10000000000000)

print('Не оптимизированная функция recursive_reverse')
num_len = 100
print(
    timeit(
        'call_reverse_func(num_len)',
        setup='from __main__ import call_reverse_func, num_len',
        number=10000))

num_len = 1000
print(
    timeit(
        'call_reverse_func(num_len)',
        setup='from __main__ import call_reverse_func, num_len',
        number=10000))

num_len = 10000
print(
    timeit(
        'call_reverse_func(num_len)',
        setup='from __main__ import call_reverse_func, num_len',
        number=10000))


def memoize(f):
    cache = {}

    def decorate(*args):

        if args in cache:
            # print(f'Found value in cache: {cache}')
            return cache[args]
        else:
            cache[args] = f(*args)
            #print(cache)
            return cache[args]
    return decorate


@memoize
def recursive_reverse_mem(number):
    if number == 0:
        return ''
    return f'{str(number % 10)}{recursive_reverse_mem(number // 10)}'


def call_reverse_func_mem(num_len):
    if num_len == 100:
        num = randint(10000, 1000000)
        # print(f'num_100 {num}')
        recursive_reverse_mem(num)

    elif num_len == 1000:
        num = randint(1000000, 10000000)
        # print(f'num_1000 {num}')
        recursive_reverse_mem(num)

    elif num_len == 10000:
        num = randint(100000000, 10000000000000)
        # print(f'num_10000 {num}')
        recursive_reverse_mem(num)


num_len = 100
print('Оптимизированная функция recursive_reverse_mem')
print(
    timeit(
        'call_reverse_func_mem(num_len)',
        setup='from __main__ import call_reverse_func_mem, num_len',
        number=10000))

num_len = 1000
print(
    timeit(
        'call_reverse_func_mem(num_len)',
        setup='from __main__ import call_reverse_func_mem, num_len',
        number=10000))

num_len = 10000
print(
    timeit(
        'call_reverse_func_mem(num_len)',
        setup='from __main__ import call_reverse_func_mem, num_len',
        number=10000))

# Что-то мне подсказывает, что в исходном коде не оптимизированный и мемоизированный алгоритмы
# вызываются 10000 раз для одного и того же числа. Кэшировать одно и то же число
# в случае мемоизированного алгоритма смысла нет. Если бы при каждой итерации передаваемое
# в функцию число было разным, замеры скорости выполнения были бы другими

# Внес изменения в код: теперь в каждый вызов функции реверса передается разное число.
# Результаты замеров следующие:

# Не оптимизированная функция recursive_reverse
# 0.064840629
# 0.039523932
# 0.06580236499999997
# Оптимизированная функция recursive_reverse_mem
# 0.034466883000000004
# 0.047352597999999996
# 0.11996126199999996

# Отсюда следующее предположение:
# для "длинного" диапазона случайных чисел (randint(100000000, 10000000000000))
# кэширование смысла не имеет, так как на 10000 итераций очень низкая вероятность
# нахождения в кэше уже сохраненного ранее значения (даже с учетом следующего ниже
# вывода)

# И еще предположение: так как в кэш сохраняются числа на каждом этапе реверса исходного числа,
# например, вот такой фрагмент кэша:
# (24,): '42', (242,): '242', (2427,): '7242', (24270,): '07242', (242701,): '107242',
# то (хоть мы этого еще не проходили, но...) велика вероятность утечки памяти

# И еще обнаружил: в кэш сохраняется пара ключ - значение. В нашем случае сохраняется только прямая
# последовательность, реверсивная - нет. Если randint сгенерит число, реверсивное сохраненному ранее,
# то поиск в кэше ничего не вернет
