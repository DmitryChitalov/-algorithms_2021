"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните операции, равные по смыслу, с каждым из объектов и сделайте замеры.
Опишите полученные результаты, сделайте выводы.

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях?
"""

from collections import OrderedDict
from timeit import timeit

my_dict = {i: i for i in range(100000)}
my_ordered = OrderedDict(my_dict)

print(f'keys dict : {timeit("my_dict.keys()", number=100000, globals=globals())}')
print(f'keys OrderedDict : {timeit("my_ordered.keys()", number=100000, globals=globals())}')
print('*' * 20)
print(f'values dict : {timeit("my_dict.values()", number=100000, globals=globals())}')
print(f'values OrderedDict : {timeit("my_ordered.values()", number=100000, globals=globals())}')
print('*' * 20)
print(f'get dict : {timeit("my_dict.get(20000)", number=100000, globals=globals())}')
print(f'get OrderedDict : {timeit("my_ordered.get(20000)", number=100000, globals=globals())}')
print('*' * 20)
print(f'popitem dict: {timeit("my_dict.popitem()", number=100000, globals=globals())}')
print(f'popitem OrderedDict : {timeit("my_ordered.popitem()", number=100000, globals=globals())}')

"""
keys dict : 0.007319299999999987
keys OrderedDict : 0.007569699999999999
********************
values dict : 0.0074285000000000045
values OrderedDict : 0.01006209999999999
********************
get dict : 0.0079621
get OrderedDict : 0.010936500000000016
********************
popitem dict: 0.014465599999999995
popitem OrderedDict : 0.023523900000000014

OrderedDict оптимизирован хуже, смысла в использовании нет.
В Python 3.6  -  словарь упорядоченный.
"""