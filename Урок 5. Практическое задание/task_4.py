"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните операции, равные по смыслу, с каждым из объектов и сделайте замеры.
Опишите полученные результаты, сделайте выводы.

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях?
"""
from collections import OrderedDict
from timeit import timeit


def dictionary_1():
    return {i: i for i in range(10000)}


def ordered_dict_1():
    return OrderedDict([(i, i) for i in range(10000)])

test_dict = dictionary_1()
test_or_dict = ordered_dict_1()

print('Создание словарей:')
print(f'Dictionary: {timeit("dictionary_1()", globals=globals(), number=1000)}')
print(f'Ordered Dictionary: {timeit("ordered_dict_1()", globals=globals(), number=1000)} \n')

print('Взятие значений:')
print(f'Dictionary: {timeit("test_dict.values", globals=globals(), number=1000)}')
print(f'Ordered Dictionary: {timeit("test_or_dict.values", globals=globals(), number=1000)} \n')

print('Взятие ключей:')
print(f'Dictionary: {timeit("test_dict.keys", globals=globals(), number=1000)}')
print(f'Ordered Dictionary: {timeit("test_or_dict.keys", globals=globals(), number=1000)} \n')

# Создание обычного славаря значительно быстрее, чем создание ordered dictionary.
# У обычного словаря взятия ключа и значения происходит немного быстрее (незначительно).
# Получается, что OrderedDict не нужен в Python 3.6 и более поздних версиях.