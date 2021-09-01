"""
Задание 1.

Реализуйте свои пользовательские функции, в которых реализуйте:

a) заполнение списка и словаря,
   сделайте замеры и сделайте выводы, что выполняется быстрее и почему
   И укажите сложность каждой ф-ции, которую вы применяете для заполнения.
   У этих ф-ций может быть разная сложность.
   Поэтому время заполнения списка и словаря может как совпадать, так и отличаться.
b) выполните набор операций и со списком, и со словарем,
   сделайте замеры и сделайте выводы, что и где выполняется быстрее и почему
   И укажите сложность ф-ций, которые вы используете для операций.

Подсказка: для замеров воспользуйтесь модулем time (см. примеры урока 1)

Примечание: Если вы уже знаете, что такое декоратор и как его реализовать,
то реализуйте ф-цию-декоратор для подсчета времени работы ваших пользовательских функций
И примените ее к своим функциям!

Прошу вас внимательно читать ТЗ и не забыть выполнить все пункты.
"""

import random
import time
from datetime import timedelta


def log_time(func):  # O(1)
    def wrapper(*args, **kwargs):
        start_time = time.monotonic()
        result = func(*args, **kwargs)
        end_time = time.monotonic()
        print(timedelta(seconds=end_time - start_time))
        return result

    return wrapper


@log_time
def fill_list(count):  # O(n)
    return [random.randint(0, 100) for _ in range(count)]


@log_time
def fill_dict(count, shift):  # O(n)
    return {idx + shift: random.randint(0, 100) for idx in range(count)}


@log_time
def read_list_elem(lst, idx):  # O(1)
    return lst[idx]


@log_time
def read_dict_elem(dct, idx):  # O(1)
    return dct[idx]


@log_time
def del_list_elem(lst, idx):  # O(n)
    del lst[idx]
    return lst


@log_time
def del_dict_elem(dct, idx):  # O(1)
    del dct[idx]
    return dct


@log_time
def add_list_elem(lst, el):  # O(n)
    lst.extend(el)
    return lst


@log_time
def add_dict_elem(dct, el):  # O(n)
    dct.update(el)
    return dct


LENGTH = 10000000

print('fill in the list/dict:')
print(fill_list(10))
print(fill_dict(10, 0))

print('large volumes: ')
my_list = fill_list(LENGTH)
my_dict = fill_dict(LENGTH, 0)

print('read:')
read_list = read_list_elem(my_list, 100000)
read_dict = read_dict_elem(my_dict, 100000)

print('delete:')
del_list = del_list_elem(my_list, 50000)
del_dict = del_dict_elem(my_dict, 50000)

print('create new:')
my_list_2 = fill_list(1000000)
my_dict_2 = fill_dict(1000000, LENGTH)

print('add:')
add_list = add_list_elem(my_list, my_list_2)
add_dict = add_dict_elem(my_dict, my_dict_2)
