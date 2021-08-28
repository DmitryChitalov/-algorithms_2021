"""
Задание 1.

Реализуйте свои пользовательские функции, в которых реализуйте:

a) заполнение списка и словаря,
   сделайте замеры и сделайте выводы, что выполняется быстрее и почему
   И укажите сложность каждой ф-ции, которую вы применяете для заполнения.
   У этих ф-ций может быть разная сложность. Поэтому время заполнения списка и словаря может как совпадать, так и отличаться.
b) выполните набор операций и со списком, и со словарем,
   сделайте замеры и сделайте выводы, что и где выполняется быстрее и почему
   И укажите сложность ф-ций, которые вы используете для операций.

Подсказка: для замеров воспользуйтесь модулем time (см. примеры урока 1)

Примечание: eсли вы уже знаете, что такое декоратор и как его реализовать,
то реализуйте ф-цию-декоратор для подсчета времени работы ваших пользовательских функций
И примените ее к своим функциям!

Прошу вас внимательно читать ТЗ и не забыть выполнить все пункты.
"""

import random
import time
from datetime import timedelta


def fix_time(func):
    """O(1)"""
    def wraper(*args, **kwargs):
        start_time = time.monotonic()
        res = func(*args, **kwargs)
        end_time = time.monotonic()
        print(timedelta(seconds=end_time - start_time))
        return res

    return wraper


@fix_time
def fill_list(cnt):
    """O(n)"""
    return [random.randint(0, 100) for _ in range(cnt)]


@fix_time
def fill_dict(cnt, shift):
    """O(n)"""
    return {idx + shift: random.randint(0, 100) for idx in range(cnt)}


@fix_time
def get_list_elem(lst, idx):
    """O(1)"""
    return lst[idx]


@fix_time
def get_dict_elem(dct, idx):
    """O(1)"""
    return dct[idx]


@fix_time
def del_list_elem(lst, idx):
    """O(n)"""
    del lst[idx]
    return lst


@fix_time
def del_dict_elem(dct, idx):
    """O(1)"""
    del dct[idx]
    return dct


@fix_time
def add_list_elem(lst, el):
    """O(n)"""
    lst.extend(el)
    return lst


@fix_time
def add_dict_elem(dct, el):
    """O(n)"""
    dct.update(el)
    return dct


LENGTH = 100000

print('Демонстрация работоспособности:')
print(fill_list(10))
print(fill_dict(10, 0))

print('Засечка времени заполнения на больших объемах:')
my_list = fill_list(LENGTH)
my_dict = fill_dict(LENGTH, 0)
# Заполнение списка и словаря выполняется одинаково

print('Засечка времени получения элемента:')
my_list_elem = get_list_elem(my_list, 10000)
my_dict_elem = get_dict_elem(my_dict, 10000)

print('Засечка времени удаления элемента:')
my_list = del_list_elem(my_list, 5000)
my_dict = del_dict_elem(my_dict, 5000)

print('Создаем список и словарь, которые добавим к основным:')
my_list_2 = fill_list(10000)
my_dict_2 = fill_dict(10000, LENGTH)

print('Засечка времени добавления элемента:')
my_list = add_list_elem(my_list, my_list_2)
my_dict = add_dict_elem(my_dict, my_dict_2)
