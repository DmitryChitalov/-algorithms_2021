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


def time_of_function(function):
    def time_func(*args, **kwargs):
        start = time.time()
        result = function(*args, **kwargs)
        return result, time.time() - start

    return time_func


@time_of_function
def create_list(count):
    list_count = [el for el in range(count)]
    return list_count


@time_of_function
def create_dict(count):
    dict_count = {el: el for el in range(count)}
    return dict_count


@time_of_function
def pop_list_items(start_list, count):
    for i in range(count):
        start_list.pop(i)
    return start_list


@time_of_function
def pop_dict_items(start_dict, count):
    for i in range(count):
        start_dict.pop(i)
    return start_dict


n = 10000000
list_test, time_create_list = create_list(n)[0], create_list(n)[1]
print(f'time to create list of {n} items: {time_create_list}')
dict_test, time_create_dict = create_dict(n)[0], create_dict(n)[1]
print(f'time to create dict of {n} items: {time_create_dict}')
# time to create list of 10000000 items: 0.5876383781433105
# time to create dict of 10000000 items: 0.9004416465759277
# время создания словаря больше, так как к каждому ключу словаря создается хэш

n = 10000
print(f'time to delete from list {n} items: {pop_list_items(list_test, n)[1]}')
print(f'time to delete from dict {n} items: {pop_dict_items(dict_test, n)[1]}')
# time to delete from list 10000 items: 48.998823404312134
# time to delete from dict 10000 items: 0.0019865036010742188
# удаление элементов из словаря по ключу происходит быстрее, чем из списка по индексу
