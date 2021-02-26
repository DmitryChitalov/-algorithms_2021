"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните операции, равные по смыслу, с каждым из объектов и сделайте замеры.
Опишите полученные результаты, сделайте выводы.

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях?
"""

import collections
import timeit

count = 100000


def fill_dict():
    return {i: i + 1 for i in range(count)}


def fill_ordered_dict():
    return collections.OrderedDict([(i, i + 2) for i in range(count)])


simple_dict = fill_dict()
ordered_dict = fill_ordered_dict()


def dict_get(d):
    for i in range(count):
        c = d[i]


def ordered_dict_get(o_d):
    for i in range(count):
        c = o_d[i]


def dict_pop(d: dict):
    for i in range(count):
        d.pop(i)


def ordered_dict_pop(o_d):
    for i in range(count):
        o_d.popitem(last=False)


t1 = timeit.Timer('fill_dict()', 'from __main__ import fill_dict', globals=globals())
print("fill_dict work time", t1.timeit(number=1000), "milliseconds")

t2 = timeit.Timer('fill_ordered_dict()', 'from __main__ import fill_ordered_dict',
                  globals=globals())
print("fill_ordered_dict work time", t2.timeit(number=1000), "milliseconds")

"""
заполнение обычного словаря происходит гораздо быстрее
fill_dict work time 6.940686220000089 milliseconds
fill_ordered_dict work time 20.39261167099994 milliseconds
"""


t1 = timeit.Timer('dict_get(simple_dict)', 'from __main__ import dict_get, simple_dict', globals=globals())
print("dict_get work time", t1.timeit(number=1000), "milliseconds")

t2 = timeit.Timer('ordered_dict_get(ordered_dict)', 'from __main__ import ordered_dict_get, ordered_dict',
                  globals=globals())
print("ordered_dict_get work time", t2.timeit(number=1000), "milliseconds")

"""
Получение данных происходимт примерно одинаково
dict_get work time 4.23479701600013 milliseconds
ordered_dict_get work time 4.226552025999808 milliseconds
"""

t1 = timeit.Timer('dict_pop(simple_dict)', 'from __main__ import dict_pop, simple_dict', globals=globals())
print("dict_pop work time", t1.timeit(number=1), "milliseconds")

t2 = timeit.Timer('ordered_dict_pop(ordered_dict)', 'from __main__ import ordered_dict_pop, ordered_dict',
                  globals=globals())
print("ordered_dict_pop work time", t2.timeit(number=1), "milliseconds")


"""
удаление документов тоже в обычном словаре работает быстрее
dict_pop work time 0.00713484600009906 milliseconds
ordered_dict_pop work time 0.01312002799977563 milliseconds



Итого, смысла использовать упорядоченный словарь нет, т.е. в Python 3.6 и более поздних версиях словарь итак помнит 
порядок добавления элементов
"""

