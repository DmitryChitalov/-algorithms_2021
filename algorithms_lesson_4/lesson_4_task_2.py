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

'''
ОТВЕТ: В данном алгоритме мемоизация ничего не дает, т.к. здесь не производится повторных вычислений. 
Пример: число 123. 1-й шаг: '3' + f(12); 
                   2-й шаг: '2' + f(1); 
                   3-й шаг: '1' + f(0) - базовый случай 
Т.о., в рамках одного запуска функции в кэш все время будут попадать уникальные значения, поэтому
брать из кэша будет нечего. Если запускать функцию несколько раз, тогда ускорение возможно. 
Цифры показывают эффект от мемоизации, т.к. кэш заполняет декоратор, который пропускает функцию через себя еще до того, 
как она будет вызвана. '''
