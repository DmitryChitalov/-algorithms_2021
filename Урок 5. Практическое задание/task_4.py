"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните операции с каждым их них (заполнение, получение элемента) и сделайте замеры.
Опишите полученные результаты, сделайте выводы.

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях?
"""
from collections import OrderedDict
from timeit import timeit

order_dict = OrderedDict({i: i for i in range(100)})
my_dict = {i: i for i in range(100)}
new1 = {i: i for i in range(1, 50)}

print('Заполнение')
print('OrderedDict', timeit('order_dict = OrderedDict({i: i for i in range(100)})', globals=globals()))
print('dict', timeit('my_dict= {i: i for i in range(100)}', globals=globals()))
print('Обращение по ключу')
print('OrderedDict', timeit('order_dict[50]', globals=globals()))
print('dict', timeit('my_dict[50]', globals=globals()))
print('Копирование')
print('OrderedDict', timeit('order_dict.copy()', globals=globals()))
print('dict', timeit('my_dict.copy()', globals=globals()))
print('Обращение к элементам')
print('OrderedDict', timeit('order_dict.items()', globals=globals()))
print('dict', timeit('my_dict.items()', globals=globals()))
print('Обновление')
print('OrderedDict', timeit('order_dict.update(new1)', globals=globals()))
print('dict', timeit('my_dict.update(new1)', globals=globals()))
""" 
Заполнение
OrderedDict 18.4865014
dict 4.704196
Обращение по ключу
OrderedDict 0.032001399999998625
dict 0.031435899999998185
Копирование
OrderedDict 7.548558199999999
dict 0.4626917999999982
Обращение к элементам
OrderedDict 0.0539051999999991
dict 0.049386999999999404
Обновление
OrderedDict 4.545159699999996
dict 0.745866999999997

Судя по замерам использование OrderedDict иногда даже медленнее, а значит в современных версиях Python его использовать 
не стоит. 
"""
