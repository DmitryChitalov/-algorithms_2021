"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните операции с каждым их них (заполнение, получение элемента) и сделайте замеры.
Опишите полученные результаты, сделайте выводы.

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях?
"""

from collections import OrderedDict
from random import randint
from timeit import timeit

test_keys = ['Один', 'Два', 'Три', 'Четыре', 'Пять', 'Шесть', 'Семь', 'Восемь', 'Девять', 'Десять']
test_values = ['One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten']


def fill_dict(k, v):
    new_dict = {}
    for i, key in enumerate(k):
        new_dict[key] = v[i]
    return new_dict


def fill_ordered_dict(k, v):
    new_dict = OrderedDict()
    for i, key in enumerate(k):
        new_dict[key] = v[i]
    return new_dict


def get_value(t_dict):
    i = randint(0, 9)
    key = list(t_dict.keys())[i]
    return t_dict.get(key)


test_dict = fill_dict(test_keys, test_values)
test_ordered_dict = fill_ordered_dict(test_keys, test_values)
print('Заполнение dict: ', timeit("fill_dict(test_keys, test_values)", globals=globals(), number=10000))
print('Заполнение OrderedDict: ', timeit("fill_ordered_dict(test_keys, test_values)", globals=globals(), number=10000))
print('Получение элемента из dict: ', timeit("get_value(test_dict)", globals=globals(), number=10000))
print('Получение элемента из OrderedDict: ', timeit("get_value(test_ordered_dict)", globals=globals(), number=10000))

'''
По данным замерам видно, что особых отличий в скорости работы с обычным словарем и OrderedDict нет 
(но OrderedDict стабильно чуть медленнее). 
Кажется, что OrderedDict имеет смысл только если требуется менять порядок ключей в словаре.

Заполнение dict:  0.012172100000000005
Заполнение OrderedDict:  0.0229751
Получение элемента из dict:  0.012211200000000005
Получение элемента из OrderedDict:  0.01420650000000001
'''