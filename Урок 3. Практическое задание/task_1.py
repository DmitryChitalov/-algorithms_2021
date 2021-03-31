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

def time_function (func):
    def time_func(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        stop = time.time()
        return result, stop-start
    return time_func

@time_function
def create_list(n):
    cr_list = [i for i in range(n)]
    return cr_list


@time_function
def create_dict(n):
    cr_dict = {i: i for i in range(n)}
    return cr_dict


@time_function
def add_to_list(cr_list, a):
    cr_list.append(a)
    return cr_list

@time_function
def add_to_dict(cr_dict, key, val):
    cr_dict.update({key: val})
    return cr_dict

@time_function
def del_from_list(cr_list, how_much, n_from):
    for i in range(n_from, n_from + how_much):
        cr_list.pop(i)
    return cr_list


@time_function
def del_from_dict(cr_dict, how_much, n_from):
    for i in range(n_from, n_from + how_much):
        cr_dict.pop(i)
    return cr_dict



n=10000000
cr_list = create_list(n)[0]
cr_dict = create_dict(n)[0]

print(f'Создание списка: {create_list(n)[1]}')
print(f'Создание словаря: {create_dict(n)[1]}')
# Список создается быстрее, поскольку для каждого ключа словаря считается хэш

print(f'Добавление элемента в список: {add_to_list(cr_list,100)[1]}')
print(f'Добавление элемента в словарь: {add_to_dict(cr_dict, 111, 243)[1]}')
# Время добавление практически одинаково

print(f'Удаление элемента в списке: {del_from_list(cr_list,100, 100)[1]}')
print(f'Удаление элемента в словаре: {add_to_dict(cr_dict, 100, 100)[1]}')

#Удаление элемента по ключу из словаря происходит гораздо быстрее, чем удаление по инжексу из списка
