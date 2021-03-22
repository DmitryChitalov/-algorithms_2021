"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните операции, равные по смыслу, с каждым из объектов и сделайте замеры.
Опишите полученные результаты, сделайте выводы.

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях?
"""
from collections import OrderedDict
from timeit import timeit

simple_dict = {i: i for i in range(1000000)}
order_dict = OrderedDict(simple_dict)

print(timeit('simple_dict.get(1)', globals=globals()))
print(timeit('order_dict.get(1)', globals=globals()))

print()

print(timeit('simple_dict.popitem()', globals=globals()))
print(timeit('order_dict.popitem()', globals=globals()))

print()

print(timeit('sorted(simple_dict.items(), key=lambda t: t[0])', globals=globals()))
print(timeit('sorted(order_dict.items(), key=lambda t: t[0])', globals=globals()))


'''
Время выполнения аналогичных операций в обычном словаре и OrderedDict отличается незначительно, 
поэтому в поздних версиях Python нет смысла его применять.
'''