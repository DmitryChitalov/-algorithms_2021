"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните операции с каждым их них (заполнение, получение элемента) и сделайте замеры.
Опишите полученные результаты, сделайте выводы.
И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях?
"""
from collections import OrderedDict
from timeit import timeit

numbers_ord_dict = OrderedDict(one=1, two=2, three=3)
numbers_dict = {'one': 1, 'two': 2, 'three': 3}


def dict_func_iter(dict_1):
    for key in dict_1:
        # print(key, " ", dict[key])
        return dict_1

    # for key, value in dict_1.items():
    #     print(key, " ", value)
    #
    # for value in dict_1.values():
    #     print(value)


dict_func_iter(numbers_ord_dict)
dict_func_iter(numbers_dict)

print(
    timeit(
        "dict_func_iter(numbers_ord_dict)",
        setup='from __main__ import dict_func_iter, numbers_ord_dict',
        number=10000))

print(
    timeit(
        "dict_func_iter(numbers_dict)",
        setup='from __main__ import dict_func_iter, numbers_dict',
        number=10000))

#  итерации в OrderedDict выполняются дольше, чем в обычном, поэтому смысла в использовании OrderedDict, но
#  возможностей взаимодействия с OrderedDict я как понял больше, например с версии 3.8+ есть возможность сделать
#  reversed и move_to_end.
