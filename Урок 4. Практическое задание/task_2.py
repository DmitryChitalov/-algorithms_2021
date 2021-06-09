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
        globals=globals(),
        number=10000))
print(
    timeit(
        "recursive_reverse(num_1000)",
        globals=globals(),
        number=10000))
print(
    timeit(
        "recursive_reverse(num_10000)",
        globals=globals(),
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


print('\nОптимизированная функция recursive_reverse_mem')
print(
    timeit(
        'recursive_reverse_mem(num_100)',
        globals=globals(),
        number=10000))
print(
    timeit(
        'recursive_reverse_mem(num_1000)',
        globals=globals(),
        number=10000))
print(
    timeit(
        'recursive_reverse_mem(num_10000)',
        globals=globals(),
        number=10000))

"""
Результаты замеров (ниже) демонстрируют, что мемоизация позволяет ускорить выполнение функции на порядок за счет 
сохранения значений в кэше.
Вместе с тем, абсолютное время выполнения неоптимизированной функции при 10000 повторов составляет менее 0,1 сек
и в этой ситуации оптимизация не является критичной для общего времени выполнения, если предусматривается однократный
вызов функции. При многократных вызовах использование мемоизации оправдано за счет (данные уже находятся в кэше).

Не оптимизированная функция recursive_reverse
0.03582467
0.04252163599999999
0.082934968

Оптимизированная функция recursive_reverse_mem
0.0027335130000000207
0.0028296560000000137
0.0027750420000000053

"""
