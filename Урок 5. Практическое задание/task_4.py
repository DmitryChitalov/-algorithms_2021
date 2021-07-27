"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните операции с каждым их них (заполнение, получение элемента) и сделайте замеры.
Опишите полученные результаты, сделайте выводы.

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях?
"""

from timeit import timeit
from collections import OrderedDict

new_dict = dict(a=1, b=2, c=3)
order_dict = OrderedDict(new_dict)


def load_dict():
    step = 0
    for i in range(4, 10):
        new_dict[chr(100 + step)] = i
        step += 1


def load_order():
    step = 0
    for i in range(4, 10):
        order_dict[chr(100 + step)] = i
        step += 1


def dict_get():
    return new_dict.get('b')


def order_get():
    return order_dict.get('b')


print(f'Заполнение словаря: {timeit("load_dict()", globals=globals(), number=10000)}')
print(f'Заполнение Order_словаря: {timeit("load_order()", globals=globals(), number=10000)}')
print(f'Получение словаря: {timeit("dict_get()", globals=globals(), number=10000)}')
print(f'Получение Order_словаря: {timeit("order_get()", globals=globals(), number=10000)}')

# Заполнение словаря: 0.018864899999999997
# Заполнение Order_словаря: 0.017898700000000003
# Получение словаря: 0.0013876000000000027
# Получение Order_словаря: 0.0014049999999999896


# Тип данных OrderedDict после Python3.6 не актуален.
# Заполнение немного быстрее через OrderDict, а получение через dict.
