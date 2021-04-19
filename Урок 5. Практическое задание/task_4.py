"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните операции, равные по смыслу, с каждым из объектов и сделайте замеры.
Опишите полученные результаты, сделайте выводы.

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях?
"""

# Полезная документация:
# https://docs.python.org/3/library/collections.html#collections.OrderedDict

from timeit import repeat, default_timer

OrderedDict_import_code = "from collections import OrderedDict"

dict_create_code = "d = dict.fromkeys('BCDEFGHIJKLMNOPQRSTUVWXY')"
OrderedDict_create_code = "o = OrderedDict.fromkeys('BCDEFGHIJKLMNOPQRSTUVWXY')"


def get_dict_create_code(length=pow(10, 4)):
    return f'd = dict.fromkeys([item for item in range({length})])'


def get_ordered_dict_create_code(length=pow(10, 4)):
    return f'o = OrderedDict.fromkeys([item for item in range({length})])'


dict_setup = dict_create_code
OrderedDict_setup = f'{OrderedDict_import_code}\n{OrderedDict_create_code}'


def get_dict_setup(length):
    return get_dict_create_code(length)


def get_ordered_dict_setup(length):
    return f'{OrderedDict_import_code}\n{get_ordered_dict_create_code(length)}'


repeat_number = pow(10, 5)
print(f'1. make a new OrderedDict {repeat_number} times')

print('dict')
# [0.10278680000000001, 0.099834, 0.09878739999999997]
print(repeat(dict_create_code, "", default_timer, 3, repeat_number))
print('OrderedDict')
# [0.18607449999999998, 0.22278530000000007, 0.2241419]
print(repeat(OrderedDict_create_code, OrderedDict_import_code, default_timer, 3, pow(10, 5)))

print('OrderedDict')
# [0.2058701999999999, 0.19478989999999996, 0.19370310000000002]
print(repeat(OrderedDict_create_code, OrderedDict_import_code, default_timer, 3, pow(10, 5)))
print('dict')
# [0.0959038000000001, 0.09804170000000001, 0.09838860000000005]
print(repeat(dict_create_code, "", default_timer, 3, pow(10, 5)))

print()

# создание OrderedDict из списка ключей занимает в два раза больше времени
# OrderedDict медленнее dict

repeat_number = pow(10, 5)
print(f'2. ["key"] = "value". add a new value {repeat_number} times')

print('dict')
# [0.002918500000000046, 0.0027026000000001105, 0.0030159999999999076]
print(repeat("d['Z'] = 'Z'", dict_setup, default_timer, 3, repeat_number))
print('OrderedDict')
# [0.004037100000000127, 0.003958499999999976, 0.004081099999999838]
print(repeat("o['Z'] = 'Z'", OrderedDict_setup, default_timer, 3, repeat_number))

print()

# изменение элемента в OrderedDict занимает на 25% дольше, чем в dict
# OrderedDict медленнее dict

repeat_number = pow(10, 4)
print(f'3. del. deleting elements {repeat_number} times')

print('dict')
# [0.5052783999999999, 0.5051160000000001, 0.5118465000000003]
print(repeat("for key in list(d):\n\tdel d[key]", get_dict_setup(repeat_number), default_timer, 3,
             repeat_number))
print('OrderedDict')
# [0.0006184000000000189, 0.0006186000000001357, 0.000617899999999949]
print(repeat("for key in list(o):\n\tdel o[key]", get_ordered_dict_setup(repeat_number), default_timer, 3,
             repeat_number))

print()

# удаление элемента из OrderedDict занимает разы меньше времени чем из dict
# OrderedDict быстрее dict

# Вывод: если нужно часто делать создание, добавление, изменение - то лучше подойдет dict
# если нужно часто удалять - то лучше подойдет OrderedDict
