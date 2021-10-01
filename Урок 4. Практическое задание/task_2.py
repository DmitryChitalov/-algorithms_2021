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
В среднем функция recursive_reverse выполняется за следующее время:
0.0152 для 1 числа.
0.0179 для 2 числа.
0.0306 для 3 числа.
Оптимизированная функция recursive_reverse_mem выполняется в среднем за:
0.0013 для 1 числа.
0.0012 для 2 числа.
0.0013 для 3 числа.
Декоратор оптимизированной функции создает словарь по виду:
(для числа 1234) : {(0,): '', (1,): '1', (12,): '21', (123,): '321', (1234,): '4321'}
То есть для каждого прохода функции запоминает, какому виду строки будет соотноситься число.
Именно в данном случае, когда функции подается заранее сгенерированное и зафиксированное число, появляется польза в 
скорости вывполнения этой функции. 
Не оптимизированная функция 10 000 рассчитывает рекурсию для одного и того же числа, потому что нигде не сохраняет
промежуточный результат.
Оптимизированная функция рассчитывает промежуточные значения через рекурсию в первый раз, а для последующих вызовов 
подставляет значение из словаря.
ВЫВОД: Конкретно в данной функции, для одного вызова уникального числа, мемоизация бесполезна. Применение мемоизации
имеет смысл только при многократном повторном вызове этой функции. В замерах можно заметить, насколько вторая функция
с мемоизацией исполняется быстрее первой функции, без мемоизации. 
"""
