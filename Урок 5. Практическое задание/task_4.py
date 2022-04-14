"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните операции с каждым их них (заполнение, получение элемента) и сделайте замеры.
Опишите полученные результаты, сделайте выводы.

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях?
"""

from collections import OrderedDict
import time
from timeit import timeit
from random import randint, random, choice
import string

def get_time_count(f): # создание функции для замеров времени и использования в качестве декоратора
    def t(obj):
        start_time = time.time()
        f(obj)
        end_time = time.time()
        return end_time - start_time, type(obj)
    return t

# a) заполнение словаря и OrderedDict:

# использую choice для генерации ключей, random - для длины ключа и для генерации значений словаря:
@get_time_count
def get_dict_filled(dict_obj, n=10000):
    l = string.ascii_lowercase
    for _ in range(n):
        str_key_len = int(random() * 5 + 1)
        new_dict_el = dict.fromkeys([''.join(choice(l) for i in range(str_key_len))], int(random() * 1000 + 1))
        dict_obj.update(new_dict_el)
    return dict_obj

dict_1 = {}

print('Заполнение словаря:')
print(get_dict_filled(dict_1))
print()

@get_time_count
def get_OrderedDict_filled(ordered_dict_obj, n=10000):
    l = string.ascii_lowercase
    for _ in range(n):
        str_key_len = int(random() * 5 + 1)
        new_ord_dict_el = dict.fromkeys([''.join(choice(l) for i in range(str_key_len))], int(random() * 1000 + 1))
        ordered_dict_obj.update(new_ord_dict_el)
    return ordered_dict_obj

ordered_dict_1 = OrderedDict()

print('Заполнение OrderedDict:')
print(get_OrderedDict_filled(ordered_dict_1))
print()


# Вывод: заполнение словаря и OrderedDict практически не отличаюся  по затратам времени


# b) выполние операций со словарем, OrderedDict:

print('Изменение словаря: операции со словарем: ')

@get_time_count
def get_dict_modified_1(dict_obj): # без вывода результатов изменений
    dict_test = dict_obj.copy()
    dict_test.clear()
    dict_obj.update([('one', 1), ('two', 2), ('three', 3), ('four', 4)])
    dict_obj.items()
    dict_obj.keys()
    dict_obj.values()
    dict_obj.pop('two')
    dict_obj.popitem() # удаляет и возвращает ключ-значение с конца словаря
    dict_obj.setdefault('three')
    return dict_obj

print(get_dict_modified_1(dict_1))
print(timeit("get_dict_modified_1", globals=globals(), number=1000000))
print()

print('Изменение OrderedDict: операции с OrderedDict: ')

@get_time_count
def get_OrderedDict_modified_1(ordered_dict_obj): # без вывода результатов изменений
    ordered_dict_test = ordered_dict_obj.copy()
    ordered_dict_test.clear()
    ordered_dict_obj.update([('one', 1), ('two', 2), ('three', 3), ('four', 4)])
    ordered_dict_obj.items()
    ordered_dict_obj.keys()
    ordered_dict_obj.values()
    ordered_dict_obj.pop('two')
    ordered_dict_obj.popitem() # удаляет и возвращает ключ-значение с конца словаря
    ordered_dict_obj.setdefault('three')
    return ordered_dict_obj


print(get_OrderedDict_modified_1(ordered_dict_1))
print(timeit("get_OrderedDict_modified_1", globals=globals(), number=1000000))

# Вывод: операций со словарем выполняются быстрее, чем с OrderedDict (использовала два метода
# замера времени: через декоратор и через timeit),  поэтому нет смысла использовать OrderedDict
# в Python 3.6 и более поздних версиях.