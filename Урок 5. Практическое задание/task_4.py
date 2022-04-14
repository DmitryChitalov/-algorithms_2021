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


def ord_dict_filling(my_str):
    my_dict = OrderedDict()
    for e in my_str:
        my_dict[e] = my_str.count(e)
    return my_dict


def dict_filling(my_str):
    my_dict = {}
    for e in my_str:
        my_dict[e] = my_str.count(e)
    return my_dict


def ord_dict_getting(my_dict, i):
    return my_dict.get(i)


def dict_getting(my_dict, i):
    return my_dict.get(i)


if __name__ == '__main__':
    data = 'Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the ' \
           'industry standard dummy text ever since the 1500s, when an unknown printer took a galley of type and ' \
           'scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap ' \
           'into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the ' \
           'release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing ' \
           'software like Aldus PageMaker including versions of Lorem Ipsum. '
    data_upd = "".join(data.split())
    print(timeit('ord_dict_filling(data_upd)', globals=globals()))  # 187.30054389999998
    print(timeit('dict_filling(data_upd)', globals=globals()))  # 180.83236259999998
    ord_dict = ord_dict_filling(data_upd)
    com_dict = dict_filling(data_upd)
    print(timeit('ord_dict_getting(ord_dict, data_upd[randint(0, len(data_upd) - 1)])', globals=globals()))  #
    # 0.7450680999999999
    print(timeit('dict_getting(com_dict, data_upd[randint(0, len(data_upd) - 1)])', globals=globals()))  # 0.7393128

#  Вывод. Ни в скорости заполнения Ordereddict, ни в получении элемента по ключу - существенного выигрыша нет.
# Использовать данный функционал в Python свежих версий нет никакого смысла
