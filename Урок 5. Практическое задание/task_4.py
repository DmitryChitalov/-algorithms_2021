"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните операции с каждым их них (заполнение, получение элемента) и сделайте замеры.
Опишите полученные результаты, сделайте выводы.

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях?
"""

import collections
import timeit


my_dict = {}
my_ordered_dict = collections.OrderedDict()


def fill_dict(some_dict):
    for i in range(1000):
        some_dict[i] = i + 10
    return some_dict


print('Заполнение dict')
print(timeit.timeit('fill_dict(my_dict)', globals=globals(), number=1000))


def fill_od(some_od):
    for i in range(1000):
        some_od[i] = i + 10
    return some_od


print('Заполнение OrderedDict')
print(timeit.timeit('fill_dict(my_ordered_dict)', globals=globals(), number=1000))

my_list = []


def get_from_dict(some_dict):
    for i in range(100, 200):
        my_list.append(some_dict[i])
    return some_dict


print('Получение элемента dict')
print(timeit.timeit('get_from_dict(my_dict)', globals=globals(), number=1000))


def get_from_od(some_od):
    for i in range(100, 200):
        my_list.append(some_od[i])
    return some_od


print('Получение элемента OrderedDict')
print(timeit.timeit('get_from_od(my_ordered_dict)', globals=globals(), number=1000))


def pop_dict(some_dict):
    some_dict.pop(1, 'default')
    return some_dict


print('Удаление элемента dict')
print(timeit.timeit('pop_dict(my_dict)', globals=globals(), number=1000))


def pop_od(some_od):
    some_od.popitem(last=False)
    return some_od


print('Удаление элемента OrderedDict')
print(timeit.timeit('pop_od(my_ordered_dict)', globals=globals(), number=1000))

"""
Вывод: Из замеров следует что OrderedDict немного медленнее обычного словаря во всех рассмотренных операциях. Вероятно
его использование в версиях Python 3.6 и выше может быть уместно только когда важна обратная совместимость кода.
"""
