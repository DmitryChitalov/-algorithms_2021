"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните операции с каждым их них (заполнение, получение элемента) и сделайте замеры.
Опишите полученные результаты, сделайте выводы.

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях?
"""

from collections import OrderedDict
from timeit import timeit

order_dict = OrderedDict([(i, i) for i in range(100)])
simple_dict = {i: i for i in range(100)}

print(timeit('order_dict = OrderedDict([(i, i) for i in range(100)])', globals=globals()))  # 14.05598889
print(timeit('simple_dict = {i: i for i in range(100)}', globals=globals()))  # 4.366042348999999
# заполнение OrderedDict дольше по времени чем обычного словаря

print(timeit('order_dict[50]', globals=globals()))  # 0.03164073700000003
print(timeit('simple_dict[50]', globals=globals()))  # 0.030413644999999434
# обращение по ключу одинаково по времени

print(timeit('order_dict.copy()', globals=globals()))  # 0.03164073700000003
print(timeit('simple_dict.copy()', globals=globals()))  # 0.030413644999999434
# копирование OrderedDict дольше чем у обычного словаря

print(timeit('order_dict.items()', globals=globals()))  # 0.03164073700000003
print(timeit('simple_dict.items()', globals=globals()))  # 0.030413644999999434
# обращение к элементам одинаково по времени

new1 = {i: i for i in range(80, 120)}

print(timeit('order_dict.update(new1)', globals=globals()))  # 3.318477562
print(timeit('simple_dict.update(new1)', globals=globals()))  # 0.5296854670000002

new2 = {i: i for i in range(1, 30)}
print(timeit('order_dict.update(new1)', globals=globals()))  # 3.2306044499999995
print(timeit('simple_dict.update(new1)', globals=globals()))  # 0.5137349650000003
# Обновление OrderedDict так же дольше

""" 
Видя подобную разницу, и отсутствие каких либо преимуществ в современных версиях Python
Делаю вывод, что OrderedDict - устарел и нет смысла его больше использовать
"""
