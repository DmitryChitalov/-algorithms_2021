"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните операции, равные по смыслу, с каждым из объектов и сделайте замеры.
Опишите полученные результаты, сделайте выводы.

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях?
"""
from collections import OrderedDict
from timeit import timeit


def dict_create():
    return {k: v for (k, v) in zip([x for x in range(50)],
                                   [k for k in range(50)])}


def ord_dict_create():
    return OrderedDict({k: v for (k, v) in zip([x for x in range(50)],
                                               [k for k in range(50)])})


# Время создания словарей
print(f'Обычный словарь: {timeit("dict_create()", globals=globals(), number=10000)}')
print(f'OrderedDict    : {timeit("ord_dict_create()", globals=globals(), number=10000)}')

just_dict = dict_create()
ord_dict = ord_dict_create()

# Добавление новой пары
key, value = 'key', 'value'
print(f'Обычный словарь: {timeit("just_dict[key] = value", globals=globals(), number=1000000)}')
print(f'OrderedDict    : {timeit("ord_dict[key] = value", globals=globals(), number=1000000)}')

"""
OrderedDict нет смысла использовать, так как операции с ним занимают больше времени, чем с обычным dict. Это
связано с тем, что OrderedDict является подклассом dict и требует больше памяти для отслеживания порядка 
добавления ключей.
"""
