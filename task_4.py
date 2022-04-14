"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните операции с каждым их них (заполнение, получение элемента) и сделайте замеры.
Опишите полученные результаты, сделайте выводы.
И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях?
"""

import timeit
from collections import OrderedDict

usual_dict = {}
order_dict = OrderedDict()


def create_usual_dict():
    for i in range(100):
        usual_dict[i] = i + 1


def create_order_dict():
    for i in range(100):
        order_dict[i] = i + 1


def get_val_usual_dict():
    for i in range(100):
        v = usual_dict[i]
        return v


def get_val_order_dict():
    for i in range(100):
        v = order_dict[i]
        return v


def del_key_from_usual_dict():
    for i in range(100):
        usual_dict.pop(i, 0)


def del_key_from_order_dict():
    for i in range(100):
        order_dict.pop(i, 0)


print(f'Создание обычного словаря {timeit.timeit("create_usual_dict()", globals=globals(), number=1000)}')
print(f'Создание OrderedDict {timeit.timeit("create_order_dict()", globals=globals(), number=1000)}')
print(
    f'Получение значения по ключу в обычном словаре {timeit.timeit("get_val_usual_dict()", globals=globals(), number=1000)}')
print(
    f'Получение значения по ключу в OrderedDict {timeit.timeit("get_val_order_dict()", globals=globals(), number=1000)}')
print(f'Удаление в обычном словаре {timeit.timeit("del_key_from_usual_dict()", globals=globals(), number=1000)}')
print(f'Удаление в OrderedDict {timeit.timeit("del_key_from_order_dict()", globals=globals(), number=1000)}')

'''
Создание обычного словаря 0.0053092
Создание OrderedDict 0.00681770000000001
Получение значения по ключу в обычном словаре 0.00024180000000000035
Получение значения по ключу в OrderedDict 0.00023779999999999635
Удаление в обычном словаре 0.004922700000000002
Удаление в OrderedDict 0.010637899999999992

Большого преймущества по времени OrderedDict не дает
'''
