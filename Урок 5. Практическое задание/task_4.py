"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните операции с каждым их них (заполнение, получение элемента) и сделайте замеры.
Опишите полученные результаты, сделайте выводы.

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях?
"""
from collections import OrderedDict
from timeit import timeit

my_dict = {}
my_ordered_dict = OrderedDict()
items_count = 1000


def dct_fill(dct):
    for i in range(items_count):
        dct[i] = i
    return dct


def ordered_dct_fill(dct):
    for i in range(items_count):
        dct[i] = i
    return dct


def get_from_dct(dct, item):
    dct.get(item)


def get_from_orddct(dct, item):
    dct.get(item)


print(f'dct_fill: {timeit("dct_fill(my_dict)", globals=globals(), number=100000)}')
print(f'ordered_dct_fill: {timeit("ordered_dct_fill(my_ordered_dict)", globals=globals(), number=100000)}')
print(f'get_from_dct: {timeit("get_from_dct(my_dict, 5)", globals=globals(), number=100000)}')
print(f'get_from_orddct: {timeit("get_from_orddct(my_ordered_dict, 5)", globals=globals(), number=100000)}')


"""
Выводы:

Смысла использовать OrderedDict нет, т.к. работает медленее обычного словаря.

"""