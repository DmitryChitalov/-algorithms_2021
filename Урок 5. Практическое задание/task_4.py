"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните операции с каждым их них (заполнение, получение элемента) и сделайте замеры.
Опишите полученные результаты, сделайте выводы.

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях?
"""

from collections import OrderedDict
from timeit import timeit


simple_dict = dict()
order_dict = OrderedDict(simple_dict)

"""
согласно документации, у OrderedDict есть функции,
не доступные обычному словарю - move_to_end и popitem
Замерим разницу между обычным удалением по ключу и popitem
"""


def filling_dict(my_dict, num):
    for i in range(num):
        my_dict[i] = i
    return my_dict


def filling_od_dict(od_dict, num):
    for i in range(num):
        od_dict.update({i: i})


def del_el_dict(my_dict, num):
    for i in range(num):
        my_dict.pop(i, None)


def del_el_od_dict(od_dict, num):
    for i in range(num):
        od_dict.popitem(last=False)


print(timeit('filling_dict(simple_dict, 100)', globals=globals(), number=10000))  # 0.0718354299897328
print(timeit('filling_od_dict(order_dict, 100)', globals=globals(), number=10000))  # 0.3662117039784789
filling_od_dict(order_dict, 1000000)
print(timeit('del_el_dict(simple_dict, 100)', globals=globals(), number=10000))  # 0.053893076023086905
print(timeit('del_el_od_dict(order_dict, 100)', globals=globals(), number=10000))  # 0.19878526800312102

"""
из замеров видно, что OrderedDict работает медленнее
Его единственное преимущество - move_to_end, позволяющая менять местоположение елементов (изменять порядок)
и popitem - возможность удалять элементы не по индексу, а сначала или с конца (как deque для списка)
"""
