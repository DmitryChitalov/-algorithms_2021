"""
Задание 1.

Выполните профилирование памяти в скриптах
Проанализировать результат и определить программы с
наиболее эффективным использованием памяти.

Примечание: Для анализа возьмите любые 3-5 ваших РАЗНЫХ скриптов!
(хотя бы 3 разных для получения оценки отл).
На каждый скрипт вы должны сделать как минимум по две реализации.

Можно взять только домашние задания с курса Основ
или с текущего курса Алгоритмов

Результаты профилирования добавьте в виде комментариев к коду.
Обязательно сделайте аналитику (что с памятью в ваших скриптах, в чем ваша оптимизация и т.д.)

ВНИМАНИЕ: ЗАДАНИЯ, В КОТОРЫХ БУДУТ ГОЛЫЕ ЦИФРЫ ЗАМЕРОВ (БЕЗ АНАЛИТИКИ)
БУДУТ ПРИНИМАТЬСЯ С ОЦЕНКОЙ УДОВЛЕТВОРИТЕЛЬНО

Попытайтесь дополнительно свой декоратор используя ф-цию memory_usage из memory_profiler
С одновременным замером времени (timeit.default_timer())!
"""
from memory_profiler import memory_usage, profile
from timeit import default_timer
from recordclass import recordclass
from numpy import array



def decor(func):
    def wrapper(*args, **kwargs):
        start_time = default_timer()
        m1 = memory_usage()
        m2 = memory_usage()
        mem_diff = m2[0] - m1[0]
        time_diff = default_timer() - start_time
        return f' {func.__name__} затронуто памяти {mem_diff} MiB, время выполнения {time_diff} c'
    return wrapper


"""Первый скрипт"""



n = list(range(1000000))

@decor
def f(n):
    new_arr = []
    for i in range(len(n)):
        if n[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


print(f'Итерация {f(n)}')


"""Оптимизация"""


@decor
def f2(n):
    for i in range(len(n)):
        if n[i] % 2 == 0:
            yield i


print(f'Генератор {f2(n)}')


@decor
def f3(n):
    return [i for i in range(len(n)) if n[i] % 2 == 0]


print(f'List compr  {f3(n)}')

"Генератор самый быстрый и памяти не занимает"

print('_' * 100)

length = 100

@profile
def for_in(length_val):
    elem = 1
    amount = 0
    for i in range(length_val):
        amount += elem
        elem = -elem / 2
    return print(f'Сумма последовательности из {length_val} элементов равна {amount}')

for_in(length)

@profile
def recursion(length_val):
    def sum_series_numbers(n, elem=1):
        if n <= 0:
            return 0
        return elem + sum_series_numbers(n - 1, -elem / 2)
    print(
        f'Сумма последовательности из {length_val} элементов равна '
        f'{sum_series_numbers(length)}'
    )

recursion(length)

"""Рекурсия требует больше памяти т. к. при ее вызове хранится стек памяти"""


print('_' * 100)

@profile
def f4(lst, value):
    for i in range(value):
        lst.append(i)


@profile
def f5(dict, value):
    for i in range(value):
        dict[i] = i


"""Оптимизированый вариант"""

@profile
def f6(lst, value):
    lst = array([i for i in range(value)])
    return lst


@profile
def f7(dict, value):
    for i in range(value):
        elements = recordclass("var", ["numb_1", "numb_2"])
        dict[elements.numb_1] = elements.numb_2
    return dict


new_list = []
new_dict = {}

f4(new_list, 100000)

f5(new_dict, 100000)

f6(new_list, 100000)

f7(new_dict, 100000)

