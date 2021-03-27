"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните операции, равные по смыслу, с каждым из объектов и сделайте замеры.
Опишите полученные результаты, сделайте выводы.

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях?
"""
from collections import OrderedDict
from random import randint
from timeit import timeit

dict_min = 1
dict_max = 1000


def classic_dict(classic):
    classic = {key: randint(dict_min, dict_max) for key in range(dict_max)}
    return classic


def classic_dict_get(classic):
    return classic.get(dict_max - dict_min)


def classic_dict_pop(classic):
    for item in range(len(classic)):
        classic.pop(item)
    return classic


to_test = {}
dict_ord = OrderedDict()

print(f'Обычный словарь, создание/заполнение: {timeit("classic_dict(to_test)", globals=globals(), number=10000)}')
print(f'Обычный словарь, получение: {timeit("classic_dict_get(to_test)", globals=globals(), number=10000)}')
print(f'Обычный словарь, удаление: {timeit("classic_dict_pop(to_test)", globals=globals(), number=10000)}')
print('=' * 50)
print(f'OrderDict словарь, создание/заполнение: {timeit("classic_dict(dict_ord)", globals=globals(), number=10000)}')
print(f'OrderDict словарь, получение: {timeit("classic_dict_get(dict_ord)", globals=globals(), number=10000)}')
print(f'OrderDict словарь, удаление: {timeit("classic_dict_pop(dict_ord)", globals=globals(), number=10000)}')
"""
Результат на моем ноутбуке:

Обычный словарь, создание/заполнение: 6.560466
Обычный словарь, получение: 0.00118029999999969
Обычный словарь, удаление: 0.0016126999999999114
==================================================
OrderDict словарь, создание/заполнение: 6.7765341999999995
OrderDict словарь, получение: 0.0013980000000000103
OrderDict словарь, удаление: 0.0015562999999989557

Исходя из тестов можно сделать вывод, что результаты равны, видимая разница на уровне погрешности вычислений.
Смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях - отсутствует.
"""