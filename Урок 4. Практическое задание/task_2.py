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


"""
Результат тестов на моём пк:
Не оптимизированная функция recursive_reverse
0.050936096999976144
0.02752111900002774
0.03295965300003445
Оптимизированная функция recursive_reverse_mem
0.0013353159999951458
0.0014254999999820939
0.0014048720000232606

Мы видим что оптимизированная функция работает явно быстрее чем не оптимизированная.
Так что уже по результатам замеров уже был некий смысл её оптимизировать.
Что касается нужности мемоизации с точки зрения выполнения функции, то она нужна
если функция будет вызываться для одного и того же значения многократно. В нашем
случае эта оптимизация бесуловно нужна так как одно и тоже число будет крутится в
функции реверс 10000 потом другое число 10000 раз. Эти 10000 раз будет по кусочку
от числа отрываться и создаваться с помощью этого другое число развёрнутое в обратную
сторону. И будет гораздо быстрее и эффективнее если повторный вызов с одинаковым
значением не будет приводить к рекурсии, а вместо этого будет взято из словаря, который использует
мемоизация. Таким образом рекурсия будет лишь для одной операции реверса числа из 10000, а
у нас таких чисел 6 и они ещё все разной величины. Таким образом рекурсия для каждого
числа выполнится при полной операции реверс по одной такой операции из 10000.
"""
