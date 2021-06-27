"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните операции с каждым их них (заполнение, получение элемента) и сделайте замеры.
Опишите полученные результаты, сделайте выводы.

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях?
"""
from collections import OrderedDict
from timeit import timeit


def simple_dict_lc():
    return {el: el * el for el in range(10000)}


def ordered_dict_lc():
    return OrderedDict([(el, el * el) for el in range(10000)])


def simple_dict_pop(dct, count):
    while count > 0:
        dct.pop(int(count), 'some')
        count -= 1
    return dct


def ordered_dict_pop(dct, count):
    while count > 0:
        dct.pop(int(count), 'some')
        count -= 1
    return dct


def simple_dict_change(dct):
    for i in dct:
        dct[i] *= 2
    return dct


def ordered_dict_change(dct):
    for i in dct:
        dct[i] *= 2
    return dct


my_dict = simple_dict_lc()

print("Заполнение списков:")
print(f'{simple_dict_lc.__name__}:\n', timeit('simple_dict_lc()', globals=globals(), number=100))
print(f'{ordered_dict_lc.__name__}:\n', timeit('ordered_dict_lc()', globals=globals(), number=100))
print()
print("Извлечение из списков:")
print(f'{simple_dict_pop.__name__}:\n',
      timeit('simple_dict_pop(my_dict, len(my_dict) / 2)', globals=globals(), number=100))
print(f'{ordered_dict_lc.__name__}:\n',
      timeit('ordered_dict_pop(my_dict, len(my_dict) / 2)', globals=globals(), number=100))
print()
print("Изменение списков:")
print(f'{simple_dict_change.__name__}:\n', timeit('simple_dict_change(my_dict)', globals=globals(), number=100))
print(f'{ordered_dict_change.__name__}:\n', timeit('ordered_dict_change(my_dict)', globals=globals(), number=100))

'''
Заполнение списков:
simple_dict_lc:
 0.18987483
ordered_dict_lc:
 0.43191687999999995

Извлечение из списков:
simple_dict_pop:
 0.15700826
ordered_dict_lc:
 0.141789324

Изменение списков:
simple_dict_change:
 0.12388530599999992
ordered_dict_change:
 0.1286784190000001
 
 
 Заполнение OrderedDict через List Comprehension медленнее в 2 раза 
 такого же метода заполнения обычного словаря.
 
 У извлечения и изменения словарей существенной разницы не обнаружено.
 *** либо код кривой :З ***
  
'''
