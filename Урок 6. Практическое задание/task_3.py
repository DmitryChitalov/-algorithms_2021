"""
Задание 3 *.
Сделать профилировку для скриптов с рекурсией и сделать описание,
можно ли так профилировать и есть ли 'подводные камни' в профилировании?
Придумать как это решить!
Есть очень простое решение!
"""
import memory_profiler
from random import randint


def recursive_reverse(number):
    if number == 0:
        return str(number % 10)
    return f'{str(number % 10)}{recursive_reverse(number // 10)}'


@memory_profiler.profile()
def wrap(number):
    recursive_reverse(number)
    return recursive_reverse


num_10000 = randint(100000000, 10000000000000)

wrap(num_10000)

"""
При профилировке рекурсии происходит многократный вызов декоратора-профилировщика,
тк рекурсия вызывает сама себя многократно. ЧТобы избежать этого, можно обернуть профилируемую
функцию и выполнить профилировку обертки над рекурсивной функцией
"""