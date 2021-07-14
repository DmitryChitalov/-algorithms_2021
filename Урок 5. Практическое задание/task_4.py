"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните операции с каждым их них (заполнение, получение элемента) и сделайте замеры.
Опишите полученные результаты, сделайте выводы.
И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях?
"""

from collections import OrderedDict
from timeit import timeit

my_dict = {i: i for i in range(100)}
order_dict = OrderedDict([(i, i) for i in range(100)])

# Заполнение словаря
print('my_dict ', timeit('my_dict = {i: i for i in range(1000)}', globals=globals(), number=10000))
print('order_dict ', timeit('order_dict = OrderedDict([(i, i) for i in range(1000)])', globals=globals(), number=10000))
'''
my_dict  0.42988519999999997
order_dict  1.1175903
'''

# Получение элементов
print('my_dict', timeit('my_dict.items()', globals=globals(), number=100000))
print('order_dict', timeit('order_dict.items()', globals=globals(), number=100000))
'''
my_dict 0.00042800000000009497
order_dict 0.00043930000000003133
'''

# Обращение по ключу
print('my_dict', timeit('my_dict[99]', globals=globals(), number=100000))
print('order_dict', timeit('order_dict[99]', globals=globals(), number=100000))

'''
my_dict 0.0032833999999999364
order_dict 0.003144100000000094
'''

'''

'''