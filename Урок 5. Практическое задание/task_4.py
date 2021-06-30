"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните операции с каждым их них (заполнение, получение элемента) и сделайте замеры.
Опишите полученные результаты, сделайте выводы.

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях?
"""
from timeit import timeit
from collections import OrderedDict

my_dict = {}
my_ordered_dict = OrderedDict()


def create_dict(dct):
    for i in range(10000):
        dct[i] = i + 1
    return dct


def create_ordered_dict(dct):
    for i in range(10000):
        dct[i] = i + 1
    return dct


def change_my_dict(dct):
    for i in range(10000):
        dct[i] = i + 1


def change_my_ordered_dict(dct):
    for i in range(10000):
        dct[i] = i + 1


print(f"create_dict {timeit('create_dict(my_dict)', globals=globals(), number = 10)}")
print(f"create_ordered_dict {timeit('create_ordered_dict(my_ordered_dict)', globals=globals(), number = 10)}")
full_dict = create_dict(my_dict)
full_ordered_dict = create_ordered_dict(my_ordered_dict)

print(f"change_my_dict {timeit('change_my_dict(full_dict)', globals=globals(), number = 10)}")
print(f"change_my_ordered_dict {timeit('change_my_ordered_dict(full_ordered_dict)', globals=globals(), number = 10)}")

"""Операции заполнения и изменения словаря быстрее, чем в OrderedDict. Следовательно в Python 3.6 и выше использование 
OrderedDict не целесообразно."""