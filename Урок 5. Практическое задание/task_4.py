"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните операции с каждым их них (заполнение, получение элемента) и сделайте замеры.
Опишите полученные результаты, сделайте выводы.

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях?
"""
from collections import OrderedDict
from timeit import timeit
from random import randint

my_dict = {}
ord_dict = OrderedDict( )


def dict_fill():
    for i in range(10000):
        my_dict[str(i)] = i
    return my_dict


def ord_dict_fill():
    for i in range(10000):
        ord_dict[str(i)] = i
    return ord_dict


print('Заполнение словарей')
print(timeit('dict_fill()', globals=globals( ), number=1000))
print(timeit('ord_dict_fill()', globals=globals( ), number=1000))
"""
Заполнение обычного словаря осуществляется быстрее.
"""


def get_el_dct():
    return my_dict[str(randint(0, 9999))]


def get_el_ord_dct():
    return ord_dict[str(randint(0, 9999))]


print('Получение элемента по ключу')
print(timeit('get_el_dct()', globals=globals( )))
print(timeit('get_el_ord_dct()', globals=globals( )))
"""
Получение элемента по ключу осуществляется с одинаковой скоростью.
"""


def pop_from_dct():
    my_dict.pop('100')
    my_dict.pop('101')
    my_dict.pop('105')
    my_dict.pop('106')

    return my_dict


def pop_from_ord_dct():
    ord_dict.pop('100')
    ord_dict.pop('101')
    ord_dict.pop('105')
    ord_dict.pop('106')

    return ord_dict


print('Удаление элемента по ключу')
print(timeit('pop_from_dct()', globals=globals( ), number=1))
print(timeit('pop_from_ord_dct()', globals=globals( ), number=1))
"""
Удаление элемента выполяется быстрее при использовании OrderedDict
"""

"""
Можно сделать следующие выводы: 
начиная с 3.6, использование OrderedDict непосредственно для работы с порядком добавления ключей потеряло свой смысл,
так как dict теперь запоминает порядок заполнения.
Однако OrderedDict имеет преимущества при работе с операциями, которые требуют реорганизации порядка элементов словаря,
а также поддерживает несколько дополнительных методов.
"""