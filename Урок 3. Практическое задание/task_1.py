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
        print(f'Время выполнения функции {func.__name__}: {end - start} секунд.')
        return return_value

    return wrapper


@time_stamp
def get_list(elem_count):
    return [i for i in range(elem_count)]


@time_stamp
def get_dict(elem_count):
    return {i: i for i in range(elem_count)}


big_list = get_list(9999999)
big_dict = get_dict(9999999)

small_list = get_list(90000)
small_dict = get_dict(90000)

"""
Время выполнения функции get_list: 0.44780445098876953 секунд.
Время выполнения функции get_dict: 0.7280566692352295 секунд.

Время выполнения функции get_list: 0.0029916763305664062 секунд.
Время выполнения функции get_dict: 0.006983518600463867 секунд.

Сложность выполнения одинаковая, зависит от длины (O(N)), но т.к. 
cловари требуют больше памяти, то на создание словаря уходит больше времени.

Далнейшие вычисления будем проводить на больших данных
"""


@time_stamp
def get_item_from_list(items_list):
    return items_list[9999]


@time_stamp
def get_item_from_dict(dict_of_items):
    return dict_of_items[9999]


get_item_from_list(big_list)
get_item_from_dict(big_dict)
"""
Время выполнения функции get_item_from_list: 0.0 секунд.
Время выполнения функции get_item_from_dict: 0.0 секунд.
Обе функции выполняются почти что мгновенно

Проверим вставку элементов
"""


@time_stamp
def add_item_to_list(items_list, item):
    items_list.append(item)


@time_stamp
def add_item_to_dict(dict_of_items, item):
    dict_of_items[item] = item


add_item_to_list(big_list, 1111111111111)
add_item_to_dict(big_dict, 1111111111111)

'''
@time_stamp
def remove_from_list(items_list, item):
    items_list.remove(item)


@time_stamp
def remove_from_dict(dict_of_items, item):
    dict_of_items.pop(item)


remove_from_list(my_list, 1111111111111)
remove_from_dict(my_dict, 1111111111111)
'''