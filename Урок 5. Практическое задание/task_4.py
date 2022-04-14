"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните операции с каждым их них (заполнение, получение элемента) и сделайте замеры.
Опишите полученные результаты, сделайте выводы.

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях?
"""

from collections import OrderedDict
from timeit import timeit


def pull_usual_dict():
    usual_dict = {}
    for i in range(10000):
        usual_dict[i] = i
    return usual_dict

def pull_order_dict():
    order_dict = OrderedDict()
    for i in range(10000):
        order_dict[i] = i
    return order_dict

def get_item_us_dict(usual_dict, n):
    return usual_dict[n]

def get_item_order_dict(order_dict, n):
    return order_dict[n]


usual_dict = pull_usual_dict()
order_dict = pull_order_dict()
n = 100

print(timeit("pull_usual_dict()", globals=globals(),number=10000))
print(timeit("pull_order_dict()", globals=globals(),number=10000))
print('-' * 30)
print(timeit("get_item_us_dict(usual_dict, n)", globals=globals(),number=10000))
print(timeit("get_item_order_dict(order_dict, n)", globals=globals(),number=10000))
"""
Можем видеть, что время заполнения сильно отличается и обычный словарь быстрее Ordereddict, однако 
на получение элемента уходит одинаковое время.
Так как в версиях Python новее 3.6 обычный словарь и так запоминает порядок ключей, использование
OrderedDict считаю не целесообразным.
"""

