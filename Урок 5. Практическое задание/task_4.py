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
    for i in range(10000):
        some_dict[f'key-{i}'] = i


def fill_ordered_dict():
    for i in range(10000):
        some_ordered_dict[f'key-{i}'] = i


def get_elem_dict(key):
    return some_dict.get(key)


def get_elem_ordered_dict(key):
    return some_ordered_dict.get(key)


print(timeit('fill_dict()', globals=globals(), number=1000))
print(timeit('fill_ordered_dict()', globals=globals(), number=1000))
print()
fill_dict()
fill_ordered_dict()
print(timeit('get_elem_dict("key-1000")', globals=globals(), number=1000000))
print(timeit('get_elem_ordered_dict("key-1000")', globals=globals(), number=1000000))

"""Смысла использовать OrderedDict в версиях python 3.6 и выше нет, так как в более 
поздних версиях словари помнят порядок добавления в них элементов.
Имеет смысл их использовать только если нужны специфические методы, например перемещения элемента"""
