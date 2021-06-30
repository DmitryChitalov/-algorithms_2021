"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните операции с каждым их них (заполнение, получение элемента) и сделайте замеры.
Опишите полученные результаты, сделайте выводы.

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях?
"""

# Краткий вывод: использовать OrderedDict в Python 3.6 и выше смысла нет.
# Доказательство:

from collections import OrderedDict
from timeit import timeit
from uuid import uuid4
from random import randint

my_dict = {}
my_ord_dict = OrderedDict()

def fill_dict():
    my_dict[uuid4()] = randint(100, 1000)
    return my_dict

def fill_ordered_dict():
    my_ord_dict[uuid4()] = randint(100, 1000)
    return my_ord_dict


print('Заполнение:')
print('Словарь : ', timeit('fill_dict()', globals=globals(), number=100_000))
print('OrderedDict: ', timeit('fill_ordered_dict()', globals=globals(), number=100_000))

# OrderedDict показывает немного медленнее результаты при заполнении данными
# Словарь :  0.6012591999999999
# OrderedDict:  0.6226053999999999

my_dict['abc'] = 1
my_ord_dict['abc'] = 1

def get_dict():
    x = my_dict['abc']
    return x

def get_ordered_dict():
    x = my_ord_dict['abc']
    return x

print('Получение по ключу:')
print('Словарь : ', timeit('get_dict()', globals=globals(), number=1_000_000))
print('OrderedDict: ', timeit('get_ordered_dict()', globals=globals(), number=1_000_000))

# Результаты сопоставимы, обычный словарь немного быстрее:
# Словарь :  0.16761380000000003
# OrderedDict:  0.15988540000000007

# использовать OrderedDict в Python 3.6 и выше смысла нет.
