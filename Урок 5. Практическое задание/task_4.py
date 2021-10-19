"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните операции, равные по смыслу, с каждым из объектов и сделайте замеры.
Опишите полученные результаты, сделайте выводы.

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях?
"""
from collections import OrderedDict
from timeit import timeit

dict_obj = dict()
for el in range(100000):
    dict_obj[el] = el

ord_dict_obj = OrderedDict(dict_obj)


def get_in_dict_obj():
    for el in range(1000, 3000):
        dict_obj.get(el)


def get_in_ord_dict_obj():
    for el in range(1000, 3000):
        ord_dict_obj.get(el)


def pop_in_dict_obj():
    dict_obj = dict()
    for el in range(100000):
        dict_obj[el] = el
    ord_dict_obj = OrderedDict(dict_obj)
    for el in range(1000):
        dict_obj.popitem()


def pop_in_ord_dict_obj():
    dict_obj = dict()
    for el in range(100000):
        dict_obj[el] = el
    ord_dict_obj = OrderedDict(dict_obj)
    for el in range(1000):
        ord_dict_obj.popitem()


print('get_in_dict_obj\n', timeit("get_in_dict_obj()", globals=globals(), number=1000))
print('get_in_ord_dict_obj\n', timeit("get_in_ord_dict_obj()", globals=globals(), number=1000))
print()
print('pop_in_dict_obj\n', timeit("pop_in_dict_obj()", globals=globals(), number=1000))
print('pop_in_ord_dict_obj\n', timeit("pop_in_ord_dict_obj()", globals=globals(), number=1000))
