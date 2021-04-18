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

def time_function(func):
    def time_func(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        stop = time.time()
        return result, stop - start
    return time_func

@time_function
def create_list(n):
    created_list = [i for i in range(n)]
    return created_list


@time_function
def create_dict(n):
    created_dict = {i: i*2 for i in range(n)}
    return created_dict


@time_function
def add_to_list(created_list, item):
    created_list.append(item)
    return created_list

@time_function
def add_to_dict(created_dict, key, val):
    created_dict.update({key: val})
    return created_dict

@time_function
def del_from_list(created_list, start, quantity):
    for i in range(start, start + quantity):
        created_list.pop(i)
    return created_list


@time_function
def del_from_dict(created_dict, start, quantity):
    for i in range(start, start + quantity):
        created_dict.pop(i)
    return created_dict


num_elems=1000000
created_list = create_list(num_elems)[0]
created_dict = create_dict(num_elems)[0]

print(f'1. Список (создание): {create_list(num_elems)[1]}')
print(f'   Словарь (создание): {create_dict(num_elems)[1]}')
# Список создается быстрее, чем словарь (тк для каждого ключа словаря создается хеш)

print(f'2. Список (добавление элемента): {add_to_list(created_list, 999)[1]}')
print(f'   Словарь (добавление элемента): {add_to_dict(created_dict, 999, 999)[1]}')
# Добавление элемента происходит за близкое по значению время

print(f'3. Список (удаление элементов): {del_from_list(created_list, 1, 100)[1]}')
print(f'   Словарь (удаление элементов): {add_to_dict(created_dict, 1, 100)[1]}')
# Удаление из словаря происходит дольше, чем из списка
