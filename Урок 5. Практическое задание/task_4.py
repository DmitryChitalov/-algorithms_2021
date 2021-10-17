"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните операции с каждым их них (заполнение, получение элемента) и сделайте замеры.
Опишите полученные результаты, сделайте выводы.

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях?
"""
from collections import OrderedDict
from timeit import timeit

dict_simp = dict()
dict_order = OrderedDict()

print(timeit(stmt="for i in range(100): dict_simp[i]=i", globals=globals()))
print(timeit(stmt="for i in range(100): dict_order[i]=i", globals=globals()))

print(timeit(stmt="dict_simp[10]", globals=globals()))
print(timeit(stmt="dict_order[10]", globals=globals()))

'''
5.9231307
8.796454699999998
0.044851599999999436
0.06697029999999948
'''
# Начиная с версии Python 3.6, словарь запоминает порядок заполнения по умолчанию,
# поэтому использовать OrderdDict не имеет особого смысла.