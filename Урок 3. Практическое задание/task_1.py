"""
Задание 1.

Реализуйте свои пользовательские функции, в которых реализуйте:

a) заполнение списка и словаря,
   сделайте замеры и сделайте выводы, что выполняется быстрее и почему
b) выполните набор операций и со списком, и со словарем,
   сделайте замеры и сделайте выводы, что и где выполняется быстрее и почему

Подсказка: для замеров воспользуйтесь модулем time (см. примеры урока 1)

Примечание: eсли вы уже знаете, что такое декоратор и как его реализовать,
то реализуйте ф-цию-декоратор для подсчета времени работы ваших пользовательских функций
И примените ее к своим функциям!

Прошу вас внимательно читать ТЗ и не забыть выполнить все пункты.
"""

import time as tm

test_list_1 = []
test_list_2 = []

test_dict_1 = {}
test_dict_2 = {}

def time_decor(func):
    def timer(*args, **kwargs):
        start = tm.time()
        result = func(*args, **kwargs)
        end = tm.time()
        print(f'Время составило {end - start}')
        return result
    return timer

#Добавление элементов в список с помощью APPEND
@time_decor
def list_filling_append(num, list_name, list_value):
    for i in range(num):
        list_name.append(list_value)

#Добавление элементов в список с помощью INSERT
@time_decor
def list_filling_insert(num, list_name, list_value):
    for i in range(num):
        list_name.insert(0, list_value)

@time_decor
def list_remove(num, list_name, list_value):
    for i in range(num):
        list_name.remove(list_value)

@time_decor
def list_pop(num, list_name, list_value):
    for i in range(num):
        list_name.pop()


#Добавление ключ-значение в словарь с помощью UPDATE
@time_decor
def dict_filling_update(num, dict_name, dict_value):
    for i in range(num):
        dict_name.update({i: dict_value})

#Добавление ключ-значение в словарь
@time_decor
def dict_filling_simple(num, dict_name, dict_value):
    for i in range(num):
        dict_name[i] = dict_value


list_filling_append(100000, test_list_1, '1')
list_filling_insert(100000, test_list_2, '1')
list_pop(100000, test_list_1, '1')
list_remove(100000, test_list_2, '1')

dict_filling_update(100000, test_dict_1, '1')
dict_filling_simple(100000, test_dict_2, '1')