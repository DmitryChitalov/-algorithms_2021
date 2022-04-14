"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните операции с каждым их них (заполнение, получение элемента) и сделайте замеры.
Опишите полученные результаты, сделайте выводы.

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях?
"""

from collections import OrderedDict
from timeit import timeit

my_dict = {}
ordered_dict = OrderedDict()


def fill_dict():
    for i in range(1, 101):
        my_dict[i] = i
    return my_dict


fill_dict()


def fill_ord_dict():
    for i in range(1, 101):
        ordered_dict[i] = i
    return ordered_dict


fill_ord_dict()

print("Время заполнения обчыного словаря:", timeit("fill_dict()", globals=globals(), number=10000), "сек")
print("Время заполнения OrderedDict", timeit("fill_ord_dict()", globals=globals(), number=10000), "сек")
print("Время получения элемента у обычного словаря:", timeit("my_dict[80]", globals=globals(), number=1000000), "сек")
print("Время получения элемента у OrderedDict:", timeit("ordered_dict[80]", globals=globals(), number=1000000), "сек")


"""
Время заполнения обчыного словаря: 0.09837211700000001 сек
Время заполнения OrderedDict 0.11620740699999998 сек
Время получения элемента у обычного словаря: 0.08281355699999998 сек
Время получения элемента у OrderedDict: 0.08066180300000003 сек

Полуечение элементов занимает примерно одинаковое время.
Заполнение у обычного словаря чуть быстрее.
В версии Python 3.6 и выше использовать OrderedDict нет смысла, так как порядок ключей у обычных словарей также
соблюдается.
"""