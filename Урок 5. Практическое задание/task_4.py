"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните различные операции с каждым из объектов и сделайте замеры.
Опишите полученные результаты, сделайте выводы.
"""
from collections import OrderedDict
from timeit import timeit

my_dict = {i: i + 2 for i in range(1000000)}
my_ordered = OrderedDict(my_dict)

print('OrderedDict pop')
print(timeit('my_ordered.popitem()', globals=globals(), number=1000000))
print('Dict pop')
print(timeit('my_dict.popitem()', globals=globals(), number=1000000))
print('OrderedDict values')
print(timeit('my_ordered.values', globals=globals(), number=1000000))
print('Dict values')
print(timeit('my_dict.values', globals=globals(), number=1000000))
print('OrderedDict keys')
print(timeit('my_ordered.keys', globals=globals(), number=1000000))
print('Dict keys')
print(timeit('my_dict.keys', globals=globals(), number=1000000))

"""Cмысла в использовании OrderedDict нет, так как словарь в новых версиях Python уже упорядоченный,
а увеличение в скорости незначительно
"""