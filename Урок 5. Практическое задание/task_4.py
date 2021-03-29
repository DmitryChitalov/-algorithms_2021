"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните операции, равные по смыслу, с каждым из объектов и сделайте замеры.
Опишите полученные результаты, сделайте выводы.

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях?
"""
from collections import OrderedDict
from timeit import timeit


def setdefault_dict(li):
    '''setdefault'''
    d = {}
    for k, v in li:
        d.setdefault(k, []).append(v)
    return d


def ordered_dict(li):
    '''OrderedDict'''
    d = OrderedDict()
    for k, v in li:
        d.setdefault(k, []).append(v)
    return d


my_list = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]

print(f'Используем добавление dict.setdefault(key, []).append(value)')
print(f'setdefault_dict= {timeit("setdefault_dict(my_list)", globals=globals())}')
print(f'ordered_dict= {timeit("ordered_dict(my_list)", globals=globals())}')
print()


def setdefault_dict1(n):
    '''setdefault'''
    d = dict()
    for i in range(n):
        d[i] = 'value' + str(i)
    return d


def ordered_dict1(n):
    '''OrderedDict'''
    d = OrderedDict()
    for i in range(n):
        d[i] = 'value' + str(i)
    return d


n = 100
print(f'Через цикл используем присвоение dict[key] = value')
print(f'setdefault_dict= {timeit("setdefault_dict1(n)", globals=globals(), number=10000)}')
print(f'ordered_dict= {timeit("ordered_dict1(n)", globals=globals(), number=10000)}')
print()

"""
Мы провели 2 сравнения dict VS ordered dict. Добавление в словарь ключа и значения. В обоих случаях обычный словарь 
справился быстрей.
При том, что с версии Python 3.7 dict стал упорядоченным, то никаких преимуществ ordered dict больше не имеет.
Ниже мы выведем оба словаря и убедимся в их упорядоченности.
"""


def setdefault_dict_number(n):
    '''setdefault'''
    d = dict()
    for i in range(n):
        d[i] = 'value' + str(i)
    return d


def ordered_dict_number(n):
    '''OrderedDict'''
    d = OrderedDict()
    for i in range(n):
        d[i] = 'value' + str(i)
    return d


print(f'Сделаем вывод обоих словарей.\nУбедимся в их упорядоченности.')
print(setdefault_dict_number(n))
print(ordered_dict_number(n))
