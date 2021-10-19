"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните операции с каждым их них (заполнение, получение элемента) и сделайте замеры.
Опишите полученные результаты, сделайте выводы.

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях?
"""

from collections import OrderedDict
from timeit import timeit


def gen_dict():
    data = {}
    for i in range(10000):
        data[i] = i
    return data


def gen_ordereddict():
    data = OrderedDict()
    for i in range(10000):
        data[i] = i
    return data


def get_item_dict(data: dict, count: int):
    return data[count]


def get_item_ordereddict(data: OrderedDict, count: int):
    return data[count]


my_dict = gen_dict()
my_ordereddict = gen_ordereddict()
count = 100

print(timeit("gen_dict()", globals=globals(), number=10000))
print(timeit("gen_ordereddict()", globals=globals(), number=10000))
print('-' * 80)
print(
    timeit("get_item_dict(my_dict, count)", globals=globals(), number=10000))
print(timeit("get_item_ordereddict(my_ordereddict, count)", globals=globals(),
             number=10000))
"""
6.690288209
10.953491973999999
--------------------------------------------------------------------------------
0.0011894109999985858
0.0012368530000017586

Заполнение словаря быстрее в стандартном словаре,
а на взятие элемента вообще одинаковое время.

Так как начиная с Python 3.6 обычный словарь тоже запоминает порядок ключей,
использование OrderedDict уже не имеет смысла.
"""