"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните операции, равные по смыслу, с каждым из объектов и сделайте замеры.
Опишите полученные результаты, сделайте выводы.

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях?
"""

import collections
import timeit
import random


dict1 = {i: i for i in range(500)}
odict1 = collections.OrderedDict((i, i) for i in range(500))


print(timeit.timeit('dict1.items()', globals=globals()))
print(timeit.timeit('odict1.items()', globals=globals()))

print(timeit.timeit('dict1.get(random.randint(0,500))', globals=globals()))
print(timeit.timeit('odict1.get(random.randint(0,500))', globals=globals()))

print(timeit.timeit('dict1.values()', globals=globals()))
print(timeit.timeit('odict1.values()', globals=globals()))

print(timeit.timeit('dict1.pop(random.randint(0,500), 0)', globals=globals()))
print(timeit.timeit('odict1.pop(random.randint(0,500), 0)', globals=globals()))

print(timeit.timeit('dict1.update({ 1: 1})', globals=globals()))
print(timeit.timeit('odict1.update({ 1: 1})', globals=globals()))

#Особой разницы в скорости не наблюдается
