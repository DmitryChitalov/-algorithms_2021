"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните операции, равные по смыслу, с каждым из объектов и сделайте замеры.
Опишите полученные результаты, сделайте выводы.

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях?
"""

from timeit import timeit
from collections import OrderedDict
import random

random_keys = list(range(0, 10000))
random.shuffle(random_keys)

test_dict = {}
for i in random_keys:
    test_dict['key'+str(i)] = random.randrange(10000)

test_ordered_dict = OrderedDict()
for i in random_keys:
    test_ordered_dict['key'+str(i)] = random.randrange(10000)

print('Добавление элемента:')
print(timeit("test_dict['key50000'] = 0", number=10**7, globals=globals()))
print(timeit("test_ordered_dict['key50000'] = 0", number=10**7, globals=globals()))

print('Изменение элемента:')
print(timeit("test_dict['key0'] = 0", number=10**7, globals=globals()))
print(timeit("test_ordered_dict['key0'] = 0", number=10**7, globals=globals()))

print('Получение ключей:')
print(timeit("test_dict.keys()", number=10**7, globals=globals()))
print(timeit("test_ordered_dict.keys()", number=10**7, globals=globals()))

print('Получение значений:')
print(timeit("test_dict.values()", number=10**7, globals=globals()))
print(timeit("test_ordered_dict.values()", number=10**7, globals=globals()))

print('Получение значения по ключу:')
print(timeit("test_dict.get('key0')", number=10**7, globals=globals()))
print(timeit("test_ordered_dict.get('key0')", number=10**7, globals=globals()))

print('Получение пар ключ-значение:')
print(timeit("test_dict.items()", number=10**7, globals=globals()))
print(timeit("test_ordered_dict.items()", number=10**7, globals=globals()))

print('Удаление и получение пары ключ-значение:')
print(timeit("test_dict.popitem()", number=10**4, globals=globals()))
print(timeit("test_ordered_dict.popitem()", number=10**4, globals=globals()))

"""
Добавление элемента - Dict отрабатывает быстрее (в среднем на 30%), чем OrderedDict
0.5039891
0.6776582999999999

Изменение элемента - Dict отрабатывает быстрее (в среднем на 30%), чем OrderedDict
0.5290591
0.9284265999999999

Получение ключей - разница не существенная и лидер меняется раз от раза
0.7048473999999998
0.7934819000000002

Получение значений - разница не существенная и лидер меняется раз от раза
0.6771446999999999
0.6693021999999997

Получение значения по ключу - разница не существенная и лидер меняется раз от раза
0.8082273999999998
0.8439976999999996

Получение пар ключ-значение - разница не существенная и лидер меняется раз от раза
0.7103396000000002
0.6587911999999996

Удаление и получение пары ключ-значение - Dict отрабатывает намного быстрее (в среднем в 2 раза), чем OrderedDict
0.0010149000000003738
0.0019252000000005154

Вывод:
Ни в одном из сравнительных опытов OrderedDict не показал стабильного преимущества над обычным Dict, а даже наоборот
существенно отстал в паре-тройке тестов. Исходя из этого я не вижу целесообразности в использовании OrderedDict в 
Python 3.6 и более поздних версиях.
"""
