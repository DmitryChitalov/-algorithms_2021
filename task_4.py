"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните операции с каждым их них (заполнение, получение элемента) и сделайте замеры.
Опишите полученные результаты, сделайте выводы.

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях?
"""


import collections
import timeit


def push_orderdict():
    for el in range(10001):
        test_orderdict[el] = el


def get_orderdict():
    for el in range(10001):
        test_orderdict.get(el)


def push_dict():
    for el in range(10001):
        test_dict[el] = el


def get_dict():
    for el in range(10001):
        test_dict.get(el)


# При заполнении OrderedDict медленнее: 1.3896696 против 1.0497835000000002.
# При получении эллемента разницы нет.
# Смысла использловать OrderedDict на Python 3.6+ нет.


if __name__ == '__main__':
    test_orderdict = collections.OrderedDict()
    test_dict = {}
    print(timeit.timeit('push_orderdict()', globals=globals(), number=1000))
    print(timeit.timeit('push_dict()', globals=globals(), number=1000))
    print(timeit.timeit('get_orderdict()', globals=globals(), number=1000))
    print(timeit.timeit('get_dict()', globals=globals(), number=1000))
