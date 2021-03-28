"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните операции, равные по смыслу, с каждым из объектов и сделайте замеры.
Опишите полученные результаты, сделайте выводы.

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях?
"""

from collections import OrderedDict
from timeit import timeit

COUNT = 1000


def create_dict(n, mode=None):
    if mode == 'ordered':
        tp = [(i, i) for i in range(n + 1)]
        return OrderedDict(tp)
    else:
        return {i: i for i in range(n + 1)}


def get_key(dt):
    return dt.get(COUNT)


def pop_key(dt):
    for row in range(len(dt)):
        dt.pop(row)


def simple_key(dt):
    for row in range(len(dt)):
        dt[row]


order_dt = create_dict(COUNT, 'ordered')
dt = create_dict(COUNT)

print('Стандартный словарь: ')
print(timeit('get_key(dt)', globals=globals()))
print(timeit('pop_key(dt)', globals=globals()))
print(timeit('simple_key(dt)', globals=globals()))
print('OrderedDict: ')
print(timeit('get_key(order_dt)', globals=globals()))
print(timeit('pop_key(order_dt)', globals=globals()))
print(timeit('simple_key(order_dt)', globals=globals()))

"""
Результаты прыгают и однозначного победителя нет. Исходя из этого, могу предположить, что сильных различий между ними нет.
Для более точных вычислений необходима изолированная машина, но критических различий все равно не будет.
Вывод: использовать можно, однако на производительности не скажется и будет являтся личным делом вкуса.
"""
