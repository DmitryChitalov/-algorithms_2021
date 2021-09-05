"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните операции с каждым их них (заполнение, получение элемента) и сделайте замеры.
Опишите полученные результаты, сделайте выводы.

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях?
"""


from timeit import timeit
from collections import OrderedDict


def simply_create():
    return {k: v for (k, v) in zip([x for x in range(100)],
                                   [k for k in range(100)])}


def or_create():
    return OrderedDict({k: v for (k, v) in zip([x for x in range(100)],
                                               [k for k in range(100)])})



print(f'Создаение обычного словаря: {timeit("simply_create()", globals=globals(), number=10000)} сек')
print(f'Создание OrderedDict    : {timeit("or_create()", globals=globals(), number=10000)} сек')

simply_dict = simply_create()
or_dict = or_create()

key, value = 'key', 'value'

print()
print(f'Добавление пары: обычный словарь: {timeit("simply_dict[key] = value", globals=globals(), number=1000000)} сек')
print(f'Добавление пары: OrderedDict    : {timeit("or_dict[key] = value", globals=globals(), number=1000000)} сек')

print()
print(f'Доступ по ключу: обычный словарь: {timeit("a = simply_dict[key]", globals=globals(), number=1000000)} сек')
print(f'Доступ по ключу: OrderedDict    : {timeit("a = or_dict[key]", globals=globals(), number=1000000)} сек')

"""
Результат замеров показывает, что использовать OrderedDict нет необходимости, т.к. выполняется медленее чем dict

Создаение обычного словаря: 0.1905281 сек
Создание OrderedDict    : 0.35047740000000005 сек

Добавление пары: обычный словарь: 0.0741117 сек
Добавление пары: OrderedDict    : 0.09317799999999998 сек

Доступ по ключу: обычный словарь: 0.06283539999999999 сек
Доступ по ключу: OrderedDict    : 0.06172840000000002 сек
"""