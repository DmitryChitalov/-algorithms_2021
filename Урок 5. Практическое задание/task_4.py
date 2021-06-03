"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните операции с каждым их них (заполнение, получение элемента) и сделайте замеры.
Опишите полученные результаты, сделайте выводы.

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях?
"""

from collections import OrderedDict
from timeit import timeit


def fill_ordered_dict():
    dict = OrderedDict()
    return {i: i**2 for i in range(10)}


def fill_reg_dict():
    reg_dict = dict()
    return {i: i**2 for i in range(10)}


def get_el_ordered_dict(dict):
    return dict[1]


def get_el_reg_dict(dict):
    return dict[1]


order_dic = fill_ordered_dict()
reg_dec = fill_reg_dict()
get_el_ordered_dict(order_dic)
# get_el_reg_dict(reg_dec)

print(
    'fill_OrderedDict: ',
    timeit(
        f'fill_ordered_dict()',
        globals=globals(),  number=100000))
print(
    'fill_reg_dict: ',
    timeit(
        f'fill_reg_dict()',
        globals=globals(), number=100000))
print(
    'get_el_ordered_dict: ',
    timeit(
        f'get_el_ordered_dict(order_dic)',
        globals=globals(),  number=1000000))
print(
    'get_el_reg_dict: ',
    timeit(
        f'get_el_reg_dict(reg_dec)',
        globals=globals(), number=1000000))

"""Операции заполнения словаря и поиска элемента в обычных словарях выполняются соизмеримо, 
   а иногда даже быстрее, чем в OrderedDict.
   Смысла использовать OrderedDict в Python нет
"""