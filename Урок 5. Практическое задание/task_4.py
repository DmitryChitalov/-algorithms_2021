"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните операции с каждым их них (заполнение, получение элемента) и сделайте замеры.
Опишите полученные результаты, сделайте выводы.

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях?
"""
from collections import OrderedDict
from timeit import timeit

my_dict = dict((int(n), int(n)) for n in range(100000))
my_order_dict = OrderedDict(dict((int(n), int(n)) for n in range(100000)))

print(
    timeit(
        "dict((int(n), int(n)) for n in range(1000000))",
        globals=globals(),
        number=10))

print(
    timeit(
        "OrderedDict(dict((int(n), int(n)) for n in range(1000000)))",
        globals=globals(),
        number=10))

print(
    timeit(
        "my_dict[999]",
        globals=globals(),
        number=1000))

print(
    timeit(
        "my_order_dict[999]",
        globals=globals(),
        number=1000))

'''
2.5532546
4.7805632
4.7000000000352316e-05
4.830000000044521e-05

Заполнение словаря быстрее без OrderDict
Получение элемента почти одинаково
Начиная с версии python 3.7 порядок ввода в словаре сохранялся
Так что не имеет смысла
'''