"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните операции с каждым их них (заполнение, получение элемента) и сделайте замеры.
Опишите полученные результаты, сделайте выводы.

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях?
"""

import collections
from timeit import timeit


test_dict = dict((int(n), int(n)) for n in range(1000000))
test_order_dict = collections.OrderedDict(dict((int(n), int(n)) for n in range(1000000)))


def dict_filling(input_dict):
    dict1 = {}
    for key, value in input_dict.items():
        dict1[key] = value
    return dict1


print(
    timeit(
        "dict_filling(dict((int(n), int(n)) for n in range(1000000)))",
        globals=globals(),
        number=5))

print(
    timeit(
        "dict_filling(collections.OrderedDict(dict((int(n), int(n)) for n in range(1000000))))",
        globals=globals(),
        number=5))

print(
    timeit(
        "test_dict[50000]",
        globals=globals(),
        number=10000))

print(
    timeit(
        "test_order_dict[50000]",
        globals=globals(),
        number=10000))


# Заполнение словаря с использованием OrderedDict происходит медленнее, поиск почти идентичен по времени.
# В версиях Python начиная с 3.6 нет смысла использовать OrderedDict, так как словари в них упорядочены.
