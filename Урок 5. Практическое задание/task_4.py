"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните операции, равные по смыслу, с каждым из объектов и сделайте замеры.
Опишите полученные результаты, сделайте выводы.

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях?
"""

import random
import sys
from timeit import timeit
from collections import OrderedDict


random_keys = list(range(0, 10000))

random.shuffle(random_keys)

print(random_keys)

test_dict = {}

for i in random_keys:

    test_dict['key'+str(i)] = random.randrange(10000)


test_ordered_dict = OrderedDict()

for i in random_keys:

    test_ordered_dict['key'+str(i)] = random.randrange(10000)

print(sys.version)

print("Add element")

print(timeit("test_dict['key50000'] = 0", number=1000000, globals=globals()))
print(timeit("test_ordered_dict['key50000'] = 0", number=1000000, globals=globals()))

print("Change element")

print(timeit("test_dict['key0'] = 0", number=1000000, globals=globals()))
print(timeit("test_ordered_dict['key0'] = 0", number=1000000, globals=globals()))

print("Get keys")

print(timeit("test_dict.keys()", number=10000000, globals=globals()))
print(timeit("test_ordered_dict.keys()", number=10000000, globals=globals()))

print("Get value")

print(timeit("test_dict.get('key0')", number=10000000, globals=globals()))
print(timeit("test_ordered_dict.get('key0')", number=10000000, globals=globals()))

print("Get item")

print(timeit("test_dict.items()", number=10000000, globals=globals()))
print(timeit("test_ordered_dict.items()", number=10000000, globals=globals()))

print("Pop item")

print(timeit("test_dict.popitem()", number=10000, globals=globals()))
print(timeit("test_ordered_dict.popitem()", number=10000, globals=globals()))

"""
-----------------------------------------------------------------------------------------------------------------------
Add element
Обычный словарь быстрее

0.03648390000000001
0.08587030000000001
-----------------------------------------------------------------------------------------------------------------------
Change element
Обычный словарь быстрее

0.0713277
0.1090273
-----------------------------------------------------------------------------------------------------------------------
Get keys
Обычный словарь быстрее

0.8695930000000001
0.8151327000000002
-----------------------------------------------------------------------------------------------------------------------
Get value
Обычный словарь быстрее

0.7323369
0.6902724
-----------------------------------------------------------------------------------------------------------------------
Get item
OrderedDict словарь быстрее (но не слишком сильно)

0.8636351000000002
0.8709061
-----------------------------------------------------------------------------------------------------------------------
Pop item
Обычный словарь быстрее

0.002714999999999357
0.0015686000000005862
-----------------------------------------------------------------------------------------------------------------------
Я считаю что использовать OrderedDict в даннйо версии Python, смысла как такого нет, потому что OrderedDict оказался 
быстрее только в одном случае и с небольшим отрывом.
"""
