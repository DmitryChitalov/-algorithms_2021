"""
Задание 1.

Реализуйте свои пользовательские функции, в которых реализуйте:

a) заполнение списка и словаря программно,
   сделайте замеры и сделайте выводы, что выполняется быстрее и почему
b) выполните набор операций и со списком, и со словарем,
   сделайте замеры и сделайте выводы, что и где выполняется быстрее и почему

Подсказка: для замеров воспользуйтесь модулем time (см. примеры урока 1)

Примечание: eсли вы уже знаете, что такое декоратор и как его реализовать,
то реализуйте ф-цию-декоратор для подсчета времени работы ваших пользовательских функций
И примените ее к своим функциям!
"""

import random
import time


def fill_set(amount_el=1000):
    my_set = set()
    while len(my_set) < amount_el:
        my_set.add(str(random.randint(0, amount_el * 100)) + 'word')
    return my_set


def timer_for_func(func):
   def timer(*args, **kwargs):
       start_val = time.time()
       result = func(*args, **kwargs)
       end_val = time.time()
       return result, end_val-start_val
   return timer


def timer_for_proc(func):
   def timer(*args, **kwargs):
       start_val = time.time()
       func(*args, **kwargs)
       end_val = time.time()
       return end_val-start_val
   return timer


@timer_for_func
def fill_list_or_dict(type_object, my_set):
    if type_object == 'list':
        obj = []
        for el in my_set:
            obj.append(el)
    elif type_object == 'dict':
        obj = {}
        for el in my_set:
            obj[el] = 'simple_word'
    else:
        return None
    return obj


@timer_for_proc
def find_el_in_list_or_dict(obj, my_set):
    if str(type(obj)).find('list') != - 1:
        for el in my_set:
            get_el = obj.count(el)
    elif str(type(obj)).find('dict') != -1:
        for el in my_set:
            get_el = obj[el]


@timer_for_proc
def del_el_in_list_or_dict(obj, my_set):
    if str(type(obj)).find('list') != - 1:
        for el in my_set:
            obj.remove(el)
    elif str(type(obj)).find('dict') != -1:
        for el in my_set:
            obj.pop(el)


len_obj = 10000
my_set = fill_set(len_obj)

my_list, time_list = fill_list_or_dict('list', my_set)
my_dict, time_dict = fill_list_or_dict('dict', my_set)
percent_dict_in_list = int(time_dict / time_list * 100)
print('Заполнение {} элементов заняло для списка: {:.6f}, для словаря: {:.6f} ({}%)'.format(len_obj, time_list,
                                                                                            time_dict,
                                                                                            percent_dict_in_list))

time_list = find_el_in_list_or_dict(my_list, my_set)
time_dict = find_el_in_list_or_dict(my_dict, my_set)
percent_dict_in_list = int(time_dict / time_list * 100)
print('Поиск/чтение {} элементов заняло для списка: {:.6f}, для словаря: {:.6f} ({}%)'.format(len_obj, time_list,
                                                                                              time_dict,
                                                                                              percent_dict_in_list))

time_list = del_el_in_list_or_dict(my_list, my_set)
time_dict = del_el_in_list_or_dict(my_dict, my_set)
percent_dict_in_list = int(time_dict / time_list * 100)
print('Удаление {} элементов заняло для списка: {:.6f}, для словаря: {:.6f} ({}%)'.format(len_obj, time_list,
                                                                                              time_dict,
                                                                                              percent_dict_in_list))