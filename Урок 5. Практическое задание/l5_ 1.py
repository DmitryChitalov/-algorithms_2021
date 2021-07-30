"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните операции, равные по смыслу, с каждым из объектов и сделайте замеры.
Опишите полученные результаты, сделайте выводы.

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях?
"""

from collections import OrderedDict
from time import time


def timer(func):
    def temporary(*args, **kwargs):
        start_time = time()
        result = func(*args, **kwargs)
        delta_time = time() - start_time
        print(f'Время выполнения функции {func.__name__} = {delta_time}')
        return result

    return temporary


ordered_dict = OrderedDict({i: i + i for i in range(10000)})
basic_dict = {i: i + i for i in range(10000)}


@timer
def ordered_fill():  # 0.007506847381591797

    return OrderedDict({i: i for i in range(10000)})


@timer
def basic_fill():  # 0.001001119613647461

    return {i: i for i in range(10000)}


@timer
def for_in_ordered():  # 0.002501964569091797
     for i, ii in ordered_dict.items():
         i, ii = ii, i


@timer
def for_in_basic():  # 0.0015022754669189453
     for i, ii in basic_dict.items():
         i, ii = ii, i


@timer
def ordered_pop():  # 0.0040035247802734375
    while len(ordered_dict) > 0:
        ordered_dict.popitem()


@timer
def basic_pop():  # 0.0030028820037841797
    while len(basic_dict) > 0:
        basic_dict.popitem()


for j in [ordered_fill(), basic_fill(), for_in_ordered(), for_in_basic(), ordered_pop(), basic_pop()]:
    j


'''Во всех замерах встроенный dict показывает лучшие результаты по скорости работы. 
На осоновании этого при работе в python версии 3.6+ необходимости в использовании этого модуля я не вижу.'''