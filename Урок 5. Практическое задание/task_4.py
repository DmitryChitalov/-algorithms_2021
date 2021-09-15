"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните операции с каждым их них (заполнение, получение элемента) и сделайте замеры.
Опишите полученные результаты, сделайте выводы.

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях?
"""


from collections import OrderedDict
from timeit import timeit


ORD = OrderedDict([])
DIC = {}


def dict_test_1():
    for i in range(1000):
        DIC[i] = i + 1


def ordi_test_1():
    for i in range(1000):
        ORD[i] = i + 1


def dict_test_2():
    for i in range(1000):
        a = DIC[i]


def ordi_test_2():
    for i in range(1000):
        a = ORD[i]

print('first test:')
print(f"Dict result: {timeit('dict_test_1()', setup='from __main__ import dict_test_1, DIC', number=10000)}")
print(f"OrderedDict result: {timeit('ordi_test_1()', setup='from __main__ import ordi_test_1, ORD', number=10000)}")
print()
print('second test:')
print(f"Dict result: {timeit('dict_test_2()', setup='from __main__ import dict_test_2, DIC', number=10000)}")
print(f"OrderedDict result: {timeit('ordi_test_2()', setup='from __main__ import ordi_test_2, ORD', number=10000)}")
