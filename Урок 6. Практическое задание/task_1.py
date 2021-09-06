"""
Задание 1.

Выполните профилирование памяти в скриптах.
Проанализируйте результат и определите программы с
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
from random import randrange
from timeit import default_timer
from timeit import timeit
import memory_profiler


def func(n_val):
    if n_val < 2:
        return n_val
    return func(n_val - 1) + func(n_val - 2)


@profile
def func_wrapper(func, n):
    return func(n)


n = 8

func_wrapper(func, n)

print(timeit("func(n)", globals=globals()))     # 15.765922000000002

"""
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    40     19.3 MiB     19.3 MiB           1   @profile
    41                                         def func_wrapper(func, n):
    42     19.3 MiB      0.0 MiB           1       return func(n)
"""


def memorize(func):
    def wrapper(n_val, memory={}):
        res = memory.get(n_val)
        if res is None:
            res = func(n_val)
            memory[n_val] = res
        return res
    return wrapper


@memorize
@profile
def func(n_val):
    if n_val < 2:
        return n_val
    return func(n_val - 1) + func(n_val - 2)


n = 8

print(timeit("func(n)", globals=globals()))     # 0.6833441

"""
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    64     19.3 MiB     19.3 MiB           9   @memorize
    65                                         @profile
    66                                         def func(n_val):
    67     19.3 MiB      0.0 MiB           9       if n_val < 2:
    68     19.3 MiB      0.0 MiB           2           return n_val
    69     19.3 MiB      0.0 MiB           7       return func(n_val - 1) + func(n_val - 2)


Одинаковое количство памяти занимает, только благодаря мемоизации - скорость выше.
"""

print(100 * '=')

@profile
def func_1(lst_arg):
    origin_lst = [item * 2 for item in lst_arg]
    new_lst = origin_lst
    del origin_lst
    return new_lst


lst_to_test_2 = list(range(10000))
func_1(lst_to_test_2)


"""
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    35     30.9 MiB     30.9 MiB           1   @profile
    36                                         def func_1(lst_arg):
    37     31.4 MiB      0.5 MiB       10003       origin_lst = [item * 2 for item in lst_arg]
    38     31.4 MiB      0.0 MiB           1       new_lst = origin_lst
    39     31.4 MiB      0.0 MiB           1       del origin_lst
    40     31.4 MiB      0.0 MiB           1       return new_lst
"""


@profile
def func_2(lst_arg):
    origin_lst = [item * 2 for item in lst_arg]
    new_lst = origin_lst
    del origin_lst
    del new_lst
    new_lst = []
    return new_lst


func_2(lst_to_test_2)

"""
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    58     31.4 MiB     31.4 MiB           1   @profile
    59                                         def func_2(lst_arg):
    60     31.4 MiB      0.0 MiB       10003       origin_lst = [item * 2 for item in lst_arg]
    61     31.4 MiB      0.0 MiB           1       new_lst = origin_lst
    62     31.4 MiB      0.0 MiB           1       del origin_lst
    63     31.4 MiB      0.0 MiB           1       del new_lst
    64     31.4 MiB      0.0 MiB           1       new_lst = []
    65     31.4 MiB      0.0 MiB           1       return new_lst
"""
"""
На последних замерах видим, что при удалении ссылок в func_2() - освобождается память.
"""


def decor(func):
    def wrapper(*args, **kwargs):
        m1 = memory_profiler.memory_usage()
        start_time = default_timer()
        result = func(*args)
        m2 = memory_profiler.memory_usage()
        mem_usage = m2[0] - m1[0]
        run_time = default_timer() - start_time
        return result, mem_usage, run_time
    return wrapper


@decor
def check_1(test_lst):
    new_lst_1 = [elem for elem in test_lst if test_lst.count(elem) == 1]
    return new_lst_1


@decor
def check_2(test_lst):
    new_lst = [elem for num, elem in enumerate(test_lst) if elem not in test_lst[num + 1:]
                and elem not in test_lst[:num]]
    return new_lst


@decor
def check_3(test_lst):
    for num, elem in enumerate(test_lst):
        if elem not in test_lst[num + 1:] and elem not in test_lst[:num]:
            yield elem


if __name__ == '__main__':

    origin_lst = [randrange(1, 9999, 2) for i in range(10000)]

    res_1, mem_diff, runtime = check_1(origin_lst)
    print(f"Выполнение заняло {mem_diff} Mib и {runtime} сек")   # 0.01171875 Mib и 2.2553982 сек

    res_2, mem_diff, runtime = check_2(origin_lst)
    print(f"Выполнение заняло {mem_diff} Mib и {runtime} сек")   # 0.42578125 Mib и 1.3373634 сек

    my_generator, mem_diff, runtime = check_3(origin_lst)
    print(f"Выполнение заняло {mem_diff} Mib и {runtime} сек")   # 0.0 Mib и 0.11295399999999933 сек