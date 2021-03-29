"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните операции, равные по смыслу, с каждым из объектов и сделайте замеры.
Опишите полученные результаты, сделайте выводы.

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях?
"""
from timeit import timeit
from collections import OrderedDict


def dict_filler(my_dict):
    my_dict = {k: k**2 for k in range(10000)}
    return my_dict


def dict_search(my_dict):
    return my_dict[9000]


def dict_pop(my_dict):
    my_dict = {k: k ** 2 for k in range(10000)}
    for i in range(1000, 9000):
        my_dict.pop(i)
    return my_dict


my_dict = {}
o_dict = OrderedDict()

print(timeit('dict_filler(my_dict)', 'from __main__ import dict_filler, my_dict', number=100))
print(timeit('dict_filler(o_dict)', 'from __main__ import dict_filler, o_dict', number=100))

my_dict = dict_filler(my_dict)
o_dict = dict_filler(o_dict)

assert list(my_dict.items()) == list(o_dict.items())

print(timeit('dict_filler(my_dict)', 'from __main__ import dict_filler, my_dict', number=100))
print(timeit('dict_filler(o_dict)', 'from __main__ import dict_filler, o_dict', number=100))

print(timeit('dict_pop(my_dict)', 'from __main__ import dict_pop, my_dict', number=100))
print(timeit('dict_pop(o_dict)', 'from __main__ import dict_pop, o_dict', number=100))


# Замеры времени показали одинаковые результаты, порядок элементов в обоих словарях одинаков.
# Смысла использовать OrderedDict вместо обычного нет.
