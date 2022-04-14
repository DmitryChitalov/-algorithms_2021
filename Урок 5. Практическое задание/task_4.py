"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните операции с каждым их них (заполнение, получение элемента) и сделайте замеры.
Опишите полученные результаты, сделайте выводы.

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях?
"""
import timeit
from collections import OrderedDict

dct = OrderedDict([('a', 1), ('s', 2)])


def orderedict_append(el):
    for i in range(el):
        dct[f'{i}']= i + i


def orderedict_get():
    for i in dct.keys():
        yield dct[i]


d = {'banana': 3, 'apple': 4, 'pear': 1, 'orange': 2}


def dct_append(el):
    for i in range(el):
        d[f'i']= i + i


def dct_get():
    for i in d.keys():
        yield d[i]


function_list = ['orderedict_append(el)', 'orderedict_get()', 'dct_append(el)', 'dct_get()']

el = 10
for i in function_list:
    print(i, min(timeit.repeat(i, globals=globals(), number=(10**5))))


""" Вывод: OrderedDict заполняется в разы медленнее чемобчный словарь, скорость получение элемента
равна скорости обычного словаря, поэтому я не вижу смысла в OrderedDict, если не пользоватся методами
popitem(last=True) или move_to_end(key, last=False)
"""