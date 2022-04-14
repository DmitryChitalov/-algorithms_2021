"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните операции с каждым их них (заполнение, получение элемента) и сделайте замеры.
Опишите полученные результаты, сделайте выводы.

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях?
"""

from collections import OrderedDict
from timeit import timeit

d = {}
for i in range(1000000):
    d.setdefault(i, 'default_val')
d_o = OrderedDict(d)


print(timeit('d_o.popitem()', globals=globals(), number=1000000))
print(timeit('d.popitem()', globals=globals(), number=1000000))
print('==============')
print(timeit('d_o.items', globals=globals(), number=1000000))
print(timeit('d.items', globals=globals(), number=1000000))


"""Аналитика.
0.1552852
0.09235500000000008
==============
0.05615480000000006
0.056314500000000045

Замеры показали примерно равный результат, поэтому разницы особо нет. Начиная с версии 3.6
словарь стал упорядоченым. Вывод: OrderedDict не используем.
"""