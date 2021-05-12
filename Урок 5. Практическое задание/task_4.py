"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните операции, равные по смыслу, с каждым из объектов и сделайте замеры.
Опишите полученные результаты, сделайте выводы.

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях?
"""

from collections import OrderedDict
from timeit import timeit

some_dict = {f'key_{i}': f'val_{i}' for i in range(10000)}
ordered_dict = OrderedDict(some_dict)

key = 'key_1234'
print(f"Метод get в dict:  {timeit('some_dict.get(key)', globals=globals(),number=10000000)}")
print(f"Метод get в OrderedDict:  {timeit('ordered_dict.get(key)', globals=globals(),number=10000000)}")
# Метод get в dict:  0.7612156
# Метод get в OrderedDict:  0.8148097999999999
print(f"Метод values в dict:  {timeit('some_dict.values()', globals=globals(),number=10000000)}")
print(f"Метод values в OrderedDict:  {timeit('ordered_dict.values()', globals=globals(),number=10000000)}")
# Метод values в dict:  0.6466119999999997
# Метод values в OrderedDict:  0.5627468000000002
print(f"Метод items в dict:  {timeit('some_dict.items()', globals=globals(),number=10000000)}")
print(f"Метод items в OrderedDict:  {timeit('ordered_dict.items()', globals=globals(),number=10000000)}")
# Метод items в dict:  0.6719317
# Метод items в OrderedDict:  0.6388456999999996
'''
Замеры показали равноценные результаты поэтому особого смысла использовать OrderedDict
в Python 3.6 и более поздних версиях нет. За исключением работы с csv о чём мы узнали на уроке.
'''