"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните операции с каждым их них (заполнение, получение элемента) и сделайте замеры.
Опишите полученные результаты, сделайте выводы.

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях?
"""
from collections import OrderedDict
from timeit import timeit

dict_1 = {}
dict_2 = OrderedDict()
dict_1.keys()


def full_func(dic):
    for i in range(100):
        dic[i] = i


print("Заполнение словаря", timeit("full_func(dict_1)", globals=globals(), number=10000))
print("Заполнение упорядочного словаря", timeit("full_func(dict_2)", globals=globals(), number=10000))
"""Время заполнение больше у упорядочного словаря, чем у словаря исходя из замеров"""


def func_1(dic):
    dic.items()


def func_2(dic):
    dic.keys()


print("взятия элементов из словаря", timeit("func_1(dict_1)", globals=globals(), number=10000))
print("взятия элементов из упорядочного словаря", timeit("func_1(dict_2)", globals=globals(), number=10000))
print("взятия ключей словаря", timeit("func_2(dict_1)", globals=globals(), number=10000))
print("взятия ключей упорядочного словаря", timeit("func_2(dict_2)", globals=globals(), number=10000))
"""Время выполнение больше у упорядочного словаря, чем у словаря исходя из замеров"""

"""Вывод: упорядочные словари лудшее исполезовать в версии до 3.6 так как в позних версиях они тратят больше времени
и дают такие же результаты как и обычный словарь"""
