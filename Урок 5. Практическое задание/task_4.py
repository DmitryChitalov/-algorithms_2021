"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните операции с каждым их них (заполнение, получение элемента) и сделайте замеры.
Опишите полученные результаты, сделайте выводы.

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях?
"""

from timeit import timeit
from collections import OrderedDict


test_dict = {}
test_ordered_dict = OrderedDict()


# заполнение
def fill_dict(elem_count):
    for i in range(elem_count):
        test_dict[i] = None


def fill_ordered_dict(elem_count):
    for i in range(elem_count):
        test_ordered_dict[i] = None


print(f'Заполнение dict '
      f'{timeit("fill_dict(100000)", globals=globals(), number=100)}')
print(f'Заполнение ordered dict '
      f'{timeit("fill_ordered_dict(100000)", globals=globals(), number=100)}')
"""
Заполнение dict 0.9275087
Заполнение ordered dict 1.3303311
"""


# получение элементов
def get_dict_elem():
    for i in range(len(test_dict)):
        test_dict[i]


def get_ordered_dict_elem():
    for i in range(len(test_ordered_dict)):
        test_ordered_dict[i]


print(f'Получение элементов dict '
      f'{timeit("get_dict_elem()", globals=globals(), number=100)}')
print(f'Получение элементов ordered dict '
      f'{timeit("get_ordered_dict_elem()", globals=globals(), number=100)}')
"""
Получение элементов dict 0.6967209000000003
Получение элементов ordered dict 0.7478993999999997
"""


# копирование
print(f'Копирование dict '
      f'{timeit("test_dict.copy()", globals=globals(), number=100)}')
print(f'Копирование ordered dict '
      f'{timeit("test_ordered_dict.copy()", globals=globals(), number=100)}')
"""
Копирование dict 0.2725316999999996
Копирование ordered dict 1.7976627
"""


# Извлечение элемента
def del_from_dict():
    for i in range(len(test_dict)):
        test_dict.popitem()


def del_from_ordered_dict():
    for i in range(len(test_ordered_dict)):
        test_ordered_dict.popitem()


print(f'Извлечение элемента dict '
      f'{timeit("del_from_dict()", globals=globals(), number=100)}')
print(f'Извлечение элемента ordered dict '
      f'{timeit("del_from_ordered_dict()", globals=globals(), number=100)}')
"""
Извлечение элемента dict 0.00944889999999976
Извлечение элемента ordered dict 0.018336699999999873
"""

"""
Согласно замерам OrderedDict работает медленнее обычного.
Так как в python 3.6 и далее обычный словарь запоминает
порядок добавления элементов, использование упорядоченного словаря
не имеет смысла.
"""
