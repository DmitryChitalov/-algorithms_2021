"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните операции с каждым их них (заполнение, получение элемента) и сделайте замеры.
Опишите полученные результаты, сделайте выводы.

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях?
"""
from collections import OrderedDict
from timeit import timeit


dt = {}
odt = OrderedDict([])


def fill_1(dt: dict):
    for i in range(1000):
        dt[i] = i


def fill_2(odt: OrderedDict):
    for i in range(1000):
        odt[i] = i


def get_el1(dt: dict, el):
    return dt.get(el)


def get_el2(odt: OrderedDict, el):
    return odt.get(el)


def pop_1(dt: dict):
    return dt.popitem()


def pop_2(odt: OrderedDict):
    return odt.popitem()


print('Заполнение:')
print(timeit('fill_1(dt)', globals=globals(), number=1000))
print(timeit('fill_2(odt)', globals=globals(), number=1000))
print('Получение элемента:')
print(timeit('get_el1(dt, 1)', globals=globals(), number=1000))
print(timeit('get_el2(odt, 1)', globals=globals(), number=1000))
print('Выброс элемента:')
print(timeit('pop_1(dt)', globals=globals(), number=1000))
print(timeit('pop_2(odt)', globals=globals(), number=1000))

'''
Основные операции выполняются примерно одинаково, у OrderedDict чуть медленнее, смысл использовать OrderedDict 
в новых версиях языка есть только если нужно подвигать элементы с помощью movetoend   
'''