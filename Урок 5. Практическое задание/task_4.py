"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните операции с каждым их них (заполнение, получение элемента) и сделайте замеры.
Опишите полученные результаты, сделайте выводы.

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях?
"""

from collections import OrderedDict
from timeit import timeit


def fill_dict(cnt):
    return {i: i for i in range(cnt)}


def fill_o_dict(cnt):
    return OrderedDict([(i, i) for i in range(cnt)])


def add_to_dict(dct: dict, key_, value_):
    dct[key_] = value_
    return dct


def add_to_o_dict(dct: OrderedDict, key_, value_):
    dct[key_] = value_
    return dct


def get_from_dict_1(dct: dict, key_):
    return dct.get(key_)


def get_from_dict_2(dct: dict, key_):
    return dct[key_]


def get_from_o_dict_1(dct: OrderedDict, key_):
    return dct.get(key_)


def get_from_o_dict_2(dct: OrderedDict, key_):
    return dct[key_]


my_dict = fill_dict(10)
my_o_dict = fill_o_dict(10)

ELEM_FOR_ADD = 'new'

print('Work demonstration:')
print(f'Dict: {my_dict}')
print(f'Add to dict: {add_to_dict(my_dict, ELEM_FOR_ADD, ELEM_FOR_ADD)}')
print(f'Get from dict (dict.get(key)): {get_from_dict_1(my_dict, ELEM_FOR_ADD)}')
print(f'Get from dict (dict[key]): {get_from_dict_2(my_dict, ELEM_FOR_ADD)}')

print(f'OrderedDict: {my_o_dict}')
print(f'Add to o_dict: {add_to_o_dict(my_o_dict, ELEM_FOR_ADD, ELEM_FOR_ADD)}')
print(f'Get from o_dict (o_dict[key]): {get_from_o_dict_1(my_o_dict, ELEM_FOR_ADD)}')
print(f'Get from o_dict (o_dict[key]): {get_from_o_dict_2(my_o_dict, ELEM_FOR_ADD)}')

print('Timing:')

print(f'fill_dict(1000):   {timeit("fill_dict(1000)", globals=globals(), number=1000)}')
print(f'fill_o_dict(1000): {timeit("fill_o_dict(1000)", globals=globals(), number=1000)}')

print(f'add_to_dict(my_dict, elem_for_add, elem_for_add):      '
      f'{timeit("add_to_dict(my_dict, elem_for_add, elem_for_add)", globals=globals(), number=1000)}')
print(f'add_to_o_dict(my_o_dict, elem_for_add, elem_for_add):  '
      f'{timeit("add_to_o_dict(my_o_dict, elem_for_add, elem_for_add)", globals=globals(), number=1000)}')

print(f'get_from_dict_1(my_dict, elem_for_add):   '
      f'{timeit("get_from_dict_1(my_dict, elem_for_add)", globals=globals(), number=1000)}')
print(f'get_from_o_dict_1(my_dict, elem_for_add): '
      f'{timeit("get_from_o_dict_1(my_dict, elem_for_add)", globals=globals(), number=1000)}')

print(f'get_from_dict_2(my_dict, elem_for_add):   '
      f'{timeit("get_from_dict_2(my_dict, elem_for_add)", globals=globals(), number=1000)}')
print(f'get_from_o_dict_2(my_dict, elem_for_add): '
      f'{timeit("get_from_o_dict_2(my_dict, elem_for_add)", globals=globals(), number=1000)}')

"""
Timing:
fill_dict(1000):   0.15971562099999997  # Заполнение быстрее у dict
fill_o_dict(1000): 0.403062992
add_to_dict(my_dict, ELEM_FOR_ADD, ELEM_FOR_ADD):      0.00032472299999997123  # Добавление немного быстрее у dict
add_to_o_dict(my_o_dict, ELEM_FOR_ADD, ELEM_FOR_ADD):  0.00038948599999999445
get_from_dict_1(my_dict, ELEM_FOR_ADD):   0.00035552000000005357    # Извлечение очень близко по скорости
get_from_o_dict_1(my_dict, ELEM_FOR_ADD): 0.00033966799999995967
get_from_dict_2(my_dict, ELEM_FOR_ADD):   0.00026584699999998573
get_from_o_dict_2(my_dict, ELEM_FOR_ADD): 0.0002653940000000299

Смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях есть ради совместимости с более старыми версиями
без ущерба в скорости
"""
