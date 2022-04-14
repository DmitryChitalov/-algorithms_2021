"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните операции с каждым их них (заполнение, получение элемента) и сделайте замеры.
Опишите полученные результаты, сделайте выводы.

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях?
"""
from collections import OrderedDict
from timeit import timeit

simple_dict = {}
order_dict = OrderedDict()


def dict_fill():
    for i in range(50):
        simple_dict[i] = i ** 2


def order_fill():
    for i in range(50):
        order_dict[i] = i ** 2


def get_key_dict():
    for i in range(50):
        _ = simple_dict[i]


def get_key_order():
    for i in range(50):
        _ = order_dict[i]


def del_key_from_dict():
    for i in range(50):
        simple_dict.pop(i, 0)


def del_key_order():
    for i in range(50):
        order_dict.pop(i, 0)


print('dict_fill: ', timeit('dict_fill()', globals=globals(), number=1000))
print('order_fill: ', timeit('order_fill()', globals=globals(), number=1000))
print('get_key_dict: ', timeit('get_key_dict()', globals=globals(), number=1000))
print('get_key_order: ', timeit('get_key_order()', globals=globals(), number=1000))
print('del_key_from_dict: ', timeit('del_key_from_dict()', globals=globals(), number=1000))
print('del_key_order: ', timeit('del_key_order()', globals=globals(), number=1000))

"""
dict_fill:  0.027492399999999986
order_fill:  0.02722280000000002
get_key_dict:  0.004505999999999982
get_key_order:  0.004928899999999986
del_key_from_dict:  0.007514899999999991
del_key_order:  0.01351819999999998
Смысла использования OrderDict нет, поскольку он не дает преимуществ по времени, а на данный момент 
базовые словари тоже запоминают порядок ключей.
"""
