"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните операции с каждым их них (заполнение, получение элемента) и сделайте замеры.
Опишите полученные результаты, сделайте выводы.

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях?
"""
from collections import OrderedDict
from time import time
from timeit import timeit

my_dict = {}
my_ordereddict = OrderedDict()


def timer(func):
    def wrapped(*args):
        start = time()
        response = func(*args)
        print(f'Время выполнения функции {func.__name__}: {time() - start}')  #
        return response
    return wrapped


@timer
def filling_dict(dct):
    for i in (range(1000000)):
        dct[i] = i + 1


@timer
def filling_ordereddict(orddct):
    for i in (range(1000000)):
        orddct[i] = i + 1


def get_el_dict(dct):
    return dct[1]


def get_el_ordereddict(orddct):
    return orddct[1]


filling_dict(my_dict)
filling_ordereddict(my_ordereddict)
print(f'Получение элемента из dict занимает: '
      f'{timeit("get_el_dict(my_dict)", globals=globals(), number=1000000)}')
print(f'Получение элемента из OrderedDict занимает: '
      f'{timeit("get_el_ordereddict(my_ordereddict)", globals=globals(), number=1000000)}')

"""
Время выполнения функции filling_dict: 0.11410331726074219
Время выполнения функции filling_ordereddict: 0.1711561679840088
Получение элемента из dict занимает: 0.08189420000000003
Получение элемента из OrderedDict занимает: 0.08686779999999994

Вывод: Время заполнения OrderedDict занимает больше времени, чем заполнение dict. Времени на получение
элемента в OrderedDict также затрачивается больше, чем в dict.
Отсюда можно сделать вывод, что OrderedDict, начиная с Python 3.6 абсолютно не нужен.
"""
