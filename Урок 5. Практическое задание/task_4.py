"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните операции с каждым их них (заполнение, получение элемента) и сделайте замеры.
Опишите полученные результаты, сделайте выводы.

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях?
"""

from collections import OrderedDict
from timeit import timeit


def filling_orderdict():
    DCT = OrderedDict()
    for num, x in enumerate(range(1, 1000)):
        DCT[num] = x
    return DCT


def filling_dict():
    dct = {}
    for num, x in enumerate(range(1, 1000)):
        dct[num] = x
    return dct


def iter_orderdict(OrderDCT):
    for i in OrderDCT.items():
        pass


def iter_dict(dct):
    for i in dct.items():
        pass


dct = filling_dict()
OrderDCT = OrderedDict(dct)


def get_orderdict(OrderDCT):
    for i in range(1, 100):
        x = None
        x = OrderDCT.get(i)


def get_dict(dct):
    for i in range(1, 100):
        x = None
        x = dct.get(i)


print('Заполнение orderdict', timeit("filling_orderdict()", globals=globals(), number=100000))
print('Заполнение dict', timeit("filling_dict()", globals=globals(), number=100000))

print('Итерация orderdict', timeit("iter_orderdict(OrderDCT)", globals=globals(), number=100000))
print('Итерация dict', timeit("iter_dict(dct)", globals=globals(), number=100000))

print('Взятие элемента orderdict', timeit("get_orderdict(OrderDCT)", globals=globals(), number=100000))
print('Взятие элемента dict', timeit("get_dict(dct)", globals=globals(), number=100000))

# Вывод: Заполнение простого словаря происходит быстрее более чем на 25% чем OrderDict
# Итерация по обычному словарю быстрее в несколько раз, чем OrderDict - более чем в 2 раза.
# Взятие элементов происходит практически за одно время.
# Смысла в использовании OrderDict нет на современных версиях Python выеш 3.6 нет
# Я думаю, что разработчики правильно сделали, что теперь в словаре элементы выдаются упорядочено.
