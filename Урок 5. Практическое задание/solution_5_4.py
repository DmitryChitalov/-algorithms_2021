from collections import OrderedDict
from timeit import timeit
"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните операции с каждым их них (заполнение, получение элемента) и сделайте замеры.
Опишите полученные результаты, сделайте выводы.
И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях?

Нет смысла использовать OrderedDict в Python 3.6 и поздних версиях, 
тем более запись в словарь происходит быстрее.
"""


dct = {}
ord_dct = OrderedDict()


print('*' * 50)
print(timeit('dct["one"] = 1', globals=globals(), number=1), '- write dict')
print(timeit('ord_dct["one"] = 1', globals=globals(), number=1), '- write OrderedDict')
print('*' * 50)
print(timeit('dct["one"]', globals=globals(), number=10000), '- read dict')
print(timeit('ord_dct["one"]', globals=globals(), number=10000), '- read OrderedDict')
print('*' * 50)
