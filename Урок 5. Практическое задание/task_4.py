"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните операции, равные по смыслу, с каждым из объектов и сделайте замеры.
Опишите полученные результаты, сделайте выводы.

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях?
"""
from timeit import timeit
from collections import OrderedDict
ord_dict = OrderedDict()
dict_ = dict()


def ord_dict_insert():
    for value in range(10000):
        ord_dict[value] = value


def dict_insert():
    for value in range(10000):
        dict_[value] = value


print(timeit('ord_dict_insert()', globals=globals(), number=10))
print(timeit('dict_insert()', globals=globals(), number=10))
# print(dict_)
# print(ord_dict)
'''Смысла использовать OrderedDict в Python 3.6 и более поздних версиях нет т.к. начиная с версии Python 3.6
    списки изначально упорядоченны и не требуют дополнительных операций над ними, и по скорости они не уступают 
    OrderedDict'''
