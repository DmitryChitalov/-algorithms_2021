"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните операции с каждым их них (заполнение, получение элемента) и сделайте замеры.
Опишите полученные результаты, сделайте выводы.

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях?
"""
from collections import OrderedDict
import timeit

my_dict = {}
my_ordered_dict = OrderedDict()


def fill_dict(dct):
    for i in range(100000):
        dct[i] = i


def fill_ord_dict(ord_dct):
    for i in range(100000):
        ord_dct[i] = i


print(timeit.timeit(
    'fill_dict(my_dict)',
    globals=globals(),
    number=1000
))

print(timeit.timeit(
    'fill_ord_dict(my_ordered_dict)',
    globals=globals(),
    number=1000
))


def work_with_dict(dct):
    for i in range(10000, 40000):
        dct[i] = 10


def work_with_ord_dict(ord_dct):
    for i in range(10000, 40000):
        ord_dct[i] = 10


print(timeit.timeit(
    'work_with_dict(my_dict)',
    globals=globals(),
    number=1000
))

print(timeit.timeit(
    'work_with_ord_dict(my_ordered_dict)',
    globals=globals(),
    number=1000
))


def items_dict(dct):
    for key, value in dct.items():
        dct[key] = 'value'


def items_ord_dict(ord_dct):
    for key, value in ord_dct.items():
        ord_dct[key] = 'value'


print(timeit.timeit(
    'items_dict(my_dict)',
    globals=globals(),
    number=1000
))

print(timeit.timeit(
    'items_ord_dict(my_ordered_dict)',
    globals=globals(),
    number=1000
))

# 7.1859535
# 6.781299200000001
# 1.1383577999999996
# 1.933136000000001
# 3.896352399999998
# 7.777556199999999
# 
# Использование OrderedDict не имеет смысла, так как некоторые операции с ним выполняются
# чуть быстрее, где-то он немного проигрывает по времени. При работе в ключом и значением он же значительно отстаёт
