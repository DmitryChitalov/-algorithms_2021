"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните операции с каждым их них (заполнение, получение элемента) и сделайте замеры.
Опишите полученные результаты, сделайте выводы.

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях?
"""

from timeit import timeit
from collections import OrderedDict

experimental_dict = {i: i for i in range(10)}
experemental_ord_dict = OrderedDict({i: i for i in range(10)})



def fill_dict():   
    dict = {i: i for i in range(10)}
    return dict

print(f"{fill_dict.__name__} \
    {timeit('fill_dict()', globals=globals(), number=10000)}")


def fill_ord_dict(): 
    ord_dict = OrderedDict({i: i for i in range(10)})
    return ord_dict

print(f"{fill_ord_dict.__name__} \
    {timeit('fill_ord_dict()', globals=globals(), number=10000)}")


def get_elm_dict(experimental_dict):
    return experimental_dict.get(7)

print(f"{get_elm_dict.__name__} \
    {timeit('get_elm_dict(experimental_dict)', globals=globals(), number=10000)}")


def get_elm_ord_dict(experemental_ord_dict):
    return experemental_ord_dict.get(7)

print(f"{get_elm_ord_dict.__name__} \
    {timeit('get_elm_ord_dict(experemental_ord_dict)', globals=globals(), number=10000)}")

 
     
# Python 3.8.10

# fill_dict           0.007075538000208326
# fill_ord_dict       0.019693026999448193

# get_elm_dict        0.0010672850003174972
# get_elm_ord_dict    0.0011290509974060114

# И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях?
# -нет

# Версия по умолчанию оказась более быстродейственной.