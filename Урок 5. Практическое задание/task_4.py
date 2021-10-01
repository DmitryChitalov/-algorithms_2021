"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните операции с каждым их них (заполнение, получение элемента) и сделайте замеры.
Опишите полученные результаты, сделайте выводы.

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях?
"""
from collections import OrderedDict
from timeit import timeit

my_ordered_dict = OrderedDict()
my_dict = {}

print(my_ordered_dict)


def filling_dict(n):
    for i in range(n):
        my_dict.setdefault(i, i)


def filling_ordered_dict(n):
    for i in range(n):
        my_ordered_dict.setdefault(i, i)


def change_dict(n):
    for i in range(n):
        my_dict[i] = 'new_data'


def change_ordered_dict(n):
    for i in range(n):
        my_ordered_dict[i] = 'new_data'


N = 10000
print('Заполнение словарей')
print(timeit('filling_dict(N)', globals=globals(), number=1000))
print(timeit('filling_ordered_dict(N)', globals=globals(), number=1000))
"""
1.664091106
1.609300623000000
2"""

print('Получение элементов')
print(timeit('change_dict(N)', globals=globals(), number=1000))
print(timeit('change_ordered_dict(N)', globals=globals(), number=1000))
"""
1.1638266869999998
1.5288722449999996

Заполнение словарей происходит практически на равных. А поиск и изменение даже немного 
быстрее работае в обычном словаре.
Смысла использовать OrderedDict в Python 3.6 и более поздних версиях нет.
"""
