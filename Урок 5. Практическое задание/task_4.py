"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните операции с каждым их них (заполнение, получение элемента) и сделайте замеры.
Опишите полученные результаты, сделайте выводы.

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях?
"""
from collections import OrderedDict
from timeit import timeit
import random

my_list = list(range(1000))
random_list = random.sample(range(0, 1000), 1000)
my_dict = {}
for key, value in enumerate(my_list):
    my_dict[key] = value
my_OrderedDict = OrderedDict(enumerate(my_list))


def create_dict(my_list):
    my_dict = {}
    for key, value in enumerate(my_list):
        my_dict[key] = value
    return my_dict


def create_OrderedDict(my_list):
    my_OrderedDict = OrderedDict(enumerate(my_list))
    return my_OrderedDict


def update_dict(my_dict, random_list):
    for i in range(1000):
        my_dict[i] = random_list[i]
    return my_dict


def update_OrderedDict(my_OrderedDict, random_list):
    for i in range(1000):
        my_OrderedDict[i] = random_list[i]
    return my_OrderedDict


def del_dict(my_list):
    my_dict = {}
    for key, value in enumerate(my_list):
        my_dict[key] = value
    for i in range(500):
        del my_dict[i]
    return my_dict


def del_OrderedDict(my_list):
    my_OrderedDict = OrderedDict(enumerate(my_list))
    for i in range(500):
        my_OrderedDict.pop(i)
    return my_OrderedDict

print(f'Создание словаря {timeit("create_dict(my_list)", globals=globals(), number=10000)} sec')
print(f'Создание OrderedDict {timeit("create_OrderedDict(my_list)", globals=globals(), number=10000)} sec')
print(f'Обновление элементов словаря {timeit("update_dict(my_dict,random_list)", globals=globals(), number=10000)} sec')
print(
    f'Обновление элементов OrderedDict {timeit("update_OrderedDict(my_OrderedDict,random_list)", globals=globals(), number=10000)} sec')
print(f'Удаление 500 элементов словаря {timeit("del_dict(my_list)", globals=globals(), number=10000)} sec')
print(
    f'Удаление 500 элементов из OrderedDict {timeit("del_OrderedDict(my_list)", globals=globals(), number=10000)} sec')

"""
1 замер
Создание словаря 4.3067798 sec
Создание OrderedDict 7.133752100000001 sec
Обновление элементов словаря 2.8636695999999997 sec
Обновление элементов OrderedDict 3.5539281999999996 sec
Удаление 500 элементов словаря 4.955632600000001 sec
Удаление 500 элементов из OrderedDict 11.9649434 sec

2 замер
Создание словаря 3.6199809999999997 sec
Создание OrderedDict 6.8659132 sec
Обновление элементов словаря 3.3122562999999996 sec
Обновление элементов OrderedDict 4.4391680000000004 sec
Удаление 500 элементов словаря 6.255326099999998 sec
Удаление 500 элементов из OrderedDict 12.151628799999997 sec

3 замер
Создание словаря 3.6258318999999997 sec
Создание OrderedDict 6.8892097 sec
Обновление элементов словаря 3.0647181999999997 sec
Обновление элементов OrderedDict 4.7832726 sec
Удаление 500 элементов словаря 4.602915500000002 sec
Удаление 500 элементов из OrderedDict 12.816226799999999 sec

4 замер
Создание словаря 3.6370611 sec
Создание OrderedDict 7.763460100000001 sec
Обновление элементов словаря 2.726983200000001 sec
Обновление элементов OrderedDict 3.8162971 sec
Удаление 500 элементов словаря 4.839808699999999 sec
Удаление 500 элементов из OrderedDict 11.403635800000004 sec

5 замер
Создание словаря 3.5448036 sec
Создание OrderedDict 6.6010664000000006 sec
Обновление элементов словаря 2.7681763000000004 sec
Обновление элементов OrderedDict 3.6791535999999994 sec
Удаление 500 элементов словаря 4.547612300000001 sec
Удаление 500 элементов из OrderedDict 10.1324778 sec

Замеры показывают, что смысла использовать OrderedDict в версиях Python 3.6 и выше нет.
Операции с обычными словарями производятся в несколько раз быстрее.
"""