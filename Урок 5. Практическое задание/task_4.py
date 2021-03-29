"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните операции, равные по смыслу, с каждым из объектов и сделайте замеры.
Опишите полученные результаты, сделайте выводы.

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях?
"""

from collections import OrderedDict
from timeit import timeit


def ordinary_dict_fill():
    ordinary_dict_test = dict()
    for i in range(10000):
        ordinary_dict_test[f"Number-{i}"] = i
    return ordinary_dict_test


def ordered_dict_fill():
    ordered_dict_test = dict()
    for i in range(10000):
        ordered_dict_test[f"Number-{i}"] = i
    return ordered_dict_test


def ordinary_dict_read(dict_arg):
    for k, v in dict_arg.items():
        t1, t2 = k, v


def ordered_dict_read(dict_arg):
    for k, v in dict_arg.items():
        t1, t2 = k, v


def ordinary_dict_pop(dict_arg):
    for i in range(1000):
        dict_arg.popitem()


def ordered_dict_pop(dict_arg):
    for i in range(1000):
        dict_arg.popitem()


functions = ['ordinary_dict_fill()',
             'ordered_dict_fill()',
             'ordinary_dict_read(ordinary_dict)',
             'ordered_dict_read(ordered_dict)']

functions_2 = ['ordinary_dict_pop(ordinary_dict)', 'ordered_dict_pop(ordered_dict)']

ordinary_dict = ordinary_dict_fill()
ordered_dict = ordered_dict_fill()

for item in functions:
    print(f"Функция {item}\t ---> {timeit(item, globals=globals(), number=10000)}")

for item in functions_2:
    print(f"Функция {item}\t ---> {timeit(item, globals=globals(), number=1)}")

'''
Нельзя сделать однозначый вывод что быстрее, но мне кажется что обчный словарь чуточку быстрее.
При заполнении незначительное преимущество у обычного словаря, при чтении разницы практически нет, при удалении быстрее
обчный словарь.

Функция ordinary_dict_fill()	 ---> 22.4594044
Функция ordered_dict_fill()	 ---> 22.690406899999996

Функция ordinary_dict_read(ordinary_dict)	 ---> 3.2631078000000002
Функция ordered_dict_read(ordered_dict)	 ---> 3.261617600000001

Функция ordinary_dict_pop(ordinary_dict)	 ---> 0.00011890000000391865
Функция ordered_dict_pop(ordered_dict)	 ---> 9.860000000116997e-05
'''