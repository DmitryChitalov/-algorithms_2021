"""
Задание 1.

Выполните профилирование памяти в скриптах
Проанализировать результат и определить программы с
наиболее эффективным использованием памяти.

Примечание: Для анализа возьмите любые 3-5 ваших РАЗНЫХ скриптов!
(хотя бы 3 разных для получения оценки отл).
На каждый скрипт вы должны сделать как минимум по две реализации.

Можно взять задачи с курса Основ
или с текущего курса Алгоритмов

Результаты профилирования добавьте в виде комментариев к коду.
Обязательно сделайте аналитику (что с памятью в ваших скриптах, в чем ваша оптимизация и т.д.)

ВНИМАНИЕ: ЗАДАНИЯ, В КОТОРЫХ БУДУТ ГОЛЫЕ ЦИФРЫ ЗАМЕРОВ (БЕЗ АНАЛИТИКИ)
БУДУТ ПРИНИМАТЬСЯ С ОЦЕНКОЙ УДОВЛЕТВОРИТЕЛЬНО

Попытайтесь дополнительно свой декоратор используя ф-цию memory_usage из memory_profiler
С одновременным замером времени (timeit.default_timer())!
"""

# Любимое Решето Эратосфена

from memory_profiler import profile
import memory_profiler
import timeit


def decor(func):
    def wrapper(*args):
        start_time = timeit.default_timer()
        m1 = memory_profiler.memory_usage()
        res1 = func(args[0])
        m2 = memory_profiler.memory_usage()
        end_time = timeit.default_timer()
        return res1, m2[0] - m1[0], end_time - start_time
    return wrapper


@decor
def simple_1(n):
    a = list(range(10000))
    a[1] = 0

    i = 2
    while i < len(a):
        if a[i] != 0:
            j = i + i
            while j < len(a):
                a[j] = 0
                j = j + i
        i += 1

    b = [a[i] for i in a if a[i] != 0]

    if len(b) >= n:
        return b[n-1]
    else:
        return -1


@decor
def simple_3(n):
    # import перенес внутрь функции, так как sqrt вызывается один раз
    from math import sqrt

    lst_len = 10000
    lst = list(range(lst_len))
    lst[1] = 0
    # уменьшил количество итераций до квадратного корня от длины массива
    iter_count = int(sqrt(lst_len)) + 1

    for i in range(2, iter_count):
        if lst[i] !=0:
            for j in range(i + i, lst_len, i):
                if lst[j] != 0:
                    lst[j] = 0

    return [lst[i] for i in lst if lst[i] != 0][n-1]


simple_num = 100

el, mem_diff, exec_time = simple_1(simple_num)
print(f'Простое число с порядковым номером {simple_num} равно {el}')
print(f'simple_1. Использовано {mem_diff} Mib памяти')
print(f'Время выполнения simple_1 = {exec_time}')

el, mem_diff, exec_time = simple_3(simple_num)
print(f'Простое число с порядковым номером {simple_num} равно {el}')
print(f'simple_3. Использовано {mem_diff} Mib памяти')
print(f'Время выполнения simple_3 = {exec_time}')


# В целом: не испытал щенячьего восторга от @profile - Overhead очень продолжительный
# по времени, меня это сбило с толку, потратил слишком много
# времени на выполнение задания

# Здесь протокол работы с использованием profile:

# Line #    Mem usage    Increment  Occurences   Line Contents
# ============================================================
#     43     21.7 MiB     21.7 MiB           1   @decor
#     44                                         @profile
#     45                                         def simple_1(n):
#     46
#     47     22.0 MiB      0.3 MiB           1       a = list(range(10000))
#     48     22.0 MiB      0.0 MiB           1       a[1] = 0
#     49
#     50     22.0 MiB      0.0 MiB           1       i = 2
#     51     22.0 MiB      0.0 MiB        9999       while i < len(a):
#     52     22.0 MiB      0.0 MiB        9998           if a[i] != 0:
#     53     22.0 MiB      0.0 MiB        1229               j = i + i
#     54     22.0 MiB      0.0 MiB       24298               while j < len(a):
#     55     22.0 MiB      0.0 MiB       23069                   a[j] = 0
#     56     22.0 MiB      0.0 MiB       23069                   j = j + i
#     57     22.0 MiB      0.0 MiB        9998           i += 1
#     58
#     59     22.1 MiB      0.0 MiB       10003       b = [a[i] for i in a if a[i] != 0]
#     60
#     61     22.1 MiB      0.0 MiB           1       if len(b) >= n:
#     62     22.1 MiB      0.0 MiB           1           return b[n-1]
#     63                                             else:
#     64                                                 return -1
#
#
# Простое число с порядковым номером 100 равно 541
# simple_1. Использовано 0.48828125 Mib памяти
# Время выполнения simple_1 = 11.9905693
# Filename: C:\OneDrive\Geekbrains\Алгоритмы\-algorithms_2021\Урок 6. Практическое задание\task_1_3.py
#
# Line #    Mem usage    Increment  Occurences   Line Contents
# ============================================================
#     67     22.1 MiB     22.1 MiB           1   @decor
#     68                                         @profile
#     69                                         def simple_3(n):
#     70                                             # import перенес внутрь функции, так как функция вызывается один раз, так будет оптимальнее
#     71     22.1 MiB      0.0 MiB           1       from math import sqrt
#     72
#     73     22.1 MiB      0.0 MiB           1       lst_len = 10000
#     74     22.1 MiB      0.0 MiB           1       lst = list(range(lst_len))
#     75     22.1 MiB      0.0 MiB           1       lst[1] = 0
#     76                                             # уменьшил количество итераций до квадратного корня от длины массива
#     77     22.1 MiB      0.0 MiB           1       iter_count = int(sqrt(lst_len)) + 1
#     78
#     79     22.1 MiB      0.0 MiB         100       for i in range(2, iter_count):
#     80     22.1 MiB      0.0 MiB          99           if lst[i] !=0:
#     81     22.1 MiB      0.0 MiB       18014               for j in range(i + i, lst_len, i):
#     82     22.1 MiB      0.0 MiB       17989                   if lst[j] != 0:
#     83     22.1 MiB      0.0 MiB        8769                       lst[j] = 0
#     84
#     85     22.1 MiB      0.1 MiB       10003       return [lst[i] for i in lst if lst[i] != 0][n-1]
#
#
# Простое число с порядковым номером 100 равно 541
# simple_3. Использовано 0.05078125 Mib памяти
# Время выполнения simple_3 = 9.761282099999999


# Здесь протокол работы без использования profile, разница во времени выполнения почти в 40(!) раз

# Простое число с порядковым номером 100 равно 541
# simple_1. Использовано 0.44921875 Mib памяти
# Время выполнения simple_1 = 0.22996660000000002
# Простое число с порядковым номером 100 равно 541
# simple_3. Использовано 0.046875 Mib памяти
# Время выполнения simple_3 = 0.2748995999999999

# Итого оптимизация алгоритма дала 11-кратную экономию памяти
