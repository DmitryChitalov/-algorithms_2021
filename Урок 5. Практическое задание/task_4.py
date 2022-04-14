"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните операции с каждым их них (заполнение, получение элемента) и сделайте замеры.
Опишите полученные результаты, сделайте выводы.

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях?
"""
from collections import OrderedDict
from timeit import timeit


def fill_dict():
    dct = {}
    for num, x in enumerate(range(1, 1000)):
        dct[num] = x
    return dct


def fill_orderdict():
    DCT = OrderedDict()
    for num, x in enumerate(range(1, 1000)):
        DCT[num] = x
    return DCT


def iterr_dict(dct):
    for items in dct.items():
        items = None
        # print(items, end=' ')


def iterr_orderdict(OrderDCT):
    for items in OrderDCT.items():
        items = None
        # print(items, end=' ')


dct = fill_dict()
OrderDCT = OrderedDict(dct)


def get_el_dict(dct):
    for i in range(1, 100):
        x = None
        x = dct.get(i)


def get_el_orderdict(OrderDCT):
    for i in range(1, 100):
        x = None
        x = OrderDCT.get(i)


print(timeit("fill_dict()", globals=globals(), number=100000))
print(timeit("fill_orderdict()", globals=globals(), number=100000))
print(timeit("iterr_dict(dct)", globals=globals(), number=100000))
print(timeit("iterr_orderdict(OrderDCT)", globals=globals(), number=100000))
print(timeit("get_el_dict(dct)", globals=globals(), number=100000))
print(timeit("get_el_orderdict(OrderDCT)", globals=globals(), number=100000))

"""
Результат:
    15.762021275 - Наполнение dict
    23.553963458000002 - Наполнение OrderDict
    3.5196729640000015 - Итеррация dict
    8.431687082000003 - Итеррация OrderDict
    0.9456608700000046 - Получение эл-ов dict
    0.9664383940000008 - Получение эл-ов OrderDict
    
Вывод: Наполнение современного словаря происходит быстре на порядки, чем OrderDict
обход словаря тоже быстрее, чем OrderDict - более чем в 2 раза. Изъятие эл-ов с одинаковой
скоростью, это объясняется тем, что оба словаря в результате идентичные хеш-таблицы. Я думаю
смысла в использовании OrderDict нет, кроме тех случаев, если кто-то использует старые версии
Python.
"""