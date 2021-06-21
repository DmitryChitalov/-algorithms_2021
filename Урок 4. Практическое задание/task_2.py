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
            print('yes')
            return cache[args]

        else:
            cache[args] = f(*args)
            print('no')
            return cache[args]
    return decorate


@memoize
def recursive_reverse_mem(number):
    if number == 0:
        return ''
    return f'{str(number % 10)}{recursive_reverse_mem(number // 10)}'


# print('Оптимизированная функция recursive_reverse_mem')
# print(
#     timeit(
#         'recursive_reverse_mem(num_100)',
#         setup='from __main__ import recursive_reverse_mem, num_100',
#         number=10000))
# print(
#     timeit(
#         'recursive_reverse_mem(num_1000)',
#         setup='from __main__ import recursive_reverse_mem, num_1000',
#         number=10000))
# print(
#     timeit(
#         'recursive_reverse_mem(num_10000)',
#         setup='from __main__ import recursive_reverse_mem, num_10000',
#         number=10000))

"""
Не оптимизированная функция recursive_reverse
0.03707431798102334
0.03688436804804951
0.058582818950526416
Оптимизированная функция recursive_reverse_mem
0.0021946349879726768
0.0028201459790579975
0.0024547390057705343

судя по полученным цифрам, оптимизация действительно помогла на порядок, но есть один вопрос:
а не использует ли 'оптимизированная' функция одни и те же данные в течение всей проверки?
Проверю, сохраняет ли декоратор данные от запуска к запуску.
Для этого добавим print в декоратор и запустим оптимизированную функцию:
"""

print('Оптимизированная функция recursive_reverse_mem')
print(
    timeit(
        'recursive_reverse_mem(num_100)',
        setup='from __main__ import recursive_reverse_mem, num_100',
        number=1000,
            ))
"""
Оптимизированная функция recursive_reverse_mem
no
no
no
no
no
no
no
yes
yes
yes
yes
yes
yes
yes
yes
yes
...
yes
"""

"""
в итоге можно увидеть, что от вызова к вызову функция просто читает уже записанные данные,
которые при очередном запуске константны и не меняются,
следовательно замер времени не показывает реальные показатели.
В целом мемоизация тут не нужна (на вход подается число заданной длины, 
а для оптимизации кода лучше всего просто уйти от рекурсии.
"""
