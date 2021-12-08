"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните операции с каждым их них (заполнение, получение элемента) и сделайте замеры.
Опишите полученные результаты, сделайте выводы.

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях?
- нет, ибо в этих версиях обычный словарь помнит порядок добавления в него элементов, те уже обладает свойством OrderedDict
"""

from time import time
from datetime import timedelta
import random
from collections import OrderedDict

def log_time(func):  # O(1)
    def wrapper(*args, **kwargs):
        start_time = time()
        result = func(*args, **kwargs)
        end_time = time()
        print(f"Время выполнения ф-ции {func.__name__} составило: {timedelta(seconds=end_time - start_time)}")
        return result
    return wrapper


@log_time
def create_dict(count):  # O(n)
    new_dict = {idx: random.randint(0, 100) for idx in range(count)}
    return new_dict

@log_time
def create_OrderedDict(count):
    return OrderedDict({idx: random.randint(0, 100) for idx in range(count)})


number_get_operations = 1000000
@log_time
def get_elem_dict(dict, idx):
    for _ in range(number_get_operations):
        dict[idx]
    return dict

@log_time
def get_elem_OrderedDict(dict, idx):
    # return dict[idx]
    for _ in range(number_get_operations):
        dict[idx]
    return dict


dict_1 = create_dict(10000)
dict_2 = create_OrderedDict(10000)

get_elem_dict(dict_1, 3)
get_elem_OrderedDict(dict_2, 3)

'''
Время выполнения ф-ции create_dict составило: 0:00:00.039888
Время выполнения ф-ции create_OrderedDict составило: 0:00:00.043890
Время выполнения ф-ции get_elem_dict составило: 0:00:00.097726
Время выполнения ф-ции get_elem_OrderedDict составило: 0:00:00.053854

Заполняется и создается быстрее словарь, а вот работать быстрее с OrderedDict
'''