"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните операции, равные по смыслу, с каждым из объектов и сделайте замеры.
Опишите полученные результаты, сделайте выводы.

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях?
"""
from random import randint
from collections import OrderedDict
from timeit import Timer

dict_obj = {x: [y for y in range(x, randint(1, 20))] for x in range(randint(1, 20))}
print('            ', dict_obj)  # добавил пробелов для наглядности
ordered_dict_obj = OrderedDict(dict_obj)
print(ordered_dict_obj)


def dict_obj_func():
    dict_obj.pop(0)
    dict_obj.keys()
    dict_obj.clear()


def ordered_dict_func():
    ordered_dict_obj.pop(0)
    ordered_dict_obj.keys()
    ordered_dict_obj.clear()


t1 = Timer("dict_obj_func()", "from __main__ import dict_obj_func")
print("Simple dict", t1.timeit(number=10000), "seconds")

t2 = Timer("ordered_dict_func()", "from __main__ import ordered_dict_func")
print("Ordered dict", t2.timeit(number=10000), "seconds")
