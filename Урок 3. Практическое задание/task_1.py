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
from time import time


def exec_time(func):
    def inner(*args, **kwargs):
        start_time = time()
        res = func(*args, **kwargs)
        print(time() - start_time)
        return res
    return inner


@exec_time
def dict_filler(some_dict):  # Время выполнения ~0.77 сек
    some_dict = {i: i for i in range(10000000)}
    return some_dict


@exec_time
def list_filler(some_list):  # Время выполнения ~0.48 сек
    some_list = [i for i in range(10000000)]
    return some_list


@exec_time
def list_filler2(some_list):  # Время выполнения ~0.17 сек
    some_list = list(range(10000000))
    return some_list


@exec_time
def dict_operations(some_dict):  # Время выполнения ~3.26 сек
    for k, v in some_dict.items():
        some_dict[k] = v**2
    return some_dict


@exec_time
def list_operations(some_list):  # Время выполнения ~2.85 сек
    some_list = [elem**2 for elem in some_list]
    return some_list


@exec_time
def dict_replace(some_dict):  # Время выполнения ~0.11 сек
    for k in range(0, 10000000, 10):
        some_dict[k] = k
    return some_dict


@exec_time
def list_replace(some_list):  # Время выполнения ~0.07 сек
    for i in range(0, 10000000, 10):
        some_list[i] = i
    return some_list


@exec_time
def dict_pop(some_dict):  # Время выполнения ~0.0 сек
    for k in range(10000, 11000, 2):
        some_dict.pop(k)
    return some_dict


@exec_time
def list_pop(some_list):  # Время выполнения ~1.93 сек
    for i in range(10000, 11000, 2):
        some_list.pop(i)
    return some_list


my_dict = {}
my_list = []


my_dict = dict_filler(my_dict)
my_list = list_filler(my_list)
my_list = list_filler2(my_list)

my_dict = dict_operations(my_dict)
my_list = list_operations(my_list)

my_dict = dict_replace(my_dict)
my_list = list_replace(my_list)

my_dict = dict_pop(my_dict)
my_list = list_pop(my_list)


"""Во всех случаях, кроме удаления элементов (pop), список выполняется быстрее. 
В случае с .рор, в списке требуется очень много времени на пересчет индексов, а в словаре обращение по ключу
занимает константное время O(1)"""
