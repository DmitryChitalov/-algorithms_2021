"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните операции с каждым их них (заполнение, получение элемента) и сделайте
замеры.
Опишите полученные результаты, сделайте выводы.

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях?
"""
from collections import OrderedDict
from timeit import timeit

order_dict = OrderedDict([(i, i) for i in range(100)])
my_dict = {i: i for i in range(100)}

print('Заполнение')
print('order', timeit('order_dict = OrderedDict([(i, i) for i in range(100)])',
                      globals=globals()))
print('dict', timeit('my_dict= {i: i for i in range(100)}', globals=globals()))

print('\nОбращение по ключу')
print('order', timeit('order_dict[50]', globals=globals()))
print('dict', timeit('my_dict[50]', globals=globals()))

print('\nКопирование')
print('order', timeit('order_dict.copy()', globals=globals()))
print('dict', timeit('my_dict.copy()', globals=globals()))

print('\nОбращение к элементам')
print('order', timeit('order_dict.items()', globals=globals()))
print('dict', timeit('my_dict.items()', globals=globals()))

new1 = {i: i for i in range(1, 50)}
print('\nОбновление')
print('order', timeit('order_dict.update(new1)', globals=globals()))
print('dict', timeit('my_dict.update(new1)', globals=globals()))

""" 
Видя разницу в некоторых операциях на порядок и отсутствие каких либо 
преимуществ в современных версиях Python Делаю вывод, что OrderedDict - устарел
и нет смысла его больше использовать.
"""
