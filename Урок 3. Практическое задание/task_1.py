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

count = 999999


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


big_list = get_list(count)
big_dict = get_dict(count)

"""
Время выполнения функции get_list: 0.03143739700317383 секунд.
Время выполнения функции get_dict: 0.08406925201416016 секунд.

Сложность выполнения одинаковая, зависит от длины (O(N)), но т.к. 
cловари требуют больше памяти, то на создание словаря уходит больше времени.

Далнейшие вычисления будем проводить на больших данных
"""


@time_stamp
def get_item_from_list(items_list):
    for i in range(count):
        c = items_list[i]


@time_stamp
def get_item_from_dict(dict_of_items):
    for i in range(count):
        c = dict_of_items[i]


get_item_from_list(big_list)
get_item_from_dict(big_dict)


@time_stamp
def add_item_to_list(items_list):
    for i in range(999999 + 1, 999999 + 1000000):
        items_list.append(i)


@time_stamp
def add_item_to_dict(dict_of_items):
    for i in range(999999 + 1, 999999 + 1000000):
        dict_of_items[i] = i


add_item_to_list(big_list)
add_item_to_dict(big_dict)


@time_stamp
def remove_from_list(items_list):
    for i in range(10000):
        items_list.remove(i)


@time_stamp
def remove_from_dict(dict_of_items):
    for i in range(10000):
        dict_of_items.pop(i)


remove_from_list(big_list)
remove_from_dict(big_dict)


@time_stamp
def find_in_list(items_list, item):
    return item in items_list


@time_stamp
def find_in_dict(dict_of_items, item):
    return item in dict_of_items


find_in_list(big_list, 1111111111111)
find_in_dict(big_dict, 1111111111111)


"""
/usr/bin/python3.8 "/home/sitdikovdr/PycharmProjects/-algorithms_2021/Урок 3. Практическое задание/task_1.py"
Время выполнения функции get_list: 0.03143739700317383 секунд.
Время выполнения функции get_dict: 0.08406925201416016 секунд.
Время выполнения функции get_item_from_list: 0.029572010040283203 секунд.
Время выполнения функции get_item_from_dict: 0.0441737174987793 секунд.
Время выполнения функции add_item_to_list: 0.04752826690673828 секунд.
Время выполнения функции add_item_to_dict: 0.0811452865600586 секунд.
Время выполнения функции remove_from_list: 16.420578956604004 секунд.
Время выполнения функции remove_from_dict: 0.000637054443359375 секунд.
Время выполнения функции find_in_list: 0.01659083366394043 секунд.
Время выполнения функции find_in_dict: 1.1920928955078125e-06 секунд.

Заполнение списка происходит в 2-3 раза быстрее чем словаря, хоть и сложность одинаковая. 
Такая же ситуация с получением данных. Это происходит из-за того, что словари требуют больше памяти и тратят время на 
генерацию хешей.

Однако поиск и удалением данных отличаются в сотни тысяч раз, т.к. имеют константную и линейную сложность.
"""