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
dict_obj['ключ'] = '45'
print('            ', dict_obj)  # добавил пробелов для наглядности
ordered_dict_obj = OrderedDict(dict_obj)
print(ordered_dict_obj)


def dict_keys():
    ordered_dict_obj.keys()


def ordered_dict_keys():
    dict_obj.keys()


def dict_clear():
    dict_obj.clear()


def ordered_dict_clear():
    ordered_dict_obj.clear()


def dict_update():
    dict_obj.update([])


def ordered_dict_update():
    ordered_dict_obj.update([])


t3 = Timer("dict_keys()", "from __main__ import dict_keys")
print("dict keys", t3.timeit(number=10000), "seconds")

t4 = Timer("ordered_dict_keys()", "from __main__ import ordered_dict_keys")
print("Ordered dict keys", t4.timeit(number=10000), "seconds")

t5 = Timer("dict_clear()", "from __main__ import dict_clear")
print("dict clear", t5.timeit(number=10000), "seconds")

t6 = Timer("ordered_dict_clear()", "from __main__ import ordered_dict_clear")
print("Ordered dict clear", t6.timeit(number=10000), "seconds")

t7 = Timer("dict_update()", "from __main__ import dict_update")
print("dict update", t7.timeit(number=10000), "seconds")

t8 = Timer("ordered_dict_update()", "from __main__ import ordered_dict_update")
print("Ordered dict update", t8.timeit(number=10000), "seconds")
"""
OrderedDict работает медленнее

dict keys 0.0008522000000000043 seconds
Ordered dict keys 0.0008977999999999972 seconds

dict clear 0.0007484000000000032 seconds
Ordered dict clear 0.000681000000000001 seconds

dict update 0.0012327000000000032 seconds
Ordered dict update 0.0019298999999999983 seconds
"""
