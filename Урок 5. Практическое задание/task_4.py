"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните операции с каждым их них (заполнение, получение элемента) и сделайте замеры.
Опишите полученные результаты, сделайте выводы.

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях?
"""
from timeit import timeit
from collections import OrderedDict
from random import randint

my_dict = {}
my_ordered_dict = OrderedDict()


def add_to_dict(num):
    """Заполнение словаря"""
    for i in range(num):
        my_dict[i] = i


def get_from_dict(num):
    """Получение данных из словаря"""
    for _ in range(num):
        my_dict.get(randint(0, num))


def add_to_ordered_dict(num):
    """Заполнение OrderedDict"""
    for i in range(num):
        my_ordered_dict[i] = i


def get_from_ordered_dict(num):
    """Получение данных из OrderedDict"""
    for _ in range(num):
        my_ordered_dict.get(randint(0, num))


print("Добавление.")
print('Dict -', timeit('add_to_dict(1000)', globals=globals(), number=10000))
print('OrderedDict -', timeit('add_to_ordered_dict(1000)', globals=globals(), number=10000))
# Dict - 0.7487140940011159
# OrderedDict - 1.0259235430003173

print("\nПолучение.")
print('Dict -', timeit('get_from_dict(1000)', globals=globals(), number=10000))
print('OrderedDict -', timeit('get_from_ordered_dict(1000)', globals=globals(), number=10000))
# Dict - 9.57046577500114
# OrderedDict - 9.536334204000013

# Добаление в обчный словарь работает быстрее, получение одинаково. Использование
# OrderedDict в python3.6+ не имеет смысла, т.к. словари теперь и без этого "помнят"
# порядок добавления элементов
