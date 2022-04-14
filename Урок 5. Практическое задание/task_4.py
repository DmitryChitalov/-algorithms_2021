"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните операции с каждым их них (заполнение, получение элемента) и сделайте замеры.
Опишите полученные результаты, сделайте выводы.

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях?
"""

from timeit import timeit
from collections import OrderedDict, deque


def get_time(func_lst):
    for el in func_lst:
        print(f'Выремя выполнения функции {el}: {timeit(el, globals=globals(), number=10000)}')


# заполняем
data_ordereddict = OrderedDict({f"{el}": el for el in range(100)})
data_dict = {f"{el}": el for el in range(100)}


#  добавляем
def update_elem_orderdict():
    data_ordereddict.update({f"{el}": el for el in range(150)})


def update_elem_dict():
    data_dict.update({f"{el}": el for el in range(150)})


#  изменяем значение в цикле с условием
def get_el_orderdict():
    for key, el in data_ordereddict.items():
        if el % 2 == 0:
            data_ordereddict[key] = -el


def get_el_dict():
    for key, el in data_dict.items():
        if el % 2 == 0:
            data_dict[key] = -el


# Делаем реверс
def reverce_ordereddict():
    result = OrderedDict()
    for i in range(len(data_ordereddict) - 1):
        result.update({data_ordereddict.popitem()})
    return result


def reverce_dict():
    result = {}
    for i in range(len(data_dict) - 1):
        result.update({data_dict.popitem()})
    return result


str_for_timeit = ['data_ordereddict', 'data_dict', 'update_elem_orderdict()', 'update_elem_dict()',
                  'get_el_orderdict()', 'get_el_dict()', 'reverce_ordereddict()', 'reverce_dict()']

get_time(str_for_timeit)


"""
Результаты: 
Выремя выполнения функции data_ordereddict: 0.0001257000000000029
Выремя выполнения функции data_dict: 0.00012559999999999655
Выремя выполнения функции update_elem_orderdict(): 0.3184555
Выремя выполнения функции update_elem_dict(): 0.19829590000000002
Выремя выполнения функции get_el_orderdict(): 0.15055209999999997
Выремя выполнения функции get_el_dict(): 0.09237200000000001
Выремя выполнения функции reverce_ordereddict(): 0.002845099999999934
Выремя выполнения функции reverce_dict(): 0.002123800000000009

Стандартный словарь устойчиво демонстрирует более быструю работу.
Применять  ordereddict бессмысленно.
"""