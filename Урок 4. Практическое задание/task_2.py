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

# собственной идеи рекурсивной оптимизации нет
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

# мемоизация здесь не нужна, т.к. она будет сохранять варианты более ранних результатов работы функции
# recursive_reverse_mem в кеш.
# на время выполнения функции recursive_reverse_mem будут влиять мемоизация и значения параметра number, переданное в
# функцию timeit. Чем больше значение number, тем дольше время выполнения. Но, при первом выполнении функции
# recursive_reverse_mem, кеш будет пуст. Поэтому функция отработает полностью, а результат работы будет помещен в кеш.
# При этом в кеш будут помещены данные о числах, из которых состоят разряды исходного числа
# (т.е., например, 0: '', 7: '7', 76: '67', и т.д., пока в итоге не получим реверс исходного числа).
# При последующих вызовах функции recursive_reverse_mem, функция отрабатывать уже не будет, т.к. требуемый результат ее
# работы уже содержится в кеше (хотим развернуть то же самое число)=> будет сразу возвращено требуемое значение, без
# вызова функции recursive_reverse_mem.
# Отсюда и выходит, что результаты работы функции recursive_reverse_mem намного быстрее, чем функции recursive_reverse
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