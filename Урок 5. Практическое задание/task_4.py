"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните операции, равные по смыслу, с каждым из объектов и сделайте замеры.
Опишите полученные результаты, сделайте выводы.

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях?
"""

from collections import OrderedDict
from timeit import timeit


def dict_builder(some_dict):
    some_dict = {el: el ** el for el in range(100)}
    return some_dict


def dict_search(some_dict):
    return some_dict.get(99)


def dict_pop(some_dict):
    some_dict = {el: el ** el for el in range(100)}
    for i in range(50):
        some_dict.pop(i)
    return some_dict


dct = {}
ord_dct = OrderedDict()
dct = dict_builder(dct)
ord_dct = dict_builder(ord_dct)

print(timeit('dict_builder(dct)', globals=globals(), number=1000))
print(timeit('dict_builder(ord_dct)', globals=globals(), number=1000))

print(timeit('dict_search(dct)', globals=globals(), number=100000))
print(timeit('dict_search(ord_dct)', globals=globals(), number=100000))

print(timeit('dict_pop(dct)', globals=globals(), number=1000))
print(timeit('dict_pop(ord_dct)', globals=globals(), number=1000))

"""
По итогам замеров времени работы операций с обычным словарем и OrderedDict
вывод следующий - время работы сопоставимо, смысла использовать OrderedDict нет.
"""
