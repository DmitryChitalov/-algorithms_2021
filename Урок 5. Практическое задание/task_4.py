"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните операции с каждым их них (заполнение, получение элемента) и сделайте замеры.
Опишите полученные результаты, сделайте выводы.

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях?
"""
from collections import OrderedDict
from timeit import timeit

dct = {}
ordct = {}

# Простое заполнение словаря


def first_filling():
    for i in range(322):
        dct[i+1] = i
    return dct


first_filling()

print(timeit("first_filling", globals=globals()))


def second_filling():
    for j in range(420):
        ordct[j+1] = j
    return OrderedDict(ordct)


second_filling()

print(timeit("second_filling", globals=globals()))


def first_el_get(dct1):
    for k, v in dct1.items():
        return k, v


first_el_get(dct)

print(timeit("first_el_get", globals=globals()))


def second_el_get(dct2):
    for k, v in dct2.items():
        return OrderedDict(k)


second_el_get(ordct)

print(timeit("second_el_get", globals=globals()))
# По замерам можно понять что ordereddict работает медленнее,
# смысла в его использовании нет, так как в python после версии 3.6 все словари стали упорядочеными

