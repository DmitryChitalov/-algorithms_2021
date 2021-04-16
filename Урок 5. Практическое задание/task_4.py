"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните операции, равные по смыслу, с каждым из объектов и сделайте замеры.
Опишите полученные результаты, сделайте выводы.

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях?
"""


import random
import collections
from timeit import timeit

v_dict = {}
v_ordered_dict = collections.OrderedDict()
v_attempts = 10000000

def populate_dict():
    v_dict = {i: random.randint(1, 10000) for i in range(100000)}

def populate_ordered_dict():
    v_ordered_dict = collections.OrderedDict({i: random.randint(1, 10000) for i in range(100000)})

def append_dict():
    v_dict.update({len(v_dict): random.randint(1, 10000)})

def append_ordered_dict():
    v_ordered_dict.update({len(v_ordered_dict): random.randint(1, 10000)})

def update_several_dict():
    for i in range(1000, 1003):
        v_dict.update({i: random.randint(1, 10000)})

def update_several_ordered_dict():
    for i in range(1000, 1003):
        v_ordered_dict.update({i: random.randint(1, 10000)})

def get_random_value_dict():
    a = v_dict.get(random.randint(1, 99999))

def get_random_value_ordered_dict():
    a = v_ordered_dict.get(random.randint(1, 99999))

def popitem_dict():
    v_dict.popitem()

def popitem_ordered_dict():
    v_ordered_dict.popitem()

print('timeit populate_dict',
          round(
              timeit(
                  'populate_dict()',
                  globals=globals(),
                  number=100)
              , 4),
          'seconds')

print('timeit populate_ordered_dict',
          round(
              timeit(
                  'populate_ordered_dict()',
                  globals=globals(),
                  number=100)
              , 4),
          'seconds')

print('timeit append_dict',
          round(
              timeit(
                  'append_dict()',
                  globals=globals(),
                  number=v_attempts)
              , 4),
          'seconds')

print('timeit append_ordered_dict',
          round(
              timeit(
                  'append_ordered_dict()',
                  globals=globals(),
                  number=v_attempts)
              , 4),
          'seconds')

print('timeit update_several_dict',
          round(
              timeit(
                  'update_several_dict()',
                  globals=globals(),
                  number=v_attempts)
              , 4),
          'seconds')

print('timeit update_several_ordered_dict',
          round(
              timeit(
                  'update_several_ordered_dict()',
                  globals=globals(),
                  number=v_attempts)
              , 4),
          'seconds')


print('timeit get_random_value_dict',
          round(
              timeit(
                  'get_random_value_dict()',
                  globals=globals(),
                  number=v_attempts)
              , 4),
          'seconds')

print('timeit get_random_value_ordered_dict',
          round(
              timeit(
                  'get_random_value_ordered_dict()',
                  globals=globals(),
                  number=v_attempts)
              , 4),
          'seconds')

print('timeit popitem_dict',
          round(
              timeit(
                  'popitem_dict()',
                  globals=globals(),
                  number=v_attempts)
              , 4),
          'seconds')

print('timeit popitem_ordered_dict',
          round(
              timeit(
                  'popitem_ordered_dict()',
                  globals=globals(),
                  number=v_attempts)
              , 4),
          'seconds')
"""
timeit populate_dict 8.9063 seconds
timeit populate_ordered_dict 11.7547 seconds
timeit append_dict 10.7993 seconds
timeit append_ordered_dict 12.4437 seconds
timeit update_several_dict 32.9852 seconds
timeit update_several_ordered_dict 39.073 seconds
timeit get_random_value_dict 11.4868 seconds
timeit get_random_value_ordered_dict 11.1311 seconds
timeit popitem_dict 1.5425 seconds
timeit popitem_ordered_dict 1.9856 seconds

Класс collections.OrderedDict() был разработан для частыx операций переупорядочивания, но с версии Python 3.7 уже
встроенный класс dict получил возможность запоминать порядок вставки.
По результатам замеров мы видим, что операции с orderedDict не имеют преимуществ по сравнению со встроенным типом.
"""

