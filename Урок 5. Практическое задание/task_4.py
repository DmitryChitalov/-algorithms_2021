"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните операции с каждым их них (заполнение, получение элемента) и сделайте замеры.
Опишите полученные результаты, сделайте выводы.

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях?
"""
'''
Время работы обычного словаря и OrderedDict примерно равно, и зачастую встроенный словарь работает быстрее.
Считаю, что нет никакого смысла использовать OrderedDict в Python 3.6 и более поздних версиях.
'''
import collections
from timeit import timeit

test_dict1 = {}
test_dict2 = collections.OrderedDict([])


def app_dict1():
    for i in range(10000000):
        test_dict1[i] = i


def app_dict2():
    for i in range(10000000):
        test_dict2[i] = i


print(timeit('app_dict1', globals=globals()))
print(timeit('app_dict2', globals=globals()))


def el_dict1():
    for i, j in test_dict1.items():
        return i, j


def el_dict2():
    for i, j in test_dict2.items():
        return i, j


print(timeit('el_dict1', globals=globals()))
print(timeit('el_dict2', globals=globals()))
