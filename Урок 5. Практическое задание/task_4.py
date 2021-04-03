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


# Создаем ключи будущих словарей в случайном порядке
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
Add element - Обычный словарь отрабатывает быстрее
0.058343300000000015
0.0799668

Change element - Обычный словарь отрабатывает быстрее
0.06759169999999998
0.0957192

Get keys - Обычный словарь отрабатывает быстрее
1.0107604000000001
1.0364669000000002

Get value - Обычный словарь отрабатывает быстрее
1.0724565
1.0960557

Get item - OrderedDict отрабатывает немного быстрее
1.0347330000000001
1.0187932999999996

Pop item - Обычный словарь отрабатывает быстрее
0.0015416999999997572
0.004561500000000329

По результатам замеров можно сделать вывод, что смысла использлвать OrderedDict в python 3.7 нет,
так как он либо сравним по скорости работы, либо медленнее обычного словаря.
"""