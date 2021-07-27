"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните операции, равные по смыслу, с каждым из объектов и сделайте замеры.
Опишите полученные результаты, сделайте выводы.

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях?
"""

# пишу скрипт на версии Python 3.9
from collections import OrderedDict
from timeit import timeit
from random import randint

my_dict = {}
my_ord_dict = OrderedDict()


def dict_app():
    for i in range(1000):
        my_dict[i] = i


print(f"Время заполнения dict: {timeit('dict_app', globals=globals(), number=100000000)}")


def ord_dict_app():
    for i in range(1000):
        my_ord_dict[i] = i


print(f"Время заполнения OrderedDict: {timeit('ord_dict_app', globals=globals(), number=100000000)}")

# print(my_dict)
# print(my_ord_dict) # для проверки упорядоченности
# По итогам замеров OrderedDict заполнфется медленнее обычного словаря
# Время заполнения dict: 1.7218425
# Время заполнения OrderedDict: 1.8257187
# Также, как dict так и OrderedDict имеют упорядоченность

def pop_dict():
    for i in range(1000):
        my_dict.pop(i)


def pop_ord_dict():
    for i in range(1000):
        my_ord_dict.pop(i)


print(f"Время удаления последнего элемента в  dict: {timeit('pop_dict', globals=globals(), number=100000000)}")
print(f"Время удаления последнего элемента в  OrderedDict: {timeit('pop_ord_dict', globals=globals(), number=100000000)}")

# Удаление случайного элемента OrderedDict также производит медленнее обычногословаря
# Время удаления последнего элемента в  dict: 1.6456664000000005
# Время удаления последнего элемента в  OrderedDict: 2.0602934

# Мой вывод: для версий Python, в которых dict уже имеет упорядоченность, OrderedDict не имеет пользы
