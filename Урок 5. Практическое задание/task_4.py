"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните операции с каждым их них (заполнение, получение элемента) и сделайте замеры.
Опишите полученные результаты, сделайте выводы.

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях?
"""
from collections import OrderedDict
from timeit import timeit
from math import *

my_dict = {}
ord_dict = OrderedDict()


def dict_filling():
    for num in range(100):
        my_dict[num] = cos(num/7)


def order_filling():
    for num in range(100):
        ord_dict[num] = cos(num/7)


def get_key_dict():
    for num in range(100):
        _ = my_dict[num]


def get_key_order():
    for num in range(100):
        _ = ord_dict[num]


def dict_key_deleting():
    for num in range(100):
        my_dict.pop(num, 0)


def ord_key_deleting():
    for num in range(100):
        ord_dict.pop(num, 0)


print('dict_filling: ', timeit('dict_filling()', globals=globals(), number=100000))
print('order_filling: ', timeit('order_filling()', globals=globals(), number=100000))
print('get_key_dict: ', timeit('get_key_dict()', globals=globals(), number=100000))
print('get_key_order: ', timeit('get_key_order()', globals=globals(), number=100000))
print('dict_key_deleting: ', timeit('dict_key_deleting()', globals=globals(), number=100000))
print('ord_key_deleting: ', timeit('ord_key_deleting()', globals=globals(), number=100000))


# dict_filling:  1.7229221
# order_filling:  1.9660832
# get_key_dict:  0.4039648999999996
# get_key_order:  0.40099139999999966
# dict_key_deleting:  0.5536994000000002
# ord_key_deleting:  1.3090723999999998
# В наполнении и получении значений по ключу он такой же как и обычный словарь, а в удалении элемента по ключу
# показывает время едва ли не в три раза большее чем обычный словарь. Вероятно, что использовать OrderedDict
# в версии Python 3.X не нужно, ибо он не даст каких либо преимуществ.
