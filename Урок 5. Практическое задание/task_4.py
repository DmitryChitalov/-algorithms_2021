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


def timer(func):
    def wrapped(*args):
        start = time()
        response = func(*args)
        print(f'Время выполнения функции {func.__name__}: {time() - start}')  #
        return response
    return wrapped


@timer
def fill_dict(d):               # заполнение обычного словаря
    for i in (range(1000000)):
        d[i] = f'el{i}'


@timer
def fill_ordereddict(od):       # заполнение OrderedDict
    for i in (range(1000000)):
        od[i] = f'el{i}'


def get_elem_dict(d):           # доступ к элементу словаря
    return d[100]


def get_elem_ordereddict(od):   # доступ к элементу OrderedDict
    return od[100]


test_dict = {}                          # заполнение обычного словаря
test_ordereddict = OrderedDict()        # заполнение OrderedDict

fill_dict(test_dict)                    # доступ к элементу словаря
fill_ordereddict(test_ordereddict)      # доступ к элементу OrderedDict

print('Замер получения элемента из dict',
      timeit("get_elem_dict(test_dict)", globals=globals(), number=1000000))
print('Замер получения элемента из Ordereddict',
      timeit("get_elem_ordereddict(test_ordereddict)", globals=globals(), number=1000000))

"""
время заполнения OrderedDict всегда немного дольше
> Время выполнения функции fill_dict: 0.24184560775756836
> Время выполнения функции fill_ordereddict: 0.3088095188140869

а вот время доступа к элементам одинаковое и для обычного словаря и для OrderedDict
> Замер получения элемента из dict 0.15848090000000004
> Замер получения элемента из Ordereddict 0.16571350000000007

смысла использовать OrderedDict в Python 3.6 и более поздних версиях нет
"""

