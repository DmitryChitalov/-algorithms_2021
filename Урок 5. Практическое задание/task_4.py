"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните операции с каждым их них (заполнение, получение элемента) и сделайте замеры.
Опишите полученные результаты, сделайте выводы.

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях?
"""
import collections
from timeit import timeit

a = {}
b = collections.OrderedDict()


def add_to_dict(elements, dct):
    for elem in range(elements):
        dct[elem] = elem
    return dct


def add_to_ordered_dict(elements, dct):
    for elem in range(elements):
        dct[elem] = elem
    return dct


print(add_to_dict(10, a))
print(add_to_ordered_dict(10, b))


def get_elem(index, dct):
    return dct[index]


def get_elem_from_ordered_dict(index, dct):
    return dct[index]


print(get_elem(3, a))
print(get_elem_from_ordered_dict(6, b))

print(f'Время выполнения add_to_dict: {timeit("add_to_dict(10, a)", globals=globals())}')
print(f'Время выполнения add_to_ordered_dict: {timeit("add_to_ordered_dict(10, b)", globals=globals())}')
print(f'Время выполнения get_elem: {timeit("get_elem(3, a)", globals=globals())}')
print(f'Время выполнения get_elem_from_ordered_dict: {timeit("get_elem_from_ordered_dict(6, b)", globals=globals())}')
'''
Время выполнения add_to_dict: 0.640962038
Время выполнения add_to_ordered_dict: 0.740036397
Время выполнения get_elem: 0.11334399700000009
Время выполнения get_elem_from_ordered_dict: 0.12055770300000002
Выводы:
Операции с OrderedDict показали отсутствие выигрыша во времени, связано это с тем, что упорядоченный словарь создавался 
для запоминания порядка элементов и сейчас, так как в версиях Python выше 3.6 обычный словарь автоматически поддерживает
данную функцию, оказался не нужен.
'''
