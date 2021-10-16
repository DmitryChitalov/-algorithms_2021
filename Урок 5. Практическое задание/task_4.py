"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните операции с каждым их них (заполнение, получение элемента) и сделайте замеры.
Опишите полученные результаты, сделайте выводы.

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях?
"""

from timeit import timeit

from collections import OrderedDict

dict_object = {1: 'one', 2: 'two', 3: 'three'}

ordered_dict_object = OrderedDict(dict_object)

print(type(dict_object))


def dict_in():
    for i in range(4, 7):
        dict_object[i] = chr(93 + i)

    return dict_object


def ordered_dict_in():
    for i in range(4, 7):
        ordered_dict_object[i] = chr(93 + i)

    return ordered_dict_object


def dict_get():
    dict_object.get(3)

    return dict_object


def ordered_dict_get():
    ordered_dict_object.get(3)

    return ordered_dict_object


print(

    timeit(

        "dict_in()",

        setup="from __main__ import dict_in", number=100000))

print(

    timeit(

        "ordered_dict_in()",

        setup="from __main__ import ordered_dict_in", number=100000))

print(

    timeit(

        "dict_get()",

        setup="from __main__ import dict_get", number=100000))

print(

    timeit(

        "ordered_dict_get()",

        setup="from __main__ import ordered_dict_get", number=100000))

'''

Для 100 000 повторов:



Заполнение:

dict_in - 0.050970569999662985

ordered_dict_in - 0.055511458000182756



Получение элемента:

dict_get - 0.010101898999892

ordered_dict_get - 0.009758303000126034



Тип данных OrderedDict после Python3.6 перестал быть полезным при выводе данных, 
так как время обработки примерно одинаковое
'''
