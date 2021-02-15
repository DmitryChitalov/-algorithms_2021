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

import time


def time_stamp(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        return_value = func(*args, **kwargs)
        end = time.time()
        print('[*] Время выполнения: {} секунд.'.format(end - start))
        return return_value

    return wrapper


@time_stamp
def get_list():
    return [i for i in range(9999999)]


@time_stamp
def get_dict():
    return {i: i for i in range(9999999)}


my_list = get_list()
my_dict = get_dict()

"""
"""


@time_stamp
def get_item_from_list(items_list):
    return items_list[10000]


@time_stamp
def get_item_from_dict(dict_of_items):
    return dict_of_items[10000]


get_item_from_list(my_list)
get_item_from_dict(my_dict)
"""
"""


@time_stamp
def add_item_to_list(items_list, item):
    items_list.append(item)


@time_stamp
def add_item_to_dict(dict_of_items, item):
    dict_of_items[item] = item


add_item_to_list(my_list, 1111111111111)
add_item_to_dict(my_dict, 1111111111111)


@time_stamp
def remove_from_list(items_list, item):
    items_list.remove(item)


@time_stamp
def remove_from_dict(dict_of_items, item):
    dict_of_items.pop(item)


remove_from_list(my_list, 1111111111111)
remove_from_dict(my_dict, 1111111111111)
