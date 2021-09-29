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

from cProfile import run


def recursive_reverse(number):
    if number == 0:
        return ''
    return f'{str(number % 10)}{recursive_reverse(number // 10)}'


num_100 = randint(10000, 1000000)
num_1000 = randint(1000000, 10000000)
num_10000 = randint(100000000, 10000000000000)

print(num_100)
print(num_1000)
print(num_10000)

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


print('=' * 50)
print('=' * 50)
run('recursive_reverse(num_10000)')
print('=' * 50)
run('recursive_reverse_mem(num_10000)')

"""
Мемоизатор точно не нужен, потому что он не сработает, потому что каждый раз передавая в рекурсию функции урезанное 
число, мы никогда не повторяем аргумент, соответственно, непосредственно в алгоритме разворота цифр числа мемоизатор
точно не учавствует. Остаётся вопрос: как при замерах получается время на порядок лучшее, чем без декоратора-мемоизатора
Чтобы это понять, немного вспомним, что такое декоратор. Декоратор - это знаменитый питонячий "синтаксический сахар",
который по сути скрывает одно простое действие: изначальная функция прячется в функцию-обёртку, а имя функции, которое
по-сути является ссылкой на объект, представляющий само тело функции, теперь указывает не на этот объект, а на обёртку.
Таким образом, мы получаем "новую" функцию, которая и вызывается 10 000 раз в timeit, а кэш, который остаётся на верхнем
уровне, при этом сохраняется. Таким образом, из-за декоратора рекурсивная функция больше не вызывается, а просто 
возвращаются 9 999 раз значения из кэша, что можно увидеть, если использовать профилировщик cProfile.

==================================================
==================================================
         17 function calls (4 primitive calls) in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
     14/1    0.000    0.000    0.000    0.000 task_2.py:20(recursive_reverse)       <- ВОТ ЗДЕСЬ РЕКУРСИЯ
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


==================================================
         4 function calls in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 task_2.py:55(decorate)            <- ЗДЕСЬ ВМЕСТО НЕЁ ДЕКОРАТОР (ОБЁРТКА)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects} 
        
=================================================        
Видно, что вызывается именно функция-обёртка, а не рекурсивная функция, при этом кэш остаётся на внешнем по отношению к
обёртке уровне (как, впрочем, и задумывалось).
ВЫВОД: непосредственно алгоритму мемоизатор никак не поможет, но если предполагается использовать функцию подобным 
образом, как при много кратных вызовах в timeit, то мемоизатор, определённо, поможет.        
"""
