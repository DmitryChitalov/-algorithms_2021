"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните операции с каждым их них (заполнение, получение элемента) и сделайте замеры.
Опишите полученные результаты, сделайте выводы.

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях?
"""
from collections import OrderedDict
from timeit import timeit


def fill_dic():
    """Заполнение словаря"""
    dic1 = {i: 2 * i for i in range(10000)}
    return dic1


def fill_ord_dic():
    """Заполнение объекта OrderedDict"""
    or_dic1 = OrderedDict([(i, 2 * i) for i in range(10000)])
    return or_dic1


def add_el_d(dic):
    """Добавление объекта в словарь"""
    dic[10001] = 20002
    return dic


def add_el_od(o_dic):
    """Добавление объекта в OrderedDict"""
    o_dic[10001] = 20002
    return o_dic


def rep_val_d(dic):
    """Замена значения в словаре"""
    dic[777] = 1
    return dic


def rep_val_od(o_dic):
    """Замена значения в OrderedDict"""
    o_dic[777] = 1
    return o_dic


print('Заполнение (словарь, OrderedDict)')
print(timeit('fill_dic()', globals=globals(), number=1000))
print(timeit('fill_ord_dic()', globals=globals(), number=1000))

d1 = fill_dic()
od1 = fill_ord_dic()

print('Добавление (словарь, OrderedDict)')
print(timeit('add_el_d(d1)', globals=globals(), number=1000))
print(timeit('add_el_od(od1)', globals=globals(), number=1000))

print('Замена значения (словарь, OrderedDict)')
print(timeit('rep_val_d(d1)', globals=globals(), number=1000))
print(timeit('rep_val_od(od1)', globals=globals(), number=1000))

"""
Замеры показывают, что аналогичные операции с элементами словаря и объекта 
OrderDict приблизительно одинаково затратны по времени  и при условии упорядоченного
словаря dict, использование OrderedDict возможно если необходимо возпользоваться 
уникальными методами типа 'move_to_end', 'popitem'. 


Заполнение (словарь, OrderDict)
1.536605
2.9915497
Добавление (словарь, OrderDict)
9.760000000014202e-05
0.00011609999999961929
Замена значения (словарь, OrderDict)
0.00010650000000023141
0.0001351000000004987

"""

