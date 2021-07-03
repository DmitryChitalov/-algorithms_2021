"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните операции с каждым их них (заполнение, получение элемента) и сделайте замеры.
Опишите полученные результаты, сделайте выводы.

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях?
"""
from collections import OrderedDict
from timeit import timeit

n = 10000


def fill_dict():
    return {elems: elems for elems in range(n)}


def fill_ord_dict():
    return OrderedDict([(elems, elems) for elems in range(n)])


def get_dict(dct):
    for i in dct:
        dct[i] += 1
    return dct


def get_ord_dict(dct):
    for i in dct:
        dct[i] += 1
    return dct


my_dict = fill_dict()
my_ord_dict = fill_ord_dict()
print('fill_dict     ', timeit('fill_dict()', globals=globals(), number=1000))
print('fill_ord_dict ', timeit('fill_ord_dict()', globals=globals(), number=1000))
print('get_dict      ', timeit('get_dict(my_dict)', globals=globals(), number=1000))
print('get_ord_dict  ', timeit('get_ord_dict(my_ord_dict)', globals=globals(), number=1000))
print('')

# Заполнение элементов dict происходит почти на половину чем OrderedDict.
# Получение элементов (изменение элементов) не такая серьезная, но все равно в пользу dict.
# Смысла использовать OrderedDict я не вижу. Кстати, почитал https://realpython.com/python-ordereddict/.
# Но переваривать еще то не успел (
