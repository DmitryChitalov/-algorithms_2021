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

def create_obj_time_decorator(create_func_to_measure_time):
    def time_measure():
        start = time.time()
        obj = create_func_to_measure_time()
        print(f'Время выполнения функции {create_func_to_measure_time}: {time.time() - start} c.')
        return obj
    return time_measure

def get_numbers_list_elem_in_circle_decorator(get_func_to_measure_time):
    def time_measure(numbers_list):
        start = time.time()
        get_func_to_measure_time(numbers_list)
        print(f'Время выполнения функции {get_func_to_measure_time}: {time.time() - start} c.')
    return time_measure

def get_dict_elem_in_circle_decorator(get_func_to_measure_time):
    def time_measure(dictionary, keys):
        start = time.time()
        get_func_to_measure_time(dictionary, keys)
        print(f'Время выполнения функции {get_func_to_measure_time}: {time.time() - start} c.')
    return time_measure


@create_obj_time_decorator
def fill_numbers_list():
    return [i + 1 for i in range(100000)]

@create_obj_time_decorator
def fill_dict():
    return {f'{value + 1}':value + 1 for value in range(100000)}

@get_numbers_list_elem_in_circle_decorator
def get_numbers_list_elem_in_circle(numbers_list):
    for i in range(100):
        numbers_list[i]

@get_dict_elem_in_circle_decorator
def get_dict_elem_in_circle(dictionary, keys):
    for key in keys:
        dictionary[key]

@get_dict_elem_in_circle_decorator
def another_get_dict_elem_in_circle(dictionary, keys):
    for key in keys:
        dictionary.get(key)


list_of_numbers = fill_numbers_list()   # быстрее выполняется заполение списка (0.013 с),
                                        # т.к. при заполнении словаря (0.051 с)
                                        # происходит вычисление хеш-значений для каждого ключа
dictionary = fill_dict()

get_numbers_list_elem_in_circle(list_of_numbers)   # по результатам замеров, get_numbers_list_elem_in_circle выполняется
                                                   # за 0.0 с, get_dict_elem_in_circle - за 0.017 с. Это связано с тем,
                                                   # что в функцию get_dict_elem_in_circle передается большее число
keys = [f'{i + 1}' for i in range(100000)]         # аргументов
get_dict_elem_in_circle(dictionary, keys)

another_get_dict_elem_in_circle(dictionary, keys)   # выполняется за 0.015 с, ускорение за счет применения встроенной
                                                    # функции dict.get()