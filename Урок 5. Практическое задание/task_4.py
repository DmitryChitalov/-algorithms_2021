"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните операции, равные по смыслу, с каждым из объектов и сделайте замеры.
Опишите полученные результаты, сделайте выводы.

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях?
"""

import collections
from timeit import timeit
from random import random as rnd

def func_adding(dict):
    numbs = 10
    for i in range(numbs):
        dict[i+5] = (i + 5) * 100

def stepby_step(dict):
    i = 0
    for el in range(len(dict)):
        if el == 3:
            return el
        else:
            i += 1

def lst_app(dict):
    i = 0
    trash_ofwords = []
    while i != 3:
        trash_ofwords.append(dict[i+1])
        i += 1

newsys_dict = {1: "Cola", 2: "Fanta", 3: "Pepsi", 4: "Mirinda"}
newcoll_dict = collections.OrderedDict([(1, "Cola"), (2, "Fanta"), (3, "Pepsi"), (4, "Mirinda")])

print('func_adding Dict_syst: ', timeit('func_adding(newsys_dict)', globals=globals()))
print('func_adding Dict_from_collections: ', timeit('func_adding(newcoll_dict)', globals=globals()))

print('stepby_step Dict_syst: ', timeit('stepby_step(newsys_dict)', globals=globals()))
print('stepby_step Dict_from_collections:', timeit('stepby_step(newcoll_dict)', globals=globals()))

print('lst_app Dict_syst: ', timeit('lst_app(newsys_dict)', globals=globals()))
print('lst_app Dict_from_collections:', timeit('lst_app(newcoll_dict)', globals=globals()))

"""
Вывод:
Смысл использовать OrderedDict нет, т.к. его использование в различных операциях приводит только к увеличению
времени. Детали прилагаю ниже:
func_adding Dict_syst:  2.7178188000000003
func_adding Dict_from_collections:  3.0195561 (больше времени на OrderedDict)

stepby_step Dict_syst:  0.8822035000000001  
stepby_step Dict_from_collections: 0.9726827 (больше времени на OrderedDict)

lst_app Dict_syst:  1.0247609999999998
lst_app Dict_from_collections: 1.1124889000000007 (больше времени на OrderedDict)
"""