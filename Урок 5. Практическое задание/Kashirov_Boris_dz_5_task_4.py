"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните операции с каждым их них (заполнение, получение элемента) и сделайте замеры.
Опишите полученные результаты, сделайте выводы.

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях?
"""

import collections
from time import perf_counter_ns


def my_timer(callback):
    """Функция секундомер, для подсказки"""
    def my_tmp(*args, **kwargs):
        start = perf_counter_ns()
        res = callback(*args, **kwargs)
        func_name = str(callback).split(' ')[1]
        print(f'Время выполнения функции "{func_name}":', f'{(perf_counter_ns() - start)/(10**6):.03f}', 'мс')
        return res
    return my_tmp


VALUE_STR = 'abcdefghijklmnopqrstuvwxyz' * 2


@my_timer
def set_default_py_3():
    my_dict = {}
    for i in range(len(VALUE_STR)):
        my_dict[i] = VALUE_STR[i:i+1]
    return my_dict


@my_timer
def set_order_dict():
    my_list = []
    for i in range(len(VALUE_STR)):
        my_list.append((i, VALUE_STR[i:i+1]))
    my_dict = collections.OrderedDict(my_list)
    return my_dict


@my_timer
def read_default_py_3(dd_dict):
    my_list = []
    for key, val in dd_dict.items():
        my_list.append([key, val])
    return dd_dict


@my_timer
def read_order_dict(od_dict):
    my_list = []
    for key, val in od_dict.items():
        my_list.append([key, val])
    return od_dict


my_default_dict = set_default_py_3()
my_order_dict = set_order_dict()

rand_val_dd = read_default_py_3(my_default_dict)
rand_val_od = read_order_dict(my_order_dict)

# Через timeit
# set_default_dict:  13.720376700000001 -> timeit
# set_order_dict:  26.634752899999995   -> timeit


# Через мой декоратор с основ
# Время выполнения функции "set_default_py_3": 0.030 мс
# Время выполнения функции "set_order_dict": 0.058 мс
# Время выполнения функции "read_default_py_3": 0.020 мс
# Время выполнения функции "read_order_dict": 0.020 мс


# Вывод: создание OrderDict требует большего времени чем сосдание DefaultDict
# Работа с данными проходит (через @my_timer) примерно в одинакове время
