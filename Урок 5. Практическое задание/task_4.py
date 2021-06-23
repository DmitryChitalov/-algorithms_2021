"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните операции с каждым их них (заполнение, получение элемента) и сделайте замеры.
Опишите полученные результаты, сделайте выводы.

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях?
"""
# Использовать OrderedDict не оптимально, когда мы заполняем словарь.
# Считаю, что в целях оптимизации и читабельности Orderdict не нужен, т.к. это не мувитон
# В случае получения элементов orderedDict показывает лучшй результат, но не всегда.
# Поэтому оценить сложно, но считаю, что без него лучше обходиться в версиях 3.6 и выше.
# Есть смысл использоваться в версиях 3.6 и раньше. Сейчас словари упорядоченны.
from collections import OrderedDict
from timeit import timeit

dict = {}
dict_2 = {}


def dict_filling():
    for el in range(1000):
        dict[el + 1] = el


dict_filling()


def Order_dict_filling_2():
    for el in range(1000):
        dict_2[el + 1] = el
    return OrderedDict(dict_2)


Order_dict_filling_2()


def get_el_dct():
    for k, v in dict.items():
        return k, v


get_el_dct()


def get_el_Order_dct():
    for k, v in dict_2.items():
        return OrderedDict(dict_2)


get_el_Order_dct()

print(timeit('dict_filling', globals=globals()))
print(timeit('Order_dict_filling_2', globals=globals()))
print('Элементы')
print(timeit('get_el_dct', globals=globals()))
print(timeit('get_el_Order_dct', globals=globals()))
