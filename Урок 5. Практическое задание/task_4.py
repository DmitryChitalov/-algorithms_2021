"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните операции с каждым их них (заполнение, получение элемента) и сделайте замеры.
Опишите полученные результаты, сделайте выводы.

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях?
"""
from timeit import timeit
from collections import OrderedDict


my_dict = {}
my_ordered_dict = OrderedDict()


def full_dict(n):
    for el in range(n):
        my_dict[el] = el


def full_ordered_dict(n):
    for el in range(n):
        my_ordered_dict[el] = el


print(f'__________________________________________')
print(f'Добавление в dict')
print(f'{timeit("full_dict(10000)",globals=globals(),number=1)}'[:10])
print(f'Добавление в ordered_dict')
print(f'{timeit("full_ordered_dict(10000)",globals=globals(),number=1)}'[:10])
print('Добавление быстрее dict')


def get_dict():
    count = len(my_dict)//2
    my_dict.get(count)


def get_ordered_dict():
    count = len(my_dict) // 2
    my_ordered_dict.get(count)


print(f'__________________________________________')
print(f'Значение ключа в dict')
print(f'{timeit("get_dict()",globals=globals(),number=10000)}'[:10])
print(f'Значение ключа в ordered_dict')
print(f'{timeit("get_ordered_dict()",globals=globals(),number=10000)}'[:10])
print('Значение ключа быстрее dict')


def popitem_dict():
    my_dict.popitem()


def popitem_ordered_dict():
    my_ordered_dict.popitem()


print(f'__________________________________________')
print(f'Удаление и возвращение в dict')
print(f'{timeit("popitem_dict()",globals=globals(),number=10000)}'[:10])
print(f'Удаление и возвращение в ordered_dict')
print(f'{timeit("popitem_ordered_dict()",globals=globals(),number=10000)}'[:10])
print('Удаление и возвращение быстрее dict')
print(f'__________________________________________')
print('Исходя из замеров OrderedDict работает медленее и так,как словарь в python 3.6 запоминает последовательность, использовать его не стоит')



