"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните операции с каждым их них (заполнение, получение элемента) и сделайте замеры.
Опишите полученные результаты, сделайте выводы.

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях?
"""

from collections import OrderedDict
from timeit import timeit

simple_dict = {'a': 1, 'f': 25, 'c': 9, 't': 34, 'g': 11}
od = OrderedDict(simple_dict)

print(timeit('simple_dict["b"] = 10', globals=globals()))
print(timeit('od["b"] = 10', globals=globals()))
print('-' * 100)

print(timeit('simple_dict.get("b")', globals=globals()))
print(timeit('od.get("b")', globals=globals()))
print('-' * 100)

"""
Результат заполнения словаря:
0.0530316
0.05793100000000001

Результат получения элемента:
0.0715275
0.07406480000000001

Исходя из полученных данных видно, что время выполнения операций почти идентичны, ввиду 
чего использовать нецелесообразно, кроме специфичной фунции move_to_end()
"""