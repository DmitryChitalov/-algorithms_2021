"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните операции, равные по смыслу, с каждым из объектов и сделайте замеры.
Опишите полученные результаты, сделайте выводы.

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях?
"""

from timeit import timeit
from collections import OrderedDict
from random import random


test_dict = {}
test_ordered_dict = OrderedDict()


def fill_dict(value=1000001):
    for i in range(value):
        test_dict[f'{i}'] = i
    return test_dict


def fill_ordered_dict(value=1000001):
    for i in range(value):
        test_ordered_dict[f'{i}'] = i
    return test_ordered_dict


def get_keys(some_dict):
    return some_dict.keys()


def get_value(some_dict, key=f'{round(random() * 1000000)}'):
    return some_dict.get(key)


def pop_item(some_dict):
    return some_dict.popitem()


fill_dict()
fill_ordered_dict()

dict_functions = ['fill_dict',
                  'get_keys(test_dict)',
                  'get_value(test_dict)',
                  'pop_item(test_dict)']

ordered_dict_functions = ['fill_ordered_dict',
                          'get_keys(test_ordered_dict)',
                          'get_value(test_ordered_dict)',
                          'pop_item(test_ordered_dict)']

for d in dict_functions:
    print(f'{d}', round(timeit(f'{d}', globals=globals()), 4), 'sec')

print('\n')

for d in ordered_dict_functions:
    print(f'{d}', round(timeit(f'{d}', globals=globals()), 4), 'sec')


# fill_dict 0.0401 sec                        fill_ordered_dict 0.0383 sec
# get_keys(test_dict) 0.3123 sec              get_keys(test_ordered_dict) 0.2995 sec
# get_value(test_dict) 0.3653 sec             get_value(test_ordered_dict) 0.3626 sec
# pop_item(test_dict) 0.5256 sec              pop_item(test_ordered_dict) 0.6714 sec

# В целом результаты не слишком сильно расходятся для распространненных операций
# Там, где не важен порядок добавления значений в словарь, стоит использовать обычный словарь

# У OrderedDict есть метод move_to_end(), которого нет в обычном словаре. Также есть возможность удалять и
# извлекать пары ключ-значения из начала, а не конца словаря. Поэтому есть смысл использовать OrderedDict под
# специфичные задачи
