"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните операции, равные по смыслу, с каждым из объектов и сделайте замеры.
Опишите полученные результаты, сделайте выводы.

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях?
"""


from collections import OrderedDict
from timeit import timeit

my_dict = {i: i + 2 for i in range(1000000)}
my_ordered = OrderedDict(my_dict)

print('OrderedDict pop: ' + str(timeit('my_ordered.popitem()', globals=globals(), number=1000000)))
print('Dict pop: ' + str(timeit('my_dict.popitem()', globals=globals(), number=1000000)) + '\n')

print('OrderedDict values: ' + str(timeit('my_ordered.values', globals=globals(), number=1000000)))
print('Dict values: ' + str(timeit('my_dict.values', globals=globals(), number=1000000)) + '\n')

print('OrderedDict keys: ' + str(timeit('my_ordered.keys', globals=globals(), number=1000000)))
print('Dict keys: ' + str(timeit('my_dict.keys', globals=globals(), number=1000000)))

"""
Нет смысла использовать OrderedDict, т.к. словарь в новых версиях Python уже упорядоченный и быстрее
"""
