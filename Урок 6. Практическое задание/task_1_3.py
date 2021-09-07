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

from memory_profiler import profile
import random

############################################################### Пример 3

import collections

lst = random.sample(range(-100000, 100000), 10 ** 5)


@profile
def fill_dict(values):
    '''
    заполняем стандартный словарь значениями из списка.
    '''
    my_dict = {}
    for i in range(10 ** 5):
        my_dict[values[i]] = values[i]
    return my_dict


@profile
def fill_odict(values):
    '''
    заполняем OrderedDict словарь значениями из списка.
    как видно, он не только медленнее чем стандартный словарь,
    но еще и занимает больше памяти
    '''
    my_odict = collections.OrderedDict()
    for i in range(10 ** 5):
        my_odict[values[i]] = values[i]
    return my_odict


NEW_DICT = fill_dict(lst)
NEW_ODICT = fill_odict(lst)

'''
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    35     26.3 MiB     26.3 MiB           1   @profile
    36                                         def fill_dict(values):
    37                                             '
    38                                             заполняем стандартный словарь значениями из списка.
    39                                             '
    40     26.3 MiB      0.0 MiB           1       my_dict = {}
    41     31.4 MiB      0.0 MiB      100001       for i in range(10 ** 5):
    42     31.4 MiB      5.0 MiB      100000           my_dict[values[i]] = values[i]
    43     31.4 MiB      0.0 MiB           1       return my_dict


Filename: C:\Users\ПК\PycharmProjects\-algorithms_2021\Урок 6. Практическое задание\task_1_3.py

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    46     31.4 MiB     31.4 MiB           1   @profile
    47                                         def fill_odict(values):
    48                                             '
    49                                             заполняем OrderedDict словарь значениями из списка.
    50                                             как видно, он не только медленнее чем стандартный словарь,
    51                                             но еще и занимает больше памяти
    52                                             '
    53     31.4 MiB      0.0 MiB           1       my_odict = collections.OrderedDict()
    54     38.4 MiB      0.0 MiB      100001       for i in range(10 ** 5):
    55     38.4 MiB      7.0 MiB      100000           my_odict[values[i]] = values[i]
    56     38.4 MiB      0.0 MiB           1       return my_odict
'''