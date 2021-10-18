"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните операции с каждым их них (заполнение, получение элемента) и сделайте замеры.
Опишите полученные результаты, сделайте выводы.

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях?
"""

from collections import OrderedDict
from timeit import timeit

dict_x = dict()
dict_y = OrderedDict()


print(timeit(stmt="for i in range(100): dict_x[i]=i", globals=globals()))
print(timeit(stmt="for i in range(100): dict_y[i]=i", globals=globals()))


print(timeit(stmt="dict_x[10]", globals=globals()))
print(timeit(stmt="dict_y[10]", globals=globals()))

# После версии python 3.6 словарь по умолчанию запоминает порядок заполнения.
# Поэтому использовать OrderdDict нет необходимости.
