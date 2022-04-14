"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните операции с каждым их них (заполнение, получение элемента) и сделайте замеры.
Опишите полученные результаты, сделайте выводы.

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях?
"""

import timeit
from collections import OrderedDict


def fill_dict(dct, n):
    for i in range(n):
        dct[i] = i


def fill_ordered_dict(odct, n):
    for i in range(n):
        odct[i] = i


def dict_pop(dct):
    for i in range(10000):
        dct.pop(i)


def ordered_dict_pop(odct):
    for i in range(10000):
        odct.pop(i)


def dict_change(dct):
    for i in range(10001, 20002):
        dct[i] = 'new'


def ordered_dict_change(odct):
    for j in range(10001, 20002):
        odct[j] = 'new'


def dict_items(dct):
    for k, v in dct.items():
        dct[k] = 'yet new'


def ordered_dict_items(odct):
    for k, v in odct.items():
        odct[k] = 'yet new'


dct = {}
odct = OrderedDict()
n = 10 ** 5


stmt = ["fill_dict(dct, n)",
        "fill_ordered_dict(odct, n)",
        "dict_pop(dct)",
        "ordered_dict_pop(odct)",
        "dict_change(dct)",
        "ordered_dict_change(odct)",
        "dict_items(dct)",
        "ordered_dict_items(odct)"]

for st in stmt:
    print(f'на выполение функции {st} затрачено времени: '
          f'{timeit.timeit(st, number=1, globals=globals())}')


"""
на выполение функции fill_dict(dct, n) затрачено времени: 0.008063500000000001
на выполение функции fill_ordered_dict(odct, n) затрачено времени: 0.013666800000000003
на выполение функции dict_pop(dct) затрачено времени: 0.0008254999999999998
на выполение функции ordered_dict_pop(odct) затрачено времени: 0.0016499999999999987
на выполение функции dict_change(dct) затрачено времени: 0.0004036999999999999
на выполение функции ordered_dict_change(odct) затрачено времени: 0.0006760999999999989
на выполение функции dict_items(dct) затрачено времени: 0.0037587999999999996
на выполение функции ordered_dict_items(odct) затрачено времени: 0.007573000000000003

Словарь заполняется быстрее чем ordered_dict в связи с тем, что ordered_dict был разработан прежде всего для быстрого
упорядочивания его элементов, а словарь реализован с упором на быстродействие. 
Кроме того словарь работает быстре и при изменении или удалении элементов все по тем же причинам. 
В настоящее время использование ordered_dict обосновано только для вызова функций move_to_end и popitem
"""


