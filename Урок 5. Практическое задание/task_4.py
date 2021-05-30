"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните операции с каждым их них (заполнение, получение элемента) и сделайте замеры.
Опишите полученные результаты, сделайте выводы.

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях?
"""

from collections import OrderedDict
from random import randint
from timeit import timeit

some_dict = {}
some_ord_dict = OrderedDict()


def dict_fill(dict_obj):
    """Заполняет обычный словарь"""

    for el in range(100000):
        dict_obj[el] = randint(100, 200)
    return dict_obj


def ord_dict_fill(ord_dict_obj):
    """Заполняет OrderedDict"""

    for el in range(100000):
        ord_dict_obj[el] = randint(100, 200)
    return ord_dict_obj


def dict_change(dict_obj):
    """Удаляет и добавляет по 1000 элементов в обычном словаре"""
    for i in range(1000):
        dict_obj.pop(i)
    for j in range(1000):
        dict_obj[j] = randint(100, 200)
    return dict_obj

def ord_dict_change(ord_dict_obj):
    """Удаляет и добавляет по 1000 элементов в OrderedDict"""
    for i in range(1000):
        ord_dict_obj.pop(i)
    for j in range(1000):
        ord_dict_obj[j] = randint(100, 200)
    return ord_dict_obj

if __name__ == '__main__':
    # Измеряем скорость заполнения обычного словарря и OrderedDict
    print(f'Время заполнения обычного словаря: '
          f'{timeit("dict_fill(some_dict)", globals=globals(), number=10)}')
    print(f'Время заполнения OrderedDict: '
          f'{timeit("ord_dict_fill(some_ord_dict)", globals=globals(), number=10)}')
    """
    OrderdDict заполняется медленнее обычного словаря
    """
    print('=' * 100)

    # Измеряем скорость изменения обычного словаря и OrderedDict
    print(f'Время изменения обычного словаря: '
          f'{timeit("dict_change(dict_fill(some_dict))", globals=globals(), number=10)}')
    print(f'Время изменения OrderedDict: '
          f'{timeit("ord_dict_change(ord_dict_fill(some_ord_dict))", globals=globals(), number=10)}')

    """
    Обычный словарь изменяется быстрее OrderedDict.
    Ввиду того что с версии 3.6 и выше обычный словарь Python
    запоминает порядок добавления элементов, использование OrderedDict нецелесообразно.
    """

