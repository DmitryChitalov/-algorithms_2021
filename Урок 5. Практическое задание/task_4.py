"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните операции, равные по смыслу, с каждым из объектов и сделайте замеры.
Опишите полученные результаты, сделайте выводы.

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях?
"""

import collections
from timeit import Timer


def fill_simple_dict(n):

    dct = {}

    for i in range(n):
        dct[i] = i ** 2

    return dct


def fill_ord_dict(n):

    dct = collections.OrderedDict()

    for i in range(n):
        dct[i] = i ** 2

    return dct


def clear_simple_dict(dct):

    return dct.clear()


def clear_ord_dict(dct):

    return dct.clear()


def copy_simple_dict(dct):

    return dct.copy()


def copy_ord_dict(dct):

    return dct.copy()


def pop_simple_dict(dct):

    n = len(dct)
    for i in range(n):
        dct.popitem()

    return dct


def pop_ord_dict(dct):

    n = len(dct)
    for i in range(n):
        dct.popitem()

    return dct


el_count = 1000000
simple_dict = fill_simple_dict(el_count)
ord_dict = fill_ord_dict(el_count)
simple_dict_copy = copy_simple_dict(simple_dict)
ord_dict_copy = copy_ord_dict(ord_dict)


print('# Заполнение словарей')
t1 = Timer("fill_simple_dict(el_count)", "from __main__ import fill_simple_dict, el_count")
print('t1', t1.timeit(number=10))

t2 = Timer("fill_ord_dict(el_count)", "from __main__ import fill_ord_dict, el_count")
print('t2', t2.timeit(number=10))


print('# Копирование словарей')
t1 = Timer("copy_simple_dict(simple_dict)", "from __main__ import copy_simple_dict, simple_dict")
print('t1', t1.timeit(number=10))

t2 = Timer("copy_ord_dict(ord_dict)", "from __main__ import copy_ord_dict, ord_dict")
print('t2', t2.timeit(number=10))


print('# Очистка словарей')
t1 = Timer("clear_simple_dict(simple_dict)", "from __main__ import clear_simple_dict, simple_dict")
print('t1', t1.timeit(number=10))

t2 = Timer("clear_ord_dict(ord_dict)", "from __main__ import clear_ord_dict, ord_dict")
print('t2', t2.timeit(number=10))


print('# Метод pop')
t1 = Timer("pop_simple_dict(simple_dict_copy)", "from __main__ import pop_simple_dict, simple_dict_copy")
print('t1', t1.timeit(number=10))

t2 = Timer("pop_ord_dict(ord_dict_copy)", "from __main__ import pop_ord_dict, ord_dict_copy")
print('t2', t2.timeit(number=10))

# # Заполнение словарей
# t1 4.5431934400000005
# t2 5.070647103999999
# # Копирование словарей
# t1 0.23617151100000022
# t2 1.5754562280000002
# # Очистка словарей
# t1 0.009543518999999279
# t2 0.026025516000000692
# # Метод pop
# t1 0.10451849200000041
# t2 0.1702950750000003

# Действительно, использование OrderedDict не дает выигрыша в производительности в сравнении
# с традиционным словарем.
# Возможно функциональные отличия от традиционного словаря (например, метод pop, новый метод
# move_to_end) дадут упорядоченному словарю оправданное преимущество
