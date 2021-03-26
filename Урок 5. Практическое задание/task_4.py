"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните операции, равные по смыслу, с каждым из объектов и сделайте замеры.
Опишите полученные результаты, сделайте выводы.

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях?
"""

from collections import OrderedDict
from timeit import timeit


def chek_time(f):
    return timeit(f"{f}", globals=globals(), number=100000)


t_dct = {i: i for i in range(10000)}
t_ord_dct = OrderedDict((i, i) for i in range(10000))

print("Возвращаем пары Dict:", chek_time("t_dct.items()"))
print("Возвращаем пары OrderedDict:", chek_time("t_ord_dct.items()"))
print("Возвращаем значение ключа Dict:", chek_time("t_dct.get(0)"))
print("Возвращаем значение ключа OrderedDict:", chek_time("t_ord_dct.get(0)"))
print("Возвращаем все значения Dict:", chek_time("t_dct.values()"))
print("Возвращаем все значения OrderedDict:", chek_time("t_ord_dct.values()"))

"""
Аналитика:
Нет отличий в скорости работы Dict и OrderDict.
Смысла использования OrderDict, также нет.
"""
