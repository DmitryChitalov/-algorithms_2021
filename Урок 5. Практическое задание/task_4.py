"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните операции с каждым их них (заполнение, получение элемента) и сделайте замеры.
Опишите полученные результаты, сделайте выводы.

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях?
"""

from timeit import timeit
from collections import OrderedDict


def fill_dict(count_el):
    return {i: i for i in range(count_el)}


def fill_order(count_el):
    return OrderedDict({i: i for i in range(count_el)})


def get_dict(simple_dict):
    return simple_dict.get(len(simple_dict) / 2)


def get_order(order_dict):
    return order_dict.get(len(order_dict) / 2)


n = 10000
my_dict = fill_dict(10)
my_order = fill_order(10)

print(f"Заполнение словаря: {timeit('fill_dict(10)', globals=globals(), number=n)}")
print(f"Заполнение OrderedDict: {timeit('fill_order(10)', globals=globals(), number=n)}")

print(f"Получение элемента словаря: {timeit('get_dict(my_dict)', globals=globals(), number=n)}")
print(f"полуение элемента OrderedDict: {timeit('get_order(my_order)', globals=globals(), number=n)}")

'''
В вкрсиях Python 3.6 и более поздних словари запоминают расположение элементов и применение OrderedDict теряет смысл, 
тем более что время на заполнение у OrderedDict примерно в 2 раза болье чем у простого словаря.
'''
