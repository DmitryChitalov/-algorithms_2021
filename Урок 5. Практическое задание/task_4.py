"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните операции с каждым их них (заполнение, получение элемента) и сделайте замеры.
Опишите полученные результаты, сделайте выводы.

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях?
"""
from collections import OrderedDict
from timeit import timeit

some_dict = {}
some_ordered_dict = OrderedDict()


def fill_dict():
    for i in range(1000):
        some_dict[f'key-{i}'] = i


def fill_ordered_dict():
    for i in range(1000):
        some_ordered_dict[f'key-{i}'] = i


def get_elem_dict(key):
    return some_dict.get(key)


def get_elem_ordered_dict(key):
    return some_ordered_dict.get(key)




print(timeit('fill_dict()', globals=globals(), number=100))
print(timeit('fill_ordered_dict()', globals=globals(), number=100))
print(timeit('get_elem_dict("key-100")', globals=globals(), number=100))
print(timeit('get_elem_ordered_dict("key-100")', globals=globals(), number=100))

"""Разница в скорости не критична, имеет смысл использовать в особых случаях"""