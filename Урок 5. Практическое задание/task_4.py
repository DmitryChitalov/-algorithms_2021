"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните операции с каждым их них (заполнение, получение элемента) и сделайте замеры.
Опишите полученные результаты, сделайте выводы.

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях?
"""
from collections import OrderedDict
from timeit import timeit


def init_dict():
    return {num: num ** 3 for num in range(100)}


def init_ord_dict():
    return OrderedDict({num: num ** 3 for num in range(100)})


my_dict = init_dict()
my_od = init_ord_dict()


print(timeit("init_dict()", globals=globals(), number=100000))          # 3.3131313
print(timeit("init_ord_dict()", globals=globals(), number=100000))      # 5.4199205
print(timeit("my_dict[101] = 104060401", globals=globals()))            # 0.05477829999999926
print(timeit("my_od[101] = 104060401", globals=globals()))              # 0.088980100000000526
print(timeit("my_dict.get(95)", globals=globals()))                     # 0.072171900000000484
print(timeit("my_od.get(95)", globals=globals()))                       # 0.075835199999999965

# Согласно замерам, collection-тип OrderedDict не иммет преимуществ перед типом Dictionary
# Поэтому не вижу смысла использовать OrderedDict в последних версиях Python
