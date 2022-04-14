"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните операции с каждым их них (заполнение, получение элемента) и сделайте замеры.
Опишите полученные результаты, сделайте выводы.

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях?
"""

# По замерам (заполнение, получение элемента) словаря можно понять, что обычный словарь в версиях 3.6 справляется лучше.
# Следовательно OrderedDict нерентабелен.


import collections
from timeit import timeit


def dic_1_1():

    dic = {}
    for i in range(5):
        dic.update({i: i + 1})

    return dic.items()


def dic_1_2():

    def_dict = collections.defaultdict(list)
    for i in range(5):
        def_dict[i].append(i)

    return def_dict.items()


def dic_2():

    order_dict = collections.OrderedDict()
    for i in range(5):
        order_dict.update({i: i + 1})

    return order_dict.items()


print(
    timeit(
        "dic_1_1()",
        globals=globals()
        ))
print(
    timeit(
        "dic_1_2()",
        globals=globals()
        ))
print(
    timeit(
        "dic_2()",
        globals=globals()
        ))