"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните операции с каждым их них (заполнение, получение элемента) и сделайте замеры.
Опишите полученные результаты, сделайте выводы.

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях?
"""
from collections import OrderedDict
from timeit import timeit


def create_dict():
    return {str(i): i for i in range(1000)}


def create_ordered_dict():
    return OrderedDict({str(i): i for i in range(1000)})


test1 = create_dict()
test2 = create_ordered_dict()

print('Just_dict: ' + str(timeit("create_dict()", globals=globals(), number=10000)))
print('Ordered_dict: ' + str(timeit("create_ordered_dict()", globals=globals(), number=10000)))
#  Создание словарей через OrderedDict в два раза дольше

print('Just_dict: ' + str(timeit("test1.popitem", globals=globals(), number=10000)))
print('Ordered_dict: ' + str(timeit("test2.popitem", globals=globals(), number=10000)))
#  Удаление из словарей пары, в конце практически одинаково, но в обычном словаре быстрее
#  В Python 3.6 и более поздних версиях мало смысла использовать OrderedDict
