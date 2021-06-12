"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните операции с каждым их них (заполнение, получение элемента) и сделайте замеры.
Опишите полученные результаты, сделайте выводы.

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях?
"""
from collections import OrderedDict
from timeit import timeit

user_dict = dict((n, n) for n in range(100000))
user_order_dict = OrderedDict(dict((n, n) for n in range(100000)))

print(f'Заполнение dict: {timeit("dict((n, n) for n in range(1000000))", globals=globals(), number=100)}')  # 15.1226578
print(f'Заполнение OrderDict: {timeit("OrderedDict(dict((n, n) for n in range(1000000)))", globals=globals(), number=100)}')  # 37.6298277

print(f'Получение элемента по ключу dict: {timeit("user_dict[999]", globals=globals(), number=10000)}')  # 0.00048350000000141335
print(f'Получение элемента по ключу OrderDict: {timeit("user_order_dict[999]", globals=globals(), number=10000)}')  #  0.0005352999999956864

'''
OrderDict как показывают замеры timeit заполняется на больше чем в два раза дольше. Получение значений ключей одинаково.
Не вижу смысла в использовании OrderDict так как обычный словарь тоже упорядоченный в поздних версиях Python.
'''
