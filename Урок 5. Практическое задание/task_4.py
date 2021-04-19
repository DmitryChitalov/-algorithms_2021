"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните операции, равные по смыслу, с каждым из объектов и сделайте замеры.
Опишите полученные результаты, сделайте выводы.

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях?
"""

from collections import OrderedDict
from timeit import timeit


def update_dict(dct):
    dct.update({'100': 101})


def update_dict_ord(dct):
    dct.update({'100': 101})


def search_dict(dct):
    dct.get('333')


def search_dict_ord(dct):
    dct.get('333')


def pop_dict(dct):
    dct.popitem()


def pop_dict_ord(dct):
    dct.popitem()

now_dict = {str(i): i for i in range(10000)}
orderdict = OrderedDict(now_dict)
print(f'Update dict')
print(f'dict: {timeit("update_dict(now_dict)", globals=globals(), number=1000000)}')
print(f'ord_dict: {timeit("update_dict_ord(orderdict)", globals=globals(), number=1000000)}')
print(f'Search')
print(f'dict: {timeit("search_dict(now_dict)", globals=globals(), number=1000000)}')
print(f'ord_dict: {timeit("search_dict_ord(orderdict)", globals=globals(), number=1000000)}')
print(f'Pop')
now_dict_1 = {str(i): i for i in range(1000000)}
order_dict_1 = OrderedDict([(str(i), i) for i in range(1000000)])
print(f'dict: {timeit("pop_dict(now_dict_1)", globals=globals(), number=1000)}')
print(f'ord_dict: {timeit("pop_dict_ord(order_dict_1)", globals=globals(), number=1000)}')

#На версии вышее 3,6 скорость у встроенного словаря выше использование актуально на версиях ниже 3.6