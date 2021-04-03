"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните операции, равные по смыслу, с каждым из объектов и сделайте замеры.
Опишите полученные результаты, сделайте выводы.

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях?
"""

from collections import OrderedDict
from timeit import timeit

my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9}
my_ord_dict = OrderedDict([('a', 1), ('b', 2), ('c', 3), ('d', 4), ('e', 5), ('f', 6), ('g', 7), ('h', 8), ('i', 9)])


def get_value(array):
    return array['g']


def remove_item(array):
    array.pop('e')
    array['e'] = 5
    return


for key in my_dict:
    print(f'{key}: {my_dict[key]}')

print('Получение значения по ключу')
print(
    timeit(
        "get_value(my_dict)",
        setup='from __main__ import get_value, my_dict'))
print(
    timeit(
        "get_value(my_ord_dict)",
        setup='from __main__ import get_value, my_ord_dict'))

print('Удаление ключа и добавление ключа')
print(
    timeit(
        "remove_item(my_dict)",
        setup='from __main__ import remove_item, my_dict'))
print(
    timeit(
        "remove_item(my_ord_dict)",
        setup='from __main__ import remove_item, my_ord_dict'))

"""Получение значения по ключу одинакове. Удаление и добавление ключа в OrderedDict занимает больше времени
В python версии 3.6 и выше использовать OrderedDict нету смысла, т.к. словарь "помнит" порядок элементов """
