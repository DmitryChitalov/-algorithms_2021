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

first_list = []
first_dictionary = {}
number_operations = 10000000


def time_decorator(function):
    def time_count(*args):
        start = time.time()
        function(*args)
        end = time.time()
        time_work = end - start
        print(time_work)
    return time_count


"""блок А"""


@time_decorator
def append_list(lst, x):    # вреям заполнения 1.1620960235595703
    for i in range(x):
        lst.append(i)
    print('время заполнения списка - ')
    return lst


@time_decorator
def append_dictionary(dictionary, x):    # время заполнения словаря 1.4133682250976562
    for i in range(x):
        dictionary[i] = i
    print('время заполнения словаря - ')
    return dictionary


"""Блок Бэ"""
second_list = []
second_dictionary = {}


@time_decorator
def operations_list(lst):    # время копирования списка 1.1363658905029297
    for i in lst:
        second_list.append(i)
    print('время копирования списка - ')
    return second_list


@time_decorator
def operations_dictionary(dictionary):    # время копирования словаря 1.605518102645874
    for i in dictionary:
        second_dictionary[i] = dictionary[i]
    print('время копирования словаря - ')
    return second_dictionary


append_list(first_list, number_operations)    # вреям заполнения 1.1620960235595703
operations_list(first_list)    # время копирования списка 1.1363658905029297
append_dictionary(first_dictionary, number_operations)    # время заполнения словаря 1.4133682250976562
operations_dictionary(first_dictionary)    # время копирования словаря 1.605518102645874


"""из полученных данных замеров скорости заполнения и скорости копирования (во времени)
делаем вывод, что в данном случаем словари работают медленнее, т.к
они реализованы в виде хеш-таблиц. Хеш-таблицы требуют больше памяти и работают медленнее"""
