"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните операции с каждым их них (заполнение, получение элемента) и сделайте замеры.
Опишите полученные результаты, сделайте выводы.

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях?
"""
# Смысла нет, т.к. чтобы создать OrderedDict нужно создать словарь, потом потратить время на превращение его
# в OrderedDict. Получение элемента будет дольше, потому что это не быстрое получение из словаря, а по сути
# получение из списка отсортированных кортежей (ключ, значение)

from random import randint
from timeit import timeit
from collections import OrderedDict


def dict_filling(dct):
    for i in range(1000):
        dct[i] = randint(1, 5000)
    return dct


def ord_dict_filling(dct):
    o_dct = OrderedDict(dct.items())
    return o_dct



def get_rand_from_dict(dct):
    for i in range(1000):
        res = dct[randint(0, 999)]


def get_rand_from_ord_dict(o_dct):
    for i in range(1000):
        res = o_dct[randint(0, 999)]


dct = {}
o_dct = {}
dct = dict_filling(dct)
print(dct)
o_dct = ord_dict_filling(dct)
print(o_dct)

print('Заполнение словаря/упорядоченного словаря')
print(timeit("dict_filling(dct)", globals=globals(), number=100))
print(timeit("ord_dict_filling(o_dct)", globals=globals(), number=100))
print('Получение элемента по индексу из словаря/упорядоченного словаря')
print(timeit("get_rand_from_dict(dct)", globals=globals(), number=1000))
print(timeit("get_rand_from_ord_dict", globals=globals(), number=1000))
