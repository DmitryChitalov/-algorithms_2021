"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните операции, равные по смыслу, с каждым из объектов и сделайте замеры.
Опишите полученные результаты, сделайте выводы.

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях?
"""

""" использование OrderedDict в версиях Python 3.6 и более поздних
не имеет смысла, так как с данных версий словари "помнят" порядок добавления элементов"""

from timeit import timeit
from collections import OrderedDict


dictionary_list = {}
ordered_dict_list = OrderedDict({})
number_cycles = 100000
number_fill = 1000


def fill_dictionary():    # заполнение словаря
    dictionary_list = {i: i * i for i in range(number_fill)}
    return dictionary_list


def fill_ordered_dict():    # заполнение словаря OrderedDict
    ordered_dict_list = {i: i * i for i in range(number_fill)}
    return ordered_dict_list


def search_key_1():    # ищем значение по ключу в словаре
    dictionary_list.get(1)
    return dictionary_list


def search_key_2():    # ищем значение по ключу в словаре (OrderedDict)
    ordered_dict_list.get(1)
    return ordered_dict_list


print(f'Заполнение словаря: '
      f'{timeit("fill_dictionary()", globals=globals(), number=number_cycles)}')    # 17.25505430001067
print(f'Заполнение словаря (OrderedDict): '
      f'{timeit("fill_ordered_dict()", globals=globals(), number=number_cycles)}')    # 17.333831499970984
print(f'Поиск значение по ключу в словаре: '
      f'{timeit("search_key_1()", globals=globals(), number=number_cycles)}')    # 0.021217100031208247
print(f'Поиск значение по ключу в словаре (OrderedDict): '
      f'{timeit("search_key_2()", globals=globals(), number=number_cycles)}')    # 0.023529099998995662


"""Время работы, в данном случае, ориентировочно равно (иногда OrderedDict даже меленнее), 
следовательно использование OrderedDict в Python вресии 3,6 и выше 
нейцелесообразно (ибо это там уже есть по-умолчанию)"""
